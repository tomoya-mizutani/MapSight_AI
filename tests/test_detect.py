import cv2
import numpy as np
import json
import argparse
from pathlib import Path


def detect_player_circles(
    img_bgr,
    dp=1.2,
    min_dist=15,
    param1=50,
    param2=20,
    min_radius=5,
    max_radius=20,
    sat_threshold=80,
):
    """
    画像から「彩度の高い円」を検出してプレイヤー候補を返す。

    return: list of dict {x, y, r}
    """
    h, w = img_bgr.shape[:2]

    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, 5)

    circles = cv2.HoughCircles(
        gray_blur,
        cv2.HOUGH_GRADIENT,
        dp=dp,
        minDist=min_dist,
        param1=param1,
        param2=param2,
        minRadius=min_radius,
        maxRadius=max_radius,
    )

    if circles is None:
        return []

    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

    def mean_saturation(x, y, r):
        # 中心付近 5x5 の平均彩度を取る
        x0, x1 = max(0, x - 2), min(w, x + 3)
        y0, y1 = max(0, y - 2), min(h, y + 3)
        patch_s = hsv[y0:y1, x0:x1, 1]
        return float(patch_s.mean())

    circle_candidates = np.atleast_2d(np.round(circles[0]).astype(np.int32))
    players = []

    for (x, y, r) in circle_candidates:
        # 彩度が一定以上の円だけ採用
        if mean_saturation(x, y, r) >= sat_threshold:
            players.append({"x": int(x), "y": int(y), "r": int(r)})

    return players


def compute_mean_colors(img_bgr, players):
    """
    各プレイヤー円の中の平均 BGR 色を計算して返す。
    """
    h, w = img_bgr.shape[:2]
    colors = []

    for p in players:
        x, y, r = p["x"], p["y"], p["r"]
        # 円の中心付近の小さめな正方形パッチを使う
        x0, x1 = max(0, x - r // 2), min(w, x + r // 2)
        y0, y1 = max(0, y - r // 2), min(h, y + r // 2)
        patch = img_bgr[y0:y1, x0:x1]

        if patch.size == 0:
            colors.append((0.0, 0.0, 0.0))
            continue

        mean_bgr = patch.reshape(-1, 3).mean(axis=0)  # (B, G, R)
        colors.append(tuple(float(c) for c in mean_bgr))

    return colors


def cluster_by_color(colors, k):
    """
    BGR 平均色を K-means でクラスタリング。
    return: labels (len = N), centers (k x 3 BGR)
    """
    Z = np.array(colors, dtype=np.float32)
    criteria = (
        cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
        100,
        0.2,
    )

    best_labels = np.zeros((Z.shape[0],), dtype=np.int32)
    compactness, labels, centers = cv2.kmeans(
        Z,
        K=k,
        bestLabels=best_labels,
        criteria=criteria,
        attempts=10,
        flags=cv2.KMEANS_RANDOM_CENTERS,
    )
    centers = centers.reshape(-1, 3)  # Ensure centers is a 2D array

    return labels.flatten().tolist(), centers.tolist()


def extract_positions_by_color(image_path, k_clusters=10):
    img_bgr = cv2.imread(str(image_path))
    if img_bgr is None:
        raise FileNotFoundError(f"Cannot read image: {image_path}")

    h, w = img_bgr.shape[:2]

    # 1. 円の検出
    players = detect_player_circles(img_bgr)

    if not players:
        return {
            "image_width": w,
            "image_height": h,
            "players_by_color": [],
        }

    # 2. 各プレイヤーの平均色
    colors = compute_mean_colors(img_bgr, players)

    # 3. 色クラスタリング
    labels, centers = cluster_by_color(colors, k_clusters)

    # 4. JSON 用の構造に整形
    clusters = []
    for cluster_id in range(k_clusters):
        cluster_players = []
        for idx, label in enumerate(labels):
            if label == cluster_id:
                p = players[idx]
                cluster_players.append(
                    {"x": p["x"], "y": p["y"], "radius": p["r"]}
                )

        if not cluster_players:
            continue  # その色クラスタにはプレイヤーがいなければスキップ

        center_bgr = centers[cluster_id]
        clusters.append(
            {
                "cluster_id": cluster_id,
                # BGR をそのまま保存（必要なら後で HSV や HEX に変換）
                "color_bgr": [
                    float(center_bgr[0]),
                    float(center_bgr[1]),
                    float(center_bgr[2]),
                ],
                "players": cluster_players,
            }
        )

    result = {
        "image_width": w,
        "image_height": h,
        "players_by_color": clusters,
    }

    return result


def main():
    parser = argparse.ArgumentParser(
        description="PUBG マップ画像からプレイヤー位置(色付き●)を抽出して JSON 化するツール"
    )
    parser.add_argument("image", help="入力画像ファイルパス")
    parser.add_argument(
        "-o",
        "--output",
        default="players_by_color.json",
        help="出力 JSON ファイル名",
    )
    parser.add_argument(
        "-k",
        "--k_clusters",
        type=int,
        default=10,
        help="色クラスタ数 (チームの色数の目安)",
    )

    args = parser.parse_args()

    image_path = Path(args.image)
    data = extract_positions_by_color(image_path, k_clusters=args.k_clusters)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"saved: {args.output}")


if __name__ == "__main__":
    main()
