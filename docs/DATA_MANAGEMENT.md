# データディレクトリ管理

試合データを整理するために、以下のようなディレクトリ構造を採用します。

```
data/
├── Scrim/
│   └── YYYY/MM/DD/
│       ├── Round1/
│       └── Round2/
└── tournament/
    ├── PMGC2024/
    └── PMOT2025/
```

`src/data_dirs.py` を利用すると、これらのフォルダを自動で生成できます。

## 使い方

### スクリム用ディレクトリ

```bash
python src/data_dirs.py scrim 2024/05/06 --rounds 2
```

### 大会用ディレクトリ

```bash
python src/data_dirs.py tournament PMGC2024
```
動画URLから自動で取り込む場合は [video_pipeline.py](VIDEO_PIPELINE.md) も参照してください。
