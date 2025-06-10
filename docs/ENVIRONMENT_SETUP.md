# VSCode と Google Colab 開発環境設定ガイド

## 概要

このドキュメントでは、MapSight_AIプロジェクトでVSCodeとGoogle Colabを効率的に組み合わせるための具体的な設定手順を説明します。

## 🖥️ VSCode 開発環境構築

### 1. 前提条件

- Visual Studio Code 最新版
- Python 3.8以上
- Git
- WSL2 (Windows の場合)

### 2. プロジェクト初期設定

#### ディレクトリ構成の作成

```bash
mkdir -p MapSight_AI/{src,tests,notebooks,docs,config,utils,requirements}
cd MapSight_AI

# 基本ファイルの作成
touch README.md
touch .gitignore
touch requirements/requirements_dev.txt
touch requirements/requirements_colab.txt
touch config/dev_config.yaml
touch config/colab_config.yaml
```

#### 仮想環境セットアップ

```bash
# Python仮想環境作成
python -m venv venv

# 仮想環境有効化
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate    # Windows

# 基本パッケージインストール
pip install --upgrade pip
pip install -r requirements/requirements_dev.txt
```

### 3. VSCode 設定ファイル

#### .vscode/settings.json

```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.terminal.activateEnvironment": true,
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": [
        "tests",
        "-v",
        "--tb=short"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.autoTestDiscoverOnSaveEnabled": true,
    
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": [
        "--line-length=88"
    ],
    
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": [
        "--max-line-length=88",
        "--ignore=E203,W503"
    ],
    
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    },
    
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true,
        "**/venv": true,
        "**/.pytest_cache": true,
        "**/.*": false
    },
    
    "jupyter.askForKernelRestart": false,
    "jupyter.interactiveWindow.creationMode": "perFile",
    
    "git.autofetch": true,
    "git.confirmSync": false,
    
    "files.associations": {
        "*.yaml": "yaml",
        "*.yml": "yaml"
    }
}
```

#### .vscode/launch.json

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}",
            "env": {
                "PYTHONPATH": "${workspaceFolder}/src"
            }
        },
        {
            "name": "Python: Segment Rounds Debug",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/src/segment_rounds_updated.py",
            "args": [
                "data/frames/test",
                "--template", "data/templates/Match_End_template.jpg",
                "--dry-run",
                "--debug"
            ],
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}"
        },
        {
            "name": "Python: Test Suite",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "args": [
                "tests/",
                "-v",
                "--tb=short"
            ],
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}"
        }
    ]
}
```

#### .vscode/tasks.json

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Python: Format Code",
            "type": "shell",
            "command": "${config:python.formatting.blackPath}",
            "args": ["src/", "tests/", "utils/"],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared"
            },
            "problemMatcher": []
        },
        {
            "label": "Python: Lint Code",
            "type": "shell",
            "command": "${config:python.linting.flake8Path}",
            "args": ["src/", "tests/", "utils/"],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared"
            },
            "problemMatcher": []
        },
        {
            "label": "Python: Run Tests",
            "type": "shell",
            "command": "python",
            "args": ["-m", "pytest", "tests/", "-v"],
            "group": "test",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared"
            },
            "problemMatcher": []
        },
        {
            "label": "Environment: Check Setup",
            "type": "shell",
            "command": "python",
            "args": ["utils/env_checker.py", "--check"],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared"
            }
        },
        {
            "label": "Colab: Sync to Drive",
            "type": "shell",
            "command": "python",
            "args": ["utils/colab_sync.py", "--upload"],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared"
            }
        }
    ]
}
```

#### .vscode/extensions.json

```json
{
    "recommendations": [
        "ms-python.python",
        "ms-python.black-formatter",
        "ms-python.flake8",
        "ms-python.isort",
        "ms-toolsai.jupyter",
        "ms-vscode.test-adapter-converter",
        "github.copilot",
        "github.copilot-chat",
        "ms-vscode.vscode-json",
        "redhat.vscode-yaml",
        "ms-vscode-remote.remote-wsl",
        "eamodio.gitlens",
        "ms-python.debugpy",
        "njpwerner.autodocstring",
        "visualstudioexptteam.vscodeintellicode"
    ]
}
```

### 4. 開発用設定ファイル

#### requirements/requirements_dev.txt

