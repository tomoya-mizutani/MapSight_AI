# スタイルシートの定義

# メインウィンドウのスタイル
MAIN_WINDOW_STYLE = """
QMainWindow {
    background-color: #1a1a1a;
}
"""

# メニューバーのスタイル
MENU_BAR_STYLE = """
QMenuBar {
    background-color: #2d2d2d;
    color: #ffffff;
}

QMenuBar::item {
    padding: 4px 10px;
    background-color: transparent;
}

QMenuBar::item:selected {
    background-color: #3d3d3d;
}
"""

# マップエリアのスタイル
MAP_AREA_STYLE = """
QWidget#map_area {
    background-color: #2b2b2b;
    border: 1px solid #3d3d3d;
    border-radius: 4px;
}
"""

# データパネルのスタイル
DATA_PANEL_STYLE = """
QWidget#data_panel {
    background-color: #333333;
    border: 1px solid #3d3d3d;
    border-radius: 4px;
}
"""

# タイムラインエリアのスタイル
TIMELINE_STYLE = """
QWidget#timeline_area {
    background-color: #1e1e1e;
    border: 1px solid #3d3d3d;
    border-radius: 4px;
}
"""

# ボタンの共通スタイル
BUTTON_STYLE = """
QPushButton {
    background-color: #4a4a4a;
    color: #ffffff;
    border: none;
    padding: 5px 15px;
    border-radius: 3px;
}

QPushButton:hover {
    background-color: #5a5a5a;
}

QPushButton:pressed {
    background-color: #3a3a3a;
}
"""

# スライダーの共通スタイル
SLIDER_STYLE = """
QSlider::groove:horizontal {
    border: 1px solid #4a4a4a;
    height: 4px;
    background: #2d2d2d;
    margin: 0px;
    border-radius: 2px;
}

QSlider::handle:horizontal {
    background: #6a6a6a;
    border: 1px solid #5a5a5a;
    width: 12px;
    margin: -4px 0;
    border-radius: 6px;
}

QSlider::handle:horizontal:hover {
    background: #7a7a7a;
}
""" 