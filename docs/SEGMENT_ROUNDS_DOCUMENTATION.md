# segment_rounds.py ドキュメント

## 概要

`segment_rounds.py`は、PUBGの試合動画から抽出されたフレーム画像を自動的にラウンド単位でセグメント化するPythonスクリプトです。テンプレートマッチングとaHash（Average Hash）アルゴリズムを組み合わせて、高速で正確なラウンド境界検出を実現します。

## アルゴリズム概要

### 1. **aHash（Average Hash）セグメンテーション**
- 各フレームの8×8グレースケール画像から64ビットハッシュを生成
- 連続フレーム間のハミング距離を計算してシーン変化を検出
- 実測：20,000フレームで約2秒の高速処理（8C16T環境）

### 2. **テンプレートマッチング**
- ラウンド終了画面のテンプレート画像との類似度を計算
- OpenCVの`cv2.matchTemplate()`を使用
- クラスタリング処理で近接する検出を統合

### 3. **ハイブリッド検出**
- テンプレート検出で確実な境界を特定
- 不足分をaHashベースの類似度判定で補完

## 使用方法

### 基本コマンド
```bash
python segment_rounds.py data/frames/<upload-date> \
       --template data/templates/Match_End_template.jpg
```

### 完全なオプション一覧
```bash
python segment_rounds.py [frames_dir] [OPTIONS]

引数:
  frames_dir           フレーム画像が格納されたディレクトリ
                      例: data/frames/2025-05-02

オプション:
  --template FILE      テンプレート画像ファイルパス（必須）
  --segments N         出力ラウンド数（デフォルト: 5）
  --threshold N        aHash ハミング距離しきい値（デフォルト: 10、現在未使用）
  --cluster-gap N      同一テンプレートクラスタ判定間隔（デフォルト: 5）
  --end-th FLOAT       テンプレートマッチング類似度しきい値（デフォルト: 0.5）
  --step N             テンプレートマッチングのステップ数（デフォルト: 1）
  --peek               移動せず区切り候補を表示のみ
  --dry-run            実際のファイル操作を行わず処理内容を表示
  --log-file FILE      移動履歴を CSV ファイルに保存
  --out-root DIR       出力ルートディレクトリ（後方互換性のため残存、現在未使用）
```

## 実行例

### 1. 基本実行
```bash
python segment_rounds.py data/frames/2025-05-02 \
  --template data/templates/Match_End_template.jpg
```

### 2. しきい値調整
```bash
python segment_rounds.py data/frames/2025-05-02 \
  --template data/templates/Match_End_template.jpg \
  --end-th 0.6 --segments 6
```

### 3. 処理内容確認（ドライラン）
```bash
python segment_rounds.py data/frames/2025-05-02 \
  --template data/templates/Match_End_template.jpg \
  --dry-run
```

### 4. 区切り候補のみ表示
```bash
python segment_rounds.py data/frames/2025-05-02 \
  --template data/templates/Match_End_template.jpg \
  --peek
```

## 出力構造

### ディレクトリ構成
```
data/
├── <upload-date>/
│   ├── round1/
│   │   ├── Frames_00001.jpg
│   │   ├── Frames_00002.jpg
│   │   └── ...
│   ├── round2/
│   │   ├── Frames_00001.jpg
│   │   ├── Frames_00002.jpg
│   │   └── ...
│   └── ...
```

### ファイル命名規則
- 元ファイル: `Frames_XXXXX.jpg`
- 出力ファイル: `Frames_XXXXX.jpg`（ラウンド内で連番リセット）

## 技術詳細

### aHashアルゴリズム
```python
def ahash(path: Path, size: int = 8) -> int:
    # 1. 画像をグレースケール8x8にリサイズ
    # 2. 平均輝度を計算
    # 3. 各ピクセルが平均以上かどうかで64ビットハッシュ生成
```

