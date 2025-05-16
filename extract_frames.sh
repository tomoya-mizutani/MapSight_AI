#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# extract_frames.sh  ─  YouTube / direct‑link video ➜ frame extractor
# -----------------------------------------------------------------------------
# 既存ディレクトリをそのまま活用します。
#   * data/raw_videos/   … 元動画を保存（存在しなければ自動作成）
#   * frames/            … 抽出 JPG を保存（存在しなければ自動作成）
#
# Usage:
#   ./extract_frames.sh <VIDEO_URL> [FPS] [WIDTH]
#     VIDEO_URL : YouTube URL もしくは mp4 直リンク
#     FPS       : 1 秒あたり抽出フレーム数 (default: 2)
#     WIDTH     : 抽出フレームの横幅ピクセル       (default: 1920)
#
# 例:
#   ./extract_frames.sh "https://www.youtube.com/watch?v=tkbV9EJPak4"
#   ./extract_frames.sh "https://cdn.example.com/game.mp4" 1 1280
# -----------------------------------------------------------------------------
set -euo pipefail

VIDEO_URL="${1:-}"
if [[ -z "$VIDEO_URL" ]]; then
  echo "[ERROR] VIDEO_URL が未指定です。" >&2
  exit 1
fi

FPS="${2:-2}"
WIDTH="${3:-1920}"

RAW_DIR="data/raw_videos"
FRAMES_DIR="frames"
mkdir -p "$RAW_DIR" "$FRAMES_DIR"

# --- 1) 動画ダウンロード: URL 種別で分岐 ------------------------------------
if [[ "$VIDEO_URL" =~ (youtu\.be|youtube\.com) ]]; then
  # YouTube URL の場合: yt-dlp で mp4 (映像+音声) を DL
  VID_ID="$(yt-dlp --get-id "$VIDEO_URL")"
  OUT_FILE="$RAW_DIR/${VID_ID}.mp4"
  if [[ ! -f "$OUT_FILE" ]]; then
    echo "[INFO] Downloading YouTube video to $OUT_FILE …"
    yt-dlp -f "bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/best" \
           -o "$OUT_FILE" "$VIDEO_URL"
  else
    echo "[SKIP] Video already exists: $OUT_FILE"
  fi
else
  # 直リンク (http/https) の場合: curl で取得
  FILE_NAME="$(basename "${VIDEO_URL%%\?*}")"
  OUT_FILE="$RAW_DIR/$FILE_NAME"
  if [[ ! -f "$OUT_FILE" ]]; then
    echo "[INFO] Downloading direct link to $OUT_FILE …"
    curl -L "$VIDEO_URL" -o "$OUT_FILE"
  else
    echo "[SKIP] Video already exists: $OUT_FILE"
  fi
fi

# --- 2) フレーム抽出 -----------------------------------------------------------
echo "[INFO] Extracting frames ➜ $FRAMES_DIR (fps=$FPS, width=$WIDTH)"
ffmpeg -hide_banner -loglevel error -stats \
       -i "$OUT_FILE" \
       -vf "fps=$FPS,scale=$WIDTH:-2" -q:v 2 \
       "$FRAMES_DIR/frame_%05d.jpg"

echo "[DONE] $(ls -1 $FRAMES_DIR | wc -l) frames saved in $FRAMES_DIR"
