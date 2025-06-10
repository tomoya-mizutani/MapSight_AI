# 技術調査の記録ファイルだよ

開発における使用した，もしくは検討した技術に関して調査した記録を残しておく．

## phash処理

**同一画像を判定するためのハッシュ化アルゴリズム**  

perceptual hash アルゴリズムという．画像から人が検知しやすい特徴を抽出し，64bitのハッシュ値に変換する処理，
見た目が類似している画像同士の場合はハッシュ値間のハミング距離が近くなる特徴を持つ

<details>
<summary>ハミング距離</summary>
<blockquote>ハミング距離とは，ハッシュ値の各桁同士を見比べて異なる個数のことです．</blockquote>
</details>

### 活用例

・マッチングアプリ等で不正ユーザー対策の一環として年齢確認画像（免許証）の使いまわしなどを検知するのに使われている．

### 類似技術

#### aHash(Average Hash)

画像の輝度パターンを元にしたハッシュ値，素朴なアルゴリズム計算ができる．

1. 画像を8×8に縮小
2. グレースケールに変換
3. 画素値の平均を求める
4. 8×8ピクセルの各画素に対して，平均値よりも高いか低いかの2値分類をする
5. 分類したシーケンスに対して，ラスタスキャン順などの方法で1列にして64bitのハッシュをえる．

**アルゴリズムが簡単かつ計算が早い**。一方で柔軟性にかけるとのこと。

## hdistについて

## GNN(Graph Neural Network)

グラフニューラルネットワークを予測モデルへの活用を検討する．
プレイヤーをノード，関係性（味方とか敵とか❓）をエッジで表現し，ディープラーニングを用いて，次の局面を予測する．

関連研究では，例えばサッカーにおいて，トラッキングデータから次のパスの受け手やシュートに至る確率を予測して，守備側がどれだけ相手の攻撃をコントロールできているか定量化するモデルが開発されている．（<https://www.statsperform.com/wp-content/uploads/2021/04/Making-Offensive-Play-Predictable.pdf）>
これによって，今まで数値として評価の難しかったパスコースを切る・相手の攻撃をわかりやすくするといった守備貢献を定量的に評価できるようになった．

グラフ表現を活用した事例は他にもあり，戦術AIなるものをDeepMind社が発表している．グラフ表現と幾何学的ディープラーニング手法を組み合わせている．独自アーキテクチャの採用もしているらしい．
さらにこの予測モデルの中では，選手の配置展開について代替案を試行し，失点リスクを減らすための効果をシミュレーションする機能もある．

## 　マルチエージェント強化学習を用いた陣形の動的制御

