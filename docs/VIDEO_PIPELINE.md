# 動画取り込みパイプライン

`video_pipeline.py` は動画URLのダウンロードからフレーム抽出、
ミニマップ切り出しまでを自動化するスクリプトです。
`data_dirs.py` と組み合わせることで Scrim や tournament
ディレクトリを自動生成して処理結果を保存します。

## 使い方

```bash
python src/video_pipeline.py --url <VIDEO_URL> scrim 2024/05/06 --rounds 2
```

- `--url` : YouTube または mp4 直リンク
- `scrim` / `tournament` : データ種別
- `--rounds` : Scrim のラウンド数 (デフォルト: 2)

処理結果は `data/Scrim/2024/05/06/` 以下に
`raw_videos/`, `frames/`, `minimaps/` が作成されます。