### テンプレートマッチング
```python
def process_frame_cpu(idx, frame_path, tmpl_gray, thr, th, tw):
    # 1. フレームをグレースケールで読み込み
    # 2. cv2.matchTemplate()で類似度計算
    # 3. しきい値以上で検出判定
```

### クラスタリング処理
```python
# 近接する検出フレームをグループ化
if i - clusters[-1][-1] <= cluster_gap:
    clusters[-1].append(i)  # 既存クラスタに追加
else:
    clusters.append([i])    # 新しいクラスタ作成
```

## パフォーマンス

### 処理時間（20,000フレームの場合）
- **aHash計算**: 約2秒（8C16T環境）
- **テンプレート検出**: 約3秒
- **全体処理**: 約6秒

### メモリ効率
- グレースケール処理によりメモリ使用量を1/3に削減
- ProcessPoolExecutorによる並列処理で高速化

## トラブルシューティング

### 1. 検出漏れが発生する場合

#### 症状
特定のフレーム（例：Frames_00705）がテンプレートマッチングで検出されない

#### 原因
- テンプレートマッチングのしきい値が高すぎる
- 画像の微細な違い（圧縮アーティファクト、色調変化、ノイズ）
- わずかな位置ずれ

#### 解決策
1. **しきい値を下げる**
   ```bash
   --end-th 0.3  # デフォルト0.5から下げる
   ```

2. **ステップ数を確認**
   ```bash
   --step 1  # 全フレームをチェック
   ```

3. **デバッグモードの実装**（将来実装予定）
   ```bash
   --debug-frame 00705  # 特定フレームの類似度を表示
   ```

### 2. ファイル操作に関する注意

#### 現在の動作
- `shutil.copy2()`を使用して**元ファイルを保持**
- 元の`data/frames/<upload-date>/`ディレクトリは変更されない

#### ドライランモード
```bash
--dry-run  # 実際のファイル操作なしで処理内容を確認
```

### 3. グレースケール処理の理由

#### 利点
- **処理速度向上**: カラー画像の1/3のデータ量
- **メモリ効率**: 大幅なメモリ使用量削減
- **精度向上**: 色ノイズの影響を除去
- **aHash要件**: アルゴリズムの前提条件

#### 対象画像
- テンプレート画像: グレースケール変換
- フレーム画像: グレースケール変換
- 色情報は不要（形状・輝度パターンが重要）

## 将来的な拡張

### 1. OCR（光学文字認識）による文字検出
EasyOCRを使用した高度な文字検出機能の追加が検討されています。

#### 対象キーワード
- 日本語: `試合終了`
- 英語: `MATCH FINISHED`

#### 予想処理時間（CPU環境）
- 最適化により約50秒で処理完了
- 候補フレームを20個程度に絞り込んで実行

#### 実装案
```python
# 段階的検出
1. テンプレートマッチング（高速）
2. aHashで変化点特定
3. OCR（候補フレームのみ）
```

### 2. デバッグ機能の強化
- 特定フレームの類似度表示
- 詳細な検出ログ出力
- 可視化機能

### 3. 設定ファイル対応
- YAML/JSON形式での設定管理
- プリセット機能

## 技術スタック

### 必要ライブラリ
```python
import numpy as np
import cv2
import argparse
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import shutil
import time
```

### Python要件
- Python 3.8以上
- OpenCV
- NumPy
- その他標準ライブラリ

## 参考情報

### アルゴリズム参考
- aHash (Average Hash): 画像の平均的な特徴をハッシュ化
- ハミング距離: ビット列間の差分を測定
- テンプレートマッチング: OpenCVの標準機能

### 処理フロー
```
入力フレーム → aHash計算 → テンプレート検出 → クラスタリング → 境界決定 → ファイル分割
```

## 更新履歴

- **rev6-ahash**: pHashからaHashに変更、処理速度大幅向上
- 出力先を`data/<upload-date>/`に変更
- ファイル操作を`move`から`copy2`に変更（元ファイル保持）
- デフォルトしきい値を0.75から0.5に変更