[ロボットサッカーの分野での取り組み](https://link.springer.com/article/10.1007/s10458-023-09603-y#:~:text=Scaling%20multi,setting%20using%20limited%20computation%20resources)
もっとの近い味方のサポートをするとか，そういった戦術ルールを記述し活用．

## 画像学習・予測モデルの調査

## segment_rounds.py 将来的な拡張技術調査

### 1. OCR（光学文字認識）統合技術

#### 1.1 EasyOCR技術概要

**目的**: テンプレートマッチングで検出漏れしたフレームを文字認識で補完

**技術スタック**:

- **EasyOCR**: 80言語以上対応、PyTorchベース
- **CRAFT**: Character Region Awareness for Text detection
- **CRNN**: Convolutional Recurrent Neural Network（文字認識）

**アーキテクチャ**:

```python
# 段階的検出システム
Stage 1: Template Matching (高速、3秒)
   ↓ (検出不足の場合)
Stage 2: aHash変化点特定 (1秒)
   ↓
Stage 3: OCR実行 (候補20フレーム、40秒)
```

**処理時間分析**:

| 環境 | 単フレーム処理時間 | 20,000フレーム全処理 | 最適化後 |
|------|-------------------|---------------------|----------|
| CPU (8コア) | 1-3秒 | 11時間 | **50秒** |
| GPU使用 | 0.1-0.3秒 | 1.1時間 | **8分** |

**最適化手法**:

1. **画像前処理**: 1/4サイズ縮小、二値化処理
2. **候補絞り込み**: aHashで変化の大きい上位30箇所を選定
3. **並列処理**: ThreadPoolExecutorによる並列OCR実行
4. **早期終了**: 高信頼度キーワード検出時の即座停止

#### 1.2 対象キーワード最適化

**選定理由**: 計算量とキーワード数は線形関係だが、OCR処理が支配的（95%）

**最適化キーワードセット**:

```python
primary_keywords = ["試合終了", "MATCH FINISHED"]  # 高精度
secondary_keywords = ["ゲーム終了", "GAME OVER"]    # 補完用
```

**正規表現パターン**:

```python
patterns = [
    r'試合.*?終了',     # 試合xxxxx終了
    r'MATCH.*?FINISHED', # MATCH xxxxx FINISHED
]
```

### 2. デバッグ・解析機能強化

#### 2.1 詳細デバッグシステム
**目的**: 検出漏れの原因特定と処理の可視化

**実装予定機能**:
```python
--debug-frame 00705    # 特定フレーム解析
--debug-correlation    # 類似度分布表示
--debug-ahash          # aHashハミング距離可視化
--output-heatmap       # テンプレートマッチング結果のヒートマップ
```

**出力例**:
```
DEBUG Frame Frames_00705:
  Template correlation: 0.4823 (threshold: 0.5000)
  Best match location: (892, 456)
  aHash: 18374686479671623680
  Previous frame distance: 12
  Status: REJECTED (below threshold)
```

#### 2.2 可視化機能
**技術**: matplotlib, OpenCV描画機能

**予定機能**:
1. **境界検出グラフ**: 時系列での類似度変化
2. **ヒートマップ**: テンプレートマッチング結果
3. **aHashトレンド**: フレーム間距離の変化
4. **クラスタリング結果**: 検出フレームのグループ化

### 3. 機械学習ベース検出システム

#### 3.1 CNN分類器
**目的**: 従来手法で検出困難な多様なレイアウトに対応

**アーキテクチャ案**:
```python
class RoundEndClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        # ResNet18ベースの特徴抽出
        self.backbone = torchvision.models.resnet18(pretrained=True)
        self.backbone.fc = nn.Linear(512, 2)  # Binary classification
    
    def forward(self, x):
        return torch.sigmoid(self.backbone(x))
```

**学習データ**:
- **Positive**: ラウンド終了画面フレーム (1,000枚)
- **Negative**: 通常ゲームプレイフレーム (5,000枚)
- **Augmentation**: 回転、明度変更、ノイズ追加

**予想精度**: 95%以上（テンプレート+OCRの補完として使用）

#### 3.2 YOLO物体検出
**目的**: UI要素の位置を考慮した検出

**検出対象**:
- ラウンド終了ロゴ
- スコア表示エリア
- "MATCH FINISHED"テキスト領域

**実装案**:
```python
# YOLOv8カスタムモデル
model = YOLO('yolov8n.pt')
results = model.train(
    data='round_end_dataset.yaml',
    epochs=100,
    imgsz=640,
    batch=16
)
```

### 4. 設定管理・ワークフロー改善

#### 4.1 設定ファイルシステム
**形式**: YAML設定ファイル

```yaml
# segment_config.yaml
detection:
  template:
    threshold: 0.5
    cluster_gap: 5
    step: 1
  
  ocr:
    enabled: true
    keywords: ["試合終了", "MATCH FINISHED"]
    confidence_threshold: 0.3
    max_candidates: 20
  
  ml_classifier:
    enabled: false
    model_path: "models/round_end_classifier.pth"
    threshold: 0.8

output:
  directory: "data/{upload_date}"
  file_format: "Frames_{index:05d}.jpg"
  preserve_original: true

performance:
  max_workers: 8
  gpu_acceleration: true
  memory_limit: "8GB"
```

#### 4.2 プリセット機能
```python
# 事前定義された設定
presets = {
    "fast": {        # 高速処理優先
        "template_only": True,
        "step": 5,
        "ocr_enabled": False
    },
    "accurate": {    # 精度優先
        "template_threshold": 0.3,
        "ocr_enabled": True,
        "ml_classifier": True
    },
    "debug": {       # デバッグ用
        "debug_all": True,
        "output_heatmap": True,
        "dry_run": True
    }
}
```

### 5. 性能最適化技術

#### 5.1 GPU加速
**CUDA対応**:
```python
# OpenCV GPU処理
img_gpu = cv2.cuda_GpuMat()
img_gpu.upload(img)
template_gpu = cv2.cuda_GpuMat()
template_gpu.upload(template)

# GPU上でテンプレートマッチング
result_gpu = cv2.cuda.matchTemplate(img_gpu, template_gpu, cv2.TM_CCOEFF_NORMED)
```

**PyTorch GPU処理**:
```python
# バッチ処理によるGPU最適化
def batch_ahash_gpu(frames, batch_size=32):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    # バッチ単位でのaHash計算
```

#### 5.2 メモリ効率化
**実装予定**:
1. **ストリーミング処理**: 大量フレームの逐次読み込み
2. **メモリプール**: オブジェクト再利用
3. **遅延読み込み**: 必要時のみ画像読み込み

### 6. API・インターフェース拡張

#### 6.1 Web API化
**FastAPI実装予定**:
```python
@app.post("/segment/")
async def segment_rounds(
    frames_dir: str,
    template_file: UploadFile,
    config: SegmentConfig = SegmentConfig()
):
    result = await segment_processor.process(
        frames_dir, template_file, config
    )
    return {"boundaries": result.boundaries, "status": "completed"}
```

#### 6.2 リアルタイム処理
**WebSocket対応**:
```python
@app.websocket("/segment/realtime")
async def realtime_segment(websocket: WebSocket):
    # リアルタイム処理進捗の配信
    async for progress in segment_processor.stream_progress():
        await websocket.send_json(progress)
```

### 7. 品質保証・テスト

#### 7.1 回帰テスト
**実装予定**:
```python
# pytest テストケース
def test_detection_accuracy():
    """既知の境界フレームでの検出精度テスト"""
    known_boundaries = [150, 300, 450, 600]
    detected = segment_rounds.detect_boundaries(test_frames)
    accuracy = calculate_accuracy(known_boundaries, detected)
    assert accuracy > 0.95
```

#### 7.2 ベンチマーク
**性能指標**:
- 処理時間（フレーム数別）
- メモリ使用量
- 検出精度（Precision/Recall）
- GPU利用率

### 8. 実装ロードマップ

**Phase 1 (短期: 1-2ヶ月)**
- [ ] OCR機能統合
- [ ] デバッグ機能強化
- [ ] 設定ファイル対応

**Phase 2 (中期: 3-6ヶ月)**
- [ ] 機械学習分類器
- [ ] GPU加速実装
- [ ] Web API化

**Phase 3 (長期: 6ヶ月以降)**
- [ ] リアルタイム処理
- [ ] 高度な可視化機能
- [ ] 自動チューニング機能

### 9. 技術リスク評価

**高リスク要因**:
1. **OCR精度**: 日本語認識の不安定性
2. **計算リソース**: GPU要件の増大
3. **メンテナンス**: 複雑化による保守性低下

**リスク軽減策**:
1. **段階的導入**: 既存機能を維持したオプション追加
2. **フォールバック機能**: 高度機能失敗時の従来手法切り替え
3. **文書化**: 包括的なドキュメント整備