```txt
# 基本パッケージ
numpy>=1.24.0
opencv-python>=4.8.0
PyYAML>=6.0
pathlib2>=2.3.7
tqdm>=4.65.0

# 開発・テスト用
pytest>=7.3.0
pytest-cov>=4.0.0
pytest-mock>=3.10.0
black>=23.3.0
flake8>=6.0.0
isort>=5.12.0
mypy>=1.3.0

# Jupyter関連
jupyter>=1.0.0
ipykernel>=6.23.0
matplotlib>=3.7.0
seaborn>=0.12.0

# その他ユーティリティ
psutil>=5.9.0
cryptography>=40.0.0
gitpython>=3.1.0
```

#### config/dev_config.yaml

```yaml
# 開発環境設定
environment: development
debug: true

# パス設定
paths:
  base_dir: "."
  data_dir: "data"
  frames_dir: "data/frames"
  templates_dir: "data/templates"
  output_dir: "data/output"
  logs_dir: "logs"

# 処理設定
processing:
  max_workers: 4
  gpu_enabled: false
  memory_limit: "4GB"
  
# テンプレートマッチング
template_matching:
  threshold: 0.5
  cluster_gap: 5
  step: 1

# aHash設定
ahash:
  size: 8
  threshold: 10

# デバッグ設定
debug:
  verbose: true
  save_intermediate: true
  profile_performance: true

# テスト設定
testing:
  use_small_dataset: true
  test_data_dir: "tests/test_data"
  skip_gpu_tests: true
```

### 5. ユーティリティスクリプト

#### utils/dev_setup.py

```python
#!/usr/bin/env python3
"""
開発環境セットアップスクリプト
"""
import os
import sys
import subprocess
import platform
from pathlib import Path

def check_python_version():
    """Python バージョンチェック"""
    version = sys.version_info
    if version.major != 3 or version.minor < 8:
        print("❌ Python 3.8以上が必要です")
        sys.exit(1)
    print(f"✅ Python {version.major}.{version.minor}.{version.micro}")

def setup_virtual_environment():
    """仮想環境のセットアップ"""
    venv_path = Path("venv")
    
    if not venv_path.exists():
        print("🔧 仮想環境を作成中...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ 仮想環境作成完了")
    else:
        print("✅ 仮想環境は既に存在します")
    
    # 仮想環境のpythonパス
    if platform.system() == "Windows":
        python_path = venv_path / "Scripts" / "python.exe"
        pip_path = venv_path / "Scripts" / "pip.exe"
    else:
        python_path = venv_path / "bin" / "python"
        pip_path = venv_path / "bin" / "pip"
    
    return python_path, pip_path

def install_dependencies(pip_path):
    """依存関係のインストール"""
    requirements_files = [
        "requirements/requirements_dev.txt",
        "requirements/requirements_base.txt"
    ]
    
    for req_file in requirements_files:
        if Path(req_file).exists():
            print(f"📦 {req_file} をインストール中...")
            subprocess.run([str(pip_path), "install", "-r", req_file], check=True)
            print(f"✅ {req_file} インストール完了")

def setup_pre_commit():
    """pre-commit フックのセットアップ"""
    if Path(".pre-commit-config.yaml").exists():
        try:
            subprocess.run(["pre-commit", "install"], check=True)
            print("✅ pre-commit フック設定完了")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("⚠ pre-commit のインストールが必要です: pip install pre-commit")

def create_directory_structure():
    """ディレクトリ構造の作成"""
    directories = [
        "src",
        "tests/test_data",
        "notebooks",
        "docs",
        "config",
        "utils",
        "data/frames",
        "data/templates",
        "data/output",
        "logs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    print("✅ ディレクトリ構造作成完了")

def main():
    """メイン処理"""
    print("🚀 MapSight_AI 開発環境セットアップ開始")
    
    # Python バージョンチェック
    check_python_version()
    
    # ディレクトリ構造作成
    create_directory_structure()
    
    # 仮想環境セットアップ
    python_path, pip_path = setup_virtual_environment()
    
    # 依存関係インストール
    install_dependencies(pip_path)
    
    # pre-commit セットアップ
    setup_pre_commit()
    
    print("\n🎉 開発環境セットアップ完了!")
    print("\n次のステップ:")
    print("1. VSCode で .vscode/settings.json の python.defaultInterpreterPath を確認")
    print("2. 'source venv/bin/activate' で仮想環境を有効化")
    print("3. 'python utils/env_checker.py' で環境確認")

if __name__ == "__main__":
    main()
```

## 🌐 Google Colab 環境設定

