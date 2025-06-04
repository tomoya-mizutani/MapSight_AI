# 日本語表示サポートについて

## 概要
MapSight AIアプリケーションにおける日本語表示のサポートについて説明します。

## 実装内容

### 1. 文字エンコーディング
- ソースコードファイルはUTF-8エンコーディングを使用
- Python標準のエンコーディング指定を使用：`# -*- coding: utf-8 -*-`

### 2. ロケール設定
- アプリケーション全体で日本語ロケールを設定
- `QLocale.setDefault(QLocale(QLocale.Language.Japanese, QLocale.Country.Japan))`を使用

### 3. フォント設定
以下の優先順位でシステムフォントを設定：
1. Yu Gothic UI (Windows 10以降の標準日本語フォント)
2. Meiryo UI (Windows 7/8の標準日本語フォント)
3. MS Gothic (従来のWindows日本語フォント)
4. Noto Sans CJK JP (Linux/Unix系の標準日本語フォント)

## 動作要件
### Windows
- Windows 7以降
- 日本語フォントパックのインストール

### Linux/Unix
- フォントパッケージのインストール:
  ```bash
  # Ubuntu/Debian
  sudo apt-get install fonts-noto-cjk
  
  # Fedora/RHEL
  sudo dnf install google-noto-sans-cjk-fonts
  ```

## トラブルシューティング
### 文字化けが発生する場合
1. システムに適切な日本語フォントがインストールされているか確認
2. アプリケーションの再起動
3. システムの再起動

### フォントが見つからない場合
1. 代替フォントの追加:
   - Windows: コントロールパネル > フォント
   - Linux: フォントマネージャーで確認

## 制限事項
- 一部の特殊文字や絵文字は表示できない場合があります
- システムによってフォントの見た目が異なる場合があります

## 参考情報
- [Qt for Python ドキュメント](https://doc.qt.io/qtforpython-6/)
- [Python 日本語処理の基礎](https://docs.python.org/ja/3/howto/unicode.html) 