#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 必要なモジュールをインポート
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QMenuBar, QMenu
from PyQt6.QtCore import Qt, QLocale
from PyQt6.QtGui import QFont

# メインウィンドウクラスの定義
class MapSightAI(QMainWindow):
    def __init__(self):
        # 親クラスの初期化
        super().__init__()
        
        # ウィンドウのタイトルを設定
        self.setWindowTitle("MapSight AI")
        
        # ウィンドウサイズを設定
        self.setGeometry(100, 100, 1280, 720)
        
        # メインウィジェットを作成
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # メインレイアウトを作成
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        
        # 上部メニューエリアを作成
        self._create_menu_area()
        
        # 中央部のレイアウトを作成
        central_layout = QHBoxLayout()
        
        # マップ表示エリアを作成
        self._create_map_area()
        central_layout.addWidget(self.map_area, stretch=2)
        
        # データパネルを作成
        self._create_data_panel()
        central_layout.addWidget(self.data_panel, stretch=1)
        
        main_layout.addLayout(central_layout)
        
        # タイムラインエリアを作成
        self._create_timeline_area()
        main_layout.addWidget(self.timeline_area)
    
    def _create_menu_area(self):
        # メニューバーを作成（親クラスのメニューバーを取得）
        self.menubar = QMenuBar(self)
        self.setMenuBar(self.menubar)
        
        # ファイルメニュー
        self.file_menu = QMenu("ファイル", self)
        self.menubar.addMenu(self.file_menu)
        self.file_menu.addAction("新規プロジェクト")
        self.file_menu.addAction("開く")
        self.file_menu.addAction("保存")
        self.file_menu.addSeparator()
        self.file_menu.addAction("終了")
        
        # 表示メニュー
        self.view_menu = QMenu("表示", self)
        self.menubar.addMenu(self.view_menu)
        self.view_menu.addAction("ズームイン")
        self.view_menu.addAction("ズームアウト")
        self.view_menu.addAction("全体表示")
        
        # ツールメニュー
        self.tools_menu = QMenu("ツール", self)
        self.menubar.addMenu(self.tools_menu)
        self.tools_menu.addAction("解析")
        self.tools_menu.addAction("設定")
        
        # ヘルプメニュー
        self.help_menu = QMenu("ヘルプ", self)
        self.menubar.addMenu(self.help_menu)
        self.help_menu.addAction("ヘルプ")
        self.help_menu.addAction("バージョン情報")
    
    def _create_map_area(self):
        # マップ表示エリアを作成
        self.map_area = QWidget()
        self.map_area.setStyleSheet("background-color: #2b2b2b;")
    
    def _create_data_panel(self):
        # データパネルを作成
        self.data_panel = QWidget()
        self.data_panel.setStyleSheet("background-color: #333333;")
    
    def _create_timeline_area(self):
        # タイムラインエリアを作成
        self.timeline_area = QWidget()
        self.timeline_area.setFixedHeight(100)
        self.timeline_area.setStyleSheet("background-color: #1e1e1e;")

# メイン実行部分
def main():
    # アプリケーションを作成
    app = QApplication(sys.argv)
    
    # 日本語ロケールを設定
    QLocale.setDefault(QLocale(QLocale.Language.Japanese, QLocale.Country.Japan))
    
    # システムフォントを設定
    font = QFont("Yu Gothic UI", 9)  # Windows向け日本語フォント
    app.setFont(font)
    
    # 代替フォントも設定
    fallback_font = app.font()
    fallback_font.setFamilies(["Yu Gothic UI", "Meiryo UI", "MS Gothic", "Noto Sans CJK JP"])
    app.setFont(fallback_font)
    
    # メインウィンドウを作成
    window = MapSightAI()
    
    # ウィンドウを表示
    window.show()
    
    # アプリケーションを実行
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 