### 1. Colab用設定ファイル

#### config/colab_config.yaml

```yaml
# Google Colab環境設定
environment: colab
debug: false

# パス設定
paths:
  base_dir: "/content/drive/MyDrive/MapSight_AI"
  data_dir: "/content/drive/MyDrive/MapSight_AI/data"
  frames_dir: "/content/drive/MyDrive/MapSight_AI/data/frames"
  templates_dir: "/content/drive/MyDrive/MapSight_AI/data/templates"
  output_dir: "/content/drive/MyDrive/MapSight_AI/data/output"
  temp_dir: "/content/temp"

# 処理設定
processing:
  max_workers: 8
  gpu_enabled: true
  memory_limit: "12GB"
  session_timeout: 43200  # 12時間

# 高速化設定
optimization:
  use_gpu: true
  batch_processing: true
  parallel_execution: true
  memory_efficient: true

# セッション管理
session:
  keep_alive: true
  keep_alive_interval: 300  # 5分
  auto_save_interval: 1800  # 30分
```

#### requirements/requirements_colab.txt

```txt
# Colab特化パッケージ
easyocr>=1.7.0
yt-dlp>=2023.7.6
ffmpeg-python>=0.2.0

# 基本パッケージ（Colabで更新が必要な場合）
opencv-python>=4.8.0
numpy>=1.24.0
PyYAML>=6.0
tqdm>=4.65.0
matplotlib>=3.7.0

# GPU加速
torch>=2.0.0
torchvision>=0.15.0
```

### 2. Colab初期化スクリプト

#### utils/colab_init.py

```python
"""
Google Colab 初期化スクリプト
"""
import os
import sys
import time
import subprocess
import threading
from pathlib import Path
import json

def mount_google_drive():
    """Google Drive のマウント"""
    try:
        from google.colab import drive
        drive.mount('/content/drive')
        print("✅ Google Drive マウント完了")
        return True
    except ImportError:
        print("❌ Colab環境ではありません")
        return False
    except Exception as e:
        print(f"❌ Google Drive マウント失敗: {e}")
        return False

def setup_project_directory():
    """プロジェクトディレクトリの確認・作成"""
    project_path = Path("/content/drive/MyDrive/MapSight_AI")
    
    if not project_path.exists():
        print("🔧 プロジェクトディレクトリを作成中...")
        project_path.mkdir(parents=True)
        
        # 必要なサブディレクトリ作成
        subdirs = [
            "data/frames",
            "data/templates", 
            "data/output",
            "data/checkpoints",
            "logs"
        ]
        for subdir in subdirs:
            (project_path / subdir).mkdir(parents=True, exist_ok=True)
        
        print("✅ プロジェクトディレクトリ作成完了")
    else:
        print("✅ プロジェクトディレクトリ確認済み")
    
    return project_path

def sync_code_from_github(repo_url="https://github.com/your-repo/MapSight_AI.git"):
    """GitHub からコードの同期"""
    local_path = Path("/content/MapSight_AI")
    
    if local_path.exists():
        print("🔧 既存コードを更新中...")
        os.chdir(local_path)
        subprocess.run(["git", "pull"], check=True)
    else:
        print("🔧 GitHubからコードをクローン中...")
        subprocess.run(["git", "clone", repo_url, str(local_path)], check=True)
    
    os.chdir(local_path)
    print("✅ コード同期完了")
    return local_path

def install_colab_requirements():
    """Colab用パッケージのインストール"""
    requirements_file = "requirements/requirements_colab.txt"
    
    if Path(requirements_file).exists():
        print("📦 Colab用パッケージインストール中...")
        subprocess.run([
            sys.executable, "-m", "pip", "install", "-q", "-r", requirements_file
        ], check=True)
        print("✅ パッケージインストール完了")
    
    # システムパッケージ
    system_packages = ["ffmpeg"]
    for package in system_packages:
        try:
            subprocess.run(["apt-get", "install", "-y", "-qq", package], 
                         check=True, capture_output=True)
            print(f"✅ {package} インストール完了")
        except subprocess.CalledProcessError:
            print(f"⚠ {package} インストール失敗")

def setup_session_keeper():
    """セッション維持機能"""
    def keep_alive():
        while True:
            time.sleep(300)  # 5分間隔
            print("🔄", end="", flush=True)
    
    thread = threading.Thread(target=keep_alive, daemon=True)
    thread.start()
    print("✅ セッション維持機能開始")

def check_gpu_availability():
    """GPU利用可能性チェック"""
    try:
        import torch
        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0)
            gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1e9
            print(f"✅ GPU利用可能: {gpu_name} ({gpu_memory:.1f}GB)")
            return True
        else:
            print("⚠ GPU利用不可 - CPU実行")
            return False
    except ImportError:
        print("⚠ PyTorch未インストール - GPU確認不可")
        return False

def setup_environment_variables():
    """環境変数の設定"""
    env_vars = {
        "PYTHONPATH": "/content/MapSight_AI/src:/content/MapSight_AI",
        "MAPSIGHT_ENV": "colab",
        "MAPSIGHT_BASE": "/content/drive/MyDrive/MapSight_AI"
    }
    
    for key, value in env_vars.items():
        os.environ[key] = value
    
    print("✅ 環境変数設定完了")

def create_colab_config():
    """Colab用設定ファイルの作成"""
    config = {
        "environment": "colab",
        "gpu_available": check_gpu_availability(),
        "setup_timestamp": time.time(),
        "paths": {
            "project_root": "/content/drive/MyDrive/MapSight_AI",
            "code_root": "/content/MapSight_AI",
            "temp_dir": "/content/temp"
        }
    }
    
    config_path = Path("/content/colab_config.json")
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print("✅ Colab設定ファイル作成完了")

def main():
    """Colab初期化メイン処理"""
    print("🚀 Google Colab 環境初期化開始")
    
    # Google Drive マウント
    if not mount_google_drive():
        return False
    
    # プロジェクトディレクトリ設定
    project_path = setup_project_directory()
    
    # コード同期
    code_path = sync_code_from_github()
    
    # パッケージインストール
    install_colab_requirements()
    
    # 環境変数設定
    setup_environment_variables()
    
    # GPU確認
    gpu_available = check_gpu_availability()
    
    # セッション維持開始
    setup_session_keeper()
    
    # 設定ファイル作成
    create_colab_config()
    
    print("\n🎉 Colab環境初期化完了!")
    print(f"📁 プロジェクトパス: {project_path}")
    print(f"💻 コードパス: {code_path}")
    print(f"🖥️ GPU利用可能: {gpu_available}")
    print("\n次のステップ:")
    print("1. 必要なデータファイル（テンプレート等）をアップロード")
    print("2. production.ipynb を開いて処理実行")
    
    return True

if __name__ == "__main__":
    main()
```

