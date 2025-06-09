# マップ配信から，該当部分の抽出．マップのみを切り抜く．
# --- 設定ファイルからの読み込み ---
# config.yaml に記載された設定を読み込みます。
# "roi" は透視変換対象の四角形領域の座標リスト（4点 × 2次元）
# ROI 4 点 → 透視変換 & 512×512 保存
# "output_size" は切り抜き後の出力画像サイズ（幅, 高さ）

# 実行コマンド: python crop_minimap.py
## data/minimaps/に処理済みデータが格納される．


"""
cv2.convexHull と cv2.UMat に関するドキュメント

--------------------------------------------------------------------------------
1. cv2.convexHull（凸包）
[参考資料1](https://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html)
[公式ドキュメント](https://docs.opencv.org/3.4/d7/d1d/tutorial_hull.html)
概要：
    与えられた2次元点群を囲む最小の凸多角形（凸包）を計算する関数。
    凸包は点の集合をすべて包み込む凸な多角形であり、輪郭の形状を簡略化したり、
    外接領域を取得する際に利用される。

入力：
    - points: 2Dの点の集合（numpy配列等）
出力：
    - 凸包を構成する点のリスト（numpy配列）

用途例：
    - 画像中の輪郭点群の凸包を取得し、形状の特徴付けを行う。
    - 凸でない領域を凸領域に変換して、透視変換などの処理を安定化させる。

備考：
    - PUBGマップ解析において、ROIの4点を凸包で整形することで、
      凸でない形状に起因する誤差を防ぎ、正確な透視変換を実現している。

--------------------------------------------------------------------------------
2. cv2.UMat（ユニファイドメモリアクセス行列）
[参考資料1](https://qiita.com/dandelion1124/items/fad18a164108158585e3)
[公式資料](https://docs.opencv.org/4.x/d7/d45/classcv_1_1UMat.html)
概要：
    OpenCVにおける高速処理対応の特殊な行列型。
    GPUやその他のハードウェアアクセラレーションを活用し、
    処理速度を向上させることを目的としている。

特徴：
    - numpy配列や通常のcv2.Matと同様の操作が可能。
    - OpenCLやCUDA対応のGPUがある場合は自動的にそちらで処理を実行。
    - 対応関数はUMatを受け入れ高速化される。

メリット：
    - CPU負荷の軽減
    - 大量データ・複雑処理の高速化

注意点：
    - GPU非搭載環境では通常のCPU処理となるため速度差はない。
    - 一部関数はUMat非対応の場合がある。
    - デバッグ時の取り扱いが通常行列よりやや複雑。

用途例：
    - PUBGマップ解析で、ROI座標をUMatに変換し、
      convexHullやその他のOpenCV関数に高速処理を活用させている。

--------------------------------------------------------------------------------
"""


import cv2
import yaml
import pathlib
import tqdm
import numpy as np


cfg = yaml.safe_load(open("config.yaml", encoding="utf-8"))
points = np.array(cfg["roi"], dtype="float32").reshape((-1, 1, 2))
src_pts = cv2.convexHull(points).reshape(-1, 2).astype("float32")  # 4×2

dst_w, dst_h = cfg["output_size"]
dst_pts = np.array([[0, 0], [dst_w, 0], [dst_w, dst_h], [0, dst_h]], dtype="float32")

M = cv2.getPerspectiveTransform(src_pts, dst_pts)


# --- 入出力ディレクトリの準備 ---
in_dir = pathlib.Path("data/frames/2024-12-04")
out_dir = pathlib.Path("data/minimaps/2024-12-04")
out_dir.mkdir(exist_ok=True)

# --- 画像処理ループ ---
# 入力ディレクトリのjpgファイルを名前順に処理
for f in tqdm.tqdm(sorted(in_dir.glob("*.jpg"))):
    img   = cv2.imread(str(f))
    # 透視変換をかけて切り抜き（warp）を作成
    warp  = cv2.warpPerspective(img, M, (dst_w, dst_h))
    out_f = out_dir / f.name
    cv2.imwrite(str(out_f), warp)

# 処理完了した画像枚数を表示
print("Done:", len(list(out_dir.glob('*.jpg'))), "images")