### 3. Colab用ノートブックテンプレート

#### notebooks/colab_template.ipynb

```python
# Cell 1: 環境初期化
import sys
import os

# Colab初期化
if 'google.colab' in sys.modules:
    # 初期化スクリプト実行
    !python utils/colab_init.py
    
    # 作業ディレクトリ移動
    os.chdir('/content/MapSight_AI')
    
    # パス追加
    sys.path.append('/content/MapSight_AI/src')
    sys.path.append('/content/MapSight_AI/utils')

print("環境初期化完了")

# Cell 2: 設定読み込み
import yaml
from pathlib import Path
from utils.path_manager import PathManager
from utils.env_checker import EnvironmentChecker

# パスマネージャー初期化
pm = PathManager()
print(f"作業環境: {'Colab' if pm.is_colab else 'ローカル'}")
print(f"ベースパス: {pm.base_path}")

# 設定ファイル読み込み
config_path = pm.config_path()
with open(config_path, 'r') as f:
    config = yaml.safe_load(f)

print("設定読み込み完了")

# Cell 3: 環境確認
checker = EnvironmentChecker()
if checker.is_colab:
    checker.setup_colab_environment()

# 依存関係確認
missing, mismatches = checker.check_environment()
if missing:
    print(f"不足パッケージ: {missing}")
    checker.install_missing_packages(missing)

print("環境確認完了")

# Cell 4: GPU設定
import torch

if torch.cuda.is_available():
    device = torch.device('cuda')
    print(f"GPU使用: {torch.cuda.get_device_name(0)}")
    print(f"GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f}GB")
    
    # メモリクリア
    torch.cuda.empty_cache()
else:
    device = torch.device('cpu')
    print("CPU使用")

# Cell 5: データ確認
# フレームデータ確認
frames_dirs = list(pm.get_path("data/frames").glob("*"))
if frames_dirs:
    print("利用可能なフレームデータ:")
    for frames_dir in frames_dirs:
        frame_count = len(list(frames_dir.glob("*.jpg")))
        print(f"  {frames_dir.name}: {frame_count}フレーム")
else:
    print("フレームデータが見つかりません")

# テンプレート確認
template_path = pm.template_path()
if template_path.exists():
    print(f"テンプレート: {template_path}")
else:
    print("テンプレートファイルをアップロードしてください")

# Cell 6: 処理実行準備
# ここから実際の処理を記述
print("処理実行準備完了")
```

## 🔧 開発支援ツール

### 1. 自動同期スクリプト

#### utils/auto_sync.py

```python
"""
VSCodeとColab間の自動同期
"""
import os
import json
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ColabSyncHandler(FileSystemEventHandler):
    """ファイル変更監視ハンドラー"""
    
    def __init__(self, sync_config):
        self.sync_config = sync_config
        self.last_sync = {}
    
    def on_modified(self, event):
        if event.is_directory:
            return
        
        file_path = Path(event.src_path)
        
        # 同期対象ファイルかチェック
        if self.should_sync(file_path):
            self.sync_to_colab(file_path)
    
    def should_sync(self, file_path):
        """同期対象ファイルの判定"""
        sync_extensions = {'.py', '.yaml', '.yml', '.md', '.txt'}
        exclude_patterns = {'__pycache__', '.git', 'venv', '.pytest_cache'}
        
        # 拡張子チェック
        if file_path.suffix not in sync_extensions:
            return False
        
        # 除外パターンチェック
        for pattern in exclude_patterns:
            if pattern in str(file_path):
                return False
        
        return True
    
    def sync_to_colab(self, file_path):
        """Colabへの同期"""
        # 実装: Google Drive API または rclone 使用
        print(f"Syncing: {file_path}")

def start_auto_sync():
    """自動同期の開始"""
    config_path = Path("config/sync_config.json")
    if config_path.exists():
        with open(config_path, 'r') as f:
            sync_config = json.load(f)
    else:
        sync_config = {"auto_sync": False}
    
    if sync_config.get("auto_sync", False):
        event_handler = ColabSyncHandler(sync_config)
        observer = Observer()
        observer.schedule(event_handler, ".", recursive=True)
        observer.start()
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    else:
        print("自動同期は無効です")

if __name__ == "__main__":
    start_auto_sync()
```

### 2. デバッグ支援

#### utils/debug_helper.py

```python
"""
デバッグ支援ユーティリティ
"""
import time
import traceback
import functools
from typing import Any, Callable

def debug_timer(func: Callable) -> Callable:
    """実行時間測定デコレータ"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            print(f"🕐 {func.__name__}: {execution_time:.3f}秒")
            return result
        except Exception as e:
            execution_time = time.time() - start_time
            print(f"❌ {func.__name__}: {execution_time:.3f}秒 (エラー)")
            print(f"Error: {e}")
            traceback.print_exc()
            raise
    return wrapper

def debug_memory(func: Callable) -> Callable:
    """メモリ使用量監視デコレータ"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            import psutil
            process = psutil.Process()
            mem_before = process.memory_info().rss / 1024 / 1024  # MB
            
            result = func(*args, **kwargs)
            
            mem_after = process.memory_info().rss / 1024 / 1024  # MB
            mem_diff = mem_after - mem_before
            
            print(f"🧠 {func.__name__}: メモリ使用量 {mem_diff:+.1f}MB")
            return result
        except ImportError:
            return func(*args, **kwargs)
    return wrapper

class DebugContext:
    """デバッグコンテキストマネージャー"""
    
    def __init__(self, name: str, verbose: bool = True):
        self.name = name
        self.verbose = verbose
        self.start_time = None
    
    def __enter__(self):
        if self.verbose:
            print(f"🚀 開始: {self.name}")
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start_time
        if exc_type is None:
            if self.verbose:
                print(f"✅ 完了: {self.name} ({elapsed:.3f}秒)")
        else:
            if self.verbose:
                print(f"❌ エラー: {self.name} ({elapsed:.3f}秒)")
                print(f"Error: {exc_val}")
        return False  # 例外を再発生

# 使用例
@debug_timer
@debug_memory
def example_function():
    time.sleep(1)
    return "完了"

# コンテキストマネージャー使用例
with DebugContext("データ処理"):
    # 処理実行
    pass
```

この設定により、VSCodeとGoogle Colabを効率的に組み合わせた開発環境を構築できます。特にパス管理や環境差異の吸収、自動同期機能により、シームレスな開発体験を実現できます。
