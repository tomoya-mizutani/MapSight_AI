# MAP_SIGHT_AI

## システム概観図

### システム概要

``` text
[試合録画またはライブフィード]
          ↓（2秒間隔）
[マップ画像データ取得]
          ↓
[位置・状況データ抽出]
   ・プレイヤー位置(x,y,z)
   ・安全圏情報
   ・イベント情報（撃破、交戦）
          ↓
[データ前処理]
   ・座標正規化
   ・チーム単位のデータ統合
          ↓
[分析モデル適用]
   │
   ├───→ [行動予測モデル]
   │             ・時系列モデル（LSTM、Transformer）
   │             ・グラフニューラルネットワーク（GNN）
   │
   ├───→ [重要イベント検出]
   │             ・撃破、交戦開始などの検出
   │
   └───→ [戦術理論モデル]
                 ・安全圏戦略
                 ・カバーリング理論
                 ・物資取得・管理
                 ・エリアコントロール
                 ・リスク管理
          ↓
[分析結果統合]
          ↓
[テキストレポート生成]
   ・戦術的アドバイス
   ・イベントタイムライン
   ・次回試合への改善ポイント
          ↓
[可視化オプション]
   ・マップ軌跡表示
   ・イベントマーカー表示
          ↓
[コーチ・選手向け出力]
```

## 開発環境

terminal :bash  
python version is 3.12.3  
git version is 2.43.0.windows.1  

仮想環境: python3.12-venv  
起動コマンド: source ~/pubgmapenv/bin/activate  
終了コマンド:deactivate  

## 📂 ディレクトリ構造図
<!-- DIR-START -->
``` text
.
├── .git
.
|-- .github
|   |-- ISSUE_TEMPLATE
|   |   |-- bug.yaml
|   |   |-- log.yaml
|   |   `-- task.yaml
|   `-- workflows
|       |-- auto_ai_PR.yml
|       |-- daily-digest.yml
|       `-- update-tree.yml
|-- .venv
|   |-- bin
|   |   |-- Activate.ps1
|   |   |-- activate
|   |   |-- activate.csh
|   |   |-- activate.fish
|   |   |-- f2py
|   |   |-- fonttools
|   |   |-- numpy-config
|   |   |-- py.test
|   |   |-- pyftmerge
|   |   |-- pyftsubset
|   |   |-- pygmentize
|   |   |-- pytest
|   |   |-- python -> python3
|   |   |-- python3 -> /usr/bin/python3
|   |   |-- python3.12 -> python3
|   |   |-- tqdm
|   |   `-- ttx
|   |-- lib
|   |   `-- python3.12
|   |       `-- site-packages
|   |           |-- PIL
|   |           |   |-- __pycache__
|   |           |   |   |-- AvifImagePlugin.cpython-312.pyc
|   |           |   |   |-- BdfFontFile.cpython-312.pyc
|   |           |   |   |-- BlpImagePlugin.cpython-312.pyc
|   |           |   |   |-- BmpImagePlugin.cpython-312.pyc
|   |           |   |   |-- BufrStubImagePlugin.cpython-312.pyc
|   |           |   |   |-- ContainerIO.cpython-312.pyc
|   |           |   |   |-- CurImagePlugin.cpython-312.pyc
|   |           |   |   |-- DcxImagePlugin.cpython-312.pyc
|   |           |   |   |-- DdsImagePlugin.cpython-312.pyc
|   |           |   |   |-- EpsImagePlugin.cpython-312.pyc
|   |           |   |   |-- ExifTags.cpython-312.pyc
|   |           |   |   |-- FitsImagePlugin.cpython-312.pyc
|   |           |   |   |-- FliImagePlugin.cpython-312.pyc
|   |           |   |   |-- FontFile.cpython-312.pyc
|   |           |   |   |-- FpxImagePlugin.cpython-312.pyc
|   |           |   |   |-- FtexImagePlugin.cpython-312.pyc
|   |           |   |   |-- GbrImagePlugin.cpython-312.pyc
|   |           |   |   |-- GdImageFile.cpython-312.pyc
|   |           |   |   |-- GifImagePlugin.cpython-312.pyc
|   |           |   |   |-- GimpGradientFile.cpython-312.pyc
|   |           |   |   |-- GimpPaletteFile.cpython-312.pyc
|   |           |   |   |-- GribStubImagePlugin.cpython-312.pyc
|   |           |   |   |-- Hdf5StubImagePlugin.cpython-312.pyc
|   |           |   |   |-- IcnsImagePlugin.cpython-312.pyc
|   |           |   |   |-- IcoImagePlugin.cpython-312.pyc
|   |           |   |   |-- ImImagePlugin.cpython-312.pyc
|   |           |   |   |-- Image.cpython-312.pyc
|   |           |   |   |-- ImageChops.cpython-312.pyc
|   |           |   |   |-- ImageCms.cpython-312.pyc
|   |           |   |   |-- ImageColor.cpython-312.pyc
|   |           |   |   |-- ImageDraw.cpython-312.pyc
|   |           |   |   |-- ImageDraw2.cpython-312.pyc
|   |           |   |   |-- ImageEnhance.cpython-312.pyc
|   |           |   |   |-- ImageFile.cpython-312.pyc
|   |           |   |   |-- ImageFilter.cpython-312.pyc
|   |           |   |   |-- ImageFont.cpython-312.pyc
|   |           |   |   |-- ImageGrab.cpython-312.pyc
|   |           |   |   |-- ImageMath.cpython-312.pyc
|   |           |   |   |-- ImageMode.cpython-312.pyc
|   |           |   |   |-- ImageMorph.cpython-312.pyc
|   |           |   |   |-- ImageOps.cpython-312.pyc
|   |           |   |   |-- ImagePalette.cpython-312.pyc
|   |           |   |   |-- ImagePath.cpython-312.pyc
|   |           |   |   |-- ImageQt.cpython-312.pyc
|   |           |   |   |-- ImageSequence.cpython-312.pyc
|   |           |   |   |-- ImageShow.cpython-312.pyc
|   |           |   |   |-- ImageStat.cpython-312.pyc
|   |           |   |   |-- ImageTk.cpython-312.pyc
|   |           |   |   |-- ImageTransform.cpython-312.pyc
|   |           |   |   |-- ImageWin.cpython-312.pyc
|   |           |   |   |-- ImtImagePlugin.cpython-312.pyc
|   |           |   |   |-- IptcImagePlugin.cpython-312.pyc
|   |           |   |   |-- Jpeg2KImagePlugin.cpython-312.pyc
|   |           |   |   |-- JpegImagePlugin.cpython-312.pyc
|   |           |   |   |-- JpegPresets.cpython-312.pyc
|   |           |   |   |-- McIdasImagePlugin.cpython-312.pyc
|   |           |   |   |-- MicImagePlugin.cpython-312.pyc
|   |           |   |   |-- MpegImagePlugin.cpython-312.pyc
|   |           |   |   |-- MpoImagePlugin.cpython-312.pyc
|   |           |   |   |-- MspImagePlugin.cpython-312.pyc
|   |           |   |   |-- PSDraw.cpython-312.pyc
|   |           |   |   |-- PaletteFile.cpython-312.pyc
|   |           |   |   |-- PalmImagePlugin.cpython-312.pyc
|   |           |   |   |-- PcdImagePlugin.cpython-312.pyc
|   |           |   |   |-- PcfFontFile.cpython-312.pyc
|   |           |   |   |-- PcxImagePlugin.cpython-312.pyc
|   |           |   |   |-- PdfImagePlugin.cpython-312.pyc
|   |           |   |   |-- PdfParser.cpython-312.pyc
|   |           |   |   |-- PixarImagePlugin.cpython-312.pyc
|   |           |   |   |-- PngImagePlugin.cpython-312.pyc
|   |           |   |   |-- PpmImagePlugin.cpython-312.pyc
|   |           |   |   |-- PsdImagePlugin.cpython-312.pyc
|   |           |   |   |-- QoiImagePlugin.cpython-312.pyc
|   |           |   |   |-- SgiImagePlugin.cpython-312.pyc
|   |           |   |   |-- SpiderImagePlugin.cpython-312.pyc
|   |           |   |   |-- SunImagePlugin.cpython-312.pyc
|   |           |   |   |-- TarIO.cpython-312.pyc
|   |           |   |   |-- TgaImagePlugin.cpython-312.pyc
|   |           |   |   |-- TiffImagePlugin.cpython-312.pyc
|   |           |   |   |-- TiffTags.cpython-312.pyc
|   |           |   |   |-- WalImageFile.cpython-312.pyc
|   |           |   |   |-- WebPImagePlugin.cpython-312.pyc
|   |           |   |   |-- WmfImagePlugin.cpython-312.pyc
|   |           |   |   |-- XVThumbImagePlugin.cpython-312.pyc
|   |           |   |   |-- XbmImagePlugin.cpython-312.pyc
|   |           |   |   |-- XpmImagePlugin.cpython-312.pyc
|   |           |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |-- _binary.cpython-312.pyc
|   |           |   |   |-- _deprecate.cpython-312.pyc
|   |           |   |   |-- _tkinter_finder.cpython-312.pyc
|   |           |   |   |-- _typing.cpython-312.pyc
|   |           |   |   |-- _util.cpython-312.pyc
|   |           |   |   |-- _version.cpython-312.pyc
|   |           |   |   |-- features.cpython-312.pyc
|   |           |   |   `-- report.cpython-312.pyc
|   |           |   |-- AvifImagePlugin.py
|   |           |   |-- BdfFontFile.py
|   |           |   |-- BlpImagePlugin.py
|   |           |   |-- BmpImagePlugin.py
|   |           |   |-- BufrStubImagePlugin.py
|   |           |   |-- ContainerIO.py
|   |           |   |-- CurImagePlugin.py
|   |           |   |-- DcxImagePlugin.py
|   |           |   |-- DdsImagePlugin.py
|   |           |   |-- EpsImagePlugin.py
|   |           |   |-- ExifTags.py
|   |           |   |-- FitsImagePlugin.py
|   |           |   |-- FliImagePlugin.py
|   |           |   |-- FontFile.py
|   |           |   |-- FpxImagePlugin.py
|   |           |   |-- FtexImagePlugin.py
|   |           |   |-- GbrImagePlugin.py
|   |           |   |-- GdImageFile.py
|   |           |   |-- GifImagePlugin.py
|   |           |   |-- GimpGradientFile.py
|   |           |   |-- GimpPaletteFile.py
|   |           |   |-- GribStubImagePlugin.py
|   |           |   |-- Hdf5StubImagePlugin.py
|   |           |   |-- IcnsImagePlugin.py
|   |           |   |-- IcoImagePlugin.py
|   |           |   |-- ImImagePlugin.py
|   |           |   |-- Image.py
|   |           |   |-- ImageChops.py
|   |           |   |-- ImageCms.py
|   |           |   |-- ImageColor.py
|   |           |   |-- ImageDraw.py
|   |           |   |-- ImageDraw2.py
|   |           |   |-- ImageEnhance.py
|   |           |   |-- ImageFile.py
|   |           |   |-- ImageFilter.py
|   |           |   |-- ImageFont.py
|   |           |   |-- ImageGrab.py
|   |           |   |-- ImageMath.py
|   |           |   |-- ImageMode.py
|   |           |   |-- ImageMorph.py
|   |           |   |-- ImageOps.py
|   |           |   |-- ImagePalette.py
|   |           |   |-- ImagePath.py
|   |           |   |-- ImageQt.py
|   |           |   |-- ImageSequence.py
|   |           |   |-- ImageShow.py
|   |           |   |-- ImageStat.py
|   |           |   |-- ImageTk.py
|   |           |   |-- ImageTransform.py
|   |           |   |-- ImageWin.py
|   |           |   |-- ImtImagePlugin.py
|   |           |   |-- IptcImagePlugin.py
|   |           |   |-- Jpeg2KImagePlugin.py
|   |           |   |-- JpegImagePlugin.py
|   |           |   |-- JpegPresets.py
|   |           |   |-- McIdasImagePlugin.py
|   |           |   |-- MicImagePlugin.py
|   |           |   |-- MpegImagePlugin.py
|   |           |   |-- MpoImagePlugin.py
|   |           |   |-- MspImagePlugin.py
|   |           |   |-- PSDraw.py
|   |           |   |-- PaletteFile.py
|   |           |   |-- PalmImagePlugin.py
|   |           |   |-- PcdImagePlugin.py
|   |           |   |-- PcfFontFile.py
|   |           |   |-- PcxImagePlugin.py
|   |           |   |-- PdfImagePlugin.py
|   |           |   |-- PdfParser.py
|   |           |   |-- PixarImagePlugin.py
|   |           |   |-- PngImagePlugin.py
|   |           |   |-- PpmImagePlugin.py
|   |           |   |-- PsdImagePlugin.py
|   |           |   |-- QoiImagePlugin.py
|   |           |   |-- SgiImagePlugin.py
|   |           |   |-- SpiderImagePlugin.py
|   |           |   |-- SunImagePlugin.py
|   |           |   |-- TarIO.py
|   |           |   |-- TgaImagePlugin.py
|   |           |   |-- TiffImagePlugin.py
|   |           |   |-- TiffTags.py
|   |           |   |-- WalImageFile.py
|   |           |   |-- WebPImagePlugin.py
|   |           |   |-- WmfImagePlugin.py
|   |           |   |-- XVThumbImagePlugin.py
|   |           |   |-- XbmImagePlugin.py
|   |           |   |-- XpmImagePlugin.py
|   |           |   |-- __init__.py
|   |           |   |-- __main__.py
|   |           |   |-- _avif.cpython-312-x86_64-linux-gnu.so
|   |           |   |-- _avif.pyi
|   |           |   |-- _binary.py
|   |           |   |-- _deprecate.py
|   |           |   |-- _imaging.cpython-312-x86_64-linux-gnu.so
|   |           |   |-- _imaging.pyi
|   |           |   |-- _imagingcms.cpython-312-x86_64-linux-gnu.so
|   |           |   |-- _imagingcms.pyi
|   |           |   |-- _imagingft.cpython-312-x86_64-linux-gnu.so
|   |           |   |-- _imagingft.pyi
|   |           |   |-- _imagingmath.cpython-312-x86_64-linux-gnu.so
|   |           |   |-- _imagingmath.pyi
|   |           |   |-- _imagingmorph.cpython-312-x86_64-linux-gnu.so
|   |           |   |-- _imagingmorph.pyi
|   |           |   |-- _imagingtk.cpython-312-x86_64-linux-gnu.so
|   |           |   |-- _imagingtk.pyi
|   |           |   |-- _tkinter_finder.py
|   |           |   |-- _typing.py
|   |           |   |-- _util.py
|   |           |   |-- _version.py
|   |           |   |-- _webp.cpython-312-x86_64-linux-gnu.so
|   |           |   |-- _webp.pyi
|   |           |   |-- features.py
|   |           |   |-- py.typed
|   |           |   `-- report.py
|   |           |-- __pycache__
|   |           |   |-- py.cpython-312.pyc
|   |           |   `-- six.cpython-312.pyc
|   |           |-- _pytest
|   |           |   |-- __pycache__
|   |           |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |-- _argcomplete.cpython-312.pyc
|   |           |   |   |-- _version.cpython-312.pyc
|   |           |   |   |-- cacheprovider.cpython-312.pyc
|   |           |   |   |-- capture.cpython-312.pyc
|   |           |   |   |-- compat.cpython-312.pyc
|   |           |   |   |-- debugging.cpython-312.pyc
|   |           |   |   |-- deprecated.cpython-312.pyc
|   |           |   |   |-- doctest.cpython-312.pyc
|   |           |   |   |-- faulthandler.cpython-312.pyc
|   |           |   |   |-- fixtures.cpython-312.pyc
|   |           |   |   |-- freeze_support.cpython-312.pyc
|   |           |   |   |-- helpconfig.cpython-312.pyc
|   |           |   |   |-- hookspec.cpython-312.pyc
|   |           |   |   |-- junitxml.cpython-312.pyc
|   |           |   |   |-- legacypath.cpython-312.pyc
|   |           |   |   |-- logging.cpython-312.pyc
|   |           |   |   |-- main.cpython-312.pyc
|   |           |   |   |-- monkeypatch.cpython-312.pyc
|   |           |   |   |-- nodes.cpython-312.pyc
|   |           |   |   |-- outcomes.cpython-312.pyc
|   |           |   |   |-- pastebin.cpython-312.pyc
|   |           |   |   |-- pathlib.cpython-312.pyc
|   |           |   |   |-- pytester.cpython-312.pyc
|   |           |   |   |-- pytester_assertions.cpython-312.pyc
|   |           |   |   |-- python.cpython-312.pyc
|   |           |   |   |-- python_api.cpython-312.pyc
|   |           |   |   |-- raises.cpython-312.pyc
|   |           |   |   |-- recwarn.cpython-312.pyc
|   |           |   |   |-- reports.cpython-312.pyc
|   |           |   |   |-- runner.cpython-312.pyc
|   |           |   |   |-- scope.cpython-312.pyc
|   |           |   |   |-- setuponly.cpython-312.pyc
|   |           |   |   |-- setupplan.cpython-312.pyc
|   |           |   |   |-- skipping.cpython-312.pyc
|   |           |   |   |-- stash.cpython-312.pyc
|   |           |   |   |-- stepwise.cpython-312.pyc
|   |           |   |   |-- terminal.cpython-312.pyc
|   |           |   |   |-- threadexception.cpython-312.pyc
|   |           |   |   |-- timing.cpython-312.pyc
|   |           |   |   |-- tmpdir.cpython-312.pyc
|   |           |   |   |-- tracemalloc.cpython-312.pyc
|   |           |   |   |-- unittest.cpython-312.pyc
|   |           |   |   |-- unraisableexception.cpython-312.pyc
|   |           |   |   |-- warning_types.cpython-312.pyc
|   |           |   |   `-- warnings.cpython-312.pyc
|   |           |   |-- _code
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- code.cpython-312.pyc
|   |           |   |   |   `-- source.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- code.py
|   |           |   |   `-- source.py
|   |           |   |-- _io
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- pprint.cpython-312.pyc
|   |           |   |   |   |-- saferepr.cpython-312.pyc
|   |           |   |   |   |-- terminalwriter.cpython-312.pyc
|   |           |   |   |   `-- wcwidth.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- pprint.py
|   |           |   |   |-- saferepr.py
|   |           |   |   |-- terminalwriter.py
|   |           |   |   `-- wcwidth.py
|   |           |   |-- _py
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- error.cpython-312.pyc
|   |           |   |   |   `-- path.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- error.py
|   |           |   |   `-- path.py
|   |           |   |-- assertion
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- rewrite.cpython-312.pyc
|   |           |   |   |   |-- truncate.cpython-312.pyc
|   |           |   |   |   `-- util.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- rewrite.py
|   |           |   |   |-- truncate.py
|   |           |   |   `-- util.py
|   |           |   |-- config
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- argparsing.cpython-312.pyc
|   |           |   |   |   |-- compat.cpython-312.pyc
|   |           |   |   |   |-- exceptions.cpython-312.pyc
|   |           |   |   |   `-- findpaths.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- argparsing.py
|   |           |   |   |-- compat.py
|   |           |   |   |-- exceptions.py
|   |           |   |   `-- findpaths.py
|   |           |   |-- mark
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- expression.cpython-312.pyc
|   |           |   |   |   `-- structures.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- expression.py
|   |           |   |   `-- structures.py
|   |           |   |-- __init__.py
|   |           |   |-- _argcomplete.py
|   |           |   |-- _version.py
|   |           |   |-- cacheprovider.py
|   |           |   |-- capture.py
|   |           |   |-- compat.py
|   |           |   |-- debugging.py
|   |           |   |-- deprecated.py
|   |           |   |-- doctest.py
|   |           |   |-- faulthandler.py
|   |           |   |-- fixtures.py
|   |           |   |-- freeze_support.py
|   |           |   |-- helpconfig.py
|   |           |   |-- hookspec.py
|   |           |   |-- junitxml.py
|   |           |   |-- legacypath.py
|   |           |   |-- logging.py
|   |           |   |-- main.py
|   |           |   |-- monkeypatch.py
|   |           |   |-- nodes.py
|   |           |   |-- outcomes.py
|   |           |   |-- pastebin.py
|   |           |   |-- pathlib.py
|   |           |   |-- py.typed
|   |           |   |-- pytester.py
|   |           |   |-- pytester_assertions.py
|   |           |   |-- python.py
|   |           |   |-- python_api.py
|   |           |   |-- raises.py
|   |           |   |-- recwarn.py
|   |           |   |-- reports.py
|   |           |   |-- runner.py
|   |           |   |-- scope.py
|   |           |   |-- setuponly.py
|   |           |   |-- setupplan.py
|   |           |   |-- skipping.py
|   |           |   |-- stash.py
|   |           |   |-- stepwise.py
|   |           |   |-- terminal.py
|   |           |   |-- threadexception.py
|   |           |   |-- timing.py
|   |           |   |-- tmpdir.py
|   |           |   |-- tracemalloc.py
|   |           |   |-- unittest.py
|   |           |   |-- unraisableexception.py
|   |           |   |-- warning_types.py
|   |           |   `-- warnings.py
|   |           |-- contourpy
|   |           |   |-- __pycache__
|   |           |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |-- _version.cpython-312.pyc
|   |           |   |   |-- array.cpython-312.pyc
|   |           |   |   |-- chunk.cpython-312.pyc
|   |           |   |   |-- convert.cpython-312.pyc
|   |           |   |   |-- dechunk.cpython-312.pyc
|   |           |   |   |-- enum_util.cpython-312.pyc
|   |           |   |   |-- typecheck.cpython-312.pyc
|   |           |   |   `-- types.cpython-312.pyc
|   |           |   |-- util
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _build_config.cpython-312.pyc
|   |           |   |   |   |-- bokeh_renderer.cpython-312.pyc
|   |           |   |   |   |-- bokeh_util.cpython-312.pyc
|   |           |   |   |   |-- data.cpython-312.pyc
|   |           |   |   |   |-- mpl_renderer.cpython-312.pyc
|   |           |   |   |   |-- mpl_util.cpython-312.pyc
|   |           |   |   |   `-- renderer.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- _build_config.py
|   |           |   |   |-- bokeh_renderer.py
|   |           |   |   |-- bokeh_util.py
|   |           |   |   |-- data.py
|   |           |   |   |-- mpl_renderer.py
|   |           |   |   |-- mpl_util.py
|   |           |   |   `-- renderer.py
|   |           |   |-- __init__.py
|   |           |   |-- _contourpy.cpython-312-x86_64-linux-gnu.so
|   |           |   |-- _contourpy.pyi
|   |           |   |-- _version.py
|   |           |   |-- array.py
|   |           |   |-- chunk.py
|   |           |   |-- convert.py
|   |           |   |-- dechunk.py
|   |           |   |-- enum_util.py
|   |           |   |-- py.typed
|   |           |   |-- typecheck.py
|   |           |   `-- types.py
|   |           |-- contourpy-1.3.3.dist-info
|   |           |   |-- INSTALLER
|   |           |   |-- LICENSE
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   |-- REQUESTED
|   |           |   `-- WHEEL
|   |           |-- cv2
|   |           |   |-- Error
|   |           |   |   `-- __init__.pyi
|   |           |   |-- __pycache__
|   |           |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |-- config-3.cpython-312.pyc
|   |           |   |   |-- config.cpython-312.pyc
|   |           |   |   |-- load_config_py2.cpython-312.pyc
|   |           |   |   |-- load_config_py3.cpython-312.pyc
|   |           |   |   `-- version.cpython-312.pyc
|   |           |   |-- aruco
|   |           |   |   `-- __init__.pyi
|   |           |   |-- barcode
|   |           |   |   `-- __init__.pyi
|   |           |   |-- cuda
|   |           |   |   `-- __init__.pyi
|   |           |   |-- detail
|   |           |   |   `-- __init__.pyi
|   |           |   |-- dnn
|   |           |   |   `-- __init__.pyi
|   |           |   |-- fisheye
|   |           |   |   `-- __init__.pyi
|   |           |   |-- flann
|   |           |   |   `-- __init__.pyi
|   |           |   |-- gapi
|   |           |   |   |-- __pycache__
|   |           |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |-- core
|   |           |   |   |   |-- cpu
|   |           |   |   |   |   `-- __init__.pyi
|   |           |   |   |   |-- fluid
|   |           |   |   |   |   `-- __init__.pyi
|   |           |   |   |   |-- ocl
|   |           |   |   |   |   `-- __init__.pyi
|   |           |   |   |   `-- __init__.pyi
|   |           |   |   |-- ie
|   |           |   |   |   |-- detail
|   |           |   |   |   |   `-- __init__.pyi
|   |           |   |   |   `-- __init__.pyi
|   |           |   |   |-- imgproc
|   |           |   |   |   |-- fluid
|   |           |   |   |   |   `-- __init__.pyi
|   |           |   |   |   `-- __init__.pyi
|   |           |   |   |-- oak
|   |           |   |   |   `-- __init__.pyi
|   |           |   |   |-- onnx
|   |           |   |   |   |-- ep
|   |           |   |   |   |   `-- __init__.pyi
|   |           |   |   |   `-- __init__.pyi
|   |           |   |   |-- ot
|   |           |   |   |   |-- cpu
|   |           |   |   |   |   `-- __init__.pyi
|   |           |   |   |   `-- __init__.pyi
|   |           |   |   |-- ov
|   |           |   |   |   `-- __init__.pyi
|   |           |   |   |-- own
|   |           |   |   |   |-- detail
|   |           |   |   |   |   `-- __init__.pyi
|   |           |   |   |   `-- __init__.pyi
|   |           |   |   |-- render
|   |           |   |   |   |-- ocv
|   |           |   |   |   |   `-- __init__.pyi
|   |           |   |   |   `-- __init__.pyi
|   |           |   |   |-- streaming
|   |           |   |   |   `-- __init__.pyi
|   |           |   |   |-- video
|   |           |   |   |   `-- __init__.pyi
|   |           |   |   |-- wip
|   |           |   |   |   |-- draw
|   |           |   |   |   |   `-- __init__.pyi
|   |           |   |   |   |-- gst
|   |           |   |   |   |   `-- __init__.pyi
|   |           |   |   |   |-- onevpl
|   |           |   |   |   |   `-- __init__.pyi
|   |           |   |   |   `-- __init__.pyi
|   |           |   |   |-- __init__.py
|   |           |   |   `-- __init__.pyi
|   |           |   |-- ipp
|   |           |   |   `-- __init__.pyi
|   |           |   |-- mat_wrapper
|   |           |   |   |-- __pycache__
|   |           |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   `-- __init__.py
|   |           |   |-- misc
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   `-- version.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   `-- version.py
|   |           |   |-- ml
|   |           |   |   `-- __init__.pyi
|   |           |   |-- ocl
|   |           |   |   `-- __init__.pyi
|   |           |   |-- ogl
|   |           |   |   `-- __init__.pyi
|   |           |   |-- parallel
|   |           |   |   `-- __init__.pyi
|   |           |   |-- qt
|   |           |   |   |-- fonts
|   |           |   |   |   |-- DejaVuSans-Bold.ttf
|   |           |   |   |   |-- DejaVuSans-BoldOblique.ttf
|   |           |   |   |   |-- DejaVuSans-ExtraLight.ttf
|   |           |   |   |   |-- DejaVuSans-Oblique.ttf
|   |           |   |   |   |-- DejaVuSans.ttf
|   |           |   |   |   |-- DejaVuSansCondensed-Bold.ttf
|   |           |   |   |   |-- DejaVuSansCondensed-BoldOblique.ttf
|   |           |   |   |   |-- DejaVuSansCondensed-Oblique.ttf
|   |           |   |   |   `-- DejaVuSansCondensed.ttf
|   |           |   |   `-- plugins
|   |           |   |       `-- platforms
|   |           |   |           `-- libqxcb.so
|   |           |   |-- samples
|   |           |   |   `-- __init__.pyi
|   |           |   |-- segmentation
|   |           |   |   `-- __init__.pyi
|   |           |   |-- typing
|   |           |   |   |-- __pycache__
|   |           |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   `-- __init__.py
|   |           |   |-- utils
|   |           |   |   |-- __pycache__
|   |           |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |-- fs
|   |           |   |   |   `-- __init__.pyi
|   |           |   |   |-- nested
|   |           |   |   |   `-- __init__.pyi
|   |           |   |   |-- __init__.py
|   |           |   |   `-- __init__.pyi
|   |           |   |-- videoio_registry
|   |           |   |   `-- __init__.pyi
|   |           |   |-- LICENSE-3RD-PARTY.txt
|   |           |   |-- LICENSE.txt
|   |           |   |-- __init__.py
|   |           |   |-- __init__.pyi
|   |           |   |-- config-3.py
|   |           |   |-- config.py
|   |           |   |-- cv2.abi3.so
|   |           |   |-- load_config_py2.py
|   |           |   |-- load_config_py3.py
|   |           |   |-- py.typed
|   |           |   `-- version.py
|   |           |-- cycler
|   |           |   |-- __pycache__
|   |           |   |   `-- __init__.cpython-312.pyc
|   |           |   |-- __init__.py
|   |           |   `-- py.typed
|   |           |-- cycler-0.12.1.dist-info
|   |           |   |-- INSTALLER
|   |           |   |-- LICENSE
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   |-- REQUESTED
|   |           |   |-- WHEEL
|   |           |   `-- top_level.txt
|   |           |-- dateutil
|   |           |   |-- __pycache__
|   |           |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |-- _common.cpython-312.pyc
|   |           |   |   |-- _version.cpython-312.pyc
|   |           |   |   |-- easter.cpython-312.pyc
|   |           |   |   |-- relativedelta.cpython-312.pyc
|   |           |   |   |-- rrule.cpython-312.pyc
|   |           |   |   |-- tzwin.cpython-312.pyc
|   |           |   |   `-- utils.cpython-312.pyc
|   |           |   |-- parser
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _parser.cpython-312.pyc
|   |           |   |   |   `-- isoparser.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- _parser.py
|   |           |   |   `-- isoparser.py
|   |           |   |-- tz
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _common.cpython-312.pyc
|   |           |   |   |   |-- _factories.cpython-312.pyc
|   |           |   |   |   |-- tz.cpython-312.pyc
|   |           |   |   |   `-- win.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- _common.py
|   |           |   |   |-- _factories.py
|   |           |   |   |-- tz.py
|   |           |   |   `-- win.py
|   |           |   |-- zoneinfo
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   `-- rebuild.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- dateutil-zoneinfo.tar.gz
|   |           |   |   `-- rebuild.py
|   |           |   |-- __init__.py
|   |           |   |-- _common.py
|   |           |   |-- _version.py
|   |           |   |-- easter.py
|   |           |   |-- relativedelta.py
|   |           |   |-- rrule.py
|   |           |   |-- tzwin.py
|   |           |   `-- utils.py
|   |           |-- fontTools
|   |           |   |-- __pycache__
|   |           |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |-- afmLib.cpython-312.pyc
|   |           |   |   |-- agl.cpython-312.pyc
|   |           |   |   |-- annotations.cpython-312.pyc
|   |           |   |   |-- fontBuilder.cpython-312.pyc
|   |           |   |   |-- help.cpython-312.pyc
|   |           |   |   |-- tfmLib.cpython-312.pyc
|   |           |   |   |-- ttx.cpython-312.pyc
|   |           |   |   `-- unicode.cpython-312.pyc
|   |           |   |-- cffLib
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- CFF2ToCFF.cpython-312.pyc
|   |           |   |   |   |-- CFFToCFF2.cpython-312.pyc
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- specializer.cpython-312.pyc
|   |           |   |   |   |-- transforms.cpython-312.pyc
|   |           |   |   |   `-- width.cpython-312.pyc
|   |           |   |   |-- CFF2ToCFF.py
|   |           |   |   |-- CFFToCFF2.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- specializer.py
|   |           |   |   |-- transforms.py
|   |           |   |   `-- width.py
|   |           |   |-- colorLib
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- builder.cpython-312.pyc
|   |           |   |   |   |-- errors.cpython-312.pyc
|   |           |   |   |   |-- geometry.cpython-312.pyc
|   |           |   |   |   |-- table_builder.cpython-312.pyc
|   |           |   |   |   `-- unbuilder.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- builder.py
|   |           |   |   |-- errors.py
|   |           |   |   |-- geometry.py
|   |           |   |   |-- table_builder.py
|   |           |   |   `-- unbuilder.py
|   |           |   |-- config
|   |           |   |   |-- __pycache__
|   |           |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   `-- __init__.py
|   |           |   |-- cu2qu
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |   |-- benchmark.cpython-312.pyc
|   |           |   |   |   |-- cli.cpython-312.pyc
|   |           |   |   |   |-- cu2qu.cpython-312.pyc
|   |           |   |   |   |-- errors.cpython-312.pyc
|   |           |   |   |   `-- ufo.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __main__.py
|   |           |   |   |-- benchmark.py
|   |           |   |   |-- cli.py
|   |           |   |   |-- cu2qu.c
|   |           |   |   |-- cu2qu.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- cu2qu.py
|   |           |   |   |-- errors.py
|   |           |   |   `-- ufo.py
|   |           |   |-- designspaceLib
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |   |-- split.cpython-312.pyc
|   |           |   |   |   |-- statNames.cpython-312.pyc
|   |           |   |   |   `-- types.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __main__.py
|   |           |   |   |-- split.py
|   |           |   |   |-- statNames.py
|   |           |   |   `-- types.py
|   |           |   |-- encodings
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- MacRoman.cpython-312.pyc
|   |           |   |   |   |-- StandardEncoding.cpython-312.pyc
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   `-- codecs.cpython-312.pyc
|   |           |   |   |-- MacRoman.py
|   |           |   |   |-- StandardEncoding.py
|   |           |   |   |-- __init__.py
|   |           |   |   `-- codecs.py
|   |           |   |-- feaLib
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |   |-- ast.cpython-312.pyc
|   |           |   |   |   |-- builder.cpython-312.pyc
|   |           |   |   |   |-- error.cpython-312.pyc
|   |           |   |   |   |-- lexer.cpython-312.pyc
|   |           |   |   |   |-- location.cpython-312.pyc
|   |           |   |   |   |-- lookupDebugInfo.cpython-312.pyc
|   |           |   |   |   |-- parser.cpython-312.pyc
|   |           |   |   |   `-- variableScalar.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __main__.py
|   |           |   |   |-- ast.py
|   |           |   |   |-- builder.py
|   |           |   |   |-- error.py
|   |           |   |   |-- lexer.c
|   |           |   |   |-- lexer.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- lexer.py
|   |           |   |   |-- location.py
|   |           |   |   |-- lookupDebugInfo.py
|   |           |   |   |-- parser.py
|   |           |   |   `-- variableScalar.py
|   |           |   |-- merge
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |   |-- base.cpython-312.pyc
|   |           |   |   |   |-- cmap.cpython-312.pyc
|   |           |   |   |   |-- layout.cpython-312.pyc
|   |           |   |   |   |-- options.cpython-312.pyc
|   |           |   |   |   |-- tables.cpython-312.pyc
|   |           |   |   |   |-- unicode.cpython-312.pyc
|   |           |   |   |   `-- util.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __main__.py
|   |           |   |   |-- base.py
|   |           |   |   |-- cmap.py
|   |           |   |   |-- layout.py
|   |           |   |   |-- options.py
|   |           |   |   |-- tables.py
|   |           |   |   |-- unicode.py
|   |           |   |   `-- util.py
|   |           |   |-- misc
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- arrayTools.cpython-312.pyc
|   |           |   |   |   |-- bezierTools.cpython-312.pyc
|   |           |   |   |   |-- classifyTools.cpython-312.pyc
|   |           |   |   |   |-- cliTools.cpython-312.pyc
|   |           |   |   |   |-- configTools.cpython-312.pyc
|   |           |   |   |   |-- cython.cpython-312.pyc
|   |           |   |   |   |-- dictTools.cpython-312.pyc
|   |           |   |   |   |-- eexec.cpython-312.pyc
|   |           |   |   |   |-- encodingTools.cpython-312.pyc
|   |           |   |   |   |-- enumTools.cpython-312.pyc
|   |           |   |   |   |-- etree.cpython-312.pyc
|   |           |   |   |   |-- filenames.cpython-312.pyc
|   |           |   |   |   |-- fixedTools.cpython-312.pyc
|   |           |   |   |   |-- intTools.cpython-312.pyc
|   |           |   |   |   |-- iterTools.cpython-312.pyc
|   |           |   |   |   |-- lazyTools.cpython-312.pyc
|   |           |   |   |   |-- loggingTools.cpython-312.pyc
|   |           |   |   |   |-- macCreatorType.cpython-312.pyc
|   |           |   |   |   |-- macRes.cpython-312.pyc
|   |           |   |   |   |-- psCharStrings.cpython-312.pyc
|   |           |   |   |   |-- psLib.cpython-312.pyc
|   |           |   |   |   |-- psOperators.cpython-312.pyc
|   |           |   |   |   |-- py23.cpython-312.pyc
|   |           |   |   |   |-- roundTools.cpython-312.pyc
|   |           |   |   |   |-- sstruct.cpython-312.pyc
|   |           |   |   |   |-- symfont.cpython-312.pyc
|   |           |   |   |   |-- testTools.cpython-312.pyc
|   |           |   |   |   |-- textTools.cpython-312.pyc
|   |           |   |   |   |-- timeTools.cpython-312.pyc
|   |           |   |   |   |-- transform.cpython-312.pyc
|   |           |   |   |   |-- treeTools.cpython-312.pyc
|   |           |   |   |   |-- vector.cpython-312.pyc
|   |           |   |   |   |-- visitor.cpython-312.pyc
|   |           |   |   |   |-- xmlReader.cpython-312.pyc
|   |           |   |   |   `-- xmlWriter.cpython-312.pyc
|   |           |   |   |-- filesystem
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- _base.cpython-312.pyc
|   |           |   |   |   |   |-- _copy.cpython-312.pyc
|   |           |   |   |   |   |-- _errors.cpython-312.pyc
|   |           |   |   |   |   |-- _info.cpython-312.pyc
|   |           |   |   |   |   |-- _osfs.cpython-312.pyc
|   |           |   |   |   |   |-- _path.cpython-312.pyc
|   |           |   |   |   |   |-- _subfs.cpython-312.pyc
|   |           |   |   |   |   |-- _tempfs.cpython-312.pyc
|   |           |   |   |   |   |-- _tools.cpython-312.pyc
|   |           |   |   |   |   |-- _walk.cpython-312.pyc
|   |           |   |   |   |   `-- _zipfs.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- _base.py
|   |           |   |   |   |-- _copy.py
|   |           |   |   |   |-- _errors.py
|   |           |   |   |   |-- _info.py
|   |           |   |   |   |-- _osfs.py
|   |           |   |   |   |-- _path.py
|   |           |   |   |   |-- _subfs.py
|   |           |   |   |   |-- _tempfs.py
|   |           |   |   |   |-- _tools.py
|   |           |   |   |   |-- _walk.py
|   |           |   |   |   `-- _zipfs.py
|   |           |   |   |-- plistlib
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   `-- py.typed
|   |           |   |   |-- __init__.py
|   |           |   |   |-- arrayTools.py
|   |           |   |   |-- bezierTools.c
|   |           |   |   |-- bezierTools.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- bezierTools.py
|   |           |   |   |-- classifyTools.py
|   |           |   |   |-- cliTools.py
|   |           |   |   |-- configTools.py
|   |           |   |   |-- cython.py
|   |           |   |   |-- dictTools.py
|   |           |   |   |-- eexec.py
|   |           |   |   |-- encodingTools.py
|   |           |   |   |-- enumTools.py
|   |           |   |   |-- etree.py
|   |           |   |   |-- filenames.py
|   |           |   |   |-- fixedTools.py
|   |           |   |   |-- intTools.py
|   |           |   |   |-- iterTools.py
|   |           |   |   |-- lazyTools.py
|   |           |   |   |-- loggingTools.py
|   |           |   |   |-- macCreatorType.py
|   |           |   |   |-- macRes.py
|   |           |   |   |-- psCharStrings.py
|   |           |   |   |-- psLib.py
|   |           |   |   |-- psOperators.py
|   |           |   |   |-- py23.py
|   |           |   |   |-- roundTools.py
|   |           |   |   |-- sstruct.py
|   |           |   |   |-- symfont.py
|   |           |   |   |-- testTools.py
|   |           |   |   |-- textTools.py
|   |           |   |   |-- timeTools.py
|   |           |   |   |-- transform.py
|   |           |   |   |-- treeTools.py
|   |           |   |   |-- vector.py
|   |           |   |   |-- visitor.py
|   |           |   |   |-- xmlReader.py
|   |           |   |   `-- xmlWriter.py
|   |           |   |-- mtiLib
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   `-- __main__.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   `-- __main__.py
|   |           |   |-- otlLib
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- builder.cpython-312.pyc
|   |           |   |   |   |-- error.cpython-312.pyc
|   |           |   |   |   `-- maxContextCalc.cpython-312.pyc
|   |           |   |   |-- optimize
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |   |   `-- gpos.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- __main__.py
|   |           |   |   |   `-- gpos.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- builder.py
|   |           |   |   |-- error.py
|   |           |   |   `-- maxContextCalc.py
|   |           |   |-- pens
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- areaPen.cpython-312.pyc
|   |           |   |   |   |-- basePen.cpython-312.pyc
|   |           |   |   |   |-- boundsPen.cpython-312.pyc
|   |           |   |   |   |-- cairoPen.cpython-312.pyc
|   |           |   |   |   |-- cocoaPen.cpython-312.pyc
|   |           |   |   |   |-- cu2quPen.cpython-312.pyc
|   |           |   |   |   |-- explicitClosingLinePen.cpython-312.pyc
|   |           |   |   |   |-- filterPen.cpython-312.pyc
|   |           |   |   |   |-- freetypePen.cpython-312.pyc
|   |           |   |   |   |-- hashPointPen.cpython-312.pyc
|   |           |   |   |   |-- momentsPen.cpython-312.pyc
|   |           |   |   |   |-- perimeterPen.cpython-312.pyc
|   |           |   |   |   |-- pointInsidePen.cpython-312.pyc
|   |           |   |   |   |-- pointPen.cpython-312.pyc
|   |           |   |   |   |-- qtPen.cpython-312.pyc
|   |           |   |   |   |-- qu2cuPen.cpython-312.pyc
|   |           |   |   |   |-- quartzPen.cpython-312.pyc
|   |           |   |   |   |-- recordingPen.cpython-312.pyc
|   |           |   |   |   |-- reportLabPen.cpython-312.pyc
|   |           |   |   |   |-- reverseContourPen.cpython-312.pyc
|   |           |   |   |   |-- roundingPen.cpython-312.pyc
|   |           |   |   |   |-- statisticsPen.cpython-312.pyc
|   |           |   |   |   |-- svgPathPen.cpython-312.pyc
|   |           |   |   |   |-- t2CharStringPen.cpython-312.pyc
|   |           |   |   |   |-- teePen.cpython-312.pyc
|   |           |   |   |   |-- transformPen.cpython-312.pyc
|   |           |   |   |   |-- ttGlyphPen.cpython-312.pyc
|   |           |   |   |   `-- wxPen.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- areaPen.py
|   |           |   |   |-- basePen.py
|   |           |   |   |-- boundsPen.py
|   |           |   |   |-- cairoPen.py
|   |           |   |   |-- cocoaPen.py
|   |           |   |   |-- cu2quPen.py
|   |           |   |   |-- explicitClosingLinePen.py
|   |           |   |   |-- filterPen.py
|   |           |   |   |-- freetypePen.py
|   |           |   |   |-- hashPointPen.py
|   |           |   |   |-- momentsPen.c
|   |           |   |   |-- momentsPen.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- momentsPen.py
|   |           |   |   |-- perimeterPen.py
|   |           |   |   |-- pointInsidePen.py
|   |           |   |   |-- pointPen.py
|   |           |   |   |-- qtPen.py
|   |           |   |   |-- qu2cuPen.py
|   |           |   |   |-- quartzPen.py
|   |           |   |   |-- recordingPen.py
|   |           |   |   |-- reportLabPen.py
|   |           |   |   |-- reverseContourPen.py
|   |           |   |   |-- roundingPen.py
|   |           |   |   |-- statisticsPen.py
|   |           |   |   |-- svgPathPen.py
|   |           |   |   |-- t2CharStringPen.py
|   |           |   |   |-- teePen.py
|   |           |   |   |-- transformPen.py
|   |           |   |   |-- ttGlyphPen.py
|   |           |   |   `-- wxPen.py
|   |           |   |-- qu2cu
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |   |-- benchmark.cpython-312.pyc
|   |           |   |   |   |-- cli.cpython-312.pyc
|   |           |   |   |   `-- qu2cu.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __main__.py
|   |           |   |   |-- benchmark.py
|   |           |   |   |-- cli.py
|   |           |   |   |-- qu2cu.c
|   |           |   |   |-- qu2cu.cpython-312-x86_64-linux-gnu.so
|   |           |   |   `-- qu2cu.py
|   |           |   |-- subset
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |   |-- cff.cpython-312.pyc
|   |           |   |   |   |-- svg.cpython-312.pyc
|   |           |   |   |   `-- util.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __main__.py
|   |           |   |   |-- cff.py
|   |           |   |   |-- svg.py
|   |           |   |   `-- util.py
|   |           |   |-- svgLib
|   |           |   |   |-- __pycache__
|   |           |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |-- path
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- arc.cpython-312.pyc
|   |           |   |   |   |   |-- parser.cpython-312.pyc
|   |           |   |   |   |   `-- shapes.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- arc.py
|   |           |   |   |   |-- parser.py
|   |           |   |   |   `-- shapes.py
|   |           |   |   `-- __init__.py
|   |           |   |-- t1Lib
|   |           |   |   |-- __pycache__
|   |           |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   `-- __init__.py
|   |           |   |-- ttLib
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |   |-- macUtils.cpython-312.pyc
|   |           |   |   |   |-- removeOverlaps.cpython-312.pyc
|   |           |   |   |   |-- reorderGlyphs.cpython-312.pyc
|   |           |   |   |   |-- scaleUpem.cpython-312.pyc
|   |           |   |   |   |-- sfnt.cpython-312.pyc
|   |           |   |   |   |-- standardGlyphOrder.cpython-312.pyc
|   |           |   |   |   |-- ttCollection.cpython-312.pyc
|   |           |   |   |   |-- ttFont.cpython-312.pyc
|   |           |   |   |   |-- ttGlyphSet.cpython-312.pyc
|   |           |   |   |   |-- ttVisitor.cpython-312.pyc
|   |           |   |   |   `-- woff2.cpython-312.pyc
|   |           |   |   |-- tables
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- B_A_S_E_.cpython-312.pyc
|   |           |   |   |   |   |-- BitmapGlyphMetrics.cpython-312.pyc
|   |           |   |   |   |   |-- C_B_D_T_.cpython-312.pyc
|   |           |   |   |   |   |-- C_B_L_C_.cpython-312.pyc
|   |           |   |   |   |   |-- C_F_F_.cpython-312.pyc
|   |           |   |   |   |   |-- C_F_F__2.cpython-312.pyc
|   |           |   |   |   |   |-- C_O_L_R_.cpython-312.pyc
|   |           |   |   |   |   |-- C_P_A_L_.cpython-312.pyc
|   |           |   |   |   |   |-- D_S_I_G_.cpython-312.pyc
|   |           |   |   |   |   |-- D__e_b_g.cpython-312.pyc
|   |           |   |   |   |   |-- DefaultTable.cpython-312.pyc
|   |           |   |   |   |   |-- E_B_D_T_.cpython-312.pyc
|   |           |   |   |   |   |-- E_B_L_C_.cpython-312.pyc
|   |           |   |   |   |   |-- F_F_T_M_.cpython-312.pyc
|   |           |   |   |   |   |-- F__e_a_t.cpython-312.pyc
|   |           |   |   |   |   |-- G_D_E_F_.cpython-312.pyc
|   |           |   |   |   |   |-- G_M_A_P_.cpython-312.pyc
|   |           |   |   |   |   |-- G_P_K_G_.cpython-312.pyc
|   |           |   |   |   |   |-- G_P_O_S_.cpython-312.pyc
|   |           |   |   |   |   |-- G_S_U_B_.cpython-312.pyc
|   |           |   |   |   |   |-- G_V_A_R_.cpython-312.pyc
|   |           |   |   |   |   |-- G__l_a_t.cpython-312.pyc
|   |           |   |   |   |   |-- G__l_o_c.cpython-312.pyc
|   |           |   |   |   |   |-- H_V_A_R_.cpython-312.pyc
|   |           |   |   |   |   |-- J_S_T_F_.cpython-312.pyc
|   |           |   |   |   |   |-- L_T_S_H_.cpython-312.pyc
|   |           |   |   |   |   |-- M_A_T_H_.cpython-312.pyc
|   |           |   |   |   |   |-- M_E_T_A_.cpython-312.pyc
|   |           |   |   |   |   |-- M_V_A_R_.cpython-312.pyc
|   |           |   |   |   |   |-- O_S_2f_2.cpython-312.pyc
|   |           |   |   |   |   |-- S_I_N_G_.cpython-312.pyc
|   |           |   |   |   |   |-- S_T_A_T_.cpython-312.pyc
|   |           |   |   |   |   |-- S_V_G_.cpython-312.pyc
|   |           |   |   |   |   |-- S__i_l_f.cpython-312.pyc
|   |           |   |   |   |   |-- S__i_l_l.cpython-312.pyc
|   |           |   |   |   |   |-- T_S_I_B_.cpython-312.pyc
|   |           |   |   |   |   |-- T_S_I_C_.cpython-312.pyc
|   |           |   |   |   |   |-- T_S_I_D_.cpython-312.pyc
|   |           |   |   |   |   |-- T_S_I_J_.cpython-312.pyc
|   |           |   |   |   |   |-- T_S_I_P_.cpython-312.pyc
|   |           |   |   |   |   |-- T_S_I_S_.cpython-312.pyc
|   |           |   |   |   |   |-- T_S_I_V_.cpython-312.pyc
|   |           |   |   |   |   |-- T_S_I__0.cpython-312.pyc
|   |           |   |   |   |   |-- T_S_I__1.cpython-312.pyc
|   |           |   |   |   |   |-- T_S_I__2.cpython-312.pyc
|   |           |   |   |   |   |-- T_S_I__3.cpython-312.pyc
|   |           |   |   |   |   |-- T_S_I__5.cpython-312.pyc
|   |           |   |   |   |   |-- T_T_F_A_.cpython-312.pyc
|   |           |   |   |   |   |-- TupleVariation.cpython-312.pyc
|   |           |   |   |   |   |-- V_A_R_C_.cpython-312.pyc
|   |           |   |   |   |   |-- V_D_M_X_.cpython-312.pyc
|   |           |   |   |   |   |-- V_O_R_G_.cpython-312.pyc
|   |           |   |   |   |   |-- V_V_A_R_.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- _a_n_k_r.cpython-312.pyc
|   |           |   |   |   |   |-- _a_v_a_r.cpython-312.pyc
|   |           |   |   |   |   |-- _b_s_l_n.cpython-312.pyc
|   |           |   |   |   |   |-- _c_i_d_g.cpython-312.pyc
|   |           |   |   |   |   |-- _c_m_a_p.cpython-312.pyc
|   |           |   |   |   |   |-- _c_v_a_r.cpython-312.pyc
|   |           |   |   |   |   |-- _c_v_t.cpython-312.pyc
|   |           |   |   |   |   |-- _f_e_a_t.cpython-312.pyc
|   |           |   |   |   |   |-- _f_p_g_m.cpython-312.pyc
|   |           |   |   |   |   |-- _f_v_a_r.cpython-312.pyc
|   |           |   |   |   |   |-- _g_a_s_p.cpython-312.pyc
|   |           |   |   |   |   |-- _g_c_i_d.cpython-312.pyc
|   |           |   |   |   |   |-- _g_l_y_f.cpython-312.pyc
|   |           |   |   |   |   |-- _g_v_a_r.cpython-312.pyc
|   |           |   |   |   |   |-- _h_d_m_x.cpython-312.pyc
|   |           |   |   |   |   |-- _h_e_a_d.cpython-312.pyc
|   |           |   |   |   |   |-- _h_h_e_a.cpython-312.pyc
|   |           |   |   |   |   |-- _h_m_t_x.cpython-312.pyc
|   |           |   |   |   |   |-- _k_e_r_n.cpython-312.pyc
|   |           |   |   |   |   |-- _l_c_a_r.cpython-312.pyc
|   |           |   |   |   |   |-- _l_o_c_a.cpython-312.pyc
|   |           |   |   |   |   |-- _l_t_a_g.cpython-312.pyc
|   |           |   |   |   |   |-- _m_a_x_p.cpython-312.pyc
|   |           |   |   |   |   |-- _m_e_t_a.cpython-312.pyc
|   |           |   |   |   |   |-- _m_o_r_t.cpython-312.pyc
|   |           |   |   |   |   |-- _m_o_r_x.cpython-312.pyc
|   |           |   |   |   |   |-- _n_a_m_e.cpython-312.pyc
|   |           |   |   |   |   |-- _o_p_b_d.cpython-312.pyc
|   |           |   |   |   |   |-- _p_o_s_t.cpython-312.pyc
|   |           |   |   |   |   |-- _p_r_e_p.cpython-312.pyc
|   |           |   |   |   |   |-- _p_r_o_p.cpython-312.pyc
|   |           |   |   |   |   |-- _s_b_i_x.cpython-312.pyc
|   |           |   |   |   |   |-- _t_r_a_k.cpython-312.pyc
|   |           |   |   |   |   |-- _v_h_e_a.cpython-312.pyc
|   |           |   |   |   |   |-- _v_m_t_x.cpython-312.pyc
|   |           |   |   |   |   |-- asciiTable.cpython-312.pyc
|   |           |   |   |   |   |-- grUtils.cpython-312.pyc
|   |           |   |   |   |   |-- otBase.cpython-312.pyc
|   |           |   |   |   |   |-- otConverters.cpython-312.pyc
|   |           |   |   |   |   |-- otData.cpython-312.pyc
|   |           |   |   |   |   |-- otTables.cpython-312.pyc
|   |           |   |   |   |   |-- otTraverse.cpython-312.pyc
|   |           |   |   |   |   |-- sbixGlyph.cpython-312.pyc
|   |           |   |   |   |   |-- sbixStrike.cpython-312.pyc
|   |           |   |   |   |   `-- ttProgram.cpython-312.pyc
|   |           |   |   |   |-- B_A_S_E_.py
|   |           |   |   |   |-- BitmapGlyphMetrics.py
|   |           |   |   |   |-- C_B_D_T_.py
|   |           |   |   |   |-- C_B_L_C_.py
|   |           |   |   |   |-- C_F_F_.py
|   |           |   |   |   |-- C_F_F__2.py
|   |           |   |   |   |-- C_O_L_R_.py
|   |           |   |   |   |-- C_P_A_L_.py
|   |           |   |   |   |-- D_S_I_G_.py
|   |           |   |   |   |-- D__e_b_g.py
|   |           |   |   |   |-- DefaultTable.py
|   |           |   |   |   |-- E_B_D_T_.py
|   |           |   |   |   |-- E_B_L_C_.py
|   |           |   |   |   |-- F_F_T_M_.py
|   |           |   |   |   |-- F__e_a_t.py
|   |           |   |   |   |-- G_D_E_F_.py
|   |           |   |   |   |-- G_M_A_P_.py
|   |           |   |   |   |-- G_P_K_G_.py
|   |           |   |   |   |-- G_P_O_S_.py
|   |           |   |   |   |-- G_S_U_B_.py
|   |           |   |   |   |-- G_V_A_R_.py
|   |           |   |   |   |-- G__l_a_t.py
|   |           |   |   |   |-- G__l_o_c.py
|   |           |   |   |   |-- H_V_A_R_.py
|   |           |   |   |   |-- J_S_T_F_.py
|   |           |   |   |   |-- L_T_S_H_.py
|   |           |   |   |   |-- M_A_T_H_.py
|   |           |   |   |   |-- M_E_T_A_.py
|   |           |   |   |   |-- M_V_A_R_.py
|   |           |   |   |   |-- O_S_2f_2.py
|   |           |   |   |   |-- S_I_N_G_.py
|   |           |   |   |   |-- S_T_A_T_.py
|   |           |   |   |   |-- S_V_G_.py
|   |           |   |   |   |-- S__i_l_f.py
|   |           |   |   |   |-- S__i_l_l.py
|   |           |   |   |   |-- T_S_I_B_.py
|   |           |   |   |   |-- T_S_I_C_.py
|   |           |   |   |   |-- T_S_I_D_.py
|   |           |   |   |   |-- T_S_I_J_.py
|   |           |   |   |   |-- T_S_I_P_.py
|   |           |   |   |   |-- T_S_I_S_.py
|   |           |   |   |   |-- T_S_I_V_.py
|   |           |   |   |   |-- T_S_I__0.py
|   |           |   |   |   |-- T_S_I__1.py
|   |           |   |   |   |-- T_S_I__2.py
|   |           |   |   |   |-- T_S_I__3.py
|   |           |   |   |   |-- T_S_I__5.py
|   |           |   |   |   |-- T_T_F_A_.py
|   |           |   |   |   |-- TupleVariation.py
|   |           |   |   |   |-- V_A_R_C_.py
|   |           |   |   |   |-- V_D_M_X_.py
|   |           |   |   |   |-- V_O_R_G_.py
|   |           |   |   |   |-- V_V_A_R_.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- _a_n_k_r.py
|   |           |   |   |   |-- _a_v_a_r.py
|   |           |   |   |   |-- _b_s_l_n.py
|   |           |   |   |   |-- _c_i_d_g.py
|   |           |   |   |   |-- _c_m_a_p.py
|   |           |   |   |   |-- _c_v_a_r.py
|   |           |   |   |   |-- _c_v_t.py
|   |           |   |   |   |-- _f_e_a_t.py
|   |           |   |   |   |-- _f_p_g_m.py
|   |           |   |   |   |-- _f_v_a_r.py
|   |           |   |   |   |-- _g_a_s_p.py
|   |           |   |   |   |-- _g_c_i_d.py
|   |           |   |   |   |-- _g_l_y_f.py
|   |           |   |   |   |-- _g_v_a_r.py
|   |           |   |   |   |-- _h_d_m_x.py
|   |           |   |   |   |-- _h_e_a_d.py
|   |           |   |   |   |-- _h_h_e_a.py
|   |           |   |   |   |-- _h_m_t_x.py
|   |           |   |   |   |-- _k_e_r_n.py
|   |           |   |   |   |-- _l_c_a_r.py
|   |           |   |   |   |-- _l_o_c_a.py
|   |           |   |   |   |-- _l_t_a_g.py
|   |           |   |   |   |-- _m_a_x_p.py
|   |           |   |   |   |-- _m_e_t_a.py
|   |           |   |   |   |-- _m_o_r_t.py
|   |           |   |   |   |-- _m_o_r_x.py
|   |           |   |   |   |-- _n_a_m_e.py
|   |           |   |   |   |-- _o_p_b_d.py
|   |           |   |   |   |-- _p_o_s_t.py
|   |           |   |   |   |-- _p_r_e_p.py
|   |           |   |   |   |-- _p_r_o_p.py
|   |           |   |   |   |-- _s_b_i_x.py
|   |           |   |   |   |-- _t_r_a_k.py
|   |           |   |   |   |-- _v_h_e_a.py
|   |           |   |   |   |-- _v_m_t_x.py
|   |           |   |   |   |-- asciiTable.py
|   |           |   |   |   |-- grUtils.py
|   |           |   |   |   |-- otBase.py
|   |           |   |   |   |-- otConverters.py
|   |           |   |   |   |-- otData.py
|   |           |   |   |   |-- otTables.py
|   |           |   |   |   |-- otTraverse.py
|   |           |   |   |   |-- sbixGlyph.py
|   |           |   |   |   |-- sbixStrike.py
|   |           |   |   |   |-- table_API_readme.txt
|   |           |   |   |   `-- ttProgram.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __main__.py
|   |           |   |   |-- macUtils.py
|   |           |   |   |-- removeOverlaps.py
|   |           |   |   |-- reorderGlyphs.py
|   |           |   |   |-- scaleUpem.py
|   |           |   |   |-- sfnt.py
|   |           |   |   |-- standardGlyphOrder.py
|   |           |   |   |-- ttCollection.py
|   |           |   |   |-- ttFont.py
|   |           |   |   |-- ttGlyphSet.py
|   |           |   |   |-- ttVisitor.py
|   |           |   |   `-- woff2.py
|   |           |   |-- ufoLib
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- converters.cpython-312.pyc
|   |           |   |   |   |-- errors.cpython-312.pyc
|   |           |   |   |   |-- etree.cpython-312.pyc
|   |           |   |   |   |-- filenames.cpython-312.pyc
|   |           |   |   |   |-- glifLib.cpython-312.pyc
|   |           |   |   |   |-- kerning.cpython-312.pyc
|   |           |   |   |   |-- plistlib.cpython-312.pyc
|   |           |   |   |   |-- pointPen.cpython-312.pyc
|   |           |   |   |   |-- utils.cpython-312.pyc
|   |           |   |   |   `-- validators.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- converters.py
|   |           |   |   |-- errors.py
|   |           |   |   |-- etree.py
|   |           |   |   |-- filenames.py
|   |           |   |   |-- glifLib.py
|   |           |   |   |-- kerning.py
|   |           |   |   |-- plistlib.py
|   |           |   |   |-- pointPen.py
|   |           |   |   |-- utils.py
|   |           |   |   `-- validators.py
|   |           |   |-- unicodedata
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- Blocks.cpython-312.pyc
|   |           |   |   |   |-- Mirrored.cpython-312.pyc
|   |           |   |   |   |-- OTTags.cpython-312.pyc
|   |           |   |   |   |-- ScriptExtensions.cpython-312.pyc
|   |           |   |   |   |-- Scripts.cpython-312.pyc
|   |           |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |-- Blocks.py
|   |           |   |   |-- Mirrored.py
|   |           |   |   |-- OTTags.py
|   |           |   |   |-- ScriptExtensions.py
|   |           |   |   |-- Scripts.py
|   |           |   |   `-- __init__.py
|   |           |   |-- varLib
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |   |-- avarPlanner.cpython-312.pyc
|   |           |   |   |   |-- builder.cpython-312.pyc
|   |           |   |   |   |-- cff.cpython-312.pyc
|   |           |   |   |   |-- errors.cpython-312.pyc
|   |           |   |   |   |-- featureVars.cpython-312.pyc
|   |           |   |   |   |-- hvar.cpython-312.pyc
|   |           |   |   |   |-- interpolatable.cpython-312.pyc
|   |           |   |   |   |-- interpolatableHelpers.cpython-312.pyc
|   |           |   |   |   |-- interpolatablePlot.cpython-312.pyc
|   |           |   |   |   |-- interpolatableTestContourOrder.cpython-312.pyc
|   |           |   |   |   |-- interpolatableTestStartingPoint.cpython-312.pyc
|   |           |   |   |   |-- interpolate_layout.cpython-312.pyc
|   |           |   |   |   |-- iup.cpython-312.pyc
|   |           |   |   |   |-- merger.cpython-312.pyc
|   |           |   |   |   |-- models.cpython-312.pyc
|   |           |   |   |   |-- multiVarStore.cpython-312.pyc
|   |           |   |   |   |-- mutator.cpython-312.pyc
|   |           |   |   |   |-- mvar.cpython-312.pyc
|   |           |   |   |   |-- plot.cpython-312.pyc
|   |           |   |   |   |-- stat.cpython-312.pyc
|   |           |   |   |   `-- varStore.cpython-312.pyc
|   |           |   |   |-- avar
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |   |   |-- build.cpython-312.pyc
|   |           |   |   |   |   |-- map.cpython-312.pyc
|   |           |   |   |   |   |-- plan.cpython-312.pyc
|   |           |   |   |   |   `-- unbuild.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- __main__.py
|   |           |   |   |   |-- build.py
|   |           |   |   |   |-- map.py
|   |           |   |   |   |-- plan.py
|   |           |   |   |   `-- unbuild.py
|   |           |   |   |-- instancer
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |   |   |-- featureVars.cpython-312.pyc
|   |           |   |   |   |   |-- names.cpython-312.pyc
|   |           |   |   |   |   `-- solver.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- __main__.py
|   |           |   |   |   |-- featureVars.py
|   |           |   |   |   |-- names.py
|   |           |   |   |   `-- solver.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __main__.py
|   |           |   |   |-- avarPlanner.py
|   |           |   |   |-- builder.py
|   |           |   |   |-- cff.py
|   |           |   |   |-- errors.py
|   |           |   |   |-- featureVars.py
|   |           |   |   |-- hvar.py
|   |           |   |   |-- interpolatable.py
|   |           |   |   |-- interpolatableHelpers.py
|   |           |   |   |-- interpolatablePlot.py
|   |           |   |   |-- interpolatableTestContourOrder.py
|   |           |   |   |-- interpolatableTestStartingPoint.py
|   |           |   |   |-- interpolate_layout.py
|   |           |   |   |-- iup.c
|   |           |   |   |-- iup.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- iup.py
|   |           |   |   |-- merger.py
|   |           |   |   |-- models.py
|   |           |   |   |-- multiVarStore.py
|   |           |   |   |-- mutator.py
|   |           |   |   |-- mvar.py
|   |           |   |   |-- plot.py
|   |           |   |   |-- stat.py
|   |           |   |   `-- varStore.py
|   |           |   |-- voltLib
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |   |-- ast.cpython-312.pyc
|   |           |   |   |   |-- error.cpython-312.pyc
|   |           |   |   |   |-- lexer.cpython-312.pyc
|   |           |   |   |   |-- parser.cpython-312.pyc
|   |           |   |   |   `-- voltToFea.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __main__.py
|   |           |   |   |-- ast.py
|   |           |   |   |-- error.py
|   |           |   |   |-- lexer.py
|   |           |   |   |-- parser.py
|   |           |   |   `-- voltToFea.py
|   |           |   |-- __init__.py
|   |           |   |-- __main__.py
|   |           |   |-- afmLib.py
|   |           |   |-- agl.py
|   |           |   |-- annotations.py
|   |           |   |-- fontBuilder.py
|   |           |   |-- help.py
|   |           |   |-- tfmLib.py
|   |           |   |-- ttx.py
|   |           |   `-- unicode.py
|   |           |-- fonttools-4.60.0.dist-info
|   |           |   |-- licenses
|   |           |   |   |-- LICENSE
|   |           |   |   `-- LICENSE.external
|   |           |   |-- INSTALLER
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   |-- REQUESTED
|   |           |   |-- WHEEL
|   |           |   |-- entry_points.txt
|   |           |   `-- top_level.txt
|   |           |-- iniconfig
|   |           |   |-- __pycache__
|   |           |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |-- _parse.cpython-312.pyc
|   |           |   |   |-- _version.cpython-312.pyc
|   |           |   |   `-- exceptions.cpython-312.pyc
|   |           |   |-- __init__.py
|   |           |   |-- _parse.py
|   |           |   |-- _version.py
|   |           |   |-- exceptions.py
|   |           |   `-- py.typed
|   |           |-- iniconfig-2.1.0.dist-info
|   |           |   |-- licenses
|   |           |   |   `-- LICENSE
|   |           |   |-- INSTALLER
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   |-- REQUESTED
|   |           |   `-- WHEEL
|   |           |-- kiwisolver
|   |           |   |-- __pycache__
|   |           |   |   |-- __init__.cpython-312.pyc
|   |           |   |   `-- exceptions.cpython-312.pyc
|   |           |   |-- __init__.py
|   |           |   |-- _cext.cpython-312-x86_64-linux-gnu.so
|   |           |   |-- _cext.pyi
|   |           |   |-- exceptions.py
|   |           |   `-- py.typed
|   |           |-- kiwisolver-1.4.9.dist-info
|   |           |   |-- licenses
|   |           |   |   `-- LICENSE
|   |           |   |-- INSTALLER
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   |-- REQUESTED
|   |           |   |-- WHEEL
|   |           |   `-- top_level.txt
|   |           |-- matplotlib
|   |           |   |-- __pycache__
|   |           |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |-- _afm.cpython-312.pyc
|   |           |   |   |-- _animation_data.cpython-312.pyc
|   |           |   |   |-- _blocking_input.cpython-312.pyc
|   |           |   |   |-- _cm.cpython-312.pyc
|   |           |   |   |-- _cm_bivar.cpython-312.pyc
|   |           |   |   |-- _cm_listed.cpython-312.pyc
|   |           |   |   |-- _cm_multivar.cpython-312.pyc
|   |           |   |   |-- _color_data.cpython-312.pyc
|   |           |   |   |-- _constrained_layout.cpython-312.pyc
|   |           |   |   |-- _docstring.cpython-312.pyc
|   |           |   |   |-- _enums.cpython-312.pyc
|   |           |   |   |-- _fontconfig_pattern.cpython-312.pyc
|   |           |   |   |-- _internal_utils.cpython-312.pyc
|   |           |   |   |-- _layoutgrid.cpython-312.pyc
|   |           |   |   |-- _mathtext.cpython-312.pyc
|   |           |   |   |-- _mathtext_data.cpython-312.pyc
|   |           |   |   |-- _pylab_helpers.cpython-312.pyc
|   |           |   |   |-- _text_helpers.cpython-312.pyc
|   |           |   |   |-- _tight_bbox.cpython-312.pyc
|   |           |   |   |-- _tight_layout.cpython-312.pyc
|   |           |   |   |-- _type1font.cpython-312.pyc
|   |           |   |   |-- _version.cpython-312.pyc
|   |           |   |   |-- animation.cpython-312.pyc
|   |           |   |   |-- artist.cpython-312.pyc
|   |           |   |   |-- axis.cpython-312.pyc
|   |           |   |   |-- backend_bases.cpython-312.pyc
|   |           |   |   |-- backend_managers.cpython-312.pyc
|   |           |   |   |-- backend_tools.cpython-312.pyc
|   |           |   |   |-- bezier.cpython-312.pyc
|   |           |   |   |-- category.cpython-312.pyc
|   |           |   |   |-- cbook.cpython-312.pyc
|   |           |   |   |-- cm.cpython-312.pyc
|   |           |   |   |-- collections.cpython-312.pyc
|   |           |   |   |-- colorbar.cpython-312.pyc
|   |           |   |   |-- colorizer.cpython-312.pyc
|   |           |   |   |-- colors.cpython-312.pyc
|   |           |   |   |-- container.cpython-312.pyc
|   |           |   |   |-- contour.cpython-312.pyc
|   |           |   |   |-- dates.cpython-312.pyc
|   |           |   |   |-- dviread.cpython-312.pyc
|   |           |   |   |-- figure.cpython-312.pyc
|   |           |   |   |-- font_manager.cpython-312.pyc
|   |           |   |   |-- gridspec.cpython-312.pyc
|   |           |   |   |-- hatch.cpython-312.pyc
|   |           |   |   |-- image.cpython-312.pyc
|   |           |   |   |-- inset.cpython-312.pyc
|   |           |   |   |-- layout_engine.cpython-312.pyc
|   |           |   |   |-- legend.cpython-312.pyc
|   |           |   |   |-- legend_handler.cpython-312.pyc
|   |           |   |   |-- lines.cpython-312.pyc
|   |           |   |   |-- markers.cpython-312.pyc
|   |           |   |   |-- mathtext.cpython-312.pyc
|   |           |   |   |-- mlab.cpython-312.pyc
|   |           |   |   |-- offsetbox.cpython-312.pyc
|   |           |   |   |-- patches.cpython-312.pyc
|   |           |   |   |-- path.cpython-312.pyc
|   |           |   |   |-- pyplot.cpython-312.pyc
|   |           |   |   |-- quiver.cpython-312.pyc
|   |           |   |   |-- rcsetup.cpython-312.pyc
|   |           |   |   |-- scale.cpython-312.pyc
|   |           |   |   |-- spines.cpython-312.pyc
|   |           |   |   |-- stackplot.cpython-312.pyc
|   |           |   |   |-- streamplot.cpython-312.pyc
|   |           |   |   |-- table.cpython-312.pyc
|   |           |   |   |-- texmanager.cpython-312.pyc
|   |           |   |   |-- text.cpython-312.pyc
|   |           |   |   |-- textpath.cpython-312.pyc
|   |           |   |   |-- ticker.cpython-312.pyc
|   |           |   |   |-- transforms.cpython-312.pyc
|   |           |   |   |-- units.cpython-312.pyc
|   |           |   |   `-- widgets.cpython-312.pyc
|   |           |   |-- _api
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   `-- deprecation.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __init__.pyi
|   |           |   |   |-- deprecation.py
|   |           |   |   `-- deprecation.pyi
|   |           |   |-- axes
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _axes.cpython-312.pyc
|   |           |   |   |   |-- _base.cpython-312.pyc
|   |           |   |   |   `-- _secondary_axes.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __init__.pyi
|   |           |   |   |-- _axes.py
|   |           |   |   |-- _axes.pyi
|   |           |   |   |-- _base.py
|   |           |   |   |-- _base.pyi
|   |           |   |   |-- _secondary_axes.py
|   |           |   |   `-- _secondary_axes.pyi
|   |           |   |-- backends
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _backend_gtk.cpython-312.pyc
|   |           |   |   |   |-- _backend_pdf_ps.cpython-312.pyc
|   |           |   |   |   |-- _backend_tk.cpython-312.pyc
|   |           |   |   |   |-- backend_agg.cpython-312.pyc
|   |           |   |   |   |-- backend_cairo.cpython-312.pyc
|   |           |   |   |   |-- backend_gtk3.cpython-312.pyc
|   |           |   |   |   |-- backend_gtk3agg.cpython-312.pyc
|   |           |   |   |   |-- backend_gtk3cairo.cpython-312.pyc
|   |           |   |   |   |-- backend_gtk4.cpython-312.pyc
|   |           |   |   |   |-- backend_gtk4agg.cpython-312.pyc
|   |           |   |   |   |-- backend_gtk4cairo.cpython-312.pyc
|   |           |   |   |   |-- backend_macosx.cpython-312.pyc
|   |           |   |   |   |-- backend_mixed.cpython-312.pyc
|   |           |   |   |   |-- backend_nbagg.cpython-312.pyc
|   |           |   |   |   |-- backend_pdf.cpython-312.pyc
|   |           |   |   |   |-- backend_pgf.cpython-312.pyc
|   |           |   |   |   |-- backend_ps.cpython-312.pyc
|   |           |   |   |   |-- backend_qt.cpython-312.pyc
|   |           |   |   |   |-- backend_qt5.cpython-312.pyc
|   |           |   |   |   |-- backend_qt5agg.cpython-312.pyc
|   |           |   |   |   |-- backend_qt5cairo.cpython-312.pyc
|   |           |   |   |   |-- backend_qtagg.cpython-312.pyc
|   |           |   |   |   |-- backend_qtcairo.cpython-312.pyc
|   |           |   |   |   |-- backend_svg.cpython-312.pyc
|   |           |   |   |   |-- backend_template.cpython-312.pyc
|   |           |   |   |   |-- backend_tkagg.cpython-312.pyc
|   |           |   |   |   |-- backend_tkcairo.cpython-312.pyc
|   |           |   |   |   |-- backend_webagg.cpython-312.pyc
|   |           |   |   |   |-- backend_webagg_core.cpython-312.pyc
|   |           |   |   |   |-- backend_wx.cpython-312.pyc
|   |           |   |   |   |-- backend_wxagg.cpython-312.pyc
|   |           |   |   |   |-- backend_wxcairo.cpython-312.pyc
|   |           |   |   |   |-- qt_compat.cpython-312.pyc
|   |           |   |   |   `-- registry.cpython-312.pyc
|   |           |   |   |-- qt_editor
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- _formlayout.cpython-312.pyc
|   |           |   |   |   |   `-- figureoptions.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- _formlayout.py
|   |           |   |   |   `-- figureoptions.py
|   |           |   |   |-- web_backend
|   |           |   |   |   |-- css
|   |           |   |   |   |   |-- boilerplate.css
|   |           |   |   |   |   |-- fbm.css
|   |           |   |   |   |   |-- mpl.css
|   |           |   |   |   |   `-- page.css
|   |           |   |   |   |-- js
|   |           |   |   |   |   |-- mpl.js
|   |           |   |   |   |   |-- mpl_tornado.js
|   |           |   |   |   |   `-- nbagg_mpl.js
|   |           |   |   |   |-- all_figures.html
|   |           |   |   |   |-- ipython_inline_figure.html
|   |           |   |   |   `-- single_figure.html
|   |           |   |   |-- __init__.py
|   |           |   |   |-- _backend_agg.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- _backend_agg.pyi
|   |           |   |   |-- _backend_gtk.py
|   |           |   |   |-- _backend_pdf_ps.py
|   |           |   |   |-- _backend_tk.py
|   |           |   |   |-- _macosx.pyi
|   |           |   |   |-- _tkagg.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- _tkagg.pyi
|   |           |   |   |-- backend_agg.py
|   |           |   |   |-- backend_cairo.py
|   |           |   |   |-- backend_gtk3.py
|   |           |   |   |-- backend_gtk3agg.py
|   |           |   |   |-- backend_gtk3cairo.py
|   |           |   |   |-- backend_gtk4.py
|   |           |   |   |-- backend_gtk4agg.py
|   |           |   |   |-- backend_gtk4cairo.py
|   |           |   |   |-- backend_macosx.py
|   |           |   |   |-- backend_mixed.py
|   |           |   |   |-- backend_nbagg.py
|   |           |   |   |-- backend_pdf.py
|   |           |   |   |-- backend_pgf.py
|   |           |   |   |-- backend_ps.py
|   |           |   |   |-- backend_qt.py
|   |           |   |   |-- backend_qt5.py
|   |           |   |   |-- backend_qt5agg.py
|   |           |   |   |-- backend_qt5cairo.py
|   |           |   |   |-- backend_qtagg.py
|   |           |   |   |-- backend_qtcairo.py
|   |           |   |   |-- backend_svg.py
|   |           |   |   |-- backend_template.py
|   |           |   |   |-- backend_tkagg.py
|   |           |   |   |-- backend_tkcairo.py
|   |           |   |   |-- backend_webagg.py
|   |           |   |   |-- backend_webagg_core.py
|   |           |   |   |-- backend_wx.py
|   |           |   |   |-- backend_wxagg.py
|   |           |   |   |-- backend_wxcairo.py
|   |           |   |   |-- qt_compat.py
|   |           |   |   `-- registry.py
|   |           |   |-- mpl-data
|   |           |   |   |-- fonts
|   |           |   |   |   |-- afm
|   |           |   |   |   |   |-- cmex10.afm
|   |           |   |   |   |   |-- cmmi10.afm
|   |           |   |   |   |   |-- cmr10.afm
|   |           |   |   |   |   |-- cmsy10.afm
|   |           |   |   |   |   |-- cmtt10.afm
|   |           |   |   |   |   |-- pagd8a.afm
|   |           |   |   |   |   |-- pagdo8a.afm
|   |           |   |   |   |   |-- pagk8a.afm
|   |           |   |   |   |   |-- pagko8a.afm
|   |           |   |   |   |   |-- pbkd8a.afm
|   |           |   |   |   |   |-- pbkdi8a.afm
|   |           |   |   |   |   |-- pbkl8a.afm
|   |           |   |   |   |   |-- pbkli8a.afm
|   |           |   |   |   |   |-- pcrb8a.afm
|   |           |   |   |   |   |-- pcrbo8a.afm
|   |           |   |   |   |   |-- pcrr8a.afm
|   |           |   |   |   |   |-- pcrro8a.afm
|   |           |   |   |   |   |-- phvb8a.afm
|   |           |   |   |   |   |-- phvb8an.afm
|   |           |   |   |   |   |-- phvbo8a.afm
|   |           |   |   |   |   |-- phvbo8an.afm
|   |           |   |   |   |   |-- phvl8a.afm
|   |           |   |   |   |   |-- phvlo8a.afm
|   |           |   |   |   |   |-- phvr8a.afm
|   |           |   |   |   |   |-- phvr8an.afm
|   |           |   |   |   |   |-- phvro8a.afm
|   |           |   |   |   |   |-- phvro8an.afm
|   |           |   |   |   |   |-- pncb8a.afm
|   |           |   |   |   |   |-- pncbi8a.afm
|   |           |   |   |   |   |-- pncr8a.afm
|   |           |   |   |   |   |-- pncri8a.afm
|   |           |   |   |   |   |-- pplb8a.afm
|   |           |   |   |   |   |-- pplbi8a.afm
|   |           |   |   |   |   |-- pplr8a.afm
|   |           |   |   |   |   |-- pplri8a.afm
|   |           |   |   |   |   |-- psyr.afm
|   |           |   |   |   |   |-- ptmb8a.afm
|   |           |   |   |   |   |-- ptmbi8a.afm
|   |           |   |   |   |   |-- ptmr8a.afm
|   |           |   |   |   |   |-- ptmri8a.afm
|   |           |   |   |   |   |-- putb8a.afm
|   |           |   |   |   |   |-- putbi8a.afm
|   |           |   |   |   |   |-- putr8a.afm
|   |           |   |   |   |   |-- putri8a.afm
|   |           |   |   |   |   |-- pzcmi8a.afm
|   |           |   |   |   |   `-- pzdr.afm
|   |           |   |   |   |-- pdfcorefonts
|   |           |   |   |   |   |-- Courier-Bold.afm
|   |           |   |   |   |   |-- Courier-BoldOblique.afm
|   |           |   |   |   |   |-- Courier-Oblique.afm
|   |           |   |   |   |   |-- Courier.afm
|   |           |   |   |   |   |-- Helvetica-Bold.afm
|   |           |   |   |   |   |-- Helvetica-BoldOblique.afm
|   |           |   |   |   |   |-- Helvetica-Oblique.afm
|   |           |   |   |   |   |-- Helvetica.afm
|   |           |   |   |   |   |-- Symbol.afm
|   |           |   |   |   |   |-- Times-Bold.afm
|   |           |   |   |   |   |-- Times-BoldItalic.afm
|   |           |   |   |   |   |-- Times-Italic.afm
|   |           |   |   |   |   |-- Times-Roman.afm
|   |           |   |   |   |   |-- ZapfDingbats.afm
|   |           |   |   |   |   `-- readme.txt
|   |           |   |   |   `-- ttf
|   |           |   |   |       |-- DejaVuSans-Bold.ttf
|   |           |   |   |       |-- DejaVuSans-BoldOblique.ttf
|   |           |   |   |       |-- DejaVuSans-Oblique.ttf
|   |           |   |   |       |-- DejaVuSans.ttf
|   |           |   |   |       |-- DejaVuSansDisplay.ttf
|   |           |   |   |       |-- DejaVuSansMono-Bold.ttf
|   |           |   |   |       |-- DejaVuSansMono-BoldOblique.ttf
|   |           |   |   |       |-- DejaVuSansMono-Oblique.ttf
|   |           |   |   |       |-- DejaVuSansMono.ttf
|   |           |   |   |       |-- DejaVuSerif-Bold.ttf
|   |           |   |   |       |-- DejaVuSerif-BoldItalic.ttf
|   |           |   |   |       |-- DejaVuSerif-Italic.ttf
|   |           |   |   |       |-- DejaVuSerif.ttf
|   |           |   |   |       |-- DejaVuSerifDisplay.ttf
|   |           |   |   |       |-- LICENSE_DEJAVU
|   |           |   |   |       |-- LICENSE_STIX
|   |           |   |   |       |-- STIXGeneral.ttf
|   |           |   |   |       |-- STIXGeneralBol.ttf
|   |           |   |   |       |-- STIXGeneralBolIta.ttf
|   |           |   |   |       |-- STIXGeneralItalic.ttf
|   |           |   |   |       |-- STIXNonUni.ttf
|   |           |   |   |       |-- STIXNonUniBol.ttf
|   |           |   |   |       |-- STIXNonUniBolIta.ttf
|   |           |   |   |       |-- STIXNonUniIta.ttf
|   |           |   |   |       |-- STIXSizFiveSymReg.ttf
|   |           |   |   |       |-- STIXSizFourSymBol.ttf
|   |           |   |   |       |-- STIXSizFourSymReg.ttf
|   |           |   |   |       |-- STIXSizOneSymBol.ttf
|   |           |   |   |       |-- STIXSizOneSymReg.ttf
|   |           |   |   |       |-- STIXSizThreeSymBol.ttf
|   |           |   |   |       |-- STIXSizThreeSymReg.ttf
|   |           |   |   |       |-- STIXSizTwoSymBol.ttf
|   |           |   |   |       |-- STIXSizTwoSymReg.ttf
|   |           |   |   |       |-- cmb10.ttf
|   |           |   |   |       |-- cmex10.ttf
|   |           |   |   |       |-- cmmi10.ttf
|   |           |   |   |       |-- cmr10.ttf
|   |           |   |   |       |-- cmss10.ttf
|   |           |   |   |       |-- cmsy10.ttf
|   |           |   |   |       `-- cmtt10.ttf
|   |           |   |   |-- images
|   |           |   |   |   |-- back-symbolic.svg
|   |           |   |   |   |-- back.pdf
|   |           |   |   |   |-- back.png
|   |           |   |   |   |-- back.svg
|   |           |   |   |   |-- back_large.png
|   |           |   |   |   |-- filesave-symbolic.svg
|   |           |   |   |   |-- filesave.pdf
|   |           |   |   |   |-- filesave.png
|   |           |   |   |   |-- filesave.svg
|   |           |   |   |   |-- filesave_large.png
|   |           |   |   |   |-- forward-symbolic.svg
|   |           |   |   |   |-- forward.pdf
|   |           |   |   |   |-- forward.png
|   |           |   |   |   |-- forward.svg
|   |           |   |   |   |-- forward_large.png
|   |           |   |   |   |-- hand.pdf
|   |           |   |   |   |-- hand.png
|   |           |   |   |   |-- hand.svg
|   |           |   |   |   |-- help-symbolic.svg
|   |           |   |   |   |-- help.pdf
|   |           |   |   |   |-- help.png
|   |           |   |   |   |-- help.svg
|   |           |   |   |   |-- help_large.png
|   |           |   |   |   |-- home-symbolic.svg
|   |           |   |   |   |-- home.pdf
|   |           |   |   |   |-- home.png
|   |           |   |   |   |-- home.svg
|   |           |   |   |   |-- home_large.png
|   |           |   |   |   |-- matplotlib.pdf
|   |           |   |   |   |-- matplotlib.png
|   |           |   |   |   |-- matplotlib.svg
|   |           |   |   |   |-- matplotlib_large.png
|   |           |   |   |   |-- move-symbolic.svg
|   |           |   |   |   |-- move.pdf
|   |           |   |   |   |-- move.png
|   |           |   |   |   |-- move.svg
|   |           |   |   |   |-- move_large.png
|   |           |   |   |   |-- qt4_editor_options.pdf
|   |           |   |   |   |-- qt4_editor_options.png
|   |           |   |   |   |-- qt4_editor_options.svg
|   |           |   |   |   |-- qt4_editor_options_large.png
|   |           |   |   |   |-- subplots-symbolic.svg
|   |           |   |   |   |-- subplots.pdf
|   |           |   |   |   |-- subplots.png
|   |           |   |   |   |-- subplots.svg
|   |           |   |   |   |-- subplots_large.png
|   |           |   |   |   |-- zoom_to_rect-symbolic.svg
|   |           |   |   |   |-- zoom_to_rect.pdf
|   |           |   |   |   |-- zoom_to_rect.png
|   |           |   |   |   |-- zoom_to_rect.svg
|   |           |   |   |   `-- zoom_to_rect_large.png
|   |           |   |   |-- plot_directive
|   |           |   |   |   `-- plot_directive.css
|   |           |   |   |-- sample_data
|   |           |   |   |   |-- axes_grid
|   |           |   |   |   |   `-- bivariate_normal.npy
|   |           |   |   |   |-- Minduka_Present_Blue_Pack.png
|   |           |   |   |   |-- README.txt
|   |           |   |   |   |-- Stocks.csv
|   |           |   |   |   |-- data_x_x2_x3.csv
|   |           |   |   |   |-- eeg.dat
|   |           |   |   |   |-- embedding_in_wx3.xrc
|   |           |   |   |   |-- goog.npz
|   |           |   |   |   |-- grace_hopper.jpg
|   |           |   |   |   |-- jacksboro_fault_dem.npz
|   |           |   |   |   |-- logo2.png
|   |           |   |   |   |-- membrane.dat
|   |           |   |   |   |-- msft.csv
|   |           |   |   |   |-- s1045.ima.gz
|   |           |   |   |   `-- topobathy.npz
|   |           |   |   |-- stylelib
|   |           |   |   |   |-- Solarize_Light2.mplstyle
|   |           |   |   |   |-- _classic_test_patch.mplstyle
|   |           |   |   |   |-- _mpl-gallery-nogrid.mplstyle
|   |           |   |   |   |-- _mpl-gallery.mplstyle
|   |           |   |   |   |-- bmh.mplstyle
|   |           |   |   |   |-- classic.mplstyle
|   |           |   |   |   |-- dark_background.mplstyle
|   |           |   |   |   |-- fast.mplstyle
|   |           |   |   |   |-- fivethirtyeight.mplstyle
|   |           |   |   |   |-- ggplot.mplstyle
|   |           |   |   |   |-- grayscale.mplstyle
|   |           |   |   |   |-- petroff10.mplstyle
|   |           |   |   |   |-- seaborn-v0_8-bright.mplstyle
|   |           |   |   |   |-- seaborn-v0_8-colorblind.mplstyle
|   |           |   |   |   |-- seaborn-v0_8-dark-palette.mplstyle
|   |           |   |   |   |-- seaborn-v0_8-dark.mplstyle
|   |           |   |   |   |-- seaborn-v0_8-darkgrid.mplstyle
|   |           |   |   |   |-- seaborn-v0_8-deep.mplstyle
|   |           |   |   |   |-- seaborn-v0_8-muted.mplstyle
|   |           |   |   |   |-- seaborn-v0_8-notebook.mplstyle
|   |           |   |   |   |-- seaborn-v0_8-paper.mplstyle
|   |           |   |   |   |-- seaborn-v0_8-pastel.mplstyle
|   |           |   |   |   |-- seaborn-v0_8-poster.mplstyle
|   |           |   |   |   |-- seaborn-v0_8-talk.mplstyle
|   |           |   |   |   |-- seaborn-v0_8-ticks.mplstyle
|   |           |   |   |   |-- seaborn-v0_8-white.mplstyle
|   |           |   |   |   |-- seaborn-v0_8-whitegrid.mplstyle
|   |           |   |   |   |-- seaborn-v0_8.mplstyle
|   |           |   |   |   `-- tableau-colorblind10.mplstyle
|   |           |   |   |-- kpsewhich.lua
|   |           |   |   `-- matplotlibrc
|   |           |   |-- projections
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- geo.cpython-312.pyc
|   |           |   |   |   `-- polar.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __init__.pyi
|   |           |   |   |-- geo.py
|   |           |   |   |-- geo.pyi
|   |           |   |   |-- polar.py
|   |           |   |   `-- polar.pyi
|   |           |   |-- sphinxext
|   |           |   |   |-- __init__.py
|   |           |   |   |-- figmpl_directive.py
|   |           |   |   |-- mathmpl.py
|   |           |   |   |-- plot_directive.py
|   |           |   |   `-- roles.py
|   |           |   |-- style
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   `-- core.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- core.py
|   |           |   |   `-- core.pyi
|   |           |   |-- testing
|   |           |   |   |-- jpl_units
|   |           |   |   |   |-- Duration.py
|   |           |   |   |   |-- Epoch.py
|   |           |   |   |   |-- EpochConverter.py
|   |           |   |   |   |-- StrConverter.py
|   |           |   |   |   |-- UnitDbl.py
|   |           |   |   |   |-- UnitDblConverter.py
|   |           |   |   |   |-- UnitDblFormatter.py
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __init__.pyi
|   |           |   |   |-- _markers.py
|   |           |   |   |-- compare.py
|   |           |   |   |-- compare.pyi
|   |           |   |   |-- conftest.py
|   |           |   |   |-- conftest.pyi
|   |           |   |   |-- decorators.py
|   |           |   |   |-- decorators.pyi
|   |           |   |   |-- exceptions.py
|   |           |   |   |-- widgets.py
|   |           |   |   `-- widgets.pyi
|   |           |   |-- tests
|   |           |   |   |-- __init__.py
|   |           |   |   |-- conftest.py
|   |           |   |   |-- test_afm.py
|   |           |   |   |-- test_agg.py
|   |           |   |   |-- test_agg_filter.py
|   |           |   |   |-- test_animation.py
|   |           |   |   |-- test_api.py
|   |           |   |   |-- test_arrow_patches.py
|   |           |   |   |-- test_artist.py
|   |           |   |   |-- test_axes.py
|   |           |   |   |-- test_axis.py
|   |           |   |   |-- test_backend_bases.py
|   |           |   |   |-- test_backend_cairo.py
|   |           |   |   |-- test_backend_gtk3.py
|   |           |   |   |-- test_backend_inline.py
|   |           |   |   |-- test_backend_macosx.py
|   |           |   |   |-- test_backend_nbagg.py
|   |           |   |   |-- test_backend_pdf.py
|   |           |   |   |-- test_backend_pgf.py
|   |           |   |   |-- test_backend_ps.py
|   |           |   |   |-- test_backend_qt.py
|   |           |   |   |-- test_backend_registry.py
|   |           |   |   |-- test_backend_svg.py
|   |           |   |   |-- test_backend_template.py
|   |           |   |   |-- test_backend_tk.py
|   |           |   |   |-- test_backend_tools.py
|   |           |   |   |-- test_backend_webagg.py
|   |           |   |   |-- test_backends_interactive.py
|   |           |   |   |-- test_basic.py
|   |           |   |   |-- test_bbox_tight.py
|   |           |   |   |-- test_bezier.py
|   |           |   |   |-- test_category.py
|   |           |   |   |-- test_cbook.py
|   |           |   |   |-- test_collections.py
|   |           |   |   |-- test_colorbar.py
|   |           |   |   |-- test_colors.py
|   |           |   |   |-- test_compare_images.py
|   |           |   |   |-- test_constrainedlayout.py
|   |           |   |   |-- test_container.py
|   |           |   |   |-- test_contour.py
|   |           |   |   |-- test_cycles.py
|   |           |   |   |-- test_dates.py
|   |           |   |   |-- test_datetime.py
|   |           |   |   |-- test_determinism.py
|   |           |   |   |-- test_doc.py
|   |           |   |   |-- test_dviread.py
|   |           |   |   |-- test_figure.py
|   |           |   |   |-- test_font_manager.py
|   |           |   |   |-- test_fontconfig_pattern.py
|   |           |   |   |-- test_ft2font.py
|   |           |   |   |-- test_getattr.py
|   |           |   |   |-- test_gridspec.py
|   |           |   |   |-- test_image.py
|   |           |   |   |-- test_legend.py
|   |           |   |   |-- test_lines.py
|   |           |   |   |-- test_marker.py
|   |           |   |   |-- test_mathtext.py
|   |           |   |   |-- test_matplotlib.py
|   |           |   |   |-- test_mlab.py
|   |           |   |   |-- test_multivariate_colormaps.py
|   |           |   |   |-- test_offsetbox.py
|   |           |   |   |-- test_patches.py
|   |           |   |   |-- test_path.py
|   |           |   |   |-- test_patheffects.py
|   |           |   |   |-- test_pickle.py
|   |           |   |   |-- test_png.py
|   |           |   |   |-- test_polar.py
|   |           |   |   |-- test_preprocess_data.py
|   |           |   |   |-- test_pyplot.py
|   |           |   |   |-- test_quiver.py
|   |           |   |   |-- test_rcparams.py
|   |           |   |   |-- test_sankey.py
|   |           |   |   |-- test_scale.py
|   |           |   |   |-- test_simplification.py
|   |           |   |   |-- test_skew.py
|   |           |   |   |-- test_sphinxext.py
|   |           |   |   |-- test_spines.py
|   |           |   |   |-- test_streamplot.py
|   |           |   |   |-- test_style.py
|   |           |   |   |-- test_subplots.py
|   |           |   |   |-- test_table.py
|   |           |   |   |-- test_testing.py
|   |           |   |   |-- test_texmanager.py
|   |           |   |   |-- test_text.py
|   |           |   |   |-- test_textpath.py
|   |           |   |   |-- test_ticker.py
|   |           |   |   |-- test_tightlayout.py
|   |           |   |   |-- test_transforms.py
|   |           |   |   |-- test_triangulation.py
|   |           |   |   |-- test_type1font.py
|   |           |   |   |-- test_units.py
|   |           |   |   |-- test_usetex.py
|   |           |   |   `-- test_widgets.py
|   |           |   |-- tri
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _triangulation.cpython-312.pyc
|   |           |   |   |   |-- _tricontour.cpython-312.pyc
|   |           |   |   |   |-- _trifinder.cpython-312.pyc
|   |           |   |   |   |-- _triinterpolate.cpython-312.pyc
|   |           |   |   |   |-- _tripcolor.cpython-312.pyc
|   |           |   |   |   |-- _triplot.cpython-312.pyc
|   |           |   |   |   |-- _trirefine.cpython-312.pyc
|   |           |   |   |   `-- _tritools.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- _triangulation.py
|   |           |   |   |-- _triangulation.pyi
|   |           |   |   |-- _tricontour.py
|   |           |   |   |-- _tricontour.pyi
|   |           |   |   |-- _trifinder.py
|   |           |   |   |-- _trifinder.pyi
|   |           |   |   |-- _triinterpolate.py
|   |           |   |   |-- _triinterpolate.pyi
|   |           |   |   |-- _tripcolor.py
|   |           |   |   |-- _tripcolor.pyi
|   |           |   |   |-- _triplot.py
|   |           |   |   |-- _triplot.pyi
|   |           |   |   |-- _trirefine.py
|   |           |   |   |-- _trirefine.pyi
|   |           |   |   |-- _tritools.py
|   |           |   |   `-- _tritools.pyi
|   |           |   |-- __init__.py
|   |           |   |-- __init__.pyi
|   |           |   |-- _afm.py
|   |           |   |-- _animation_data.py
|   |           |   |-- _blocking_input.py
|   |           |   |-- _c_internal_utils.cpython-312-x86_64-linux-gnu.so
|   |           |   |-- _c_internal_utils.pyi
|   |           |   |-- _cm.py
|   |           |   |-- _cm_bivar.py
|   |           |   |-- _cm_listed.py
|   |           |   |-- _cm_multivar.py
|   |           |   |-- _color_data.py
|   |           |   |-- _color_data.pyi
|   |           |   |-- _constrained_layout.py
|   |           |   |-- _docstring.py
|   |           |   |-- _docstring.pyi
|   |           |   |-- _enums.py
|   |           |   |-- _enums.pyi
|   |           |   |-- _fontconfig_pattern.py
|   |           |   |-- _image.cpython-312-x86_64-linux-gnu.so
|   |           |   |-- _image.pyi
|   |           |   |-- _internal_utils.py
|   |           |   |-- _layoutgrid.py
|   |           |   |-- _mathtext.py
|   |           |   |-- _mathtext_data.py
|   |           |   |-- _path.cpython-312-x86_64-linux-gnu.so
|   |           |   |-- _path.pyi
|   |           |   |-- _pylab_helpers.py
|   |           |   |-- _pylab_helpers.pyi
|   |           |   |-- _qhull.cpython-312-x86_64-linux-gnu.so
|   |           |   |-- _qhull.pyi
|   |           |   |-- _text_helpers.py
|   |           |   |-- _tight_bbox.py
|   |           |   |-- _tight_layout.py
|   |           |   |-- _tri.cpython-312-x86_64-linux-gnu.so
|   |           |   |-- _tri.pyi
|   |           |   |-- _type1font.py
|   |           |   |-- _version.py
|   |           |   |-- animation.py
|   |           |   |-- animation.pyi
|   |           |   |-- artist.py
|   |           |   |-- artist.pyi
|   |           |   |-- axis.py
|   |           |   |-- axis.pyi
|   |           |   |-- backend_bases.py
|   |           |   |-- backend_bases.pyi
|   |           |   |-- backend_managers.py
|   |           |   |-- backend_managers.pyi
|   |           |   |-- backend_tools.py
|   |           |   |-- backend_tools.pyi
|   |           |   |-- bezier.py
|   |           |   |-- bezier.pyi
|   |           |   |-- category.py
|   |           |   |-- cbook.py
|   |           |   |-- cbook.pyi
|   |           |   |-- cm.py
|   |           |   |-- cm.pyi
|   |           |   |-- collections.py
|   |           |   |-- collections.pyi
|   |           |   |-- colorbar.py
|   |           |   |-- colorbar.pyi
|   |           |   |-- colorizer.py
|   |           |   |-- colorizer.pyi
|   |           |   |-- colors.py
|   |           |   |-- colors.pyi
|   |           |   |-- container.py
|   |           |   |-- container.pyi
|   |           |   |-- contour.py
|   |           |   |-- contour.pyi
|   |           |   |-- dates.py
|   |           |   |-- dviread.py
|   |           |   |-- dviread.pyi
|   |           |   |-- figure.py
|   |           |   |-- figure.pyi
|   |           |   |-- font_manager.py
|   |           |   |-- font_manager.pyi
|   |           |   |-- ft2font.cpython-312-x86_64-linux-gnu.so
|   |           |   |-- ft2font.pyi
|   |           |   |-- gridspec.py
|   |           |   |-- gridspec.pyi
|   |           |   |-- hatch.py
|   |           |   |-- hatch.pyi
|   |           |   |-- image.py
|   |           |   |-- image.pyi
|   |           |   |-- inset.py
|   |           |   |-- inset.pyi
|   |           |   |-- layout_engine.py
|   |           |   |-- layout_engine.pyi
|   |           |   |-- legend.py
|   |           |   |-- legend.pyi
|   |           |   |-- legend_handler.py
|   |           |   |-- legend_handler.pyi
|   |           |   |-- lines.py
|   |           |   |-- lines.pyi
|   |           |   |-- markers.py
|   |           |   |-- markers.pyi
|   |           |   |-- mathtext.py
|   |           |   |-- mathtext.pyi
|   |           |   |-- mlab.py
|   |           |   |-- mlab.pyi
|   |           |   |-- offsetbox.py
|   |           |   |-- offsetbox.pyi
|   |           |   |-- patches.py
|   |           |   |-- patches.pyi
|   |           |   |-- path.py
|   |           |   |-- path.pyi
|   |           |   |-- patheffects.py
|   |           |   |-- patheffects.pyi
|   |           |   |-- py.typed
|   |           |   |-- pylab.py
|   |           |   |-- pyplot.py
|   |           |   |-- quiver.py
|   |           |   |-- quiver.pyi
|   |           |   |-- rcsetup.py
|   |           |   |-- rcsetup.pyi
|   |           |   |-- sankey.py
|   |           |   |-- sankey.pyi
|   |           |   |-- scale.py
|   |           |   |-- scale.pyi
|   |           |   |-- spines.py
|   |           |   |-- spines.pyi
|   |           |   |-- stackplot.py
|   |           |   |-- stackplot.pyi
|   |           |   |-- streamplot.py
|   |           |   |-- streamplot.pyi
|   |           |   |-- table.py
|   |           |   |-- table.pyi
|   |           |   |-- texmanager.py
|   |           |   |-- texmanager.pyi
|   |           |   |-- text.py
|   |           |   |-- text.pyi
|   |           |   |-- textpath.py
|   |           |   |-- textpath.pyi
|   |           |   |-- ticker.py
|   |           |   |-- ticker.pyi
|   |           |   |-- transforms.py
|   |           |   |-- transforms.pyi
|   |           |   |-- typing.py
|   |           |   |-- units.py
|   |           |   |-- widgets.py
|   |           |   `-- widgets.pyi
|   |           |-- matplotlib-3.10.6.dist-info
|   |           |   |-- LICENSE
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   `-- WHEEL
|   |           |-- mpl_toolkits
|   |           |   |-- axes_grid1
|   |           |   |   |-- tests
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- conftest.py
|   |           |   |   |   `-- test_axes_grid1.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- anchored_artists.py
|   |           |   |   |-- axes_divider.py
|   |           |   |   |-- axes_grid.py
|   |           |   |   |-- axes_rgb.py
|   |           |   |   |-- axes_size.py
|   |           |   |   |-- inset_locator.py
|   |           |   |   |-- mpl_axes.py
|   |           |   |   `-- parasite_axes.py
|   |           |   |-- axisartist
|   |           |   |   |-- tests
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- conftest.py
|   |           |   |   |   |-- test_angle_helper.py
|   |           |   |   |   |-- test_axis_artist.py
|   |           |   |   |   |-- test_axislines.py
|   |           |   |   |   |-- test_floating_axes.py
|   |           |   |   |   |-- test_grid_finder.py
|   |           |   |   |   `-- test_grid_helper_curvelinear.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- angle_helper.py
|   |           |   |   |-- axes_divider.py
|   |           |   |   |-- axis_artist.py
|   |           |   |   |-- axisline_style.py
|   |           |   |   |-- axislines.py
|   |           |   |   |-- floating_axes.py
|   |           |   |   |-- grid_finder.py
|   |           |   |   |-- grid_helper_curvelinear.py
|   |           |   |   `-- parasite_axes.py
|   |           |   `-- mplot3d
|   |           |       |-- __pycache__
|   |           |       |   |-- __init__.cpython-312.pyc
|   |           |       |   |-- art3d.cpython-312.pyc
|   |           |       |   |-- axes3d.cpython-312.pyc
|   |           |       |   |-- axis3d.cpython-312.pyc
|   |           |       |   `-- proj3d.cpython-312.pyc
|   |           |       |-- tests
|   |           |       |   |-- __init__.py
|   |           |       |   |-- conftest.py
|   |           |       |   |-- test_art3d.py
|   |           |       |   |-- test_axes3d.py
|   |           |       |   `-- test_legend3d.py
|   |           |       |-- __init__.py
|   |           |       |-- art3d.py
|   |           |       |-- axes3d.py
|   |           |       |-- axis3d.py
|   |           |       `-- proj3d.py
|   |           |-- numpy
|   |           |   |-- __pycache__
|   |           |   |   |-- __config__.cpython-312.pyc
|   |           |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |-- _array_api_info.cpython-312.pyc
|   |           |   |   |-- _configtool.cpython-312.pyc
|   |           |   |   |-- _distributor_init.cpython-312.pyc
|   |           |   |   |-- _expired_attrs_2_0.cpython-312.pyc
|   |           |   |   |-- _globals.cpython-312.pyc
|   |           |   |   |-- _pytesttester.cpython-312.pyc
|   |           |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |-- ctypeslib.cpython-312.pyc
|   |           |   |   |-- dtypes.cpython-312.pyc
|   |           |   |   |-- exceptions.cpython-312.pyc
|   |           |   |   |-- matlib.cpython-312.pyc
|   |           |   |   `-- version.cpython-312.pyc
|   |           |   |-- _core
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _add_newdocs.cpython-312.pyc
|   |           |   |   |   |-- _add_newdocs_scalars.cpython-312.pyc
|   |           |   |   |   |-- _asarray.cpython-312.pyc
|   |           |   |   |   |-- _dtype.cpython-312.pyc
|   |           |   |   |   |-- _dtype_ctypes.cpython-312.pyc
|   |           |   |   |   |-- _exceptions.cpython-312.pyc
|   |           |   |   |   |-- _internal.cpython-312.pyc
|   |           |   |   |   |-- _machar.cpython-312.pyc
|   |           |   |   |   |-- _methods.cpython-312.pyc
|   |           |   |   |   |-- _string_helpers.cpython-312.pyc
|   |           |   |   |   |-- _type_aliases.cpython-312.pyc
|   |           |   |   |   |-- _ufunc_config.cpython-312.pyc
|   |           |   |   |   |-- arrayprint.cpython-312.pyc
|   |           |   |   |   |-- cversions.cpython-312.pyc
|   |           |   |   |   |-- defchararray.cpython-312.pyc
|   |           |   |   |   |-- einsumfunc.cpython-312.pyc
|   |           |   |   |   |-- fromnumeric.cpython-312.pyc
|   |           |   |   |   |-- function_base.cpython-312.pyc
|   |           |   |   |   |-- getlimits.cpython-312.pyc
|   |           |   |   |   |-- memmap.cpython-312.pyc
|   |           |   |   |   |-- multiarray.cpython-312.pyc
|   |           |   |   |   |-- numeric.cpython-312.pyc
|   |           |   |   |   |-- numerictypes.cpython-312.pyc
|   |           |   |   |   |-- overrides.cpython-312.pyc
|   |           |   |   |   |-- printoptions.cpython-312.pyc
|   |           |   |   |   |-- records.cpython-312.pyc
|   |           |   |   |   |-- shape_base.cpython-312.pyc
|   |           |   |   |   |-- strings.cpython-312.pyc
|   |           |   |   |   `-- umath.cpython-312.pyc
|   |           |   |   |-- include
|   |           |   |   |   `-- numpy
|   |           |   |   |       |-- random
|   |           |   |   |       |   |-- LICENSE.txt
|   |           |   |   |       |   |-- bitgen.h
|   |           |   |   |       |   |-- distributions.h
|   |           |   |   |       |   `-- libdivide.h
|   |           |   |   |       |-- __multiarray_api.c
|   |           |   |   |       |-- __multiarray_api.h
|   |           |   |   |       |-- __ufunc_api.c
|   |           |   |   |       |-- __ufunc_api.h
|   |           |   |   |       |-- _neighborhood_iterator_imp.h
|   |           |   |   |       |-- _numpyconfig.h
|   |           |   |   |       |-- _public_dtype_api_table.h
|   |           |   |   |       |-- arrayobject.h
|   |           |   |   |       |-- arrayscalars.h
|   |           |   |   |       |-- dtype_api.h
|   |           |   |   |       |-- halffloat.h
|   |           |   |   |       |-- ndarrayobject.h
|   |           |   |   |       |-- ndarraytypes.h
|   |           |   |   |       |-- npy_1_7_deprecated_api.h
|   |           |   |   |       |-- npy_2_compat.h
|   |           |   |   |       |-- npy_2_complexcompat.h
|   |           |   |   |       |-- npy_3kcompat.h
|   |           |   |   |       |-- npy_common.h
|   |           |   |   |       |-- npy_cpu.h
|   |           |   |   |       |-- npy_endian.h
|   |           |   |   |       |-- npy_math.h
|   |           |   |   |       |-- npy_no_deprecated_api.h
|   |           |   |   |       |-- npy_os.h
|   |           |   |   |       |-- numpyconfig.h
|   |           |   |   |       |-- ufuncobject.h
|   |           |   |   |       `-- utils.h
|   |           |   |   |-- lib
|   |           |   |   |   |-- npy-pkg-config
|   |           |   |   |   |   |-- mlib.ini
|   |           |   |   |   |   `-- npymath.ini
|   |           |   |   |   |-- pkgconfig
|   |           |   |   |   |   `-- numpy.pc
|   |           |   |   |   `-- libnpymath.a
|   |           |   |   |-- tests
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- _locales.cpython-312.pyc
|   |           |   |   |   |   |-- _natype.cpython-312.pyc
|   |           |   |   |   |   |-- test__exceptions.cpython-312.pyc
|   |           |   |   |   |   |-- test_abc.cpython-312.pyc
|   |           |   |   |   |   |-- test_api.cpython-312.pyc
|   |           |   |   |   |   |-- test_argparse.cpython-312.pyc
|   |           |   |   |   |   |-- test_array_api_info.cpython-312.pyc
|   |           |   |   |   |   |-- test_array_coercion.cpython-312.pyc
|   |           |   |   |   |   |-- test_array_interface.cpython-312.pyc
|   |           |   |   |   |   |-- test_arraymethod.cpython-312.pyc
|   |           |   |   |   |   |-- test_arrayobject.cpython-312.pyc
|   |           |   |   |   |   |-- test_arrayprint.cpython-312.pyc
|   |           |   |   |   |   |-- test_casting_floatingpoint_errors.cpython-312.pyc
|   |           |   |   |   |   |-- test_casting_unittests.cpython-312.pyc
|   |           |   |   |   |   |-- test_conversion_utils.cpython-312.pyc
|   |           |   |   |   |   |-- test_cpu_dispatcher.cpython-312.pyc
|   |           |   |   |   |   |-- test_cpu_features.cpython-312.pyc
|   |           |   |   |   |   |-- test_custom_dtypes.cpython-312.pyc
|   |           |   |   |   |   |-- test_cython.cpython-312.pyc
|   |           |   |   |   |   |-- test_datetime.cpython-312.pyc
|   |           |   |   |   |   |-- test_defchararray.cpython-312.pyc
|   |           |   |   |   |   |-- test_deprecations.cpython-312.pyc
|   |           |   |   |   |   |-- test_dlpack.cpython-312.pyc
|   |           |   |   |   |   |-- test_dtype.cpython-312.pyc
|   |           |   |   |   |   |-- test_einsum.cpython-312.pyc
|   |           |   |   |   |   |-- test_errstate.cpython-312.pyc
|   |           |   |   |   |   |-- test_extint128.cpython-312.pyc
|   |           |   |   |   |   |-- test_function_base.cpython-312.pyc
|   |           |   |   |   |   |-- test_getlimits.cpython-312.pyc
|   |           |   |   |   |   |-- test_half.cpython-312.pyc
|   |           |   |   |   |   |-- test_hashtable.cpython-312.pyc
|   |           |   |   |   |   |-- test_indexerrors.cpython-312.pyc
|   |           |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |-- test_item_selection.cpython-312.pyc
|   |           |   |   |   |   |-- test_limited_api.cpython-312.pyc
|   |           |   |   |   |   |-- test_longdouble.cpython-312.pyc
|   |           |   |   |   |   |-- test_machar.cpython-312.pyc
|   |           |   |   |   |   |-- test_mem_overlap.cpython-312.pyc
|   |           |   |   |   |   |-- test_mem_policy.cpython-312.pyc
|   |           |   |   |   |   |-- test_memmap.cpython-312.pyc
|   |           |   |   |   |   |-- test_multiarray.cpython-312.pyc
|   |           |   |   |   |   |-- test_multithreading.cpython-312.pyc
|   |           |   |   |   |   |-- test_nditer.cpython-312.pyc
|   |           |   |   |   |   |-- test_nep50_promotions.cpython-312.pyc
|   |           |   |   |   |   |-- test_numeric.cpython-312.pyc
|   |           |   |   |   |   |-- test_numerictypes.cpython-312.pyc
|   |           |   |   |   |   |-- test_overrides.cpython-312.pyc
|   |           |   |   |   |   |-- test_print.cpython-312.pyc
|   |           |   |   |   |   |-- test_protocols.cpython-312.pyc
|   |           |   |   |   |   |-- test_records.cpython-312.pyc
|   |           |   |   |   |   |-- test_regression.cpython-312.pyc
|   |           |   |   |   |   |-- test_scalar_ctors.cpython-312.pyc
|   |           |   |   |   |   |-- test_scalar_methods.cpython-312.pyc
|   |           |   |   |   |   |-- test_scalarbuffer.cpython-312.pyc
|   |           |   |   |   |   |-- test_scalarinherit.cpython-312.pyc
|   |           |   |   |   |   |-- test_scalarmath.cpython-312.pyc
|   |           |   |   |   |   |-- test_scalarprint.cpython-312.pyc
|   |           |   |   |   |   |-- test_shape_base.cpython-312.pyc
|   |           |   |   |   |   |-- test_simd.cpython-312.pyc
|   |           |   |   |   |   |-- test_simd_module.cpython-312.pyc
|   |           |   |   |   |   |-- test_stringdtype.cpython-312.pyc
|   |           |   |   |   |   |-- test_strings.cpython-312.pyc
|   |           |   |   |   |   |-- test_ufunc.cpython-312.pyc
|   |           |   |   |   |   |-- test_umath.cpython-312.pyc
|   |           |   |   |   |   |-- test_umath_accuracy.cpython-312.pyc
|   |           |   |   |   |   |-- test_umath_complex.cpython-312.pyc
|   |           |   |   |   |   `-- test_unicode.cpython-312.pyc
|   |           |   |   |   |-- examples
|   |           |   |   |   |   |-- cython
|   |           |   |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |   `-- setup.cpython-312.pyc
|   |           |   |   |   |   |   |-- checks.pyx
|   |           |   |   |   |   |   |-- meson.build
|   |           |   |   |   |   |   `-- setup.py
|   |           |   |   |   |   `-- limited_api
|   |           |   |   |   |       |-- __pycache__
|   |           |   |   |   |       |   `-- setup.cpython-312.pyc
|   |           |   |   |   |       |-- limited_api1.c
|   |           |   |   |   |       |-- limited_api2.pyx
|   |           |   |   |   |       |-- limited_api_latest.c
|   |           |   |   |   |       |-- meson.build
|   |           |   |   |   |       `-- setup.py
|   |           |   |   |   |-- _locales.py
|   |           |   |   |   |-- _natype.py
|   |           |   |   |   |-- test__exceptions.py
|   |           |   |   |   |-- test_abc.py
|   |           |   |   |   |-- test_api.py
|   |           |   |   |   |-- test_argparse.py
|   |           |   |   |   |-- test_array_api_info.py
|   |           |   |   |   |-- test_array_coercion.py
|   |           |   |   |   |-- test_array_interface.py
|   |           |   |   |   |-- test_arraymethod.py
|   |           |   |   |   |-- test_arrayobject.py
|   |           |   |   |   |-- test_arrayprint.py
|   |           |   |   |   |-- test_casting_floatingpoint_errors.py
|   |           |   |   |   |-- test_casting_unittests.py
|   |           |   |   |   |-- test_conversion_utils.py
|   |           |   |   |   |-- test_cpu_dispatcher.py
|   |           |   |   |   |-- test_cpu_features.py
|   |           |   |   |   |-- test_custom_dtypes.py
|   |           |   |   |   |-- test_cython.py
|   |           |   |   |   |-- test_datetime.py
|   |           |   |   |   |-- test_defchararray.py
|   |           |   |   |   |-- test_deprecations.py
|   |           |   |   |   |-- test_dlpack.py
|   |           |   |   |   |-- test_dtype.py
|   |           |   |   |   |-- test_einsum.py
|   |           |   |   |   |-- test_errstate.py
|   |           |   |   |   |-- test_extint128.py
|   |           |   |   |   |-- test_function_base.py
|   |           |   |   |   |-- test_getlimits.py
|   |           |   |   |   |-- test_half.py
|   |           |   |   |   |-- test_hashtable.py
|   |           |   |   |   |-- test_indexerrors.py
|   |           |   |   |   |-- test_indexing.py
|   |           |   |   |   |-- test_item_selection.py
|   |           |   |   |   |-- test_limited_api.py
|   |           |   |   |   |-- test_longdouble.py
|   |           |   |   |   |-- test_machar.py
|   |           |   |   |   |-- test_mem_overlap.py
|   |           |   |   |   |-- test_mem_policy.py
|   |           |   |   |   |-- test_memmap.py
|   |           |   |   |   |-- test_multiarray.py
|   |           |   |   |   |-- test_multithreading.py
|   |           |   |   |   |-- test_nditer.py
|   |           |   |   |   |-- test_nep50_promotions.py
|   |           |   |   |   |-- test_numeric.py
|   |           |   |   |   |-- test_numerictypes.py
|   |           |   |   |   |-- test_overrides.py
|   |           |   |   |   |-- test_print.py
|   |           |   |   |   |-- test_protocols.py
|   |           |   |   |   |-- test_records.py
|   |           |   |   |   |-- test_regression.py
|   |           |   |   |   |-- test_scalar_ctors.py
|   |           |   |   |   |-- test_scalar_methods.py
|   |           |   |   |   |-- test_scalarbuffer.py
|   |           |   |   |   |-- test_scalarinherit.py
|   |           |   |   |   |-- test_scalarmath.py
|   |           |   |   |   |-- test_scalarprint.py
|   |           |   |   |   |-- test_shape_base.py
|   |           |   |   |   |-- test_simd.py
|   |           |   |   |   |-- test_simd_module.py
|   |           |   |   |   |-- test_stringdtype.py
|   |           |   |   |   |-- test_strings.py
|   |           |   |   |   |-- test_ufunc.py
|   |           |   |   |   |-- test_umath.py
|   |           |   |   |   |-- test_umath_accuracy.py
|   |           |   |   |   |-- test_umath_complex.py
|   |           |   |   |   `-- test_unicode.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __init__.pyi
|   |           |   |   |-- _add_newdocs.py
|   |           |   |   |-- _add_newdocs.pyi
|   |           |   |   |-- _add_newdocs_scalars.py
|   |           |   |   |-- _add_newdocs_scalars.pyi
|   |           |   |   |-- _asarray.py
|   |           |   |   |-- _asarray.pyi
|   |           |   |   |-- _dtype.py
|   |           |   |   |-- _dtype.pyi
|   |           |   |   |-- _dtype_ctypes.py
|   |           |   |   |-- _dtype_ctypes.pyi
|   |           |   |   |-- _exceptions.py
|   |           |   |   |-- _exceptions.pyi
|   |           |   |   |-- _internal.py
|   |           |   |   |-- _internal.pyi
|   |           |   |   |-- _machar.py
|   |           |   |   |-- _machar.pyi
|   |           |   |   |-- _methods.py
|   |           |   |   |-- _methods.pyi
|   |           |   |   |-- _multiarray_tests.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- _multiarray_umath.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- _operand_flag_tests.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- _rational_tests.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- _simd.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- _simd.pyi
|   |           |   |   |-- _string_helpers.py
|   |           |   |   |-- _string_helpers.pyi
|   |           |   |   |-- _struct_ufunc_tests.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- _type_aliases.py
|   |           |   |   |-- _type_aliases.pyi
|   |           |   |   |-- _ufunc_config.py
|   |           |   |   |-- _ufunc_config.pyi
|   |           |   |   |-- _umath_tests.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- arrayprint.py
|   |           |   |   |-- arrayprint.pyi
|   |           |   |   |-- cversions.py
|   |           |   |   |-- defchararray.py
|   |           |   |   |-- defchararray.pyi
|   |           |   |   |-- einsumfunc.py
|   |           |   |   |-- einsumfunc.pyi
|   |           |   |   |-- fromnumeric.py
|   |           |   |   |-- fromnumeric.pyi
|   |           |   |   |-- function_base.py
|   |           |   |   |-- function_base.pyi
|   |           |   |   |-- getlimits.py
|   |           |   |   |-- getlimits.pyi
|   |           |   |   |-- memmap.py
|   |           |   |   |-- memmap.pyi
|   |           |   |   |-- multiarray.py
|   |           |   |   |-- multiarray.pyi
|   |           |   |   |-- numeric.py
|   |           |   |   |-- numeric.pyi
|   |           |   |   |-- numerictypes.py
|   |           |   |   |-- numerictypes.pyi
|   |           |   |   |-- overrides.py
|   |           |   |   |-- overrides.pyi
|   |           |   |   |-- printoptions.py
|   |           |   |   |-- printoptions.pyi
|   |           |   |   |-- records.py
|   |           |   |   |-- records.pyi
|   |           |   |   |-- shape_base.py
|   |           |   |   |-- shape_base.pyi
|   |           |   |   |-- strings.py
|   |           |   |   |-- strings.pyi
|   |           |   |   |-- umath.py
|   |           |   |   `-- umath.pyi
|   |           |   |-- _pyinstaller
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   `-- hook-numpy.cpython-312.pyc
|   |           |   |   |-- tests
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- pyinstaller-smoke.cpython-312.pyc
|   |           |   |   |   |   `-- test_pyinstaller.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- pyinstaller-smoke.py
|   |           |   |   |   `-- test_pyinstaller.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __init__.pyi
|   |           |   |   |-- hook-numpy.py
|   |           |   |   `-- hook-numpy.pyi
|   |           |   |-- _typing
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _add_docstring.cpython-312.pyc
|   |           |   |   |   |-- _array_like.cpython-312.pyc
|   |           |   |   |   |-- _char_codes.cpython-312.pyc
|   |           |   |   |   |-- _dtype_like.cpython-312.pyc
|   |           |   |   |   |-- _extended_precision.cpython-312.pyc
|   |           |   |   |   |-- _nbit.cpython-312.pyc
|   |           |   |   |   |-- _nbit_base.cpython-312.pyc
|   |           |   |   |   |-- _nested_sequence.cpython-312.pyc
|   |           |   |   |   |-- _scalars.cpython-312.pyc
|   |           |   |   |   |-- _shape.cpython-312.pyc
|   |           |   |   |   `-- _ufunc.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- _add_docstring.py
|   |           |   |   |-- _array_like.py
|   |           |   |   |-- _callable.pyi
|   |           |   |   |-- _char_codes.py
|   |           |   |   |-- _dtype_like.py
|   |           |   |   |-- _extended_precision.py
|   |           |   |   |-- _nbit.py
|   |           |   |   |-- _nbit_base.py
|   |           |   |   |-- _nested_sequence.py
|   |           |   |   |-- _scalars.py
|   |           |   |   |-- _shape.py
|   |           |   |   |-- _ufunc.py
|   |           |   |   `-- _ufunc.pyi
|   |           |   |-- _utils
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _convertions.cpython-312.pyc
|   |           |   |   |   |-- _inspect.cpython-312.pyc
|   |           |   |   |   `-- _pep440.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __init__.pyi
|   |           |   |   |-- _convertions.py
|   |           |   |   |-- _convertions.pyi
|   |           |   |   |-- _inspect.py
|   |           |   |   |-- _inspect.pyi
|   |           |   |   |-- _pep440.py
|   |           |   |   `-- _pep440.pyi
|   |           |   |-- char
|   |           |   |   |-- __pycache__
|   |           |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   `-- __init__.pyi
|   |           |   |-- compat
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   `-- py3k.cpython-312.pyc
|   |           |   |   |-- tests
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- __init__.py
|   |           |   |   `-- py3k.py
|   |           |   |-- core
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _dtype.cpython-312.pyc
|   |           |   |   |   |-- _dtype_ctypes.cpython-312.pyc
|   |           |   |   |   |-- _internal.cpython-312.pyc
|   |           |   |   |   |-- _multiarray_umath.cpython-312.pyc
|   |           |   |   |   |-- _utils.cpython-312.pyc
|   |           |   |   |   |-- arrayprint.cpython-312.pyc
|   |           |   |   |   |-- defchararray.cpython-312.pyc
|   |           |   |   |   |-- einsumfunc.cpython-312.pyc
|   |           |   |   |   |-- fromnumeric.cpython-312.pyc
|   |           |   |   |   |-- function_base.cpython-312.pyc
|   |           |   |   |   |-- getlimits.cpython-312.pyc
|   |           |   |   |   |-- multiarray.cpython-312.pyc
|   |           |   |   |   |-- numeric.cpython-312.pyc
|   |           |   |   |   |-- numerictypes.cpython-312.pyc
|   |           |   |   |   |-- overrides.cpython-312.pyc
|   |           |   |   |   |-- records.cpython-312.pyc
|   |           |   |   |   |-- shape_base.cpython-312.pyc
|   |           |   |   |   `-- umath.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __init__.pyi
|   |           |   |   |-- _dtype.py
|   |           |   |   |-- _dtype.pyi
|   |           |   |   |-- _dtype_ctypes.py
|   |           |   |   |-- _dtype_ctypes.pyi
|   |           |   |   |-- _internal.py
|   |           |   |   |-- _multiarray_umath.py
|   |           |   |   |-- _utils.py
|   |           |   |   |-- arrayprint.py
|   |           |   |   |-- defchararray.py
|   |           |   |   |-- einsumfunc.py
|   |           |   |   |-- fromnumeric.py
|   |           |   |   |-- function_base.py
|   |           |   |   |-- getlimits.py
|   |           |   |   |-- multiarray.py
|   |           |   |   |-- numeric.py
|   |           |   |   |-- numerictypes.py
|   |           |   |   |-- overrides.py
|   |           |   |   |-- overrides.pyi
|   |           |   |   |-- records.py
|   |           |   |   |-- shape_base.py
|   |           |   |   `-- umath.py
|   |           |   |-- doc
|   |           |   |   |-- __pycache__
|   |           |   |   |   `-- ufuncs.cpython-312.pyc
|   |           |   |   `-- ufuncs.py
|   |           |   |-- f2py
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |   |-- __version__.cpython-312.pyc
|   |           |   |   |   |-- _isocbind.cpython-312.pyc
|   |           |   |   |   |-- _src_pyf.cpython-312.pyc
|   |           |   |   |   |-- auxfuncs.cpython-312.pyc
|   |           |   |   |   |-- capi_maps.cpython-312.pyc
|   |           |   |   |   |-- cb_rules.cpython-312.pyc
|   |           |   |   |   |-- cfuncs.cpython-312.pyc
|   |           |   |   |   |-- common_rules.cpython-312.pyc
|   |           |   |   |   |-- crackfortran.cpython-312.pyc
|   |           |   |   |   |-- diagnose.cpython-312.pyc
|   |           |   |   |   |-- f2py2e.cpython-312.pyc
|   |           |   |   |   |-- f90mod_rules.cpython-312.pyc
|   |           |   |   |   |-- func2subr.cpython-312.pyc
|   |           |   |   |   |-- rules.cpython-312.pyc
|   |           |   |   |   |-- symbolic.cpython-312.pyc
|   |           |   |   |   `-- use_rules.cpython-312.pyc
|   |           |   |   |-- _backends
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- _backend.cpython-312.pyc
|   |           |   |   |   |   |-- _distutils.cpython-312.pyc
|   |           |   |   |   |   `-- _meson.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- _backend.py
|   |           |   |   |   |-- _distutils.py
|   |           |   |   |   |-- _meson.py
|   |           |   |   |   `-- meson.build.template
|   |           |   |   |-- src
|   |           |   |   |   |-- fortranobject.c
|   |           |   |   |   `-- fortranobject.h
|   |           |   |   |-- tests
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_abstract_interface.cpython-312.pyc
|   |           |   |   |   |   |-- test_array_from_pyobj.cpython-312.pyc
|   |           |   |   |   |   |-- test_assumed_shape.cpython-312.pyc
|   |           |   |   |   |   |-- test_block_docstring.cpython-312.pyc
|   |           |   |   |   |   |-- test_callback.cpython-312.pyc
|   |           |   |   |   |   |-- test_character.cpython-312.pyc
|   |           |   |   |   |   |-- test_common.cpython-312.pyc
|   |           |   |   |   |   |-- test_crackfortran.cpython-312.pyc
|   |           |   |   |   |   |-- test_data.cpython-312.pyc
|   |           |   |   |   |   |-- test_docs.cpython-312.pyc
|   |           |   |   |   |   |-- test_f2cmap.cpython-312.pyc
|   |           |   |   |   |   |-- test_f2py2e.cpython-312.pyc
|   |           |   |   |   |   |-- test_isoc.cpython-312.pyc
|   |           |   |   |   |   |-- test_kind.cpython-312.pyc
|   |           |   |   |   |   |-- test_mixed.cpython-312.pyc
|   |           |   |   |   |   |-- test_modules.cpython-312.pyc
|   |           |   |   |   |   |-- test_parameter.cpython-312.pyc
|   |           |   |   |   |   |-- test_pyf_src.cpython-312.pyc
|   |           |   |   |   |   |-- test_quoted_character.cpython-312.pyc
|   |           |   |   |   |   |-- test_regression.cpython-312.pyc
|   |           |   |   |   |   |-- test_return_character.cpython-312.pyc
|   |           |   |   |   |   |-- test_return_complex.cpython-312.pyc
|   |           |   |   |   |   |-- test_return_integer.cpython-312.pyc
|   |           |   |   |   |   |-- test_return_logical.cpython-312.pyc
|   |           |   |   |   |   |-- test_return_real.cpython-312.pyc
|   |           |   |   |   |   |-- test_routines.cpython-312.pyc
|   |           |   |   |   |   |-- test_semicolon_split.cpython-312.pyc
|   |           |   |   |   |   |-- test_size.cpython-312.pyc
|   |           |   |   |   |   |-- test_string.cpython-312.pyc
|   |           |   |   |   |   |-- test_symbolic.cpython-312.pyc
|   |           |   |   |   |   |-- test_value_attrspec.cpython-312.pyc
|   |           |   |   |   |   `-- util.cpython-312.pyc
|   |           |   |   |   |-- src
|   |           |   |   |   |   |-- abstract_interface
|   |           |   |   |   |   |   |-- foo.f90
|   |           |   |   |   |   |   `-- gh18403_mod.f90
|   |           |   |   |   |   |-- array_from_pyobj
|   |           |   |   |   |   |   `-- wrapmodule.c
|   |           |   |   |   |   |-- assumed_shape
|   |           |   |   |   |   |   |-- .f2py_f2cmap
|   |           |   |   |   |   |   |-- foo_free.f90
|   |           |   |   |   |   |   |-- foo_mod.f90
|   |           |   |   |   |   |   |-- foo_use.f90
|   |           |   |   |   |   |   `-- precision.f90
|   |           |   |   |   |   |-- block_docstring
|   |           |   |   |   |   |   `-- foo.f
|   |           |   |   |   |   |-- callback
|   |           |   |   |   |   |   |-- foo.f
|   |           |   |   |   |   |   |-- gh17797.f90
|   |           |   |   |   |   |   |-- gh18335.f90
|   |           |   |   |   |   |   |-- gh25211.f
|   |           |   |   |   |   |   |-- gh25211.pyf
|   |           |   |   |   |   |   `-- gh26681.f90
|   |           |   |   |   |   |-- cli
|   |           |   |   |   |   |   |-- gh_22819.pyf
|   |           |   |   |   |   |   |-- hi77.f
|   |           |   |   |   |   |   `-- hiworld.f90
|   |           |   |   |   |   |-- common
|   |           |   |   |   |   |   |-- block.f
|   |           |   |   |   |   |   `-- gh19161.f90
|   |           |   |   |   |   |-- crackfortran
|   |           |   |   |   |   |   |-- accesstype.f90
|   |           |   |   |   |   |   |-- common_with_division.f
|   |           |   |   |   |   |   |-- data_common.f
|   |           |   |   |   |   |   |-- data_multiplier.f
|   |           |   |   |   |   |   |-- data_stmts.f90
|   |           |   |   |   |   |   |-- data_with_comments.f
|   |           |   |   |   |   |   |-- foo_deps.f90
|   |           |   |   |   |   |   |-- gh15035.f
|   |           |   |   |   |   |   |-- gh17859.f
|   |           |   |   |   |   |   |-- gh22648.pyf
|   |           |   |   |   |   |   |-- gh23533.f
|   |           |   |   |   |   |   |-- gh23598.f90
|   |           |   |   |   |   |   |-- gh23598Warn.f90
|   |           |   |   |   |   |   |-- gh23879.f90
|   |           |   |   |   |   |   |-- gh27697.f90
|   |           |   |   |   |   |   |-- gh2848.f90
|   |           |   |   |   |   |   |-- operators.f90
|   |           |   |   |   |   |   |-- privatemod.f90
|   |           |   |   |   |   |   |-- publicmod.f90
|   |           |   |   |   |   |   |-- pubprivmod.f90
|   |           |   |   |   |   |   `-- unicode_comment.f90
|   |           |   |   |   |   |-- f2cmap
|   |           |   |   |   |   |   |-- .f2py_f2cmap
|   |           |   |   |   |   |   `-- isoFortranEnvMap.f90
|   |           |   |   |   |   |-- isocintrin
|   |           |   |   |   |   |   `-- isoCtests.f90
|   |           |   |   |   |   |-- kind
|   |           |   |   |   |   |   `-- foo.f90
|   |           |   |   |   |   |-- mixed
|   |           |   |   |   |   |   |-- foo.f
|   |           |   |   |   |   |   |-- foo_fixed.f90
|   |           |   |   |   |   |   `-- foo_free.f90
|   |           |   |   |   |   |-- modules
|   |           |   |   |   |   |   |-- gh25337
|   |           |   |   |   |   |   |   |-- data.f90
|   |           |   |   |   |   |   |   `-- use_data.f90
|   |           |   |   |   |   |   |-- gh26920
|   |           |   |   |   |   |   |   |-- two_mods_with_no_public_entities.f90
|   |           |   |   |   |   |   |   `-- two_mods_with_one_public_routine.f90
|   |           |   |   |   |   |   |-- module_data_docstring.f90
|   |           |   |   |   |   |   `-- use_modules.f90
|   |           |   |   |   |   |-- negative_bounds
|   |           |   |   |   |   |   `-- issue_20853.f90
|   |           |   |   |   |   |-- parameter
|   |           |   |   |   |   |   |-- constant_array.f90
|   |           |   |   |   |   |   |-- constant_both.f90
|   |           |   |   |   |   |   |-- constant_compound.f90
|   |           |   |   |   |   |   |-- constant_integer.f90
|   |           |   |   |   |   |   |-- constant_non_compound.f90
|   |           |   |   |   |   |   `-- constant_real.f90
|   |           |   |   |   |   |-- quoted_character
|   |           |   |   |   |   |   `-- foo.f
|   |           |   |   |   |   |-- regression
|   |           |   |   |   |   |   |-- AB.inc
|   |           |   |   |   |   |   |-- assignOnlyModule.f90
|   |           |   |   |   |   |   |-- datonly.f90
|   |           |   |   |   |   |   |-- f77comments.f
|   |           |   |   |   |   |   |-- f77fixedform.f95
|   |           |   |   |   |   |   |-- f90continuation.f90
|   |           |   |   |   |   |   |-- incfile.f90
|   |           |   |   |   |   |   |-- inout.f90
|   |           |   |   |   |   |   `-- lower_f2py_fortran.f90
|   |           |   |   |   |   |-- return_character
|   |           |   |   |   |   |   |-- foo77.f
|   |           |   |   |   |   |   `-- foo90.f90
|   |           |   |   |   |   |-- return_complex
|   |           |   |   |   |   |   |-- foo77.f
|   |           |   |   |   |   |   `-- foo90.f90
|   |           |   |   |   |   |-- return_integer
|   |           |   |   |   |   |   |-- foo77.f
|   |           |   |   |   |   |   `-- foo90.f90
|   |           |   |   |   |   |-- return_logical
|   |           |   |   |   |   |   |-- foo77.f
|   |           |   |   |   |   |   `-- foo90.f90
|   |           |   |   |   |   |-- return_real
|   |           |   |   |   |   |   |-- foo77.f
|   |           |   |   |   |   |   `-- foo90.f90
|   |           |   |   |   |   |-- routines
|   |           |   |   |   |   |   |-- funcfortranname.f
|   |           |   |   |   |   |   |-- funcfortranname.pyf
|   |           |   |   |   |   |   |-- subrout.f
|   |           |   |   |   |   |   `-- subrout.pyf
|   |           |   |   |   |   |-- size
|   |           |   |   |   |   |   `-- foo.f90
|   |           |   |   |   |   |-- string
|   |           |   |   |   |   |   |-- char.f90
|   |           |   |   |   |   |   |-- fixed_string.f90
|   |           |   |   |   |   |   |-- gh24008.f
|   |           |   |   |   |   |   |-- gh24662.f90
|   |           |   |   |   |   |   |-- gh25286.f90
|   |           |   |   |   |   |   |-- gh25286.pyf
|   |           |   |   |   |   |   |-- gh25286_bc.pyf
|   |           |   |   |   |   |   |-- scalar_string.f90
|   |           |   |   |   |   |   `-- string.f
|   |           |   |   |   |   `-- value_attrspec
|   |           |   |   |   |       `-- gh21665.f90
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_abstract_interface.py
|   |           |   |   |   |-- test_array_from_pyobj.py
|   |           |   |   |   |-- test_assumed_shape.py
|   |           |   |   |   |-- test_block_docstring.py
|   |           |   |   |   |-- test_callback.py
|   |           |   |   |   |-- test_character.py
|   |           |   |   |   |-- test_common.py
|   |           |   |   |   |-- test_crackfortran.py
|   |           |   |   |   |-- test_data.py
|   |           |   |   |   |-- test_docs.py
|   |           |   |   |   |-- test_f2cmap.py
|   |           |   |   |   |-- test_f2py2e.py
|   |           |   |   |   |-- test_isoc.py
|   |           |   |   |   |-- test_kind.py
|   |           |   |   |   |-- test_mixed.py
|   |           |   |   |   |-- test_modules.py
|   |           |   |   |   |-- test_parameter.py
|   |           |   |   |   |-- test_pyf_src.py
|   |           |   |   |   |-- test_quoted_character.py
|   |           |   |   |   |-- test_regression.py
|   |           |   |   |   |-- test_return_character.py
|   |           |   |   |   |-- test_return_complex.py
|   |           |   |   |   |-- test_return_integer.py
|   |           |   |   |   |-- test_return_logical.py
|   |           |   |   |   |-- test_return_real.py
|   |           |   |   |   |-- test_routines.py
|   |           |   |   |   |-- test_semicolon_split.py
|   |           |   |   |   |-- test_size.py
|   |           |   |   |   |-- test_string.py
|   |           |   |   |   |-- test_symbolic.py
|   |           |   |   |   |-- test_value_attrspec.py
|   |           |   |   |   `-- util.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __init__.pyi
|   |           |   |   |-- __main__.py
|   |           |   |   |-- __version__.py
|   |           |   |   |-- _isocbind.py
|   |           |   |   |-- _src_pyf.py
|   |           |   |   |-- auxfuncs.py
|   |           |   |   |-- capi_maps.py
|   |           |   |   |-- cb_rules.py
|   |           |   |   |-- cfuncs.py
|   |           |   |   |-- common_rules.py
|   |           |   |   |-- crackfortran.py
|   |           |   |   |-- diagnose.py
|   |           |   |   |-- f2py2e.py
|   |           |   |   |-- f90mod_rules.py
|   |           |   |   |-- func2subr.py
|   |           |   |   |-- rules.py
|   |           |   |   |-- setup.cfg
|   |           |   |   |-- symbolic.py
|   |           |   |   `-- use_rules.py
|   |           |   |-- fft
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _helper.cpython-312.pyc
|   |           |   |   |   |-- _pocketfft.cpython-312.pyc
|   |           |   |   |   `-- helper.cpython-312.pyc
|   |           |   |   |-- tests
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_helper.cpython-312.pyc
|   |           |   |   |   |   `-- test_pocketfft.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_helper.py
|   |           |   |   |   `-- test_pocketfft.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __init__.pyi
|   |           |   |   |-- _helper.py
|   |           |   |   |-- _helper.pyi
|   |           |   |   |-- _pocketfft.py
|   |           |   |   |-- _pocketfft.pyi
|   |           |   |   |-- _pocketfft_umath.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- helper.py
|   |           |   |   `-- helper.pyi
|   |           |   |-- lib
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _array_utils_impl.cpython-312.pyc
|   |           |   |   |   |-- _arraypad_impl.cpython-312.pyc
|   |           |   |   |   |-- _arraysetops_impl.cpython-312.pyc
|   |           |   |   |   |-- _arrayterator_impl.cpython-312.pyc
|   |           |   |   |   |-- _datasource.cpython-312.pyc
|   |           |   |   |   |-- _function_base_impl.cpython-312.pyc
|   |           |   |   |   |-- _histograms_impl.cpython-312.pyc
|   |           |   |   |   |-- _index_tricks_impl.cpython-312.pyc
|   |           |   |   |   |-- _iotools.cpython-312.pyc
|   |           |   |   |   |-- _nanfunctions_impl.cpython-312.pyc
|   |           |   |   |   |-- _npyio_impl.cpython-312.pyc
|   |           |   |   |   |-- _polynomial_impl.cpython-312.pyc
|   |           |   |   |   |-- _scimath_impl.cpython-312.pyc
|   |           |   |   |   |-- _shape_base_impl.cpython-312.pyc
|   |           |   |   |   |-- _stride_tricks_impl.cpython-312.pyc
|   |           |   |   |   |-- _twodim_base_impl.cpython-312.pyc
|   |           |   |   |   |-- _type_check_impl.cpython-312.pyc
|   |           |   |   |   |-- _ufunclike_impl.cpython-312.pyc
|   |           |   |   |   |-- _user_array_impl.cpython-312.pyc
|   |           |   |   |   |-- _utils_impl.cpython-312.pyc
|   |           |   |   |   |-- _version.cpython-312.pyc
|   |           |   |   |   |-- array_utils.cpython-312.pyc
|   |           |   |   |   |-- format.cpython-312.pyc
|   |           |   |   |   |-- introspect.cpython-312.pyc
|   |           |   |   |   |-- mixins.cpython-312.pyc
|   |           |   |   |   |-- npyio.cpython-312.pyc
|   |           |   |   |   |-- recfunctions.cpython-312.pyc
|   |           |   |   |   |-- scimath.cpython-312.pyc
|   |           |   |   |   |-- stride_tricks.cpython-312.pyc
|   |           |   |   |   `-- user_array.cpython-312.pyc
|   |           |   |   |-- tests
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test__datasource.cpython-312.pyc
|   |           |   |   |   |   |-- test__iotools.cpython-312.pyc
|   |           |   |   |   |   |-- test__version.cpython-312.pyc
|   |           |   |   |   |   |-- test_array_utils.cpython-312.pyc
|   |           |   |   |   |   |-- test_arraypad.cpython-312.pyc
|   |           |   |   |   |   |-- test_arraysetops.cpython-312.pyc
|   |           |   |   |   |   |-- test_arrayterator.cpython-312.pyc
|   |           |   |   |   |   |-- test_format.cpython-312.pyc
|   |           |   |   |   |   |-- test_function_base.cpython-312.pyc
|   |           |   |   |   |   |-- test_histograms.cpython-312.pyc
|   |           |   |   |   |   |-- test_index_tricks.cpython-312.pyc
|   |           |   |   |   |   |-- test_io.cpython-312.pyc
|   |           |   |   |   |   |-- test_loadtxt.cpython-312.pyc
|   |           |   |   |   |   |-- test_mixins.cpython-312.pyc
|   |           |   |   |   |   |-- test_nanfunctions.cpython-312.pyc
|   |           |   |   |   |   |-- test_packbits.cpython-312.pyc
|   |           |   |   |   |   |-- test_polynomial.cpython-312.pyc
|   |           |   |   |   |   |-- test_recfunctions.cpython-312.pyc
|   |           |   |   |   |   |-- test_regression.cpython-312.pyc
|   |           |   |   |   |   |-- test_shape_base.cpython-312.pyc
|   |           |   |   |   |   |-- test_stride_tricks.cpython-312.pyc
|   |           |   |   |   |   |-- test_twodim_base.cpython-312.pyc
|   |           |   |   |   |   |-- test_type_check.cpython-312.pyc
|   |           |   |   |   |   |-- test_ufunclike.cpython-312.pyc
|   |           |   |   |   |   `-- test_utils.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test__datasource.py
|   |           |   |   |   |-- test__iotools.py
|   |           |   |   |   |-- test__version.py
|   |           |   |   |   |-- test_array_utils.py
|   |           |   |   |   |-- test_arraypad.py
|   |           |   |   |   |-- test_arraysetops.py
|   |           |   |   |   |-- test_arrayterator.py
|   |           |   |   |   |-- test_format.py
|   |           |   |   |   |-- test_function_base.py
|   |           |   |   |   |-- test_histograms.py
|   |           |   |   |   |-- test_index_tricks.py
|   |           |   |   |   |-- test_io.py
|   |           |   |   |   |-- test_loadtxt.py
|   |           |   |   |   |-- test_mixins.py
|   |           |   |   |   |-- test_nanfunctions.py
|   |           |   |   |   |-- test_packbits.py
|   |           |   |   |   |-- test_polynomial.py
|   |           |   |   |   |-- test_recfunctions.py
|   |           |   |   |   |-- test_regression.py
|   |           |   |   |   |-- test_shape_base.py
|   |           |   |   |   |-- test_stride_tricks.py
|   |           |   |   |   |-- test_twodim_base.py
|   |           |   |   |   |-- test_type_check.py
|   |           |   |   |   |-- test_ufunclike.py
|   |           |   |   |   `-- test_utils.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __init__.pyi
|   |           |   |   |-- _array_utils_impl.py
|   |           |   |   |-- _array_utils_impl.pyi
|   |           |   |   |-- _arraypad_impl.py
|   |           |   |   |-- _arraypad_impl.pyi
|   |           |   |   |-- _arraysetops_impl.py
|   |           |   |   |-- _arraysetops_impl.pyi
|   |           |   |   |-- _arrayterator_impl.py
|   |           |   |   |-- _arrayterator_impl.pyi
|   |           |   |   |-- _datasource.py
|   |           |   |   |-- _datasource.pyi
|   |           |   |   |-- _function_base_impl.py
|   |           |   |   |-- _function_base_impl.pyi
|   |           |   |   |-- _histograms_impl.py
|   |           |   |   |-- _histograms_impl.pyi
|   |           |   |   |-- _index_tricks_impl.py
|   |           |   |   |-- _index_tricks_impl.pyi
|   |           |   |   |-- _iotools.py
|   |           |   |   |-- _iotools.pyi
|   |           |   |   |-- _nanfunctions_impl.py
|   |           |   |   |-- _nanfunctions_impl.pyi
|   |           |   |   |-- _npyio_impl.py
|   |           |   |   |-- _npyio_impl.pyi
|   |           |   |   |-- _polynomial_impl.py
|   |           |   |   |-- _polynomial_impl.pyi
|   |           |   |   |-- _scimath_impl.py
|   |           |   |   |-- _scimath_impl.pyi
|   |           |   |   |-- _shape_base_impl.py
|   |           |   |   |-- _shape_base_impl.pyi
|   |           |   |   |-- _stride_tricks_impl.py
|   |           |   |   |-- _stride_tricks_impl.pyi
|   |           |   |   |-- _twodim_base_impl.py
|   |           |   |   |-- _twodim_base_impl.pyi
|   |           |   |   |-- _type_check_impl.py
|   |           |   |   |-- _type_check_impl.pyi
|   |           |   |   |-- _ufunclike_impl.py
|   |           |   |   |-- _ufunclike_impl.pyi
|   |           |   |   |-- _user_array_impl.py
|   |           |   |   |-- _user_array_impl.pyi
|   |           |   |   |-- _utils_impl.py
|   |           |   |   |-- _utils_impl.pyi
|   |           |   |   |-- _version.py
|   |           |   |   |-- _version.pyi
|   |           |   |   |-- array_utils.py
|   |           |   |   |-- array_utils.pyi
|   |           |   |   |-- format.py
|   |           |   |   |-- format.pyi
|   |           |   |   |-- introspect.py
|   |           |   |   |-- introspect.pyi
|   |           |   |   |-- mixins.py
|   |           |   |   |-- mixins.pyi
|   |           |   |   |-- npyio.py
|   |           |   |   |-- npyio.pyi
|   |           |   |   |-- recfunctions.py
|   |           |   |   |-- recfunctions.pyi
|   |           |   |   |-- scimath.py
|   |           |   |   |-- scimath.pyi
|   |           |   |   |-- stride_tricks.py
|   |           |   |   |-- stride_tricks.pyi
|   |           |   |   |-- user_array.py
|   |           |   |   `-- user_array.pyi
|   |           |   |-- linalg
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _linalg.cpython-312.pyc
|   |           |   |   |   `-- linalg.cpython-312.pyc
|   |           |   |   |-- tests
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_deprecations.cpython-312.pyc
|   |           |   |   |   |   |-- test_linalg.cpython-312.pyc
|   |           |   |   |   |   `-- test_regression.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_deprecations.py
|   |           |   |   |   |-- test_linalg.py
|   |           |   |   |   `-- test_regression.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __init__.pyi
|   |           |   |   |-- _linalg.py
|   |           |   |   |-- _linalg.pyi
|   |           |   |   |-- _umath_linalg.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- _umath_linalg.pyi
|   |           |   |   |-- lapack_lite.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- lapack_lite.pyi
|   |           |   |   |-- linalg.py
|   |           |   |   `-- linalg.pyi
|   |           |   |-- ma
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- core.cpython-312.pyc
|   |           |   |   |   |-- extras.cpython-312.pyc
|   |           |   |   |   |-- mrecords.cpython-312.pyc
|   |           |   |   |   |-- testutils.cpython-312.pyc
|   |           |   |   |   `-- timer_comparison.cpython-312.pyc
|   |           |   |   |-- tests
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_arrayobject.cpython-312.pyc
|   |           |   |   |   |   |-- test_core.cpython-312.pyc
|   |           |   |   |   |   |-- test_deprecations.cpython-312.pyc
|   |           |   |   |   |   |-- test_extras.cpython-312.pyc
|   |           |   |   |   |   |-- test_mrecords.cpython-312.pyc
|   |           |   |   |   |   |-- test_old_ma.cpython-312.pyc
|   |           |   |   |   |   |-- test_regression.cpython-312.pyc
|   |           |   |   |   |   `-- test_subclassing.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_arrayobject.py
|   |           |   |   |   |-- test_core.py
|   |           |   |   |   |-- test_deprecations.py
|   |           |   |   |   |-- test_extras.py
|   |           |   |   |   |-- test_mrecords.py
|   |           |   |   |   |-- test_old_ma.py
|   |           |   |   |   |-- test_regression.py
|   |           |   |   |   `-- test_subclassing.py
|   |           |   |   |-- API_CHANGES.txt
|   |           |   |   |-- LICENSE
|   |           |   |   |-- README.rst
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __init__.pyi
|   |           |   |   |-- core.py
|   |           |   |   |-- core.pyi
|   |           |   |   |-- extras.py
|   |           |   |   |-- extras.pyi
|   |           |   |   |-- mrecords.py
|   |           |   |   |-- mrecords.pyi
|   |           |   |   |-- testutils.py
|   |           |   |   `-- timer_comparison.py
|   |           |   |-- matrixlib
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   `-- defmatrix.cpython-312.pyc
|   |           |   |   |-- tests
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_defmatrix.cpython-312.pyc
|   |           |   |   |   |   |-- test_interaction.cpython-312.pyc
|   |           |   |   |   |   |-- test_masked_matrix.cpython-312.pyc
|   |           |   |   |   |   |-- test_matrix_linalg.cpython-312.pyc
|   |           |   |   |   |   |-- test_multiarray.cpython-312.pyc
|   |           |   |   |   |   |-- test_numeric.cpython-312.pyc
|   |           |   |   |   |   `-- test_regression.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_defmatrix.py
|   |           |   |   |   |-- test_interaction.py
|   |           |   |   |   |-- test_masked_matrix.py
|   |           |   |   |   |-- test_matrix_linalg.py
|   |           |   |   |   |-- test_multiarray.py
|   |           |   |   |   |-- test_numeric.py
|   |           |   |   |   `-- test_regression.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __init__.pyi
|   |           |   |   |-- defmatrix.py
|   |           |   |   `-- defmatrix.pyi
|   |           |   |-- polynomial
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _polybase.cpython-312.pyc
|   |           |   |   |   |-- chebyshev.cpython-312.pyc
|   |           |   |   |   |-- hermite.cpython-312.pyc
|   |           |   |   |   |-- hermite_e.cpython-312.pyc
|   |           |   |   |   |-- laguerre.cpython-312.pyc
|   |           |   |   |   |-- legendre.cpython-312.pyc
|   |           |   |   |   |-- polynomial.cpython-312.pyc
|   |           |   |   |   `-- polyutils.cpython-312.pyc
|   |           |   |   |-- tests
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_chebyshev.cpython-312.pyc
|   |           |   |   |   |   |-- test_classes.cpython-312.pyc
|   |           |   |   |   |   |-- test_hermite.cpython-312.pyc
|   |           |   |   |   |   |-- test_hermite_e.cpython-312.pyc
|   |           |   |   |   |   |-- test_laguerre.cpython-312.pyc
|   |           |   |   |   |   |-- test_legendre.cpython-312.pyc
|   |           |   |   |   |   |-- test_polynomial.cpython-312.pyc
|   |           |   |   |   |   |-- test_polyutils.cpython-312.pyc
|   |           |   |   |   |   |-- test_printing.cpython-312.pyc
|   |           |   |   |   |   `-- test_symbol.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_chebyshev.py
|   |           |   |   |   |-- test_classes.py
|   |           |   |   |   |-- test_hermite.py
|   |           |   |   |   |-- test_hermite_e.py
|   |           |   |   |   |-- test_laguerre.py
|   |           |   |   |   |-- test_legendre.py
|   |           |   |   |   |-- test_polynomial.py
|   |           |   |   |   |-- test_polyutils.py
|   |           |   |   |   |-- test_printing.py
|   |           |   |   |   `-- test_symbol.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __init__.pyi
|   |           |   |   |-- _polybase.py
|   |           |   |   |-- _polybase.pyi
|   |           |   |   |-- _polytypes.pyi
|   |           |   |   |-- chebyshev.py
|   |           |   |   |-- chebyshev.pyi
|   |           |   |   |-- hermite.py
|   |           |   |   |-- hermite.pyi
|   |           |   |   |-- hermite_e.py
|   |           |   |   |-- hermite_e.pyi
|   |           |   |   |-- laguerre.py
|   |           |   |   |-- laguerre.pyi
|   |           |   |   |-- legendre.py
|   |           |   |   |-- legendre.pyi
|   |           |   |   |-- polynomial.py
|   |           |   |   |-- polynomial.pyi
|   |           |   |   |-- polyutils.py
|   |           |   |   `-- polyutils.pyi
|   |           |   |-- random
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   `-- _pickle.cpython-312.pyc
|   |           |   |   |-- _examples
|   |           |   |   |   |-- cffi
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- extending.cpython-312.pyc
|   |           |   |   |   |   |   `-- parse.cpython-312.pyc
|   |           |   |   |   |   |-- extending.py
|   |           |   |   |   |   `-- parse.py
|   |           |   |   |   |-- cython
|   |           |   |   |   |   |-- extending.pyx
|   |           |   |   |   |   |-- extending_distributions.pyx
|   |           |   |   |   |   `-- meson.build
|   |           |   |   |   `-- numba
|   |           |   |   |       |-- __pycache__
|   |           |   |   |       |   |-- extending.cpython-312.pyc
|   |           |   |   |       |   `-- extending_distributions.cpython-312.pyc
|   |           |   |   |       |-- extending.py
|   |           |   |   |       `-- extending_distributions.py
|   |           |   |   |-- lib
|   |           |   |   |   `-- libnpyrandom.a
|   |           |   |   |-- tests
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_direct.cpython-312.pyc
|   |           |   |   |   |   |-- test_extending.cpython-312.pyc
|   |           |   |   |   |   |-- test_generator_mt19937.cpython-312.pyc
|   |           |   |   |   |   |-- test_generator_mt19937_regressions.cpython-312.pyc
|   |           |   |   |   |   |-- test_random.cpython-312.pyc
|   |           |   |   |   |   |-- test_randomstate.cpython-312.pyc
|   |           |   |   |   |   |-- test_randomstate_regression.cpython-312.pyc
|   |           |   |   |   |   |-- test_regression.cpython-312.pyc
|   |           |   |   |   |   |-- test_seed_sequence.cpython-312.pyc
|   |           |   |   |   |   `-- test_smoke.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_direct.py
|   |           |   |   |   |-- test_extending.py
|   |           |   |   |   |-- test_generator_mt19937.py
|   |           |   |   |   |-- test_generator_mt19937_regressions.py
|   |           |   |   |   |-- test_random.py
|   |           |   |   |   |-- test_randomstate.py
|   |           |   |   |   |-- test_randomstate_regression.py
|   |           |   |   |   |-- test_regression.py
|   |           |   |   |   |-- test_seed_sequence.py
|   |           |   |   |   `-- test_smoke.py
|   |           |   |   |-- LICENSE.md
|   |           |   |   |-- __init__.pxd
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __init__.pyi
|   |           |   |   |-- _bounded_integers.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- _bounded_integers.pxd
|   |           |   |   |-- _common.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- _common.pxd
|   |           |   |   |-- _generator.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- _generator.pyi
|   |           |   |   |-- _mt19937.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- _mt19937.pyi
|   |           |   |   |-- _pcg64.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- _pcg64.pyi
|   |           |   |   |-- _philox.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- _philox.pyi
|   |           |   |   |-- _pickle.py
|   |           |   |   |-- _pickle.pyi
|   |           |   |   |-- _sfc64.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- _sfc64.pyi
|   |           |   |   |-- bit_generator.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- bit_generator.pxd
|   |           |   |   |-- bit_generator.pyi
|   |           |   |   |-- c_distributions.pxd
|   |           |   |   |-- mtrand.cpython-312-x86_64-linux-gnu.so
|   |           |   |   `-- mtrand.pyi
|   |           |   |-- rec
|   |           |   |   |-- __pycache__
|   |           |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   `-- __init__.pyi
|   |           |   |-- strings
|   |           |   |   |-- __pycache__
|   |           |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   `-- __init__.pyi
|   |           |   |-- testing
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- overrides.cpython-312.pyc
|   |           |   |   |   `-- print_coercion_tables.cpython-312.pyc
|   |           |   |   |-- _private
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- extbuild.cpython-312.pyc
|   |           |   |   |   |   `-- utils.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- __init__.pyi
|   |           |   |   |   |-- extbuild.py
|   |           |   |   |   |-- extbuild.pyi
|   |           |   |   |   |-- utils.py
|   |           |   |   |   `-- utils.pyi
|   |           |   |   |-- tests
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   `-- test_utils.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   `-- test_utils.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- __init__.pyi
|   |           |   |   |-- overrides.py
|   |           |   |   |-- overrides.pyi
|   |           |   |   |-- print_coercion_tables.py
|   |           |   |   `-- print_coercion_tables.pyi
|   |           |   |-- tests
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- test__all__.cpython-312.pyc
|   |           |   |   |   |-- test_configtool.cpython-312.pyc
|   |           |   |   |   |-- test_ctypeslib.cpython-312.pyc
|   |           |   |   |   |-- test_lazyloading.cpython-312.pyc
|   |           |   |   |   |-- test_matlib.cpython-312.pyc
|   |           |   |   |   |-- test_numpy_config.cpython-312.pyc
|   |           |   |   |   |-- test_numpy_version.cpython-312.pyc
|   |           |   |   |   |-- test_public_api.cpython-312.pyc
|   |           |   |   |   |-- test_reloading.cpython-312.pyc
|   |           |   |   |   |-- test_scripts.cpython-312.pyc
|   |           |   |   |   `-- test_warnings.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- test__all__.py
|   |           |   |   |-- test_configtool.py
|   |           |   |   |-- test_ctypeslib.py
|   |           |   |   |-- test_lazyloading.py
|   |           |   |   |-- test_matlib.py
|   |           |   |   |-- test_numpy_config.py
|   |           |   |   |-- test_numpy_version.py
|   |           |   |   |-- test_public_api.py
|   |           |   |   |-- test_reloading.py
|   |           |   |   |-- test_scripts.py
|   |           |   |   `-- test_warnings.py
|   |           |   |-- typing
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   `-- mypy_plugin.cpython-312.pyc
|   |           |   |   |-- tests
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_isfile.cpython-312.pyc
|   |           |   |   |   |   |-- test_runtime.cpython-312.pyc
|   |           |   |   |   |   `-- test_typing.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_isfile.py
|   |           |   |   |   |-- test_runtime.py
|   |           |   |   |   `-- test_typing.py
|   |           |   |   |-- __init__.py
|   |           |   |   `-- mypy_plugin.py
|   |           |   |-- __config__.py
|   |           |   |-- __config__.pyi
|   |           |   |-- __init__.cython-30.pxd
|   |           |   |-- __init__.pxd
|   |           |   |-- __init__.py
|   |           |   |-- __init__.pyi
|   |           |   |-- _array_api_info.py
|   |           |   |-- _array_api_info.pyi
|   |           |   |-- _configtool.py
|   |           |   |-- _configtool.pyi
|   |           |   |-- _distributor_init.py
|   |           |   |-- _distributor_init.pyi
|   |           |   |-- _expired_attrs_2_0.py
|   |           |   |-- _expired_attrs_2_0.pyi
|   |           |   |-- _globals.py
|   |           |   |-- _globals.pyi
|   |           |   |-- _pytesttester.py
|   |           |   |-- _pytesttester.pyi
|   |           |   |-- conftest.py
|   |           |   |-- ctypeslib.py
|   |           |   |-- ctypeslib.pyi
|   |           |   |-- dtypes.py
|   |           |   |-- dtypes.pyi
|   |           |   |-- exceptions.py
|   |           |   |-- exceptions.pyi
|   |           |   |-- matlib.py
|   |           |   |-- matlib.pyi
|   |           |   |-- py.typed
|   |           |   |-- version.py
|   |           |   `-- version.pyi
|   |           |-- numpy-2.2.6.dist-info
|   |           |   |-- INSTALLER
|   |           |   |-- LICENSE.txt
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   |-- WHEEL
|   |           |   `-- entry_points.txt
|   |           |-- numpy.libs
|   |           |   |-- libgfortran-040039e1-0352e75f.so.5.0.0
|   |           |   |-- libquadmath-96973f99-934c22de.so.0.0.0
|   |           |   `-- libscipy_openblas64_-56d6093b.so
|   |           |-- opencv_python-4.12.0.88.dist-info
|   |           |   |-- INSTALLER
|   |           |   |-- LICENSE-3RD-PARTY.txt
|   |           |   |-- LICENSE.txt
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   |-- REQUESTED
|   |           |   |-- WHEEL
|   |           |   `-- top_level.txt
|   |           |-- opencv_python.libs
|   |           |   |-- libQt5Core-e7f476e2.so.5.15.16
|   |           |   |-- libQt5Gui-3e966859.so.5.15.16
|   |           |   |-- libQt5Test-9ac3ed15.so.5.15.16
|   |           |   |-- libQt5Widgets-cd430389.so.5.15.16
|   |           |   |-- libQt5XcbQpa-3cfa6167.so.5.15.16
|   |           |   |-- libX11-xcb-0e257303.so.1.0.0
|   |           |   |-- libXau-00ec42fe.so.6.0.0
|   |           |   |-- libaom-49d00b71.so.3.12.1
|   |           |   |-- libavcodec-e0dd92b8.so.59.37.100
|   |           |   |-- libavformat-d296e685.so.59.27.100
|   |           |   |-- libavif-850e7649.so.16.3.0
|   |           |   |-- libavutil-734d06dd.so.57.28.100
|   |           |   |-- libcrypto-01067bc0.so.1.1
|   |           |   |-- libgfortran-91cc3cb1.so.3.0.0
|   |           |   |-- libopenblas-r0-f650aae0.3.3.so
|   |           |   |-- libpng16-04239421.so.16.48.0
|   |           |   |-- libquadmath-96973f99.so.0.0.0
|   |           |   |-- libssl-28bef1ac.so.1.1
|   |           |   |-- libswresample-3e7db482.so.4.7.100
|   |           |   |-- libswscale-95ddd674.so.6.7.100
|   |           |   |-- libvpx-127417df.so.11.0.0
|   |           |   |-- libxcb-icccm-413c9f41.so.4.0.0
|   |           |   |-- libxcb-image-e82a276d.so.0.0.0
|   |           |   |-- libxcb-keysyms-21015570.so.1.0.0
|   |           |   |-- libxcb-randr-a96a5a87.so.0.1.0
|   |           |   |-- libxcb-render-637b984a.so.0.0.0
|   |           |   |-- libxcb-render-util-43ce00f5.so.0.0.0
|   |           |   |-- libxcb-shape-25c2b258.so.0.0.0
|   |           |   |-- libxcb-shm-7a199f70.so.0.0.0
|   |           |   |-- libxcb-sync-89374f40.so.1.0.0
|   |           |   |-- libxcb-util-4d666913.so.1.0.0
|   |           |   |-- libxcb-xfixes-9be3ba6f.so.0.0.0
|   |           |   |-- libxcb-xinerama-ae147f87.so.0.0.0
|   |           |   |-- libxcb-xkb-9ba31ab3.so.1.0.0
|   |           |   |-- libxkbcommon-71ae2972.so.0.0.0
|   |           |   `-- libxkbcommon-x11-c65ed502.so.0.0.0
|   |           |-- packaging
|   |           |   |-- __pycache__
|   |           |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |-- _elffile.cpython-312.pyc
|   |           |   |   |-- _manylinux.cpython-312.pyc
|   |           |   |   |-- _musllinux.cpython-312.pyc
|   |           |   |   |-- _parser.cpython-312.pyc
|   |           |   |   |-- _structures.cpython-312.pyc
|   |           |   |   |-- _tokenizer.cpython-312.pyc
|   |           |   |   |-- markers.cpython-312.pyc
|   |           |   |   |-- metadata.cpython-312.pyc
|   |           |   |   |-- requirements.cpython-312.pyc
|   |           |   |   |-- specifiers.cpython-312.pyc
|   |           |   |   |-- tags.cpython-312.pyc
|   |           |   |   |-- utils.cpython-312.pyc
|   |           |   |   `-- version.cpython-312.pyc
|   |           |   |-- licenses
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   `-- _spdx.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   `-- _spdx.py
|   |           |   |-- __init__.py
|   |           |   |-- _elffile.py
|   |           |   |-- _manylinux.py
|   |           |   |-- _musllinux.py
|   |           |   |-- _parser.py
|   |           |   |-- _structures.py
|   |           |   |-- _tokenizer.py
|   |           |   |-- markers.py
|   |           |   |-- metadata.py
|   |           |   |-- py.typed
|   |           |   |-- requirements.py
|   |           |   |-- specifiers.py
|   |           |   |-- tags.py
|   |           |   |-- utils.py
|   |           |   `-- version.py
|   |           |-- packaging-25.0.dist-info
|   |           |   |-- licenses
|   |           |   |   |-- LICENSE
|   |           |   |   |-- LICENSE.APACHE
|   |           |   |   `-- LICENSE.BSD
|   |           |   |-- INSTALLER
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   `-- WHEEL
|   |           |-- pandas
|   |           |   |-- __pycache__
|   |           |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |-- _typing.cpython-312.pyc
|   |           |   |   |-- _version.cpython-312.pyc
|   |           |   |   |-- _version_meson.cpython-312.pyc
|   |           |   |   |-- conftest.cpython-312.pyc
|   |           |   |   `-- testing.cpython-312.pyc
|   |           |   |-- _config
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- config.cpython-312.pyc
|   |           |   |   |   |-- dates.cpython-312.pyc
|   |           |   |   |   |-- display.cpython-312.pyc
|   |           |   |   |   `-- localization.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- config.py
|   |           |   |   |-- dates.py
|   |           |   |   |-- display.py
|   |           |   |   `-- localization.py
|   |           |   |-- _libs
|   |           |   |   |-- __pycache__
|   |           |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |-- tslibs
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- base.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |   |-- ccalendar.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |   |-- ccalendar.pyi
|   |           |   |   |   |-- conversion.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |   |-- conversion.pyi
|   |           |   |   |   |-- dtypes.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |   |-- dtypes.pyi
|   |           |   |   |   |-- fields.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |   |-- fields.pyi
|   |           |   |   |   |-- nattype.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |   |-- nattype.pyi
|   |           |   |   |   |-- np_datetime.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |   |-- np_datetime.pyi
|   |           |   |   |   |-- offsets.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |   |-- offsets.pyi
|   |           |   |   |   |-- parsing.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |   |-- parsing.pyi
|   |           |   |   |   |-- period.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |   |-- period.pyi
|   |           |   |   |   |-- strptime.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |   |-- strptime.pyi
|   |           |   |   |   |-- timedeltas.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |   |-- timedeltas.pyi
|   |           |   |   |   |-- timestamps.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |   |-- timestamps.pyi
|   |           |   |   |   |-- timezones.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |   |-- timezones.pyi
|   |           |   |   |   |-- tzconversion.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |   |-- tzconversion.pyi
|   |           |   |   |   |-- vectorized.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |   `-- vectorized.pyi
|   |           |   |   |-- window
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- aggregations.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |   |-- aggregations.pyi
|   |           |   |   |   |-- indexers.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |   `-- indexers.pyi
|   |           |   |   |-- __init__.py
|   |           |   |   |-- algos.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- algos.pyi
|   |           |   |   |-- arrays.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- arrays.pyi
|   |           |   |   |-- byteswap.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- byteswap.pyi
|   |           |   |   |-- groupby.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- groupby.pyi
|   |           |   |   |-- hashing.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- hashing.pyi
|   |           |   |   |-- hashtable.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- hashtable.pyi
|   |           |   |   |-- index.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- index.pyi
|   |           |   |   |-- indexing.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- indexing.pyi
|   |           |   |   |-- internals.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- internals.pyi
|   |           |   |   |-- interval.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- interval.pyi
|   |           |   |   |-- join.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- join.pyi
|   |           |   |   |-- json.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- json.pyi
|   |           |   |   |-- lib.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- lib.pyi
|   |           |   |   |-- missing.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- missing.pyi
|   |           |   |   |-- ops.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- ops.pyi
|   |           |   |   |-- ops_dispatch.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- ops_dispatch.pyi
|   |           |   |   |-- pandas_datetime.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- pandas_parser.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- parsers.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- parsers.pyi
|   |           |   |   |-- properties.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- properties.pyi
|   |           |   |   |-- reshape.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- reshape.pyi
|   |           |   |   |-- sas.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- sas.pyi
|   |           |   |   |-- sparse.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- sparse.pyi
|   |           |   |   |-- testing.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- testing.pyi
|   |           |   |   |-- tslib.cpython-312-x86_64-linux-gnu.so
|   |           |   |   |-- tslib.pyi
|   |           |   |   |-- writers.cpython-312-x86_64-linux-gnu.so
|   |           |   |   `-- writers.pyi
|   |           |   |-- _testing
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _hypothesis.cpython-312.pyc
|   |           |   |   |   |-- _io.cpython-312.pyc
|   |           |   |   |   |-- _warnings.cpython-312.pyc
|   |           |   |   |   |-- asserters.cpython-312.pyc
|   |           |   |   |   |-- compat.cpython-312.pyc
|   |           |   |   |   `-- contexts.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- _hypothesis.py
|   |           |   |   |-- _io.py
|   |           |   |   |-- _warnings.py
|   |           |   |   |-- asserters.py
|   |           |   |   |-- compat.py
|   |           |   |   `-- contexts.py
|   |           |   |-- api
|   |           |   |   |-- __pycache__
|   |           |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |-- extensions
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- indexers
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- interchange
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- types
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- typing
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   `-- __init__.py
|   |           |   |   `-- __init__.py
|   |           |   |-- arrays
|   |           |   |   |-- __pycache__
|   |           |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   `-- __init__.py
|   |           |   |-- compat
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _constants.cpython-312.pyc
|   |           |   |   |   |-- _optional.cpython-312.pyc
|   |           |   |   |   |-- compressors.cpython-312.pyc
|   |           |   |   |   |-- pickle_compat.cpython-312.pyc
|   |           |   |   |   `-- pyarrow.cpython-312.pyc
|   |           |   |   |-- numpy
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   `-- function.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   `-- function.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- _constants.py
|   |           |   |   |-- _optional.py
|   |           |   |   |-- compressors.py
|   |           |   |   |-- pickle_compat.py
|   |           |   |   `-- pyarrow.py
|   |           |   |-- core
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- accessor.cpython-312.pyc
|   |           |   |   |   |-- algorithms.cpython-312.pyc
|   |           |   |   |   |-- api.cpython-312.pyc
|   |           |   |   |   |-- apply.cpython-312.pyc
|   |           |   |   |   |-- arraylike.cpython-312.pyc
|   |           |   |   |   |-- base.cpython-312.pyc
|   |           |   |   |   |-- common.cpython-312.pyc
|   |           |   |   |   |-- config_init.cpython-312.pyc
|   |           |   |   |   |-- construction.cpython-312.pyc
|   |           |   |   |   |-- flags.cpython-312.pyc
|   |           |   |   |   |-- frame.cpython-312.pyc
|   |           |   |   |   |-- generic.cpython-312.pyc
|   |           |   |   |   |-- indexing.cpython-312.pyc
|   |           |   |   |   |-- missing.cpython-312.pyc
|   |           |   |   |   |-- nanops.cpython-312.pyc
|   |           |   |   |   |-- resample.cpython-312.pyc
|   |           |   |   |   |-- roperator.cpython-312.pyc
|   |           |   |   |   |-- sample.cpython-312.pyc
|   |           |   |   |   |-- series.cpython-312.pyc
|   |           |   |   |   |-- shared_docs.cpython-312.pyc
|   |           |   |   |   `-- sorting.cpython-312.pyc
|   |           |   |   |-- _numba
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- executor.cpython-312.pyc
|   |           |   |   |   |   `-- extensions.cpython-312.pyc
|   |           |   |   |   |-- kernels
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- mean_.cpython-312.pyc
|   |           |   |   |   |   |   |-- min_max_.cpython-312.pyc
|   |           |   |   |   |   |   |-- shared.cpython-312.pyc
|   |           |   |   |   |   |   |-- sum_.cpython-312.pyc
|   |           |   |   |   |   |   `-- var_.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- mean_.py
|   |           |   |   |   |   |-- min_max_.py
|   |           |   |   |   |   |-- shared.py
|   |           |   |   |   |   |-- sum_.py
|   |           |   |   |   |   `-- var_.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- executor.py
|   |           |   |   |   `-- extensions.py
|   |           |   |   |-- array_algos
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- datetimelike_accumulations.cpython-312.pyc
|   |           |   |   |   |   |-- masked_accumulations.cpython-312.pyc
|   |           |   |   |   |   |-- masked_reductions.cpython-312.pyc
|   |           |   |   |   |   |-- putmask.cpython-312.pyc
|   |           |   |   |   |   |-- quantile.cpython-312.pyc
|   |           |   |   |   |   |-- replace.cpython-312.pyc
|   |           |   |   |   |   |-- take.cpython-312.pyc
|   |           |   |   |   |   `-- transforms.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- datetimelike_accumulations.py
|   |           |   |   |   |-- masked_accumulations.py
|   |           |   |   |   |-- masked_reductions.py
|   |           |   |   |   |-- putmask.py
|   |           |   |   |   |-- quantile.py
|   |           |   |   |   |-- replace.py
|   |           |   |   |   |-- take.py
|   |           |   |   |   `-- transforms.py
|   |           |   |   |-- arrays
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- _arrow_string_mixins.cpython-312.pyc
|   |           |   |   |   |   |-- _mixins.cpython-312.pyc
|   |           |   |   |   |   |-- _ranges.cpython-312.pyc
|   |           |   |   |   |   |-- _utils.cpython-312.pyc
|   |           |   |   |   |   |-- base.cpython-312.pyc
|   |           |   |   |   |   |-- boolean.cpython-312.pyc
|   |           |   |   |   |   |-- categorical.cpython-312.pyc
|   |           |   |   |   |   |-- datetimelike.cpython-312.pyc
|   |           |   |   |   |   |-- datetimes.cpython-312.pyc
|   |           |   |   |   |   |-- floating.cpython-312.pyc
|   |           |   |   |   |   |-- integer.cpython-312.pyc
|   |           |   |   |   |   |-- interval.cpython-312.pyc
|   |           |   |   |   |   |-- masked.cpython-312.pyc
|   |           |   |   |   |   |-- numeric.cpython-312.pyc
|   |           |   |   |   |   |-- numpy_.cpython-312.pyc
|   |           |   |   |   |   |-- period.cpython-312.pyc
|   |           |   |   |   |   |-- string_.cpython-312.pyc
|   |           |   |   |   |   |-- string_arrow.cpython-312.pyc
|   |           |   |   |   |   `-- timedeltas.cpython-312.pyc
|   |           |   |   |   |-- arrow
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- _arrow_utils.cpython-312.pyc
|   |           |   |   |   |   |   |-- accessors.cpython-312.pyc
|   |           |   |   |   |   |   |-- array.cpython-312.pyc
|   |           |   |   |   |   |   `-- extension_types.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- _arrow_utils.py
|   |           |   |   |   |   |-- accessors.py
|   |           |   |   |   |   |-- array.py
|   |           |   |   |   |   `-- extension_types.py
|   |           |   |   |   |-- sparse
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- accessor.cpython-312.pyc
|   |           |   |   |   |   |   |-- array.cpython-312.pyc
|   |           |   |   |   |   |   `-- scipy_sparse.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- accessor.py
|   |           |   |   |   |   |-- array.py
|   |           |   |   |   |   `-- scipy_sparse.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- _arrow_string_mixins.py
|   |           |   |   |   |-- _mixins.py
|   |           |   |   |   |-- _ranges.py
|   |           |   |   |   |-- _utils.py
|   |           |   |   |   |-- base.py
|   |           |   |   |   |-- boolean.py
|   |           |   |   |   |-- categorical.py
|   |           |   |   |   |-- datetimelike.py
|   |           |   |   |   |-- datetimes.py
|   |           |   |   |   |-- floating.py
|   |           |   |   |   |-- integer.py
|   |           |   |   |   |-- interval.py
|   |           |   |   |   |-- masked.py
|   |           |   |   |   |-- numeric.py
|   |           |   |   |   |-- numpy_.py
|   |           |   |   |   |-- period.py
|   |           |   |   |   |-- string_.py
|   |           |   |   |   |-- string_arrow.py
|   |           |   |   |   `-- timedeltas.py
|   |           |   |   |-- computation
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- align.cpython-312.pyc
|   |           |   |   |   |   |-- api.cpython-312.pyc
|   |           |   |   |   |   |-- check.cpython-312.pyc
|   |           |   |   |   |   |-- common.cpython-312.pyc
|   |           |   |   |   |   |-- engines.cpython-312.pyc
|   |           |   |   |   |   |-- eval.cpython-312.pyc
|   |           |   |   |   |   |-- expr.cpython-312.pyc
|   |           |   |   |   |   |-- expressions.cpython-312.pyc
|   |           |   |   |   |   |-- ops.cpython-312.pyc
|   |           |   |   |   |   |-- parsing.cpython-312.pyc
|   |           |   |   |   |   |-- pytables.cpython-312.pyc
|   |           |   |   |   |   `-- scope.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- align.py
|   |           |   |   |   |-- api.py
|   |           |   |   |   |-- check.py
|   |           |   |   |   |-- common.py
|   |           |   |   |   |-- engines.py
|   |           |   |   |   |-- eval.py
|   |           |   |   |   |-- expr.py
|   |           |   |   |   |-- expressions.py
|   |           |   |   |   |-- ops.py
|   |           |   |   |   |-- parsing.py
|   |           |   |   |   |-- pytables.py
|   |           |   |   |   `-- scope.py
|   |           |   |   |-- dtypes
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- api.cpython-312.pyc
|   |           |   |   |   |   |-- astype.cpython-312.pyc
|   |           |   |   |   |   |-- base.cpython-312.pyc
|   |           |   |   |   |   |-- cast.cpython-312.pyc
|   |           |   |   |   |   |-- common.cpython-312.pyc
|   |           |   |   |   |   |-- concat.cpython-312.pyc
|   |           |   |   |   |   |-- dtypes.cpython-312.pyc
|   |           |   |   |   |   |-- generic.cpython-312.pyc
|   |           |   |   |   |   |-- inference.cpython-312.pyc
|   |           |   |   |   |   `-- missing.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- api.py
|   |           |   |   |   |-- astype.py
|   |           |   |   |   |-- base.py
|   |           |   |   |   |-- cast.py
|   |           |   |   |   |-- common.py
|   |           |   |   |   |-- concat.py
|   |           |   |   |   |-- dtypes.py
|   |           |   |   |   |-- generic.py
|   |           |   |   |   |-- inference.py
|   |           |   |   |   `-- missing.py
|   |           |   |   |-- groupby
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- base.cpython-312.pyc
|   |           |   |   |   |   |-- categorical.cpython-312.pyc
|   |           |   |   |   |   |-- generic.cpython-312.pyc
|   |           |   |   |   |   |-- groupby.cpython-312.pyc
|   |           |   |   |   |   |-- grouper.cpython-312.pyc
|   |           |   |   |   |   |-- indexing.cpython-312.pyc
|   |           |   |   |   |   |-- numba_.cpython-312.pyc
|   |           |   |   |   |   `-- ops.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- base.py
|   |           |   |   |   |-- categorical.py
|   |           |   |   |   |-- generic.py
|   |           |   |   |   |-- groupby.py
|   |           |   |   |   |-- grouper.py
|   |           |   |   |   |-- indexing.py
|   |           |   |   |   |-- numba_.py
|   |           |   |   |   `-- ops.py
|   |           |   |   |-- indexers
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- objects.cpython-312.pyc
|   |           |   |   |   |   `-- utils.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- objects.py
|   |           |   |   |   `-- utils.py
|   |           |   |   |-- indexes
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- accessors.cpython-312.pyc
|   |           |   |   |   |   |-- api.cpython-312.pyc
|   |           |   |   |   |   |-- base.cpython-312.pyc
|   |           |   |   |   |   |-- category.cpython-312.pyc
|   |           |   |   |   |   |-- datetimelike.cpython-312.pyc
|   |           |   |   |   |   |-- datetimes.cpython-312.pyc
|   |           |   |   |   |   |-- extension.cpython-312.pyc
|   |           |   |   |   |   |-- frozen.cpython-312.pyc
|   |           |   |   |   |   |-- interval.cpython-312.pyc
|   |           |   |   |   |   |-- multi.cpython-312.pyc
|   |           |   |   |   |   |-- period.cpython-312.pyc
|   |           |   |   |   |   |-- range.cpython-312.pyc
|   |           |   |   |   |   `-- timedeltas.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- accessors.py
|   |           |   |   |   |-- api.py
|   |           |   |   |   |-- base.py
|   |           |   |   |   |-- category.py
|   |           |   |   |   |-- datetimelike.py
|   |           |   |   |   |-- datetimes.py
|   |           |   |   |   |-- extension.py
|   |           |   |   |   |-- frozen.py
|   |           |   |   |   |-- interval.py
|   |           |   |   |   |-- multi.py
|   |           |   |   |   |-- period.py
|   |           |   |   |   |-- range.py
|   |           |   |   |   `-- timedeltas.py
|   |           |   |   |-- interchange
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- buffer.cpython-312.pyc
|   |           |   |   |   |   |-- column.cpython-312.pyc
|   |           |   |   |   |   |-- dataframe.cpython-312.pyc
|   |           |   |   |   |   |-- dataframe_protocol.cpython-312.pyc
|   |           |   |   |   |   |-- from_dataframe.cpython-312.pyc
|   |           |   |   |   |   `-- utils.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- buffer.py
|   |           |   |   |   |-- column.py
|   |           |   |   |   |-- dataframe.py
|   |           |   |   |   |-- dataframe_protocol.py
|   |           |   |   |   |-- from_dataframe.py
|   |           |   |   |   `-- utils.py
|   |           |   |   |-- internals
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- api.cpython-312.pyc
|   |           |   |   |   |   |-- array_manager.cpython-312.pyc
|   |           |   |   |   |   |-- base.cpython-312.pyc
|   |           |   |   |   |   |-- blocks.cpython-312.pyc
|   |           |   |   |   |   |-- concat.cpython-312.pyc
|   |           |   |   |   |   |-- construction.cpython-312.pyc
|   |           |   |   |   |   |-- managers.cpython-312.pyc
|   |           |   |   |   |   `-- ops.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- api.py
|   |           |   |   |   |-- array_manager.py
|   |           |   |   |   |-- base.py
|   |           |   |   |   |-- blocks.py
|   |           |   |   |   |-- concat.py
|   |           |   |   |   |-- construction.py
|   |           |   |   |   |-- managers.py
|   |           |   |   |   `-- ops.py
|   |           |   |   |-- methods
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- describe.cpython-312.pyc
|   |           |   |   |   |   |-- selectn.cpython-312.pyc
|   |           |   |   |   |   `-- to_dict.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- describe.py
|   |           |   |   |   |-- selectn.py
|   |           |   |   |   `-- to_dict.py
|   |           |   |   |-- ops
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- array_ops.cpython-312.pyc
|   |           |   |   |   |   |-- common.cpython-312.pyc
|   |           |   |   |   |   |-- dispatch.cpython-312.pyc
|   |           |   |   |   |   |-- docstrings.cpython-312.pyc
|   |           |   |   |   |   |-- invalid.cpython-312.pyc
|   |           |   |   |   |   |-- mask_ops.cpython-312.pyc
|   |           |   |   |   |   `-- missing.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- array_ops.py
|   |           |   |   |   |-- common.py
|   |           |   |   |   |-- dispatch.py
|   |           |   |   |   |-- docstrings.py
|   |           |   |   |   |-- invalid.py
|   |           |   |   |   |-- mask_ops.py
|   |           |   |   |   `-- missing.py
|   |           |   |   |-- reshape
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- api.cpython-312.pyc
|   |           |   |   |   |   |-- concat.cpython-312.pyc
|   |           |   |   |   |   |-- encoding.cpython-312.pyc
|   |           |   |   |   |   |-- melt.cpython-312.pyc
|   |           |   |   |   |   |-- merge.cpython-312.pyc
|   |           |   |   |   |   |-- pivot.cpython-312.pyc
|   |           |   |   |   |   |-- reshape.cpython-312.pyc
|   |           |   |   |   |   |-- tile.cpython-312.pyc
|   |           |   |   |   |   `-- util.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- api.py
|   |           |   |   |   |-- concat.py
|   |           |   |   |   |-- encoding.py
|   |           |   |   |   |-- melt.py
|   |           |   |   |   |-- merge.py
|   |           |   |   |   |-- pivot.py
|   |           |   |   |   |-- reshape.py
|   |           |   |   |   |-- tile.py
|   |           |   |   |   `-- util.py
|   |           |   |   |-- sparse
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   `-- api.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   `-- api.py
|   |           |   |   |-- strings
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- accessor.cpython-312.pyc
|   |           |   |   |   |   |-- base.cpython-312.pyc
|   |           |   |   |   |   `-- object_array.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- accessor.py
|   |           |   |   |   |-- base.py
|   |           |   |   |   `-- object_array.py
|   |           |   |   |-- tools
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- datetimes.cpython-312.pyc
|   |           |   |   |   |   |-- numeric.cpython-312.pyc
|   |           |   |   |   |   |-- timedeltas.cpython-312.pyc
|   |           |   |   |   |   `-- times.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- datetimes.py
|   |           |   |   |   |-- numeric.py
|   |           |   |   |   |-- timedeltas.py
|   |           |   |   |   `-- times.py
|   |           |   |   |-- util
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- hashing.cpython-312.pyc
|   |           |   |   |   |   `-- numba_.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- hashing.py
|   |           |   |   |   `-- numba_.py
|   |           |   |   |-- window
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- common.cpython-312.pyc
|   |           |   |   |   |   |-- doc.cpython-312.pyc
|   |           |   |   |   |   |-- ewm.cpython-312.pyc
|   |           |   |   |   |   |-- expanding.cpython-312.pyc
|   |           |   |   |   |   |-- numba_.cpython-312.pyc
|   |           |   |   |   |   |-- online.cpython-312.pyc
|   |           |   |   |   |   `-- rolling.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- common.py
|   |           |   |   |   |-- doc.py
|   |           |   |   |   |-- ewm.py
|   |           |   |   |   |-- expanding.py
|   |           |   |   |   |-- numba_.py
|   |           |   |   |   |-- online.py
|   |           |   |   |   `-- rolling.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- accessor.py
|   |           |   |   |-- algorithms.py
|   |           |   |   |-- api.py
|   |           |   |   |-- apply.py
|   |           |   |   |-- arraylike.py
|   |           |   |   |-- base.py
|   |           |   |   |-- common.py
|   |           |   |   |-- config_init.py
|   |           |   |   |-- construction.py
|   |           |   |   |-- flags.py
|   |           |   |   |-- frame.py
|   |           |   |   |-- generic.py
|   |           |   |   |-- indexing.py
|   |           |   |   |-- missing.py
|   |           |   |   |-- nanops.py
|   |           |   |   |-- resample.py
|   |           |   |   |-- roperator.py
|   |           |   |   |-- sample.py
|   |           |   |   |-- series.py
|   |           |   |   |-- shared_docs.py
|   |           |   |   `-- sorting.py
|   |           |   |-- errors
|   |           |   |   |-- __pycache__
|   |           |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   `-- __init__.py
|   |           |   |-- io
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _util.cpython-312.pyc
|   |           |   |   |   |-- api.cpython-312.pyc
|   |           |   |   |   |-- clipboards.cpython-312.pyc
|   |           |   |   |   |-- common.cpython-312.pyc
|   |           |   |   |   |-- feather_format.cpython-312.pyc
|   |           |   |   |   |-- gbq.cpython-312.pyc
|   |           |   |   |   |-- html.cpython-312.pyc
|   |           |   |   |   |-- orc.cpython-312.pyc
|   |           |   |   |   |-- parquet.cpython-312.pyc
|   |           |   |   |   |-- pickle.cpython-312.pyc
|   |           |   |   |   |-- pytables.cpython-312.pyc
|   |           |   |   |   |-- spss.cpython-312.pyc
|   |           |   |   |   |-- sql.cpython-312.pyc
|   |           |   |   |   |-- stata.cpython-312.pyc
|   |           |   |   |   `-- xml.cpython-312.pyc
|   |           |   |   |-- clipboard
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- excel
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- _base.cpython-312.pyc
|   |           |   |   |   |   |-- _calamine.cpython-312.pyc
|   |           |   |   |   |   |-- _odfreader.cpython-312.pyc
|   |           |   |   |   |   |-- _odswriter.cpython-312.pyc
|   |           |   |   |   |   |-- _openpyxl.cpython-312.pyc
|   |           |   |   |   |   |-- _pyxlsb.cpython-312.pyc
|   |           |   |   |   |   |-- _util.cpython-312.pyc
|   |           |   |   |   |   |-- _xlrd.cpython-312.pyc
|   |           |   |   |   |   `-- _xlsxwriter.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- _base.py
|   |           |   |   |   |-- _calamine.py
|   |           |   |   |   |-- _odfreader.py
|   |           |   |   |   |-- _odswriter.py
|   |           |   |   |   |-- _openpyxl.py
|   |           |   |   |   |-- _pyxlsb.py
|   |           |   |   |   |-- _util.py
|   |           |   |   |   |-- _xlrd.py
|   |           |   |   |   `-- _xlsxwriter.py
|   |           |   |   |-- formats
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- _color_data.cpython-312.pyc
|   |           |   |   |   |   |-- console.cpython-312.pyc
|   |           |   |   |   |   |-- css.cpython-312.pyc
|   |           |   |   |   |   |-- csvs.cpython-312.pyc
|   |           |   |   |   |   |-- excel.cpython-312.pyc
|   |           |   |   |   |   |-- format.cpython-312.pyc
|   |           |   |   |   |   |-- html.cpython-312.pyc
|   |           |   |   |   |   |-- info.cpython-312.pyc
|   |           |   |   |   |   |-- printing.cpython-312.pyc
|   |           |   |   |   |   |-- string.cpython-312.pyc
|   |           |   |   |   |   |-- style.cpython-312.pyc
|   |           |   |   |   |   |-- style_render.cpython-312.pyc
|   |           |   |   |   |   `-- xml.cpython-312.pyc
|   |           |   |   |   |-- templates
|   |           |   |   |   |   |-- html.tpl
|   |           |   |   |   |   |-- html_style.tpl
|   |           |   |   |   |   |-- html_table.tpl
|   |           |   |   |   |   |-- latex.tpl
|   |           |   |   |   |   |-- latex_longtable.tpl
|   |           |   |   |   |   |-- latex_table.tpl
|   |           |   |   |   |   `-- string.tpl
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- _color_data.py
|   |           |   |   |   |-- console.py
|   |           |   |   |   |-- css.py
|   |           |   |   |   |-- csvs.py
|   |           |   |   |   |-- excel.py
|   |           |   |   |   |-- format.py
|   |           |   |   |   |-- html.py
|   |           |   |   |   |-- info.py
|   |           |   |   |   |-- printing.py
|   |           |   |   |   |-- string.py
|   |           |   |   |   |-- style.py
|   |           |   |   |   |-- style_render.py
|   |           |   |   |   `-- xml.py
|   |           |   |   |-- json
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- _json.cpython-312.pyc
|   |           |   |   |   |   |-- _normalize.cpython-312.pyc
|   |           |   |   |   |   `-- _table_schema.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- _json.py
|   |           |   |   |   |-- _normalize.py
|   |           |   |   |   `-- _table_schema.py
|   |           |   |   |-- parsers
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- arrow_parser_wrapper.cpython-312.pyc
|   |           |   |   |   |   |-- base_parser.cpython-312.pyc
|   |           |   |   |   |   |-- c_parser_wrapper.cpython-312.pyc
|   |           |   |   |   |   |-- python_parser.cpython-312.pyc
|   |           |   |   |   |   `-- readers.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- arrow_parser_wrapper.py
|   |           |   |   |   |-- base_parser.py
|   |           |   |   |   |-- c_parser_wrapper.py
|   |           |   |   |   |-- python_parser.py
|   |           |   |   |   `-- readers.py
|   |           |   |   |-- sas
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- sas7bdat.cpython-312.pyc
|   |           |   |   |   |   |-- sas_constants.cpython-312.pyc
|   |           |   |   |   |   |-- sas_xport.cpython-312.pyc
|   |           |   |   |   |   `-- sasreader.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- sas7bdat.py
|   |           |   |   |   |-- sas_constants.py
|   |           |   |   |   |-- sas_xport.py
|   |           |   |   |   `-- sasreader.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- _util.py
|   |           |   |   |-- api.py
|   |           |   |   |-- clipboards.py
|   |           |   |   |-- common.py
|   |           |   |   |-- feather_format.py
|   |           |   |   |-- gbq.py
|   |           |   |   |-- html.py
|   |           |   |   |-- orc.py
|   |           |   |   |-- parquet.py
|   |           |   |   |-- pickle.py
|   |           |   |   |-- pytables.py
|   |           |   |   |-- spss.py
|   |           |   |   |-- sql.py
|   |           |   |   |-- stata.py
|   |           |   |   `-- xml.py
|   |           |   |-- plotting
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _core.cpython-312.pyc
|   |           |   |   |   `-- _misc.cpython-312.pyc
|   |           |   |   |-- _matplotlib
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- boxplot.cpython-312.pyc
|   |           |   |   |   |   |-- converter.cpython-312.pyc
|   |           |   |   |   |   |-- core.cpython-312.pyc
|   |           |   |   |   |   |-- groupby.cpython-312.pyc
|   |           |   |   |   |   |-- hist.cpython-312.pyc
|   |           |   |   |   |   |-- misc.cpython-312.pyc
|   |           |   |   |   |   |-- style.cpython-312.pyc
|   |           |   |   |   |   |-- timeseries.cpython-312.pyc
|   |           |   |   |   |   `-- tools.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- boxplot.py
|   |           |   |   |   |-- converter.py
|   |           |   |   |   |-- core.py
|   |           |   |   |   |-- groupby.py
|   |           |   |   |   |-- hist.py
|   |           |   |   |   |-- misc.py
|   |           |   |   |   |-- style.py
|   |           |   |   |   |-- timeseries.py
|   |           |   |   |   `-- tools.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- _core.py
|   |           |   |   `-- _misc.py
|   |           |   |-- tests
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- test_aggregation.cpython-312.pyc
|   |           |   |   |   |-- test_algos.cpython-312.pyc
|   |           |   |   |   |-- test_common.cpython-312.pyc
|   |           |   |   |   |-- test_downstream.cpython-312.pyc
|   |           |   |   |   |-- test_errors.cpython-312.pyc
|   |           |   |   |   |-- test_expressions.cpython-312.pyc
|   |           |   |   |   |-- test_flags.cpython-312.pyc
|   |           |   |   |   |-- test_multilevel.cpython-312.pyc
|   |           |   |   |   |-- test_nanops.cpython-312.pyc
|   |           |   |   |   |-- test_optional_dependency.cpython-312.pyc
|   |           |   |   |   |-- test_register_accessor.cpython-312.pyc
|   |           |   |   |   |-- test_sorting.cpython-312.pyc
|   |           |   |   |   `-- test_take.cpython-312.pyc
|   |           |   |   |-- api
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_api.cpython-312.pyc
|   |           |   |   |   |   `-- test_types.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_api.py
|   |           |   |   |   `-- test_types.py
|   |           |   |   |-- apply
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- common.cpython-312.pyc
|   |           |   |   |   |   |-- test_frame_apply.cpython-312.pyc
|   |           |   |   |   |   |-- test_frame_apply_relabeling.cpython-312.pyc
|   |           |   |   |   |   |-- test_frame_transform.cpython-312.pyc
|   |           |   |   |   |   |-- test_invalid_arg.cpython-312.pyc
|   |           |   |   |   |   |-- test_numba.cpython-312.pyc
|   |           |   |   |   |   |-- test_series_apply.cpython-312.pyc
|   |           |   |   |   |   |-- test_series_apply_relabeling.cpython-312.pyc
|   |           |   |   |   |   |-- test_series_transform.cpython-312.pyc
|   |           |   |   |   |   `-- test_str.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- common.py
|   |           |   |   |   |-- test_frame_apply.py
|   |           |   |   |   |-- test_frame_apply_relabeling.py
|   |           |   |   |   |-- test_frame_transform.py
|   |           |   |   |   |-- test_invalid_arg.py
|   |           |   |   |   |-- test_numba.py
|   |           |   |   |   |-- test_series_apply.py
|   |           |   |   |   |-- test_series_apply_relabeling.py
|   |           |   |   |   |-- test_series_transform.py
|   |           |   |   |   `-- test_str.py
|   |           |   |   |-- arithmetic
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- common.cpython-312.pyc
|   |           |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |-- test_array_ops.cpython-312.pyc
|   |           |   |   |   |   |-- test_categorical.cpython-312.pyc
|   |           |   |   |   |   |-- test_datetime64.cpython-312.pyc
|   |           |   |   |   |   |-- test_interval.cpython-312.pyc
|   |           |   |   |   |   |-- test_numeric.cpython-312.pyc
|   |           |   |   |   |   |-- test_object.cpython-312.pyc
|   |           |   |   |   |   |-- test_period.cpython-312.pyc
|   |           |   |   |   |   `-- test_timedelta64.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- common.py
|   |           |   |   |   |-- conftest.py
|   |           |   |   |   |-- test_array_ops.py
|   |           |   |   |   |-- test_categorical.py
|   |           |   |   |   |-- test_datetime64.py
|   |           |   |   |   |-- test_interval.py
|   |           |   |   |   |-- test_numeric.py
|   |           |   |   |   |-- test_object.py
|   |           |   |   |   |-- test_period.py
|   |           |   |   |   `-- test_timedelta64.py
|   |           |   |   |-- arrays
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- masked_shared.cpython-312.pyc
|   |           |   |   |   |   |-- test_array.cpython-312.pyc
|   |           |   |   |   |   |-- test_datetimelike.cpython-312.pyc
|   |           |   |   |   |   |-- test_datetimes.cpython-312.pyc
|   |           |   |   |   |   |-- test_ndarray_backed.cpython-312.pyc
|   |           |   |   |   |   |-- test_period.cpython-312.pyc
|   |           |   |   |   |   `-- test_timedeltas.cpython-312.pyc
|   |           |   |   |   |-- boolean
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_arithmetic.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_astype.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_comparison.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_construction.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_function.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_logical.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_ops.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_reduction.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_repr.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_arithmetic.py
|   |           |   |   |   |   |-- test_astype.py
|   |           |   |   |   |   |-- test_comparison.py
|   |           |   |   |   |   |-- test_construction.py
|   |           |   |   |   |   |-- test_function.py
|   |           |   |   |   |   |-- test_indexing.py
|   |           |   |   |   |   |-- test_logical.py
|   |           |   |   |   |   |-- test_ops.py
|   |           |   |   |   |   |-- test_reduction.py
|   |           |   |   |   |   `-- test_repr.py
|   |           |   |   |   |-- categorical
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_algos.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_analytics.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_api.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_astype.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_dtypes.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_map.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_missing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_operators.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_replace.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_repr.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_sorting.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_subclass.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_take.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_warnings.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_algos.py
|   |           |   |   |   |   |-- test_analytics.py
|   |           |   |   |   |   |-- test_api.py
|   |           |   |   |   |   |-- test_astype.py
|   |           |   |   |   |   |-- test_constructors.py
|   |           |   |   |   |   |-- test_dtypes.py
|   |           |   |   |   |   |-- test_indexing.py
|   |           |   |   |   |   |-- test_map.py
|   |           |   |   |   |   |-- test_missing.py
|   |           |   |   |   |   |-- test_operators.py
|   |           |   |   |   |   |-- test_replace.py
|   |           |   |   |   |   |-- test_repr.py
|   |           |   |   |   |   |-- test_sorting.py
|   |           |   |   |   |   |-- test_subclass.py
|   |           |   |   |   |   |-- test_take.py
|   |           |   |   |   |   `-- test_warnings.py
|   |           |   |   |   |-- datetimes
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_cumulative.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_reductions.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_constructors.py
|   |           |   |   |   |   |-- test_cumulative.py
|   |           |   |   |   |   `-- test_reductions.py
|   |           |   |   |   |-- floating
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_arithmetic.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_astype.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_comparison.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_concat.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_construction.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_contains.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_function.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_repr.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_to_numpy.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- conftest.py
|   |           |   |   |   |   |-- test_arithmetic.py
|   |           |   |   |   |   |-- test_astype.py
|   |           |   |   |   |   |-- test_comparison.py
|   |           |   |   |   |   |-- test_concat.py
|   |           |   |   |   |   |-- test_construction.py
|   |           |   |   |   |   |-- test_contains.py
|   |           |   |   |   |   |-- test_function.py
|   |           |   |   |   |   |-- test_repr.py
|   |           |   |   |   |   `-- test_to_numpy.py
|   |           |   |   |   |-- integer
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_arithmetic.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_comparison.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_concat.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_construction.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_dtypes.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_function.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_reduction.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_repr.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- conftest.py
|   |           |   |   |   |   |-- test_arithmetic.py
|   |           |   |   |   |   |-- test_comparison.py
|   |           |   |   |   |   |-- test_concat.py
|   |           |   |   |   |   |-- test_construction.py
|   |           |   |   |   |   |-- test_dtypes.py
|   |           |   |   |   |   |-- test_function.py
|   |           |   |   |   |   |-- test_indexing.py
|   |           |   |   |   |   |-- test_reduction.py
|   |           |   |   |   |   `-- test_repr.py
|   |           |   |   |   |-- interval
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_astype.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_formats.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_interval.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_interval_pyarrow.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_overlaps.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_astype.py
|   |           |   |   |   |   |-- test_formats.py
|   |           |   |   |   |   |-- test_interval.py
|   |           |   |   |   |   |-- test_interval_pyarrow.py
|   |           |   |   |   |   `-- test_overlaps.py
|   |           |   |   |   |-- masked
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_arithmetic.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_arrow_compat.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_function.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_arithmetic.py
|   |           |   |   |   |   |-- test_arrow_compat.py
|   |           |   |   |   |   |-- test_function.py
|   |           |   |   |   |   `-- test_indexing.py
|   |           |   |   |   |-- numpy_
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_numpy.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_indexing.py
|   |           |   |   |   |   `-- test_numpy.py
|   |           |   |   |   |-- period
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_arrow_compat.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_astype.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_reductions.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_arrow_compat.py
|   |           |   |   |   |   |-- test_astype.py
|   |           |   |   |   |   |-- test_constructors.py
|   |           |   |   |   |   `-- test_reductions.py
|   |           |   |   |   |-- sparse
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_accessor.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_arithmetics.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_array.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_astype.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_combine_concat.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_dtype.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_libsparse.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_reductions.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_unary.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_accessor.py
|   |           |   |   |   |   |-- test_arithmetics.py
|   |           |   |   |   |   |-- test_array.py
|   |           |   |   |   |   |-- test_astype.py
|   |           |   |   |   |   |-- test_combine_concat.py
|   |           |   |   |   |   |-- test_constructors.py
|   |           |   |   |   |   |-- test_dtype.py
|   |           |   |   |   |   |-- test_indexing.py
|   |           |   |   |   |   |-- test_libsparse.py
|   |           |   |   |   |   |-- test_reductions.py
|   |           |   |   |   |   `-- test_unary.py
|   |           |   |   |   |-- string_
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_concat.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_string.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_string_arrow.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_concat.py
|   |           |   |   |   |   |-- test_string.py
|   |           |   |   |   |   `-- test_string_arrow.py
|   |           |   |   |   |-- timedeltas
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_cumulative.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_reductions.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_constructors.py
|   |           |   |   |   |   |-- test_cumulative.py
|   |           |   |   |   |   `-- test_reductions.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- masked_shared.py
|   |           |   |   |   |-- test_array.py
|   |           |   |   |   |-- test_datetimelike.py
|   |           |   |   |   |-- test_datetimes.py
|   |           |   |   |   |-- test_ndarray_backed.py
|   |           |   |   |   |-- test_period.py
|   |           |   |   |   `-- test_timedeltas.py
|   |           |   |   |-- base
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- common.cpython-312.pyc
|   |           |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |-- test_conversion.cpython-312.pyc
|   |           |   |   |   |   |-- test_fillna.cpython-312.pyc
|   |           |   |   |   |   |-- test_misc.cpython-312.pyc
|   |           |   |   |   |   |-- test_transpose.cpython-312.pyc
|   |           |   |   |   |   |-- test_unique.cpython-312.pyc
|   |           |   |   |   |   `-- test_value_counts.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- common.py
|   |           |   |   |   |-- test_constructors.py
|   |           |   |   |   |-- test_conversion.py
|   |           |   |   |   |-- test_fillna.py
|   |           |   |   |   |-- test_misc.py
|   |           |   |   |   |-- test_transpose.py
|   |           |   |   |   |-- test_unique.py
|   |           |   |   |   `-- test_value_counts.py
|   |           |   |   |-- computation
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_compat.cpython-312.pyc
|   |           |   |   |   |   `-- test_eval.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_compat.py
|   |           |   |   |   `-- test_eval.py
|   |           |   |   |-- config
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_config.cpython-312.pyc
|   |           |   |   |   |   `-- test_localization.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_config.py
|   |           |   |   |   `-- test_localization.py
|   |           |   |   |-- construction
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   `-- test_extract_array.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   `-- test_extract_array.py
|   |           |   |   |-- copy_view
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_array.cpython-312.pyc
|   |           |   |   |   |   |-- test_astype.cpython-312.pyc
|   |           |   |   |   |   |-- test_chained_assignment_deprecation.cpython-312.pyc
|   |           |   |   |   |   |-- test_clip.cpython-312.pyc
|   |           |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |-- test_core_functionalities.cpython-312.pyc
|   |           |   |   |   |   |-- test_functions.cpython-312.pyc
|   |           |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |-- test_internals.cpython-312.pyc
|   |           |   |   |   |   |-- test_interp_fillna.cpython-312.pyc
|   |           |   |   |   |   |-- test_methods.cpython-312.pyc
|   |           |   |   |   |   |-- test_replace.cpython-312.pyc
|   |           |   |   |   |   |-- test_setitem.cpython-312.pyc
|   |           |   |   |   |   |-- test_util.cpython-312.pyc
|   |           |   |   |   |   `-- util.cpython-312.pyc
|   |           |   |   |   |-- index
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_datetimeindex.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_index.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_periodindex.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_timedeltaindex.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_datetimeindex.py
|   |           |   |   |   |   |-- test_index.py
|   |           |   |   |   |   |-- test_periodindex.py
|   |           |   |   |   |   `-- test_timedeltaindex.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_array.py
|   |           |   |   |   |-- test_astype.py
|   |           |   |   |   |-- test_chained_assignment_deprecation.py
|   |           |   |   |   |-- test_clip.py
|   |           |   |   |   |-- test_constructors.py
|   |           |   |   |   |-- test_core_functionalities.py
|   |           |   |   |   |-- test_functions.py
|   |           |   |   |   |-- test_indexing.py
|   |           |   |   |   |-- test_internals.py
|   |           |   |   |   |-- test_interp_fillna.py
|   |           |   |   |   |-- test_methods.py
|   |           |   |   |   |-- test_replace.py
|   |           |   |   |   |-- test_setitem.py
|   |           |   |   |   |-- test_util.py
|   |           |   |   |   `-- util.py
|   |           |   |   |-- dtypes
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_common.cpython-312.pyc
|   |           |   |   |   |   |-- test_concat.cpython-312.pyc
|   |           |   |   |   |   |-- test_dtypes.cpython-312.pyc
|   |           |   |   |   |   |-- test_generic.cpython-312.pyc
|   |           |   |   |   |   |-- test_inference.cpython-312.pyc
|   |           |   |   |   |   `-- test_missing.cpython-312.pyc
|   |           |   |   |   |-- cast
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_can_hold_element.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_construct_from_scalar.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_construct_ndarray.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_construct_object_arr.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_dict_compat.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_downcast.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_find_common_type.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_infer_datetimelike.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_infer_dtype.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_maybe_box_native.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_promote.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_can_hold_element.py
|   |           |   |   |   |   |-- test_construct_from_scalar.py
|   |           |   |   |   |   |-- test_construct_ndarray.py
|   |           |   |   |   |   |-- test_construct_object_arr.py
|   |           |   |   |   |   |-- test_dict_compat.py
|   |           |   |   |   |   |-- test_downcast.py
|   |           |   |   |   |   |-- test_find_common_type.py
|   |           |   |   |   |   |-- test_infer_datetimelike.py
|   |           |   |   |   |   |-- test_infer_dtype.py
|   |           |   |   |   |   |-- test_maybe_box_native.py
|   |           |   |   |   |   `-- test_promote.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_common.py
|   |           |   |   |   |-- test_concat.py
|   |           |   |   |   |-- test_dtypes.py
|   |           |   |   |   |-- test_generic.py
|   |           |   |   |   |-- test_inference.py
|   |           |   |   |   `-- test_missing.py
|   |           |   |   |-- extension
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |-- test_arrow.cpython-312.pyc
|   |           |   |   |   |   |-- test_categorical.cpython-312.pyc
|   |           |   |   |   |   |-- test_common.cpython-312.pyc
|   |           |   |   |   |   |-- test_datetime.cpython-312.pyc
|   |           |   |   |   |   |-- test_extension.cpython-312.pyc
|   |           |   |   |   |   |-- test_interval.cpython-312.pyc
|   |           |   |   |   |   |-- test_masked.cpython-312.pyc
|   |           |   |   |   |   |-- test_numpy.cpython-312.pyc
|   |           |   |   |   |   |-- test_period.cpython-312.pyc
|   |           |   |   |   |   |-- test_sparse.cpython-312.pyc
|   |           |   |   |   |   `-- test_string.cpython-312.pyc
|   |           |   |   |   |-- array_with_attr
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- array.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_array_with_attr.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- array.py
|   |           |   |   |   |   `-- test_array_with_attr.py
|   |           |   |   |   |-- base
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- accumulate.cpython-312.pyc
|   |           |   |   |   |   |   |-- base.cpython-312.pyc
|   |           |   |   |   |   |   |-- casting.cpython-312.pyc
|   |           |   |   |   |   |   |-- constructors.cpython-312.pyc
|   |           |   |   |   |   |   |-- dim2.cpython-312.pyc
|   |           |   |   |   |   |   |-- dtype.cpython-312.pyc
|   |           |   |   |   |   |   |-- getitem.cpython-312.pyc
|   |           |   |   |   |   |   |-- groupby.cpython-312.pyc
|   |           |   |   |   |   |   |-- index.cpython-312.pyc
|   |           |   |   |   |   |   |-- interface.cpython-312.pyc
|   |           |   |   |   |   |   |-- io.cpython-312.pyc
|   |           |   |   |   |   |   |-- methods.cpython-312.pyc
|   |           |   |   |   |   |   |-- missing.cpython-312.pyc
|   |           |   |   |   |   |   |-- ops.cpython-312.pyc
|   |           |   |   |   |   |   |-- printing.cpython-312.pyc
|   |           |   |   |   |   |   |-- reduce.cpython-312.pyc
|   |           |   |   |   |   |   |-- reshaping.cpython-312.pyc
|   |           |   |   |   |   |   `-- setitem.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- accumulate.py
|   |           |   |   |   |   |-- base.py
|   |           |   |   |   |   |-- casting.py
|   |           |   |   |   |   |-- constructors.py
|   |           |   |   |   |   |-- dim2.py
|   |           |   |   |   |   |-- dtype.py
|   |           |   |   |   |   |-- getitem.py
|   |           |   |   |   |   |-- groupby.py
|   |           |   |   |   |   |-- index.py
|   |           |   |   |   |   |-- interface.py
|   |           |   |   |   |   |-- io.py
|   |           |   |   |   |   |-- methods.py
|   |           |   |   |   |   |-- missing.py
|   |           |   |   |   |   |-- ops.py
|   |           |   |   |   |   |-- printing.py
|   |           |   |   |   |   |-- reduce.py
|   |           |   |   |   |   |-- reshaping.py
|   |           |   |   |   |   `-- setitem.py
|   |           |   |   |   |-- date
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   `-- array.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   `-- array.py
|   |           |   |   |   |-- decimal
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- array.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_decimal.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- array.py
|   |           |   |   |   |   `-- test_decimal.py
|   |           |   |   |   |-- json
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- array.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_json.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- array.py
|   |           |   |   |   |   `-- test_json.py
|   |           |   |   |   |-- list
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- array.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_list.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- array.py
|   |           |   |   |   |   `-- test_list.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- conftest.py
|   |           |   |   |   |-- test_arrow.py
|   |           |   |   |   |-- test_categorical.py
|   |           |   |   |   |-- test_common.py
|   |           |   |   |   |-- test_datetime.py
|   |           |   |   |   |-- test_extension.py
|   |           |   |   |   |-- test_interval.py
|   |           |   |   |   |-- test_masked.py
|   |           |   |   |   |-- test_numpy.py
|   |           |   |   |   |-- test_period.py
|   |           |   |   |   |-- test_sparse.py
|   |           |   |   |   `-- test_string.py
|   |           |   |   |-- frame
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- common.cpython-312.pyc
|   |           |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |-- test_alter_axes.cpython-312.pyc
|   |           |   |   |   |   |-- test_api.cpython-312.pyc
|   |           |   |   |   |   |-- test_arithmetic.cpython-312.pyc
|   |           |   |   |   |   |-- test_arrow_interface.cpython-312.pyc
|   |           |   |   |   |   |-- test_block_internals.cpython-312.pyc
|   |           |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |-- test_cumulative.cpython-312.pyc
|   |           |   |   |   |   |-- test_iteration.cpython-312.pyc
|   |           |   |   |   |   |-- test_logical_ops.cpython-312.pyc
|   |           |   |   |   |   |-- test_nonunique_indexes.cpython-312.pyc
|   |           |   |   |   |   |-- test_npfuncs.cpython-312.pyc
|   |           |   |   |   |   |-- test_query_eval.cpython-312.pyc
|   |           |   |   |   |   |-- test_reductions.cpython-312.pyc
|   |           |   |   |   |   |-- test_repr.cpython-312.pyc
|   |           |   |   |   |   |-- test_stack_unstack.cpython-312.pyc
|   |           |   |   |   |   |-- test_subclass.cpython-312.pyc
|   |           |   |   |   |   |-- test_ufunc.cpython-312.pyc
|   |           |   |   |   |   |-- test_unary.cpython-312.pyc
|   |           |   |   |   |   `-- test_validate.cpython-312.pyc
|   |           |   |   |   |-- constructors
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_from_dict.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_from_records.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_from_dict.py
|   |           |   |   |   |   `-- test_from_records.py
|   |           |   |   |   |-- indexing
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_coercion.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_delitem.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_get.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_get_value.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_getitem.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_insert.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_mask.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_set_value.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_setitem.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_take.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_where.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_xs.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_coercion.py
|   |           |   |   |   |   |-- test_delitem.py
|   |           |   |   |   |   |-- test_get.py
|   |           |   |   |   |   |-- test_get_value.py
|   |           |   |   |   |   |-- test_getitem.py
|   |           |   |   |   |   |-- test_indexing.py
|   |           |   |   |   |   |-- test_insert.py
|   |           |   |   |   |   |-- test_mask.py
|   |           |   |   |   |   |-- test_set_value.py
|   |           |   |   |   |   |-- test_setitem.py
|   |           |   |   |   |   |-- test_take.py
|   |           |   |   |   |   |-- test_where.py
|   |           |   |   |   |   `-- test_xs.py
|   |           |   |   |   |-- methods
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_add_prefix_suffix.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_align.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_asfreq.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_asof.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_assign.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_astype.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_at_time.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_between_time.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_clip.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_combine.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_combine_first.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_compare.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_convert_dtypes.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_copy.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_count.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_cov_corr.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_describe.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_diff.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_dot.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_drop.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_drop_duplicates.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_droplevel.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_dropna.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_dtypes.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_duplicated.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_equals.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_explode.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_fillna.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_filter.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_first_and_last.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_first_valid_index.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_get_numeric_data.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_head_tail.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_infer_objects.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_info.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_interpolate.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_is_homogeneous_dtype.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_isetitem.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_isin.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_iterrows.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_join.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_map.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_matmul.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_nlargest.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_pct_change.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_pipe.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_pop.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_quantile.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_rank.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_reindex.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_reindex_like.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_rename.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_rename_axis.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_reorder_levels.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_replace.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_reset_index.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_round.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_sample.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_select_dtypes.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_set_axis.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_set_index.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_shift.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_size.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_sort_index.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_sort_values.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_swapaxes.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_swaplevel.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_to_csv.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_to_dict.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_to_dict_of_blocks.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_to_numpy.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_to_period.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_to_records.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_to_timestamp.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_transpose.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_truncate.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_tz_convert.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_tz_localize.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_update.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_value_counts.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_values.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_add_prefix_suffix.py
|   |           |   |   |   |   |-- test_align.py
|   |           |   |   |   |   |-- test_asfreq.py
|   |           |   |   |   |   |-- test_asof.py
|   |           |   |   |   |   |-- test_assign.py
|   |           |   |   |   |   |-- test_astype.py
|   |           |   |   |   |   |-- test_at_time.py
|   |           |   |   |   |   |-- test_between_time.py
|   |           |   |   |   |   |-- test_clip.py
|   |           |   |   |   |   |-- test_combine.py
|   |           |   |   |   |   |-- test_combine_first.py
|   |           |   |   |   |   |-- test_compare.py
|   |           |   |   |   |   |-- test_convert_dtypes.py
|   |           |   |   |   |   |-- test_copy.py
|   |           |   |   |   |   |-- test_count.py
|   |           |   |   |   |   |-- test_cov_corr.py
|   |           |   |   |   |   |-- test_describe.py
|   |           |   |   |   |   |-- test_diff.py
|   |           |   |   |   |   |-- test_dot.py
|   |           |   |   |   |   |-- test_drop.py
|   |           |   |   |   |   |-- test_drop_duplicates.py
|   |           |   |   |   |   |-- test_droplevel.py
|   |           |   |   |   |   |-- test_dropna.py
|   |           |   |   |   |   |-- test_dtypes.py
|   |           |   |   |   |   |-- test_duplicated.py
|   |           |   |   |   |   |-- test_equals.py
|   |           |   |   |   |   |-- test_explode.py
|   |           |   |   |   |   |-- test_fillna.py
|   |           |   |   |   |   |-- test_filter.py
|   |           |   |   |   |   |-- test_first_and_last.py
|   |           |   |   |   |   |-- test_first_valid_index.py
|   |           |   |   |   |   |-- test_get_numeric_data.py
|   |           |   |   |   |   |-- test_head_tail.py
|   |           |   |   |   |   |-- test_infer_objects.py
|   |           |   |   |   |   |-- test_info.py
|   |           |   |   |   |   |-- test_interpolate.py
|   |           |   |   |   |   |-- test_is_homogeneous_dtype.py
|   |           |   |   |   |   |-- test_isetitem.py
|   |           |   |   |   |   |-- test_isin.py
|   |           |   |   |   |   |-- test_iterrows.py
|   |           |   |   |   |   |-- test_join.py
|   |           |   |   |   |   |-- test_map.py
|   |           |   |   |   |   |-- test_matmul.py
|   |           |   |   |   |   |-- test_nlargest.py
|   |           |   |   |   |   |-- test_pct_change.py
|   |           |   |   |   |   |-- test_pipe.py
|   |           |   |   |   |   |-- test_pop.py
|   |           |   |   |   |   |-- test_quantile.py
|   |           |   |   |   |   |-- test_rank.py
|   |           |   |   |   |   |-- test_reindex.py
|   |           |   |   |   |   |-- test_reindex_like.py
|   |           |   |   |   |   |-- test_rename.py
|   |           |   |   |   |   |-- test_rename_axis.py
|   |           |   |   |   |   |-- test_reorder_levels.py
|   |           |   |   |   |   |-- test_replace.py
|   |           |   |   |   |   |-- test_reset_index.py
|   |           |   |   |   |   |-- test_round.py
|   |           |   |   |   |   |-- test_sample.py
|   |           |   |   |   |   |-- test_select_dtypes.py
|   |           |   |   |   |   |-- test_set_axis.py
|   |           |   |   |   |   |-- test_set_index.py
|   |           |   |   |   |   |-- test_shift.py
|   |           |   |   |   |   |-- test_size.py
|   |           |   |   |   |   |-- test_sort_index.py
|   |           |   |   |   |   |-- test_sort_values.py
|   |           |   |   |   |   |-- test_swapaxes.py
|   |           |   |   |   |   |-- test_swaplevel.py
|   |           |   |   |   |   |-- test_to_csv.py
|   |           |   |   |   |   |-- test_to_dict.py
|   |           |   |   |   |   |-- test_to_dict_of_blocks.py
|   |           |   |   |   |   |-- test_to_numpy.py
|   |           |   |   |   |   |-- test_to_period.py
|   |           |   |   |   |   |-- test_to_records.py
|   |           |   |   |   |   |-- test_to_timestamp.py
|   |           |   |   |   |   |-- test_transpose.py
|   |           |   |   |   |   |-- test_truncate.py
|   |           |   |   |   |   |-- test_tz_convert.py
|   |           |   |   |   |   |-- test_tz_localize.py
|   |           |   |   |   |   |-- test_update.py
|   |           |   |   |   |   |-- test_value_counts.py
|   |           |   |   |   |   `-- test_values.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- common.py
|   |           |   |   |   |-- conftest.py
|   |           |   |   |   |-- test_alter_axes.py
|   |           |   |   |   |-- test_api.py
|   |           |   |   |   |-- test_arithmetic.py
|   |           |   |   |   |-- test_arrow_interface.py
|   |           |   |   |   |-- test_block_internals.py
|   |           |   |   |   |-- test_constructors.py
|   |           |   |   |   |-- test_cumulative.py
|   |           |   |   |   |-- test_iteration.py
|   |           |   |   |   |-- test_logical_ops.py
|   |           |   |   |   |-- test_nonunique_indexes.py
|   |           |   |   |   |-- test_npfuncs.py
|   |           |   |   |   |-- test_query_eval.py
|   |           |   |   |   |-- test_reductions.py
|   |           |   |   |   |-- test_repr.py
|   |           |   |   |   |-- test_stack_unstack.py
|   |           |   |   |   |-- test_subclass.py
|   |           |   |   |   |-- test_ufunc.py
|   |           |   |   |   |-- test_unary.py
|   |           |   |   |   `-- test_validate.py
|   |           |   |   |-- generic
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_duplicate_labels.cpython-312.pyc
|   |           |   |   |   |   |-- test_finalize.cpython-312.pyc
|   |           |   |   |   |   |-- test_frame.cpython-312.pyc
|   |           |   |   |   |   |-- test_generic.cpython-312.pyc
|   |           |   |   |   |   |-- test_label_or_level_utils.cpython-312.pyc
|   |           |   |   |   |   |-- test_series.cpython-312.pyc
|   |           |   |   |   |   `-- test_to_xarray.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_duplicate_labels.py
|   |           |   |   |   |-- test_finalize.py
|   |           |   |   |   |-- test_frame.py
|   |           |   |   |   |-- test_generic.py
|   |           |   |   |   |-- test_label_or_level_utils.py
|   |           |   |   |   |-- test_series.py
|   |           |   |   |   `-- test_to_xarray.py
|   |           |   |   |-- groupby
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |-- test_all_methods.cpython-312.pyc
|   |           |   |   |   |   |-- test_api.cpython-312.pyc
|   |           |   |   |   |   |-- test_apply.cpython-312.pyc
|   |           |   |   |   |   |-- test_apply_mutate.cpython-312.pyc
|   |           |   |   |   |   |-- test_bin_groupby.cpython-312.pyc
|   |           |   |   |   |   |-- test_categorical.cpython-312.pyc
|   |           |   |   |   |   |-- test_counting.cpython-312.pyc
|   |           |   |   |   |   |-- test_cumulative.cpython-312.pyc
|   |           |   |   |   |   |-- test_filters.cpython-312.pyc
|   |           |   |   |   |   |-- test_groupby.cpython-312.pyc
|   |           |   |   |   |   |-- test_groupby_dropna.cpython-312.pyc
|   |           |   |   |   |   |-- test_groupby_subclass.cpython-312.pyc
|   |           |   |   |   |   |-- test_grouping.cpython-312.pyc
|   |           |   |   |   |   |-- test_index_as_string.cpython-312.pyc
|   |           |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |-- test_libgroupby.cpython-312.pyc
|   |           |   |   |   |   |-- test_missing.cpython-312.pyc
|   |           |   |   |   |   |-- test_numba.cpython-312.pyc
|   |           |   |   |   |   |-- test_numeric_only.cpython-312.pyc
|   |           |   |   |   |   |-- test_pipe.cpython-312.pyc
|   |           |   |   |   |   |-- test_raises.cpython-312.pyc
|   |           |   |   |   |   |-- test_reductions.cpython-312.pyc
|   |           |   |   |   |   `-- test_timegrouper.cpython-312.pyc
|   |           |   |   |   |-- aggregate
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_aggregate.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_cython.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_numba.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_other.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_aggregate.py
|   |           |   |   |   |   |-- test_cython.py
|   |           |   |   |   |   |-- test_numba.py
|   |           |   |   |   |   `-- test_other.py
|   |           |   |   |   |-- methods
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_corrwith.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_describe.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_groupby_shift_diff.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_is_monotonic.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_nlargest_nsmallest.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_nth.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_quantile.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_rank.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_sample.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_size.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_skew.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_value_counts.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_corrwith.py
|   |           |   |   |   |   |-- test_describe.py
|   |           |   |   |   |   |-- test_groupby_shift_diff.py
|   |           |   |   |   |   |-- test_is_monotonic.py
|   |           |   |   |   |   |-- test_nlargest_nsmallest.py
|   |           |   |   |   |   |-- test_nth.py
|   |           |   |   |   |   |-- test_quantile.py
|   |           |   |   |   |   |-- test_rank.py
|   |           |   |   |   |   |-- test_sample.py
|   |           |   |   |   |   |-- test_size.py
|   |           |   |   |   |   |-- test_skew.py
|   |           |   |   |   |   `-- test_value_counts.py
|   |           |   |   |   |-- transform
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_numba.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_transform.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_numba.py
|   |           |   |   |   |   `-- test_transform.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- conftest.py
|   |           |   |   |   |-- test_all_methods.py
|   |           |   |   |   |-- test_api.py
|   |           |   |   |   |-- test_apply.py
|   |           |   |   |   |-- test_apply_mutate.py
|   |           |   |   |   |-- test_bin_groupby.py
|   |           |   |   |   |-- test_categorical.py
|   |           |   |   |   |-- test_counting.py
|   |           |   |   |   |-- test_cumulative.py
|   |           |   |   |   |-- test_filters.py
|   |           |   |   |   |-- test_groupby.py
|   |           |   |   |   |-- test_groupby_dropna.py
|   |           |   |   |   |-- test_groupby_subclass.py
|   |           |   |   |   |-- test_grouping.py
|   |           |   |   |   |-- test_index_as_string.py
|   |           |   |   |   |-- test_indexing.py
|   |           |   |   |   |-- test_libgroupby.py
|   |           |   |   |   |-- test_missing.py
|   |           |   |   |   |-- test_numba.py
|   |           |   |   |   |-- test_numeric_only.py
|   |           |   |   |   |-- test_pipe.py
|   |           |   |   |   |-- test_raises.py
|   |           |   |   |   |-- test_reductions.py
|   |           |   |   |   `-- test_timegrouper.py
|   |           |   |   |-- indexes
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |-- test_any_index.cpython-312.pyc
|   |           |   |   |   |   |-- test_base.cpython-312.pyc
|   |           |   |   |   |   |-- test_common.cpython-312.pyc
|   |           |   |   |   |   |-- test_datetimelike.cpython-312.pyc
|   |           |   |   |   |   |-- test_engines.cpython-312.pyc
|   |           |   |   |   |   |-- test_frozen.cpython-312.pyc
|   |           |   |   |   |   |-- test_index_new.cpython-312.pyc
|   |           |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |-- test_numpy_compat.cpython-312.pyc
|   |           |   |   |   |   |-- test_old_base.cpython-312.pyc
|   |           |   |   |   |   |-- test_setops.cpython-312.pyc
|   |           |   |   |   |   `-- test_subclass.cpython-312.pyc
|   |           |   |   |   |-- base_class
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_formats.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_pickle.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_reshape.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_setops.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_where.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_constructors.py
|   |           |   |   |   |   |-- test_formats.py
|   |           |   |   |   |   |-- test_indexing.py
|   |           |   |   |   |   |-- test_pickle.py
|   |           |   |   |   |   |-- test_reshape.py
|   |           |   |   |   |   |-- test_setops.py
|   |           |   |   |   |   `-- test_where.py
|   |           |   |   |   |-- categorical
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_append.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_astype.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_category.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_equals.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_fillna.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_formats.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_map.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_reindex.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_setops.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_append.py
|   |           |   |   |   |   |-- test_astype.py
|   |           |   |   |   |   |-- test_category.py
|   |           |   |   |   |   |-- test_constructors.py
|   |           |   |   |   |   |-- test_equals.py
|   |           |   |   |   |   |-- test_fillna.py
|   |           |   |   |   |   |-- test_formats.py
|   |           |   |   |   |   |-- test_indexing.py
|   |           |   |   |   |   |-- test_map.py
|   |           |   |   |   |   |-- test_reindex.py
|   |           |   |   |   |   `-- test_setops.py
|   |           |   |   |   |-- datetimelike_
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_drop_duplicates.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_equals.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_is_monotonic.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_nat.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_sort_values.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_value_counts.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_drop_duplicates.py
|   |           |   |   |   |   |-- test_equals.py
|   |           |   |   |   |   |-- test_indexing.py
|   |           |   |   |   |   |-- test_is_monotonic.py
|   |           |   |   |   |   |-- test_nat.py
|   |           |   |   |   |   |-- test_sort_values.py
|   |           |   |   |   |   `-- test_value_counts.py
|   |           |   |   |   |-- datetimes
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_arithmetic.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_date_range.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_datetime.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_formats.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_freq_attr.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_iter.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_join.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_npfuncs.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_ops.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_partial_slicing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_pickle.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_reindex.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_scalar_compat.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_setops.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_timezones.cpython-312.pyc
|   |           |   |   |   |   |-- methods
|   |           |   |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_asof.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_astype.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_delete.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_factorize.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_fillna.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_insert.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_isocalendar.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_map.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_normalize.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_repeat.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_resolution.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_round.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_shift.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_snap.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_to_frame.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_to_julian_date.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_to_period.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_to_pydatetime.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_to_series.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_tz_convert.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_tz_localize.cpython-312.pyc
|   |           |   |   |   |   |   |   `-- test_unique.cpython-312.pyc
|   |           |   |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |   |-- test_asof.py
|   |           |   |   |   |   |   |-- test_astype.py
|   |           |   |   |   |   |   |-- test_delete.py
|   |           |   |   |   |   |   |-- test_factorize.py
|   |           |   |   |   |   |   |-- test_fillna.py
|   |           |   |   |   |   |   |-- test_insert.py
|   |           |   |   |   |   |   |-- test_isocalendar.py
|   |           |   |   |   |   |   |-- test_map.py
|   |           |   |   |   |   |   |-- test_normalize.py
|   |           |   |   |   |   |   |-- test_repeat.py
|   |           |   |   |   |   |   |-- test_resolution.py
|   |           |   |   |   |   |   |-- test_round.py
|   |           |   |   |   |   |   |-- test_shift.py
|   |           |   |   |   |   |   |-- test_snap.py
|   |           |   |   |   |   |   |-- test_to_frame.py
|   |           |   |   |   |   |   |-- test_to_julian_date.py
|   |           |   |   |   |   |   |-- test_to_period.py
|   |           |   |   |   |   |   |-- test_to_pydatetime.py
|   |           |   |   |   |   |   |-- test_to_series.py
|   |           |   |   |   |   |   |-- test_tz_convert.py
|   |           |   |   |   |   |   |-- test_tz_localize.py
|   |           |   |   |   |   |   `-- test_unique.py
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_arithmetic.py
|   |           |   |   |   |   |-- test_constructors.py
|   |           |   |   |   |   |-- test_date_range.py
|   |           |   |   |   |   |-- test_datetime.py
|   |           |   |   |   |   |-- test_formats.py
|   |           |   |   |   |   |-- test_freq_attr.py
|   |           |   |   |   |   |-- test_indexing.py
|   |           |   |   |   |   |-- test_iter.py
|   |           |   |   |   |   |-- test_join.py
|   |           |   |   |   |   |-- test_npfuncs.py
|   |           |   |   |   |   |-- test_ops.py
|   |           |   |   |   |   |-- test_partial_slicing.py
|   |           |   |   |   |   |-- test_pickle.py
|   |           |   |   |   |   |-- test_reindex.py
|   |           |   |   |   |   |-- test_scalar_compat.py
|   |           |   |   |   |   |-- test_setops.py
|   |           |   |   |   |   `-- test_timezones.py
|   |           |   |   |   |-- interval
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_astype.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_equals.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_formats.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_interval.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_interval_range.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_interval_tree.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_join.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_pickle.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_setops.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_astype.py
|   |           |   |   |   |   |-- test_constructors.py
|   |           |   |   |   |   |-- test_equals.py
|   |           |   |   |   |   |-- test_formats.py
|   |           |   |   |   |   |-- test_indexing.py
|   |           |   |   |   |   |-- test_interval.py
|   |           |   |   |   |   |-- test_interval_range.py
|   |           |   |   |   |   |-- test_interval_tree.py
|   |           |   |   |   |   |-- test_join.py
|   |           |   |   |   |   |-- test_pickle.py
|   |           |   |   |   |   `-- test_setops.py
|   |           |   |   |   |-- multi
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_analytics.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_astype.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_compat.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_conversion.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_copy.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_drop.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_duplicates.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_equivalence.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_formats.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_get_level_values.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_get_set.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_integrity.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_isin.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_join.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_lexsort.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_missing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_monotonic.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_names.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_partial_indexing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_pickle.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_reindex.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_reshape.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_setops.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_sorting.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_take.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- conftest.py
|   |           |   |   |   |   |-- test_analytics.py
|   |           |   |   |   |   |-- test_astype.py
|   |           |   |   |   |   |-- test_compat.py
|   |           |   |   |   |   |-- test_constructors.py
|   |           |   |   |   |   |-- test_conversion.py
|   |           |   |   |   |   |-- test_copy.py
|   |           |   |   |   |   |-- test_drop.py
|   |           |   |   |   |   |-- test_duplicates.py
|   |           |   |   |   |   |-- test_equivalence.py
|   |           |   |   |   |   |-- test_formats.py
|   |           |   |   |   |   |-- test_get_level_values.py
|   |           |   |   |   |   |-- test_get_set.py
|   |           |   |   |   |   |-- test_indexing.py
|   |           |   |   |   |   |-- test_integrity.py
|   |           |   |   |   |   |-- test_isin.py
|   |           |   |   |   |   |-- test_join.py
|   |           |   |   |   |   |-- test_lexsort.py
|   |           |   |   |   |   |-- test_missing.py
|   |           |   |   |   |   |-- test_monotonic.py
|   |           |   |   |   |   |-- test_names.py
|   |           |   |   |   |   |-- test_partial_indexing.py
|   |           |   |   |   |   |-- test_pickle.py
|   |           |   |   |   |   |-- test_reindex.py
|   |           |   |   |   |   |-- test_reshape.py
|   |           |   |   |   |   |-- test_setops.py
|   |           |   |   |   |   |-- test_sorting.py
|   |           |   |   |   |   `-- test_take.py
|   |           |   |   |   |-- numeric
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_astype.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_join.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_numeric.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_setops.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_astype.py
|   |           |   |   |   |   |-- test_indexing.py
|   |           |   |   |   |   |-- test_join.py
|   |           |   |   |   |   |-- test_numeric.py
|   |           |   |   |   |   `-- test_setops.py
|   |           |   |   |   |-- object
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_astype.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_astype.py
|   |           |   |   |   |   `-- test_indexing.py
|   |           |   |   |   |-- period
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_formats.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_freq_attr.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_join.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_monotonic.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_partial_slicing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_period.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_period_range.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_pickle.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_resolution.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_scalar_compat.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_searchsorted.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_setops.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_tools.cpython-312.pyc
|   |           |   |   |   |   |-- methods
|   |           |   |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_asfreq.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_astype.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_factorize.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_fillna.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_insert.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_is_full.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_repeat.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_shift.cpython-312.pyc
|   |           |   |   |   |   |   |   `-- test_to_timestamp.cpython-312.pyc
|   |           |   |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |   |-- test_asfreq.py
|   |           |   |   |   |   |   |-- test_astype.py
|   |           |   |   |   |   |   |-- test_factorize.py
|   |           |   |   |   |   |   |-- test_fillna.py
|   |           |   |   |   |   |   |-- test_insert.py
|   |           |   |   |   |   |   |-- test_is_full.py
|   |           |   |   |   |   |   |-- test_repeat.py
|   |           |   |   |   |   |   |-- test_shift.py
|   |           |   |   |   |   |   `-- test_to_timestamp.py
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_constructors.py
|   |           |   |   |   |   |-- test_formats.py
|   |           |   |   |   |   |-- test_freq_attr.py
|   |           |   |   |   |   |-- test_indexing.py
|   |           |   |   |   |   |-- test_join.py
|   |           |   |   |   |   |-- test_monotonic.py
|   |           |   |   |   |   |-- test_partial_slicing.py
|   |           |   |   |   |   |-- test_period.py
|   |           |   |   |   |   |-- test_period_range.py
|   |           |   |   |   |   |-- test_pickle.py
|   |           |   |   |   |   |-- test_resolution.py
|   |           |   |   |   |   |-- test_scalar_compat.py
|   |           |   |   |   |   |-- test_searchsorted.py
|   |           |   |   |   |   |-- test_setops.py
|   |           |   |   |   |   `-- test_tools.py
|   |           |   |   |   |-- ranges
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_join.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_range.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_setops.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_constructors.py
|   |           |   |   |   |   |-- test_indexing.py
|   |           |   |   |   |   |-- test_join.py
|   |           |   |   |   |   |-- test_range.py
|   |           |   |   |   |   `-- test_setops.py
|   |           |   |   |   |-- string
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_astype.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_astype.py
|   |           |   |   |   |   `-- test_indexing.py
|   |           |   |   |   |-- timedeltas
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_arithmetic.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_delete.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_formats.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_freq_attr.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_join.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_ops.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_pickle.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_scalar_compat.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_searchsorted.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_setops.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_timedelta.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_timedelta_range.cpython-312.pyc
|   |           |   |   |   |   |-- methods
|   |           |   |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_astype.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_factorize.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_fillna.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_insert.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_repeat.cpython-312.pyc
|   |           |   |   |   |   |   |   `-- test_shift.cpython-312.pyc
|   |           |   |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |   |-- test_astype.py
|   |           |   |   |   |   |   |-- test_factorize.py
|   |           |   |   |   |   |   |-- test_fillna.py
|   |           |   |   |   |   |   |-- test_insert.py
|   |           |   |   |   |   |   |-- test_repeat.py
|   |           |   |   |   |   |   `-- test_shift.py
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_arithmetic.py
|   |           |   |   |   |   |-- test_constructors.py
|   |           |   |   |   |   |-- test_delete.py
|   |           |   |   |   |   |-- test_formats.py
|   |           |   |   |   |   |-- test_freq_attr.py
|   |           |   |   |   |   |-- test_indexing.py
|   |           |   |   |   |   |-- test_join.py
|   |           |   |   |   |   |-- test_ops.py
|   |           |   |   |   |   |-- test_pickle.py
|   |           |   |   |   |   |-- test_scalar_compat.py
|   |           |   |   |   |   |-- test_searchsorted.py
|   |           |   |   |   |   |-- test_setops.py
|   |           |   |   |   |   |-- test_timedelta.py
|   |           |   |   |   |   `-- test_timedelta_range.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- conftest.py
|   |           |   |   |   |-- test_any_index.py
|   |           |   |   |   |-- test_base.py
|   |           |   |   |   |-- test_common.py
|   |           |   |   |   |-- test_datetimelike.py
|   |           |   |   |   |-- test_engines.py
|   |           |   |   |   |-- test_frozen.py
|   |           |   |   |   |-- test_index_new.py
|   |           |   |   |   |-- test_indexing.py
|   |           |   |   |   |-- test_numpy_compat.py
|   |           |   |   |   |-- test_old_base.py
|   |           |   |   |   |-- test_setops.py
|   |           |   |   |   `-- test_subclass.py
|   |           |   |   |-- indexing
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- common.cpython-312.pyc
|   |           |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |-- test_at.cpython-312.pyc
|   |           |   |   |   |   |-- test_categorical.cpython-312.pyc
|   |           |   |   |   |   |-- test_chaining_and_caching.cpython-312.pyc
|   |           |   |   |   |   |-- test_check_indexer.cpython-312.pyc
|   |           |   |   |   |   |-- test_coercion.cpython-312.pyc
|   |           |   |   |   |   |-- test_datetime.cpython-312.pyc
|   |           |   |   |   |   |-- test_floats.cpython-312.pyc
|   |           |   |   |   |   |-- test_iat.cpython-312.pyc
|   |           |   |   |   |   |-- test_iloc.cpython-312.pyc
|   |           |   |   |   |   |-- test_indexers.cpython-312.pyc
|   |           |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |-- test_loc.cpython-312.pyc
|   |           |   |   |   |   |-- test_na_indexing.cpython-312.pyc
|   |           |   |   |   |   |-- test_partial.cpython-312.pyc
|   |           |   |   |   |   `-- test_scalar.cpython-312.pyc
|   |           |   |   |   |-- interval
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_interval.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_interval_new.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_interval.py
|   |           |   |   |   |   `-- test_interval_new.py
|   |           |   |   |   |-- multiindex
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_chaining_and_caching.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_datetime.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_getitem.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_iloc.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_indexing_slow.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_loc.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_multiindex.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_partial.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_setitem.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_slice.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_sorted.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_chaining_and_caching.py
|   |           |   |   |   |   |-- test_datetime.py
|   |           |   |   |   |   |-- test_getitem.py
|   |           |   |   |   |   |-- test_iloc.py
|   |           |   |   |   |   |-- test_indexing_slow.py
|   |           |   |   |   |   |-- test_loc.py
|   |           |   |   |   |   |-- test_multiindex.py
|   |           |   |   |   |   |-- test_partial.py
|   |           |   |   |   |   |-- test_setitem.py
|   |           |   |   |   |   |-- test_slice.py
|   |           |   |   |   |   `-- test_sorted.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- common.py
|   |           |   |   |   |-- conftest.py
|   |           |   |   |   |-- test_at.py
|   |           |   |   |   |-- test_categorical.py
|   |           |   |   |   |-- test_chaining_and_caching.py
|   |           |   |   |   |-- test_check_indexer.py
|   |           |   |   |   |-- test_coercion.py
|   |           |   |   |   |-- test_datetime.py
|   |           |   |   |   |-- test_floats.py
|   |           |   |   |   |-- test_iat.py
|   |           |   |   |   |-- test_iloc.py
|   |           |   |   |   |-- test_indexers.py
|   |           |   |   |   |-- test_indexing.py
|   |           |   |   |   |-- test_loc.py
|   |           |   |   |   |-- test_na_indexing.py
|   |           |   |   |   |-- test_partial.py
|   |           |   |   |   `-- test_scalar.py
|   |           |   |   |-- interchange
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_impl.cpython-312.pyc
|   |           |   |   |   |   |-- test_spec_conformance.cpython-312.pyc
|   |           |   |   |   |   `-- test_utils.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_impl.py
|   |           |   |   |   |-- test_spec_conformance.py
|   |           |   |   |   `-- test_utils.py
|   |           |   |   |-- internals
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_api.cpython-312.pyc
|   |           |   |   |   |   |-- test_internals.cpython-312.pyc
|   |           |   |   |   |   `-- test_managers.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_api.py
|   |           |   |   |   |-- test_internals.py
|   |           |   |   |   `-- test_managers.py
|   |           |   |   |-- io
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |-- generate_legacy_storage_files.cpython-312.pyc
|   |           |   |   |   |   |-- test_clipboard.cpython-312.pyc
|   |           |   |   |   |   |-- test_common.cpython-312.pyc
|   |           |   |   |   |   |-- test_compression.cpython-312.pyc
|   |           |   |   |   |   |-- test_feather.cpython-312.pyc
|   |           |   |   |   |   |-- test_fsspec.cpython-312.pyc
|   |           |   |   |   |   |-- test_gbq.cpython-312.pyc
|   |           |   |   |   |   |-- test_gcs.cpython-312.pyc
|   |           |   |   |   |   |-- test_html.cpython-312.pyc
|   |           |   |   |   |   |-- test_http_headers.cpython-312.pyc
|   |           |   |   |   |   |-- test_orc.cpython-312.pyc
|   |           |   |   |   |   |-- test_parquet.cpython-312.pyc
|   |           |   |   |   |   |-- test_pickle.cpython-312.pyc
|   |           |   |   |   |   |-- test_s3.cpython-312.pyc
|   |           |   |   |   |   |-- test_spss.cpython-312.pyc
|   |           |   |   |   |   |-- test_sql.cpython-312.pyc
|   |           |   |   |   |   `-- test_stata.cpython-312.pyc
|   |           |   |   |   |-- excel
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_odf.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_odswriter.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_openpyxl.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_readers.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_style.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_writers.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_xlrd.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_xlsxwriter.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_odf.py
|   |           |   |   |   |   |-- test_odswriter.py
|   |           |   |   |   |   |-- test_openpyxl.py
|   |           |   |   |   |   |-- test_readers.py
|   |           |   |   |   |   |-- test_style.py
|   |           |   |   |   |   |-- test_writers.py
|   |           |   |   |   |   |-- test_xlrd.py
|   |           |   |   |   |   `-- test_xlsxwriter.py
|   |           |   |   |   |-- formats
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_console.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_css.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_eng_formatting.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_format.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_ipython_compat.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_printing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_to_csv.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_to_excel.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_to_html.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_to_latex.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_to_markdown.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_to_string.cpython-312.pyc
|   |           |   |   |   |   |-- style
|   |           |   |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_bar.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_exceptions.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_format.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_highlight.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_html.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_matplotlib.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_non_unique.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_style.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_to_latex.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_to_string.cpython-312.pyc
|   |           |   |   |   |   |   |   `-- test_tooltip.cpython-312.pyc
|   |           |   |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |   |-- test_bar.py
|   |           |   |   |   |   |   |-- test_exceptions.py
|   |           |   |   |   |   |   |-- test_format.py
|   |           |   |   |   |   |   |-- test_highlight.py
|   |           |   |   |   |   |   |-- test_html.py
|   |           |   |   |   |   |   |-- test_matplotlib.py
|   |           |   |   |   |   |   |-- test_non_unique.py
|   |           |   |   |   |   |   |-- test_style.py
|   |           |   |   |   |   |   |-- test_to_latex.py
|   |           |   |   |   |   |   |-- test_to_string.py
|   |           |   |   |   |   |   `-- test_tooltip.py
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_console.py
|   |           |   |   |   |   |-- test_css.py
|   |           |   |   |   |   |-- test_eng_formatting.py
|   |           |   |   |   |   |-- test_format.py
|   |           |   |   |   |   |-- test_ipython_compat.py
|   |           |   |   |   |   |-- test_printing.py
|   |           |   |   |   |   |-- test_to_csv.py
|   |           |   |   |   |   |-- test_to_excel.py
|   |           |   |   |   |   |-- test_to_html.py
|   |           |   |   |   |   |-- test_to_latex.py
|   |           |   |   |   |   |-- test_to_markdown.py
|   |           |   |   |   |   `-- test_to_string.py
|   |           |   |   |   |-- json
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_compression.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_deprecated_kwargs.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_json_table_schema.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_json_table_schema_ext_dtype.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_normalize.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_pandas.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_readlines.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_ujson.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- conftest.py
|   |           |   |   |   |   |-- test_compression.py
|   |           |   |   |   |   |-- test_deprecated_kwargs.py
|   |           |   |   |   |   |-- test_json_table_schema.py
|   |           |   |   |   |   |-- test_json_table_schema_ext_dtype.py
|   |           |   |   |   |   |-- test_normalize.py
|   |           |   |   |   |   |-- test_pandas.py
|   |           |   |   |   |   |-- test_readlines.py
|   |           |   |   |   |   `-- test_ujson.py
|   |           |   |   |   |-- parser
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_c_parser_only.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_comment.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_compression.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_concatenate_chunks.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_converters.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_dialect.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_encoding.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_header.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_index_col.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_mangle_dupes.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_multi_thread.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_na_values.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_network.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_parse_dates.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_python_parser_only.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_quoting.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_read_fwf.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_skiprows.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_textreader.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_unsupported.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_upcast.cpython-312.pyc
|   |           |   |   |   |   |-- common
|   |           |   |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_chunksize.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_common_basic.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_data_list.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_decimal.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_file_buffer_url.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_float.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_index.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_inf.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_ints.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_iterator.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_read_errors.cpython-312.pyc
|   |           |   |   |   |   |   |   `-- test_verbose.cpython-312.pyc
|   |           |   |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |   |-- test_chunksize.py
|   |           |   |   |   |   |   |-- test_common_basic.py
|   |           |   |   |   |   |   |-- test_data_list.py
|   |           |   |   |   |   |   |-- test_decimal.py
|   |           |   |   |   |   |   |-- test_file_buffer_url.py
|   |           |   |   |   |   |   |-- test_float.py
|   |           |   |   |   |   |   |-- test_index.py
|   |           |   |   |   |   |   |-- test_inf.py
|   |           |   |   |   |   |   |-- test_ints.py
|   |           |   |   |   |   |   |-- test_iterator.py
|   |           |   |   |   |   |   |-- test_read_errors.py
|   |           |   |   |   |   |   `-- test_verbose.py
|   |           |   |   |   |   |-- dtypes
|   |           |   |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_categorical.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_dtypes_basic.cpython-312.pyc
|   |           |   |   |   |   |   |   `-- test_empty.cpython-312.pyc
|   |           |   |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |   |-- test_categorical.py
|   |           |   |   |   |   |   |-- test_dtypes_basic.py
|   |           |   |   |   |   |   `-- test_empty.py
|   |           |   |   |   |   |-- usecols
|   |           |   |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_parse_dates.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_strings.cpython-312.pyc
|   |           |   |   |   |   |   |   `-- test_usecols_basic.cpython-312.pyc
|   |           |   |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |   |-- test_parse_dates.py
|   |           |   |   |   |   |   |-- test_strings.py
|   |           |   |   |   |   |   `-- test_usecols_basic.py
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- conftest.py
|   |           |   |   |   |   |-- test_c_parser_only.py
|   |           |   |   |   |   |-- test_comment.py
|   |           |   |   |   |   |-- test_compression.py
|   |           |   |   |   |   |-- test_concatenate_chunks.py
|   |           |   |   |   |   |-- test_converters.py
|   |           |   |   |   |   |-- test_dialect.py
|   |           |   |   |   |   |-- test_encoding.py
|   |           |   |   |   |   |-- test_header.py
|   |           |   |   |   |   |-- test_index_col.py
|   |           |   |   |   |   |-- test_mangle_dupes.py
|   |           |   |   |   |   |-- test_multi_thread.py
|   |           |   |   |   |   |-- test_na_values.py
|   |           |   |   |   |   |-- test_network.py
|   |           |   |   |   |   |-- test_parse_dates.py
|   |           |   |   |   |   |-- test_python_parser_only.py
|   |           |   |   |   |   |-- test_quoting.py
|   |           |   |   |   |   |-- test_read_fwf.py
|   |           |   |   |   |   |-- test_skiprows.py
|   |           |   |   |   |   |-- test_textreader.py
|   |           |   |   |   |   |-- test_unsupported.py
|   |           |   |   |   |   `-- test_upcast.py
|   |           |   |   |   |-- pytables
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- common.cpython-312.pyc
|   |           |   |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_append.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_categorical.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_compat.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_complex.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_errors.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_file_handling.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_keys.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_put.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_pytables_missing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_read.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_retain_attributes.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_round_trip.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_select.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_store.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_subclass.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_time_series.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_timezones.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- common.py
|   |           |   |   |   |   |-- conftest.py
|   |           |   |   |   |   |-- test_append.py
|   |           |   |   |   |   |-- test_categorical.py
|   |           |   |   |   |   |-- test_compat.py
|   |           |   |   |   |   |-- test_complex.py
|   |           |   |   |   |   |-- test_errors.py
|   |           |   |   |   |   |-- test_file_handling.py
|   |           |   |   |   |   |-- test_keys.py
|   |           |   |   |   |   |-- test_put.py
|   |           |   |   |   |   |-- test_pytables_missing.py
|   |           |   |   |   |   |-- test_read.py
|   |           |   |   |   |   |-- test_retain_attributes.py
|   |           |   |   |   |   |-- test_round_trip.py
|   |           |   |   |   |   |-- test_select.py
|   |           |   |   |   |   |-- test_store.py
|   |           |   |   |   |   |-- test_subclass.py
|   |           |   |   |   |   |-- test_time_series.py
|   |           |   |   |   |   `-- test_timezones.py
|   |           |   |   |   |-- sas
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_byteswap.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_sas.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_sas7bdat.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_xport.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_byteswap.py
|   |           |   |   |   |   |-- test_sas.py
|   |           |   |   |   |   |-- test_sas7bdat.py
|   |           |   |   |   |   `-- test_xport.py
|   |           |   |   |   |-- xml
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_to_xml.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_xml.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_xml_dtypes.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- conftest.py
|   |           |   |   |   |   |-- test_to_xml.py
|   |           |   |   |   |   |-- test_xml.py
|   |           |   |   |   |   `-- test_xml_dtypes.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- conftest.py
|   |           |   |   |   |-- generate_legacy_storage_files.py
|   |           |   |   |   |-- test_clipboard.py
|   |           |   |   |   |-- test_common.py
|   |           |   |   |   |-- test_compression.py
|   |           |   |   |   |-- test_feather.py
|   |           |   |   |   |-- test_fsspec.py
|   |           |   |   |   |-- test_gbq.py
|   |           |   |   |   |-- test_gcs.py
|   |           |   |   |   |-- test_html.py
|   |           |   |   |   |-- test_http_headers.py
|   |           |   |   |   |-- test_orc.py
|   |           |   |   |   |-- test_parquet.py
|   |           |   |   |   |-- test_pickle.py
|   |           |   |   |   |-- test_s3.py
|   |           |   |   |   |-- test_spss.py
|   |           |   |   |   |-- test_sql.py
|   |           |   |   |   `-- test_stata.py
|   |           |   |   |-- libs
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_hashtable.cpython-312.pyc
|   |           |   |   |   |   |-- test_join.cpython-312.pyc
|   |           |   |   |   |   |-- test_lib.cpython-312.pyc
|   |           |   |   |   |   `-- test_libalgos.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_hashtable.py
|   |           |   |   |   |-- test_join.py
|   |           |   |   |   |-- test_lib.py
|   |           |   |   |   `-- test_libalgos.py
|   |           |   |   |-- plotting
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- common.cpython-312.pyc
|   |           |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |-- test_backend.cpython-312.pyc
|   |           |   |   |   |   |-- test_boxplot_method.cpython-312.pyc
|   |           |   |   |   |   |-- test_common.cpython-312.pyc
|   |           |   |   |   |   |-- test_converter.cpython-312.pyc
|   |           |   |   |   |   |-- test_datetimelike.cpython-312.pyc
|   |           |   |   |   |   |-- test_groupby.cpython-312.pyc
|   |           |   |   |   |   |-- test_hist_method.cpython-312.pyc
|   |           |   |   |   |   |-- test_misc.cpython-312.pyc
|   |           |   |   |   |   |-- test_series.cpython-312.pyc
|   |           |   |   |   |   `-- test_style.cpython-312.pyc
|   |           |   |   |   |-- frame
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_frame.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_frame_color.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_frame_groupby.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_frame_legend.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_frame_subplots.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_hist_box_by.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_frame.py
|   |           |   |   |   |   |-- test_frame_color.py
|   |           |   |   |   |   |-- test_frame_groupby.py
|   |           |   |   |   |   |-- test_frame_legend.py
|   |           |   |   |   |   |-- test_frame_subplots.py
|   |           |   |   |   |   `-- test_hist_box_by.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- common.py
|   |           |   |   |   |-- conftest.py
|   |           |   |   |   |-- test_backend.py
|   |           |   |   |   |-- test_boxplot_method.py
|   |           |   |   |   |-- test_common.py
|   |           |   |   |   |-- test_converter.py
|   |           |   |   |   |-- test_datetimelike.py
|   |           |   |   |   |-- test_groupby.py
|   |           |   |   |   |-- test_hist_method.py
|   |           |   |   |   |-- test_misc.py
|   |           |   |   |   |-- test_series.py
|   |           |   |   |   `-- test_style.py
|   |           |   |   |-- reductions
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_reductions.cpython-312.pyc
|   |           |   |   |   |   `-- test_stat_reductions.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_reductions.py
|   |           |   |   |   `-- test_stat_reductions.py
|   |           |   |   |-- resample
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |-- test_base.cpython-312.pyc
|   |           |   |   |   |   |-- test_datetime_index.cpython-312.pyc
|   |           |   |   |   |   |-- test_period_index.cpython-312.pyc
|   |           |   |   |   |   |-- test_resample_api.cpython-312.pyc
|   |           |   |   |   |   |-- test_resampler_grouper.cpython-312.pyc
|   |           |   |   |   |   |-- test_time_grouper.cpython-312.pyc
|   |           |   |   |   |   `-- test_timedelta.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- conftest.py
|   |           |   |   |   |-- test_base.py
|   |           |   |   |   |-- test_datetime_index.py
|   |           |   |   |   |-- test_period_index.py
|   |           |   |   |   |-- test_resample_api.py
|   |           |   |   |   |-- test_resampler_grouper.py
|   |           |   |   |   |-- test_time_grouper.py
|   |           |   |   |   `-- test_timedelta.py
|   |           |   |   |-- reshape
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_crosstab.cpython-312.pyc
|   |           |   |   |   |   |-- test_cut.cpython-312.pyc
|   |           |   |   |   |   |-- test_from_dummies.cpython-312.pyc
|   |           |   |   |   |   |-- test_get_dummies.cpython-312.pyc
|   |           |   |   |   |   |-- test_melt.cpython-312.pyc
|   |           |   |   |   |   |-- test_pivot.cpython-312.pyc
|   |           |   |   |   |   |-- test_pivot_multilevel.cpython-312.pyc
|   |           |   |   |   |   |-- test_qcut.cpython-312.pyc
|   |           |   |   |   |   |-- test_union_categoricals.cpython-312.pyc
|   |           |   |   |   |   `-- test_util.cpython-312.pyc
|   |           |   |   |   |-- concat
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_append.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_append_common.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_categorical.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_concat.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_dataframe.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_datetimes.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_empty.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_index.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_invalid.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_series.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_sort.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- conftest.py
|   |           |   |   |   |   |-- test_append.py
|   |           |   |   |   |   |-- test_append_common.py
|   |           |   |   |   |   |-- test_categorical.py
|   |           |   |   |   |   |-- test_concat.py
|   |           |   |   |   |   |-- test_dataframe.py
|   |           |   |   |   |   |-- test_datetimes.py
|   |           |   |   |   |   |-- test_empty.py
|   |           |   |   |   |   |-- test_index.py
|   |           |   |   |   |   |-- test_invalid.py
|   |           |   |   |   |   |-- test_series.py
|   |           |   |   |   |   `-- test_sort.py
|   |           |   |   |   |-- merge
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_join.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_merge.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_merge_asof.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_merge_cross.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_merge_index_as_string.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_merge_ordered.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_multi.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_join.py
|   |           |   |   |   |   |-- test_merge.py
|   |           |   |   |   |   |-- test_merge_asof.py
|   |           |   |   |   |   |-- test_merge_cross.py
|   |           |   |   |   |   |-- test_merge_index_as_string.py
|   |           |   |   |   |   |-- test_merge_ordered.py
|   |           |   |   |   |   `-- test_multi.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_crosstab.py
|   |           |   |   |   |-- test_cut.py
|   |           |   |   |   |-- test_from_dummies.py
|   |           |   |   |   |-- test_get_dummies.py
|   |           |   |   |   |-- test_melt.py
|   |           |   |   |   |-- test_pivot.py
|   |           |   |   |   |-- test_pivot_multilevel.py
|   |           |   |   |   |-- test_qcut.py
|   |           |   |   |   |-- test_union_categoricals.py
|   |           |   |   |   `-- test_util.py
|   |           |   |   |-- scalar
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_na_scalar.cpython-312.pyc
|   |           |   |   |   |   `-- test_nat.cpython-312.pyc
|   |           |   |   |   |-- interval
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_arithmetic.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_contains.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_formats.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_interval.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_overlaps.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_arithmetic.py
|   |           |   |   |   |   |-- test_constructors.py
|   |           |   |   |   |   |-- test_contains.py
|   |           |   |   |   |   |-- test_formats.py
|   |           |   |   |   |   |-- test_interval.py
|   |           |   |   |   |   `-- test_overlaps.py
|   |           |   |   |   |-- period
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_arithmetic.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_asfreq.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_period.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_arithmetic.py
|   |           |   |   |   |   |-- test_asfreq.py
|   |           |   |   |   |   `-- test_period.py
|   |           |   |   |   |-- timedelta
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_arithmetic.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_formats.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_timedelta.cpython-312.pyc
|   |           |   |   |   |   |-- methods
|   |           |   |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_as_unit.cpython-312.pyc
|   |           |   |   |   |   |   |   `-- test_round.cpython-312.pyc
|   |           |   |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |   |-- test_as_unit.py
|   |           |   |   |   |   |   `-- test_round.py
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_arithmetic.py
|   |           |   |   |   |   |-- test_constructors.py
|   |           |   |   |   |   |-- test_formats.py
|   |           |   |   |   |   `-- test_timedelta.py
|   |           |   |   |   |-- timestamp
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_arithmetic.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_comparisons.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_formats.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_timestamp.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_timezones.cpython-312.pyc
|   |           |   |   |   |   |-- methods
|   |           |   |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_as_unit.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_normalize.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_replace.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_round.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_timestamp_method.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_to_julian_date.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_to_pydatetime.cpython-312.pyc
|   |           |   |   |   |   |   |   |-- test_tz_convert.cpython-312.pyc
|   |           |   |   |   |   |   |   `-- test_tz_localize.cpython-312.pyc
|   |           |   |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |   |-- test_as_unit.py
|   |           |   |   |   |   |   |-- test_normalize.py
|   |           |   |   |   |   |   |-- test_replace.py
|   |           |   |   |   |   |   |-- test_round.py
|   |           |   |   |   |   |   |-- test_timestamp_method.py
|   |           |   |   |   |   |   |-- test_to_julian_date.py
|   |           |   |   |   |   |   |-- test_to_pydatetime.py
|   |           |   |   |   |   |   |-- test_tz_convert.py
|   |           |   |   |   |   |   `-- test_tz_localize.py
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_arithmetic.py
|   |           |   |   |   |   |-- test_comparisons.py
|   |           |   |   |   |   |-- test_constructors.py
|   |           |   |   |   |   |-- test_formats.py
|   |           |   |   |   |   |-- test_timestamp.py
|   |           |   |   |   |   `-- test_timezones.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_na_scalar.py
|   |           |   |   |   `-- test_nat.py
|   |           |   |   |-- series
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_api.cpython-312.pyc
|   |           |   |   |   |   |-- test_arithmetic.cpython-312.pyc
|   |           |   |   |   |   |-- test_constructors.cpython-312.pyc
|   |           |   |   |   |   |-- test_cumulative.cpython-312.pyc
|   |           |   |   |   |   |-- test_formats.cpython-312.pyc
|   |           |   |   |   |   |-- test_iteration.cpython-312.pyc
|   |           |   |   |   |   |-- test_logical_ops.cpython-312.pyc
|   |           |   |   |   |   |-- test_missing.cpython-312.pyc
|   |           |   |   |   |   |-- test_npfuncs.cpython-312.pyc
|   |           |   |   |   |   |-- test_reductions.cpython-312.pyc
|   |           |   |   |   |   |-- test_subclass.cpython-312.pyc
|   |           |   |   |   |   |-- test_ufunc.cpython-312.pyc
|   |           |   |   |   |   |-- test_unary.cpython-312.pyc
|   |           |   |   |   |   `-- test_validate.cpython-312.pyc
|   |           |   |   |   |-- accessors
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_cat_accessor.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_dt_accessor.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_list_accessor.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_sparse_accessor.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_str_accessor.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_struct_accessor.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_cat_accessor.py
|   |           |   |   |   |   |-- test_dt_accessor.py
|   |           |   |   |   |   |-- test_list_accessor.py
|   |           |   |   |   |   |-- test_sparse_accessor.py
|   |           |   |   |   |   |-- test_str_accessor.py
|   |           |   |   |   |   `-- test_struct_accessor.py
|   |           |   |   |   |-- indexing
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_datetime.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_delitem.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_get.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_getitem.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_indexing.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_mask.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_set_value.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_setitem.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_take.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_where.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_xs.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_datetime.py
|   |           |   |   |   |   |-- test_delitem.py
|   |           |   |   |   |   |-- test_get.py
|   |           |   |   |   |   |-- test_getitem.py
|   |           |   |   |   |   |-- test_indexing.py
|   |           |   |   |   |   |-- test_mask.py
|   |           |   |   |   |   |-- test_set_value.py
|   |           |   |   |   |   |-- test_setitem.py
|   |           |   |   |   |   |-- test_take.py
|   |           |   |   |   |   |-- test_where.py
|   |           |   |   |   |   `-- test_xs.py
|   |           |   |   |   |-- methods
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_add_prefix_suffix.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_align.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_argsort.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_asof.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_astype.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_autocorr.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_between.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_case_when.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_clip.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_combine.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_combine_first.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_compare.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_convert_dtypes.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_copy.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_count.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_cov_corr.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_describe.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_diff.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_drop.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_drop_duplicates.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_dropna.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_dtypes.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_duplicated.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_equals.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_explode.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_fillna.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_get_numeric_data.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_head_tail.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_infer_objects.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_info.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_interpolate.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_is_monotonic.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_is_unique.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_isin.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_isna.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_item.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_map.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_matmul.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_nlargest.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_nunique.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_pct_change.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_pop.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_quantile.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_rank.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_reindex.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_reindex_like.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_rename.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_rename_axis.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_repeat.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_replace.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_reset_index.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_round.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_searchsorted.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_set_name.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_size.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_sort_index.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_sort_values.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_to_csv.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_to_dict.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_to_frame.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_to_numpy.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_tolist.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_truncate.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_tz_localize.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_unique.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_unstack.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_update.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_value_counts.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_values.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_view.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_add_prefix_suffix.py
|   |           |   |   |   |   |-- test_align.py
|   |           |   |   |   |   |-- test_argsort.py
|   |           |   |   |   |   |-- test_asof.py
|   |           |   |   |   |   |-- test_astype.py
|   |           |   |   |   |   |-- test_autocorr.py
|   |           |   |   |   |   |-- test_between.py
|   |           |   |   |   |   |-- test_case_when.py
|   |           |   |   |   |   |-- test_clip.py
|   |           |   |   |   |   |-- test_combine.py
|   |           |   |   |   |   |-- test_combine_first.py
|   |           |   |   |   |   |-- test_compare.py
|   |           |   |   |   |   |-- test_convert_dtypes.py
|   |           |   |   |   |   |-- test_copy.py
|   |           |   |   |   |   |-- test_count.py
|   |           |   |   |   |   |-- test_cov_corr.py
|   |           |   |   |   |   |-- test_describe.py
|   |           |   |   |   |   |-- test_diff.py
|   |           |   |   |   |   |-- test_drop.py
|   |           |   |   |   |   |-- test_drop_duplicates.py
|   |           |   |   |   |   |-- test_dropna.py
|   |           |   |   |   |   |-- test_dtypes.py
|   |           |   |   |   |   |-- test_duplicated.py
|   |           |   |   |   |   |-- test_equals.py
|   |           |   |   |   |   |-- test_explode.py
|   |           |   |   |   |   |-- test_fillna.py
|   |           |   |   |   |   |-- test_get_numeric_data.py
|   |           |   |   |   |   |-- test_head_tail.py
|   |           |   |   |   |   |-- test_infer_objects.py
|   |           |   |   |   |   |-- test_info.py
|   |           |   |   |   |   |-- test_interpolate.py
|   |           |   |   |   |   |-- test_is_monotonic.py
|   |           |   |   |   |   |-- test_is_unique.py
|   |           |   |   |   |   |-- test_isin.py
|   |           |   |   |   |   |-- test_isna.py
|   |           |   |   |   |   |-- test_item.py
|   |           |   |   |   |   |-- test_map.py
|   |           |   |   |   |   |-- test_matmul.py
|   |           |   |   |   |   |-- test_nlargest.py
|   |           |   |   |   |   |-- test_nunique.py
|   |           |   |   |   |   |-- test_pct_change.py
|   |           |   |   |   |   |-- test_pop.py
|   |           |   |   |   |   |-- test_quantile.py
|   |           |   |   |   |   |-- test_rank.py
|   |           |   |   |   |   |-- test_reindex.py
|   |           |   |   |   |   |-- test_reindex_like.py
|   |           |   |   |   |   |-- test_rename.py
|   |           |   |   |   |   |-- test_rename_axis.py
|   |           |   |   |   |   |-- test_repeat.py
|   |           |   |   |   |   |-- test_replace.py
|   |           |   |   |   |   |-- test_reset_index.py
|   |           |   |   |   |   |-- test_round.py
|   |           |   |   |   |   |-- test_searchsorted.py
|   |           |   |   |   |   |-- test_set_name.py
|   |           |   |   |   |   |-- test_size.py
|   |           |   |   |   |   |-- test_sort_index.py
|   |           |   |   |   |   |-- test_sort_values.py
|   |           |   |   |   |   |-- test_to_csv.py
|   |           |   |   |   |   |-- test_to_dict.py
|   |           |   |   |   |   |-- test_to_frame.py
|   |           |   |   |   |   |-- test_to_numpy.py
|   |           |   |   |   |   |-- test_tolist.py
|   |           |   |   |   |   |-- test_truncate.py
|   |           |   |   |   |   |-- test_tz_localize.py
|   |           |   |   |   |   |-- test_unique.py
|   |           |   |   |   |   |-- test_unstack.py
|   |           |   |   |   |   |-- test_update.py
|   |           |   |   |   |   |-- test_value_counts.py
|   |           |   |   |   |   |-- test_values.py
|   |           |   |   |   |   `-- test_view.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_api.py
|   |           |   |   |   |-- test_arithmetic.py
|   |           |   |   |   |-- test_constructors.py
|   |           |   |   |   |-- test_cumulative.py
|   |           |   |   |   |-- test_formats.py
|   |           |   |   |   |-- test_iteration.py
|   |           |   |   |   |-- test_logical_ops.py
|   |           |   |   |   |-- test_missing.py
|   |           |   |   |   |-- test_npfuncs.py
|   |           |   |   |   |-- test_reductions.py
|   |           |   |   |   |-- test_subclass.py
|   |           |   |   |   |-- test_ufunc.py
|   |           |   |   |   |-- test_unary.py
|   |           |   |   |   `-- test_validate.py
|   |           |   |   |-- strings
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |-- test_api.cpython-312.pyc
|   |           |   |   |   |   |-- test_case_justify.cpython-312.pyc
|   |           |   |   |   |   |-- test_cat.cpython-312.pyc
|   |           |   |   |   |   |-- test_extract.cpython-312.pyc
|   |           |   |   |   |   |-- test_find_replace.cpython-312.pyc
|   |           |   |   |   |   |-- test_get_dummies.cpython-312.pyc
|   |           |   |   |   |   |-- test_split_partition.cpython-312.pyc
|   |           |   |   |   |   |-- test_string_array.cpython-312.pyc
|   |           |   |   |   |   `-- test_strings.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- conftest.py
|   |           |   |   |   |-- test_api.py
|   |           |   |   |   |-- test_case_justify.py
|   |           |   |   |   |-- test_cat.py
|   |           |   |   |   |-- test_extract.py
|   |           |   |   |   |-- test_find_replace.py
|   |           |   |   |   |-- test_get_dummies.py
|   |           |   |   |   |-- test_split_partition.py
|   |           |   |   |   |-- test_string_array.py
|   |           |   |   |   `-- test_strings.py
|   |           |   |   |-- tools
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_to_datetime.cpython-312.pyc
|   |           |   |   |   |   |-- test_to_numeric.cpython-312.pyc
|   |           |   |   |   |   |-- test_to_time.cpython-312.pyc
|   |           |   |   |   |   `-- test_to_timedelta.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_to_datetime.py
|   |           |   |   |   |-- test_to_numeric.py
|   |           |   |   |   |-- test_to_time.py
|   |           |   |   |   `-- test_to_timedelta.py
|   |           |   |   |-- tseries
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- frequencies
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_freq_code.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_frequencies.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_inference.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_freq_code.py
|   |           |   |   |   |   |-- test_frequencies.py
|   |           |   |   |   |   `-- test_inference.py
|   |           |   |   |   |-- holiday
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_calendar.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_federal.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_holiday.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_observance.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- test_calendar.py
|   |           |   |   |   |   |-- test_federal.py
|   |           |   |   |   |   |-- test_holiday.py
|   |           |   |   |   |   `-- test_observance.py
|   |           |   |   |   |-- offsets
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- common.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_business_day.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_business_hour.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_business_month.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_business_quarter.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_business_year.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_common.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_custom_business_day.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_custom_business_hour.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_custom_business_month.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_dst.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_easter.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_fiscal.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_index.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_month.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_offsets.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_offsets_properties.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_quarter.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_ticks.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_week.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_year.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- common.py
|   |           |   |   |   |   |-- test_business_day.py
|   |           |   |   |   |   |-- test_business_hour.py
|   |           |   |   |   |   |-- test_business_month.py
|   |           |   |   |   |   |-- test_business_quarter.py
|   |           |   |   |   |   |-- test_business_year.py
|   |           |   |   |   |   |-- test_common.py
|   |           |   |   |   |   |-- test_custom_business_day.py
|   |           |   |   |   |   |-- test_custom_business_hour.py
|   |           |   |   |   |   |-- test_custom_business_month.py
|   |           |   |   |   |   |-- test_dst.py
|   |           |   |   |   |   |-- test_easter.py
|   |           |   |   |   |   |-- test_fiscal.py
|   |           |   |   |   |   |-- test_index.py
|   |           |   |   |   |   |-- test_month.py
|   |           |   |   |   |   |-- test_offsets.py
|   |           |   |   |   |   |-- test_offsets_properties.py
|   |           |   |   |   |   |-- test_quarter.py
|   |           |   |   |   |   |-- test_ticks.py
|   |           |   |   |   |   |-- test_week.py
|   |           |   |   |   |   `-- test_year.py
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- tslibs
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- test_api.cpython-312.pyc
|   |           |   |   |   |   |-- test_array_to_datetime.cpython-312.pyc
|   |           |   |   |   |   |-- test_ccalendar.cpython-312.pyc
|   |           |   |   |   |   |-- test_conversion.cpython-312.pyc
|   |           |   |   |   |   |-- test_fields.cpython-312.pyc
|   |           |   |   |   |   |-- test_libfrequencies.cpython-312.pyc
|   |           |   |   |   |   |-- test_liboffsets.cpython-312.pyc
|   |           |   |   |   |   |-- test_np_datetime.cpython-312.pyc
|   |           |   |   |   |   |-- test_npy_units.cpython-312.pyc
|   |           |   |   |   |   |-- test_parse_iso8601.cpython-312.pyc
|   |           |   |   |   |   |-- test_parsing.cpython-312.pyc
|   |           |   |   |   |   |-- test_period.cpython-312.pyc
|   |           |   |   |   |   |-- test_resolution.cpython-312.pyc
|   |           |   |   |   |   |-- test_strptime.cpython-312.pyc
|   |           |   |   |   |   |-- test_timedeltas.cpython-312.pyc
|   |           |   |   |   |   |-- test_timezones.cpython-312.pyc
|   |           |   |   |   |   |-- test_to_offset.cpython-312.pyc
|   |           |   |   |   |   `-- test_tzconversion.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- test_api.py
|   |           |   |   |   |-- test_array_to_datetime.py
|   |           |   |   |   |-- test_ccalendar.py
|   |           |   |   |   |-- test_conversion.py
|   |           |   |   |   |-- test_fields.py
|   |           |   |   |   |-- test_libfrequencies.py
|   |           |   |   |   |-- test_liboffsets.py
|   |           |   |   |   |-- test_np_datetime.py
|   |           |   |   |   |-- test_npy_units.py
|   |           |   |   |   |-- test_parse_iso8601.py
|   |           |   |   |   |-- test_parsing.py
|   |           |   |   |   |-- test_period.py
|   |           |   |   |   |-- test_resolution.py
|   |           |   |   |   |-- test_strptime.py
|   |           |   |   |   |-- test_timedeltas.py
|   |           |   |   |   |-- test_timezones.py
|   |           |   |   |   |-- test_to_offset.py
|   |           |   |   |   `-- test_tzconversion.py
|   |           |   |   |-- util
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |-- test_assert_almost_equal.cpython-312.pyc
|   |           |   |   |   |   |-- test_assert_attr_equal.cpython-312.pyc
|   |           |   |   |   |   |-- test_assert_categorical_equal.cpython-312.pyc
|   |           |   |   |   |   |-- test_assert_extension_array_equal.cpython-312.pyc
|   |           |   |   |   |   |-- test_assert_frame_equal.cpython-312.pyc
|   |           |   |   |   |   |-- test_assert_index_equal.cpython-312.pyc
|   |           |   |   |   |   |-- test_assert_interval_array_equal.cpython-312.pyc
|   |           |   |   |   |   |-- test_assert_numpy_array_equal.cpython-312.pyc
|   |           |   |   |   |   |-- test_assert_produces_warning.cpython-312.pyc
|   |           |   |   |   |   |-- test_assert_series_equal.cpython-312.pyc
|   |           |   |   |   |   |-- test_deprecate.cpython-312.pyc
|   |           |   |   |   |   |-- test_deprecate_kwarg.cpython-312.pyc
|   |           |   |   |   |   |-- test_deprecate_nonkeyword_arguments.cpython-312.pyc
|   |           |   |   |   |   |-- test_doc.cpython-312.pyc
|   |           |   |   |   |   |-- test_hashing.cpython-312.pyc
|   |           |   |   |   |   |-- test_numba.cpython-312.pyc
|   |           |   |   |   |   |-- test_rewrite_warning.cpython-312.pyc
|   |           |   |   |   |   |-- test_shares_memory.cpython-312.pyc
|   |           |   |   |   |   |-- test_show_versions.cpython-312.pyc
|   |           |   |   |   |   |-- test_util.cpython-312.pyc
|   |           |   |   |   |   |-- test_validate_args.cpython-312.pyc
|   |           |   |   |   |   |-- test_validate_args_and_kwargs.cpython-312.pyc
|   |           |   |   |   |   |-- test_validate_inclusive.cpython-312.pyc
|   |           |   |   |   |   `-- test_validate_kwargs.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- conftest.py
|   |           |   |   |   |-- test_assert_almost_equal.py
|   |           |   |   |   |-- test_assert_attr_equal.py
|   |           |   |   |   |-- test_assert_categorical_equal.py
|   |           |   |   |   |-- test_assert_extension_array_equal.py
|   |           |   |   |   |-- test_assert_frame_equal.py
|   |           |   |   |   |-- test_assert_index_equal.py
|   |           |   |   |   |-- test_assert_interval_array_equal.py
|   |           |   |   |   |-- test_assert_numpy_array_equal.py
|   |           |   |   |   |-- test_assert_produces_warning.py
|   |           |   |   |   |-- test_assert_series_equal.py
|   |           |   |   |   |-- test_deprecate.py
|   |           |   |   |   |-- test_deprecate_kwarg.py
|   |           |   |   |   |-- test_deprecate_nonkeyword_arguments.py
|   |           |   |   |   |-- test_doc.py
|   |           |   |   |   |-- test_hashing.py
|   |           |   |   |   |-- test_numba.py
|   |           |   |   |   |-- test_rewrite_warning.py
|   |           |   |   |   |-- test_shares_memory.py
|   |           |   |   |   |-- test_show_versions.py
|   |           |   |   |   |-- test_util.py
|   |           |   |   |   |-- test_validate_args.py
|   |           |   |   |   |-- test_validate_args_and_kwargs.py
|   |           |   |   |   |-- test_validate_inclusive.py
|   |           |   |   |   `-- test_validate_kwargs.py
|   |           |   |   |-- window
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |-- test_api.cpython-312.pyc
|   |           |   |   |   |   |-- test_apply.cpython-312.pyc
|   |           |   |   |   |   |-- test_base_indexer.cpython-312.pyc
|   |           |   |   |   |   |-- test_cython_aggregations.cpython-312.pyc
|   |           |   |   |   |   |-- test_dtypes.cpython-312.pyc
|   |           |   |   |   |   |-- test_ewm.cpython-312.pyc
|   |           |   |   |   |   |-- test_expanding.cpython-312.pyc
|   |           |   |   |   |   |-- test_groupby.cpython-312.pyc
|   |           |   |   |   |   |-- test_numba.cpython-312.pyc
|   |           |   |   |   |   |-- test_online.cpython-312.pyc
|   |           |   |   |   |   |-- test_pairwise.cpython-312.pyc
|   |           |   |   |   |   |-- test_rolling.cpython-312.pyc
|   |           |   |   |   |   |-- test_rolling_functions.cpython-312.pyc
|   |           |   |   |   |   |-- test_rolling_quantile.cpython-312.pyc
|   |           |   |   |   |   |-- test_rolling_skew_kurt.cpython-312.pyc
|   |           |   |   |   |   |-- test_timeseries_window.cpython-312.pyc
|   |           |   |   |   |   `-- test_win_type.cpython-312.pyc
|   |           |   |   |   |-- moments
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- conftest.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_moments_consistency_ewm.cpython-312.pyc
|   |           |   |   |   |   |   |-- test_moments_consistency_expanding.cpython-312.pyc
|   |           |   |   |   |   |   `-- test_moments_consistency_rolling.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- conftest.py
|   |           |   |   |   |   |-- test_moments_consistency_ewm.py
|   |           |   |   |   |   |-- test_moments_consistency_expanding.py
|   |           |   |   |   |   `-- test_moments_consistency_rolling.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- conftest.py
|   |           |   |   |   |-- test_api.py
|   |           |   |   |   |-- test_apply.py
|   |           |   |   |   |-- test_base_indexer.py
|   |           |   |   |   |-- test_cython_aggregations.py
|   |           |   |   |   |-- test_dtypes.py
|   |           |   |   |   |-- test_ewm.py
|   |           |   |   |   |-- test_expanding.py
|   |           |   |   |   |-- test_groupby.py
|   |           |   |   |   |-- test_numba.py
|   |           |   |   |   |-- test_online.py
|   |           |   |   |   |-- test_pairwise.py
|   |           |   |   |   |-- test_rolling.py
|   |           |   |   |   |-- test_rolling_functions.py
|   |           |   |   |   |-- test_rolling_quantile.py
|   |           |   |   |   |-- test_rolling_skew_kurt.py
|   |           |   |   |   |-- test_timeseries_window.py
|   |           |   |   |   `-- test_win_type.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- test_aggregation.py
|   |           |   |   |-- test_algos.py
|   |           |   |   |-- test_common.py
|   |           |   |   |-- test_downstream.py
|   |           |   |   |-- test_errors.py
|   |           |   |   |-- test_expressions.py
|   |           |   |   |-- test_flags.py
|   |           |   |   |-- test_multilevel.py
|   |           |   |   |-- test_nanops.py
|   |           |   |   |-- test_optional_dependency.py
|   |           |   |   |-- test_register_accessor.py
|   |           |   |   |-- test_sorting.py
|   |           |   |   `-- test_take.py
|   |           |   |-- tseries
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- api.cpython-312.pyc
|   |           |   |   |   |-- frequencies.cpython-312.pyc
|   |           |   |   |   |-- holiday.cpython-312.pyc
|   |           |   |   |   `-- offsets.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- api.py
|   |           |   |   |-- frequencies.py
|   |           |   |   |-- holiday.py
|   |           |   |   `-- offsets.py
|   |           |   |-- util
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _decorators.cpython-312.pyc
|   |           |   |   |   |-- _doctools.cpython-312.pyc
|   |           |   |   |   |-- _exceptions.cpython-312.pyc
|   |           |   |   |   |-- _print_versions.cpython-312.pyc
|   |           |   |   |   |-- _test_decorators.cpython-312.pyc
|   |           |   |   |   |-- _tester.cpython-312.pyc
|   |           |   |   |   `-- _validators.cpython-312.pyc
|   |           |   |   |-- version
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- _decorators.py
|   |           |   |   |-- _doctools.py
|   |           |   |   |-- _exceptions.py
|   |           |   |   |-- _print_versions.py
|   |           |   |   |-- _test_decorators.py
|   |           |   |   |-- _tester.py
|   |           |   |   `-- _validators.py
|   |           |   |-- __init__.py
|   |           |   |-- _typing.py
|   |           |   |-- _version.py
|   |           |   |-- _version_meson.py
|   |           |   |-- conftest.py
|   |           |   |-- pyproject.toml
|   |           |   `-- testing.py
|   |           |-- pandas-2.3.2.dist-info
|   |           |   |-- INSTALLER
|   |           |   |-- LICENSE
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   |-- REQUESTED
|   |           |   |-- WHEEL
|   |           |   `-- entry_points.txt
|   |           |-- pillow-11.3.0.dist-info
|   |           |   |-- licenses
|   |           |   |   `-- LICENSE
|   |           |   |-- INSTALLER
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   |-- WHEEL
|   |           |   |-- top_level.txt
|   |           |   `-- zip-safe
|   |           |-- pillow.libs
|   |           |   |-- libXau-154567c4.so.6.0.0
|   |           |   |-- libavif-01e67780.so.16.3.0
|   |           |   |-- libbrotlicommon-c55a5f7a.so.1.1.0
|   |           |   |-- libbrotlidec-2ced2f3a.so.1.1.0
|   |           |   |-- libfreetype-083ff72c.so.6.20.2
|   |           |   |-- libharfbuzz-fe5b8f8d.so.0.61121.0
|   |           |   |-- libjpeg-8a13c6e0.so.62.4.0
|   |           |   |-- liblcms2-cc10e42f.so.2.0.17
|   |           |   |-- liblzma-64b7ab39.so.5.8.1
|   |           |   |-- libopenjp2-56811f71.so.2.5.3
|   |           |   |-- libpng16-d00bd151.so.16.49.0
|   |           |   |-- libsharpyuv-60a7c00b.so.0.1.1
|   |           |   |-- libtiff-13a02c81.so.6.1.0
|   |           |   |-- libwebp-5f0275c0.so.7.1.10
|   |           |   |-- libwebpdemux-efaed568.so.2.0.16
|   |           |   |-- libwebpmux-6f2b1ad9.so.3.1.1
|   |           |   `-- libxcb-64009ff3.so.1.1.0
|   |           |-- pip
|   |           |   |-- __pycache__
|   |           |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |-- __main__.cpython-312.pyc
|   |           |   |   `-- __pip-runner__.cpython-312.pyc
|   |           |   |-- _internal
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- build_env.cpython-312.pyc
|   |           |   |   |   |-- cache.cpython-312.pyc
|   |           |   |   |   |-- configuration.cpython-312.pyc
|   |           |   |   |   |-- exceptions.cpython-312.pyc
|   |           |   |   |   |-- main.cpython-312.pyc
|   |           |   |   |   |-- pyproject.cpython-312.pyc
|   |           |   |   |   |-- self_outdated_check.cpython-312.pyc
|   |           |   |   |   `-- wheel_builder.cpython-312.pyc
|   |           |   |   |-- cli
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- autocompletion.cpython-312.pyc
|   |           |   |   |   |   |-- base_command.cpython-312.pyc
|   |           |   |   |   |   |-- cmdoptions.cpython-312.pyc
|   |           |   |   |   |   |-- command_context.cpython-312.pyc
|   |           |   |   |   |   |-- index_command.cpython-312.pyc
|   |           |   |   |   |   |-- main.cpython-312.pyc
|   |           |   |   |   |   |-- main_parser.cpython-312.pyc
|   |           |   |   |   |   |-- parser.cpython-312.pyc
|   |           |   |   |   |   |-- progress_bars.cpython-312.pyc
|   |           |   |   |   |   |-- req_command.cpython-312.pyc
|   |           |   |   |   |   |-- spinners.cpython-312.pyc
|   |           |   |   |   |   `-- status_codes.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- autocompletion.py
|   |           |   |   |   |-- base_command.py
|   |           |   |   |   |-- cmdoptions.py
|   |           |   |   |   |-- command_context.py
|   |           |   |   |   |-- index_command.py
|   |           |   |   |   |-- main.py
|   |           |   |   |   |-- main_parser.py
|   |           |   |   |   |-- parser.py
|   |           |   |   |   |-- progress_bars.py
|   |           |   |   |   |-- req_command.py
|   |           |   |   |   |-- spinners.py
|   |           |   |   |   `-- status_codes.py
|   |           |   |   |-- commands
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- cache.cpython-312.pyc
|   |           |   |   |   |   |-- check.cpython-312.pyc
|   |           |   |   |   |   |-- completion.cpython-312.pyc
|   |           |   |   |   |   |-- configuration.cpython-312.pyc
|   |           |   |   |   |   |-- debug.cpython-312.pyc
|   |           |   |   |   |   |-- download.cpython-312.pyc
|   |           |   |   |   |   |-- freeze.cpython-312.pyc
|   |           |   |   |   |   |-- hash.cpython-312.pyc
|   |           |   |   |   |   |-- help.cpython-312.pyc
|   |           |   |   |   |   |-- index.cpython-312.pyc
|   |           |   |   |   |   |-- inspect.cpython-312.pyc
|   |           |   |   |   |   |-- install.cpython-312.pyc
|   |           |   |   |   |   |-- list.cpython-312.pyc
|   |           |   |   |   |   |-- lock.cpython-312.pyc
|   |           |   |   |   |   |-- search.cpython-312.pyc
|   |           |   |   |   |   |-- show.cpython-312.pyc
|   |           |   |   |   |   |-- uninstall.cpython-312.pyc
|   |           |   |   |   |   `-- wheel.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- cache.py
|   |           |   |   |   |-- check.py
|   |           |   |   |   |-- completion.py
|   |           |   |   |   |-- configuration.py
|   |           |   |   |   |-- debug.py
|   |           |   |   |   |-- download.py
|   |           |   |   |   |-- freeze.py
|   |           |   |   |   |-- hash.py
|   |           |   |   |   |-- help.py
|   |           |   |   |   |-- index.py
|   |           |   |   |   |-- inspect.py
|   |           |   |   |   |-- install.py
|   |           |   |   |   |-- list.py
|   |           |   |   |   |-- lock.py
|   |           |   |   |   |-- search.py
|   |           |   |   |   |-- show.py
|   |           |   |   |   |-- uninstall.py
|   |           |   |   |   `-- wheel.py
|   |           |   |   |-- distributions
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- base.cpython-312.pyc
|   |           |   |   |   |   |-- installed.cpython-312.pyc
|   |           |   |   |   |   |-- sdist.cpython-312.pyc
|   |           |   |   |   |   `-- wheel.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- base.py
|   |           |   |   |   |-- installed.py
|   |           |   |   |   |-- sdist.py
|   |           |   |   |   `-- wheel.py
|   |           |   |   |-- index
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- collector.cpython-312.pyc
|   |           |   |   |   |   |-- package_finder.cpython-312.pyc
|   |           |   |   |   |   `-- sources.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- collector.py
|   |           |   |   |   |-- package_finder.py
|   |           |   |   |   `-- sources.py
|   |           |   |   |-- locations
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- _distutils.cpython-312.pyc
|   |           |   |   |   |   |-- _sysconfig.cpython-312.pyc
|   |           |   |   |   |   `-- base.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- _distutils.py
|   |           |   |   |   |-- _sysconfig.py
|   |           |   |   |   `-- base.py
|   |           |   |   |-- metadata
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- _json.cpython-312.pyc
|   |           |   |   |   |   |-- base.cpython-312.pyc
|   |           |   |   |   |   `-- pkg_resources.cpython-312.pyc
|   |           |   |   |   |-- importlib
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- _compat.cpython-312.pyc
|   |           |   |   |   |   |   |-- _dists.cpython-312.pyc
|   |           |   |   |   |   |   `-- _envs.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- _compat.py
|   |           |   |   |   |   |-- _dists.py
|   |           |   |   |   |   `-- _envs.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- _json.py
|   |           |   |   |   |-- base.py
|   |           |   |   |   `-- pkg_resources.py
|   |           |   |   |-- models
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- candidate.cpython-312.pyc
|   |           |   |   |   |   |-- direct_url.cpython-312.pyc
|   |           |   |   |   |   |-- format_control.cpython-312.pyc
|   |           |   |   |   |   |-- index.cpython-312.pyc
|   |           |   |   |   |   |-- installation_report.cpython-312.pyc
|   |           |   |   |   |   |-- link.cpython-312.pyc
|   |           |   |   |   |   |-- pylock.cpython-312.pyc
|   |           |   |   |   |   |-- scheme.cpython-312.pyc
|   |           |   |   |   |   |-- search_scope.cpython-312.pyc
|   |           |   |   |   |   |-- selection_prefs.cpython-312.pyc
|   |           |   |   |   |   |-- target_python.cpython-312.pyc
|   |           |   |   |   |   `-- wheel.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- candidate.py
|   |           |   |   |   |-- direct_url.py
|   |           |   |   |   |-- format_control.py
|   |           |   |   |   |-- index.py
|   |           |   |   |   |-- installation_report.py
|   |           |   |   |   |-- link.py
|   |           |   |   |   |-- pylock.py
|   |           |   |   |   |-- scheme.py
|   |           |   |   |   |-- search_scope.py
|   |           |   |   |   |-- selection_prefs.py
|   |           |   |   |   |-- target_python.py
|   |           |   |   |   `-- wheel.py
|   |           |   |   |-- network
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- auth.cpython-312.pyc
|   |           |   |   |   |   |-- cache.cpython-312.pyc
|   |           |   |   |   |   |-- download.cpython-312.pyc
|   |           |   |   |   |   |-- lazy_wheel.cpython-312.pyc
|   |           |   |   |   |   |-- session.cpython-312.pyc
|   |           |   |   |   |   |-- utils.cpython-312.pyc
|   |           |   |   |   |   `-- xmlrpc.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- auth.py
|   |           |   |   |   |-- cache.py
|   |           |   |   |   |-- download.py
|   |           |   |   |   |-- lazy_wheel.py
|   |           |   |   |   |-- session.py
|   |           |   |   |   |-- utils.py
|   |           |   |   |   `-- xmlrpc.py
|   |           |   |   |-- operations
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- check.cpython-312.pyc
|   |           |   |   |   |   |-- freeze.cpython-312.pyc
|   |           |   |   |   |   `-- prepare.cpython-312.pyc
|   |           |   |   |   |-- build
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- build_tracker.cpython-312.pyc
|   |           |   |   |   |   |   |-- metadata.cpython-312.pyc
|   |           |   |   |   |   |   |-- metadata_editable.cpython-312.pyc
|   |           |   |   |   |   |   |-- metadata_legacy.cpython-312.pyc
|   |           |   |   |   |   |   |-- wheel.cpython-312.pyc
|   |           |   |   |   |   |   |-- wheel_editable.cpython-312.pyc
|   |           |   |   |   |   |   `-- wheel_legacy.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- build_tracker.py
|   |           |   |   |   |   |-- metadata.py
|   |           |   |   |   |   |-- metadata_editable.py
|   |           |   |   |   |   |-- metadata_legacy.py
|   |           |   |   |   |   |-- wheel.py
|   |           |   |   |   |   |-- wheel_editable.py
|   |           |   |   |   |   `-- wheel_legacy.py
|   |           |   |   |   |-- install
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- editable_legacy.cpython-312.pyc
|   |           |   |   |   |   |   `-- wheel.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- editable_legacy.py
|   |           |   |   |   |   `-- wheel.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- check.py
|   |           |   |   |   |-- freeze.py
|   |           |   |   |   `-- prepare.py
|   |           |   |   |-- req
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- constructors.cpython-312.pyc
|   |           |   |   |   |   |-- req_dependency_group.cpython-312.pyc
|   |           |   |   |   |   |-- req_file.cpython-312.pyc
|   |           |   |   |   |   |-- req_install.cpython-312.pyc
|   |           |   |   |   |   |-- req_set.cpython-312.pyc
|   |           |   |   |   |   `-- req_uninstall.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- constructors.py
|   |           |   |   |   |-- req_dependency_group.py
|   |           |   |   |   |-- req_file.py
|   |           |   |   |   |-- req_install.py
|   |           |   |   |   |-- req_set.py
|   |           |   |   |   `-- req_uninstall.py
|   |           |   |   |-- resolution
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   `-- base.cpython-312.pyc
|   |           |   |   |   |-- legacy
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   `-- resolver.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   `-- resolver.py
|   |           |   |   |   |-- resolvelib
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- base.cpython-312.pyc
|   |           |   |   |   |   |   |-- candidates.cpython-312.pyc
|   |           |   |   |   |   |   |-- factory.cpython-312.pyc
|   |           |   |   |   |   |   |-- found_candidates.cpython-312.pyc
|   |           |   |   |   |   |   |-- provider.cpython-312.pyc
|   |           |   |   |   |   |   |-- reporter.cpython-312.pyc
|   |           |   |   |   |   |   |-- requirements.cpython-312.pyc
|   |           |   |   |   |   |   `-- resolver.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- base.py
|   |           |   |   |   |   |-- candidates.py
|   |           |   |   |   |   |-- factory.py
|   |           |   |   |   |   |-- found_candidates.py
|   |           |   |   |   |   |-- provider.py
|   |           |   |   |   |   |-- reporter.py
|   |           |   |   |   |   |-- requirements.py
|   |           |   |   |   |   `-- resolver.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   `-- base.py
|   |           |   |   |-- utils
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- _jaraco_text.cpython-312.pyc
|   |           |   |   |   |   |-- _log.cpython-312.pyc
|   |           |   |   |   |   |-- appdirs.cpython-312.pyc
|   |           |   |   |   |   |-- compat.cpython-312.pyc
|   |           |   |   |   |   |-- compatibility_tags.cpython-312.pyc
|   |           |   |   |   |   |-- datetime.cpython-312.pyc
|   |           |   |   |   |   |-- deprecation.cpython-312.pyc
|   |           |   |   |   |   |-- direct_url_helpers.cpython-312.pyc
|   |           |   |   |   |   |-- egg_link.cpython-312.pyc
|   |           |   |   |   |   |-- entrypoints.cpython-312.pyc
|   |           |   |   |   |   |-- filesystem.cpython-312.pyc
|   |           |   |   |   |   |-- filetypes.cpython-312.pyc
|   |           |   |   |   |   |-- glibc.cpython-312.pyc
|   |           |   |   |   |   |-- hashes.cpython-312.pyc
|   |           |   |   |   |   |-- logging.cpython-312.pyc
|   |           |   |   |   |   |-- misc.cpython-312.pyc
|   |           |   |   |   |   |-- packaging.cpython-312.pyc
|   |           |   |   |   |   |-- retry.cpython-312.pyc
|   |           |   |   |   |   |-- setuptools_build.cpython-312.pyc
|   |           |   |   |   |   |-- subprocess.cpython-312.pyc
|   |           |   |   |   |   |-- temp_dir.cpython-312.pyc
|   |           |   |   |   |   |-- unpacking.cpython-312.pyc
|   |           |   |   |   |   |-- urls.cpython-312.pyc
|   |           |   |   |   |   |-- virtualenv.cpython-312.pyc
|   |           |   |   |   |   `-- wheel.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- _jaraco_text.py
|   |           |   |   |   |-- _log.py
|   |           |   |   |   |-- appdirs.py
|   |           |   |   |   |-- compat.py
|   |           |   |   |   |-- compatibility_tags.py
|   |           |   |   |   |-- datetime.py
|   |           |   |   |   |-- deprecation.py
|   |           |   |   |   |-- direct_url_helpers.py
|   |           |   |   |   |-- egg_link.py
|   |           |   |   |   |-- entrypoints.py
|   |           |   |   |   |-- filesystem.py
|   |           |   |   |   |-- filetypes.py
|   |           |   |   |   |-- glibc.py
|   |           |   |   |   |-- hashes.py
|   |           |   |   |   |-- logging.py
|   |           |   |   |   |-- misc.py
|   |           |   |   |   |-- packaging.py
|   |           |   |   |   |-- retry.py
|   |           |   |   |   |-- setuptools_build.py
|   |           |   |   |   |-- subprocess.py
|   |           |   |   |   |-- temp_dir.py
|   |           |   |   |   |-- unpacking.py
|   |           |   |   |   |-- urls.py
|   |           |   |   |   |-- virtualenv.py
|   |           |   |   |   `-- wheel.py
|   |           |   |   |-- vcs
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- bazaar.cpython-312.pyc
|   |           |   |   |   |   |-- git.cpython-312.pyc
|   |           |   |   |   |   |-- mercurial.cpython-312.pyc
|   |           |   |   |   |   |-- subversion.cpython-312.pyc
|   |           |   |   |   |   `-- versioncontrol.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- bazaar.py
|   |           |   |   |   |-- git.py
|   |           |   |   |   |-- mercurial.py
|   |           |   |   |   |-- subversion.py
|   |           |   |   |   `-- versioncontrol.py
|   |           |   |   |-- __init__.py
|   |           |   |   |-- build_env.py
|   |           |   |   |-- cache.py
|   |           |   |   |-- configuration.py
|   |           |   |   |-- exceptions.py
|   |           |   |   |-- main.py
|   |           |   |   |-- pyproject.py
|   |           |   |   |-- self_outdated_check.py
|   |           |   |   `-- wheel_builder.py
|   |           |   |-- _vendor
|   |           |   |   |-- __pycache__
|   |           |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |-- cachecontrol
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- _cmd.cpython-312.pyc
|   |           |   |   |   |   |-- adapter.cpython-312.pyc
|   |           |   |   |   |   |-- cache.cpython-312.pyc
|   |           |   |   |   |   |-- controller.cpython-312.pyc
|   |           |   |   |   |   |-- filewrapper.cpython-312.pyc
|   |           |   |   |   |   |-- heuristics.cpython-312.pyc
|   |           |   |   |   |   |-- serialize.cpython-312.pyc
|   |           |   |   |   |   `-- wrapper.cpython-312.pyc
|   |           |   |   |   |-- caches
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- file_cache.cpython-312.pyc
|   |           |   |   |   |   |   `-- redis_cache.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- file_cache.py
|   |           |   |   |   |   `-- redis_cache.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- _cmd.py
|   |           |   |   |   |-- adapter.py
|   |           |   |   |   |-- cache.py
|   |           |   |   |   |-- controller.py
|   |           |   |   |   |-- filewrapper.py
|   |           |   |   |   |-- heuristics.py
|   |           |   |   |   |-- py.typed
|   |           |   |   |   |-- serialize.py
|   |           |   |   |   `-- wrapper.py
|   |           |   |   |-- certifi
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |   |   `-- core.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- __main__.py
|   |           |   |   |   |-- cacert.pem
|   |           |   |   |   |-- core.py
|   |           |   |   |   `-- py.typed
|   |           |   |   |-- dependency_groups
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |   |   |-- _implementation.cpython-312.pyc
|   |           |   |   |   |   |-- _lint_dependency_groups.cpython-312.pyc
|   |           |   |   |   |   |-- _pip_wrapper.cpython-312.pyc
|   |           |   |   |   |   `-- _toml_compat.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- __main__.py
|   |           |   |   |   |-- _implementation.py
|   |           |   |   |   |-- _lint_dependency_groups.py
|   |           |   |   |   |-- _pip_wrapper.py
|   |           |   |   |   |-- _toml_compat.py
|   |           |   |   |   `-- py.typed
|   |           |   |   |-- distlib
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- compat.cpython-312.pyc
|   |           |   |   |   |   |-- resources.cpython-312.pyc
|   |           |   |   |   |   |-- scripts.cpython-312.pyc
|   |           |   |   |   |   `-- util.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- compat.py
|   |           |   |   |   |-- resources.py
|   |           |   |   |   |-- scripts.py
|   |           |   |   |   |-- t32.exe
|   |           |   |   |   |-- t64-arm.exe
|   |           |   |   |   |-- t64.exe
|   |           |   |   |   |-- util.py
|   |           |   |   |   |-- w32.exe
|   |           |   |   |   |-- w64-arm.exe
|   |           |   |   |   `-- w64.exe
|   |           |   |   |-- distro
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |   |   `-- distro.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- __main__.py
|   |           |   |   |   |-- distro.py
|   |           |   |   |   `-- py.typed
|   |           |   |   |-- idna
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- codec.cpython-312.pyc
|   |           |   |   |   |   |-- compat.cpython-312.pyc
|   |           |   |   |   |   |-- core.cpython-312.pyc
|   |           |   |   |   |   |-- idnadata.cpython-312.pyc
|   |           |   |   |   |   |-- intranges.cpython-312.pyc
|   |           |   |   |   |   |-- package_data.cpython-312.pyc
|   |           |   |   |   |   `-- uts46data.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- codec.py
|   |           |   |   |   |-- compat.py
|   |           |   |   |   |-- core.py
|   |           |   |   |   |-- idnadata.py
|   |           |   |   |   |-- intranges.py
|   |           |   |   |   |-- package_data.py
|   |           |   |   |   |-- py.typed
|   |           |   |   |   `-- uts46data.py
|   |           |   |   |-- msgpack
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- exceptions.cpython-312.pyc
|   |           |   |   |   |   |-- ext.cpython-312.pyc
|   |           |   |   |   |   `-- fallback.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- exceptions.py
|   |           |   |   |   |-- ext.py
|   |           |   |   |   `-- fallback.py
|   |           |   |   |-- packaging
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- _elffile.cpython-312.pyc
|   |           |   |   |   |   |-- _manylinux.cpython-312.pyc
|   |           |   |   |   |   |-- _musllinux.cpython-312.pyc
|   |           |   |   |   |   |-- _parser.cpython-312.pyc
|   |           |   |   |   |   |-- _structures.cpython-312.pyc
|   |           |   |   |   |   |-- _tokenizer.cpython-312.pyc
|   |           |   |   |   |   |-- markers.cpython-312.pyc
|   |           |   |   |   |   |-- metadata.cpython-312.pyc
|   |           |   |   |   |   |-- requirements.cpython-312.pyc
|   |           |   |   |   |   |-- specifiers.cpython-312.pyc
|   |           |   |   |   |   |-- tags.cpython-312.pyc
|   |           |   |   |   |   |-- utils.cpython-312.pyc
|   |           |   |   |   |   `-- version.cpython-312.pyc
|   |           |   |   |   |-- licenses
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   `-- _spdx.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   `-- _spdx.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- _elffile.py
|   |           |   |   |   |-- _manylinux.py
|   |           |   |   |   |-- _musllinux.py
|   |           |   |   |   |-- _parser.py
|   |           |   |   |   |-- _structures.py
|   |           |   |   |   |-- _tokenizer.py
|   |           |   |   |   |-- markers.py
|   |           |   |   |   |-- metadata.py
|   |           |   |   |   |-- py.typed
|   |           |   |   |   |-- requirements.py
|   |           |   |   |   |-- specifiers.py
|   |           |   |   |   |-- tags.py
|   |           |   |   |   |-- utils.py
|   |           |   |   |   `-- version.py
|   |           |   |   |-- pkg_resources
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- platformdirs
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |   |   |-- android.cpython-312.pyc
|   |           |   |   |   |   |-- api.cpython-312.pyc
|   |           |   |   |   |   |-- macos.cpython-312.pyc
|   |           |   |   |   |   |-- unix.cpython-312.pyc
|   |           |   |   |   |   |-- version.cpython-312.pyc
|   |           |   |   |   |   `-- windows.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- __main__.py
|   |           |   |   |   |-- android.py
|   |           |   |   |   |-- api.py
|   |           |   |   |   |-- macos.py
|   |           |   |   |   |-- py.typed
|   |           |   |   |   |-- unix.py
|   |           |   |   |   |-- version.py
|   |           |   |   |   `-- windows.py
|   |           |   |   |-- pygments
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |   |   |-- console.cpython-312.pyc
|   |           |   |   |   |   |-- filter.cpython-312.pyc
|   |           |   |   |   |   |-- formatter.cpython-312.pyc
|   |           |   |   |   |   |-- lexer.cpython-312.pyc
|   |           |   |   |   |   |-- modeline.cpython-312.pyc
|   |           |   |   |   |   |-- plugin.cpython-312.pyc
|   |           |   |   |   |   |-- regexopt.cpython-312.pyc
|   |           |   |   |   |   |-- scanner.cpython-312.pyc
|   |           |   |   |   |   |-- sphinxext.cpython-312.pyc
|   |           |   |   |   |   |-- style.cpython-312.pyc
|   |           |   |   |   |   |-- token.cpython-312.pyc
|   |           |   |   |   |   |-- unistring.cpython-312.pyc
|   |           |   |   |   |   `-- util.cpython-312.pyc
|   |           |   |   |   |-- filters
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |   `-- __init__.py
|   |           |   |   |   |-- formatters
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   `-- _mapping.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   `-- _mapping.py
|   |           |   |   |   |-- lexers
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- _mapping.cpython-312.pyc
|   |           |   |   |   |   |   `-- python.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- _mapping.py
|   |           |   |   |   |   `-- python.py
|   |           |   |   |   |-- styles
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   `-- _mapping.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   `-- _mapping.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- __main__.py
|   |           |   |   |   |-- console.py
|   |           |   |   |   |-- filter.py
|   |           |   |   |   |-- formatter.py
|   |           |   |   |   |-- lexer.py
|   |           |   |   |   |-- modeline.py
|   |           |   |   |   |-- plugin.py
|   |           |   |   |   |-- regexopt.py
|   |           |   |   |   |-- scanner.py
|   |           |   |   |   |-- sphinxext.py
|   |           |   |   |   |-- style.py
|   |           |   |   |   |-- token.py
|   |           |   |   |   |-- unistring.py
|   |           |   |   |   `-- util.py
|   |           |   |   |-- pyproject_hooks
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   `-- _impl.cpython-312.pyc
|   |           |   |   |   |-- _in_process
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   `-- _in_process.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   `-- _in_process.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- _impl.py
|   |           |   |   |   `-- py.typed
|   |           |   |   |-- requests
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- __version__.cpython-312.pyc
|   |           |   |   |   |   |-- _internal_utils.cpython-312.pyc
|   |           |   |   |   |   |-- adapters.cpython-312.pyc
|   |           |   |   |   |   |-- api.cpython-312.pyc
|   |           |   |   |   |   |-- auth.cpython-312.pyc
|   |           |   |   |   |   |-- certs.cpython-312.pyc
|   |           |   |   |   |   |-- compat.cpython-312.pyc
|   |           |   |   |   |   |-- cookies.cpython-312.pyc
|   |           |   |   |   |   |-- exceptions.cpython-312.pyc
|   |           |   |   |   |   |-- help.cpython-312.pyc
|   |           |   |   |   |   |-- hooks.cpython-312.pyc
|   |           |   |   |   |   |-- models.cpython-312.pyc
|   |           |   |   |   |   |-- packages.cpython-312.pyc
|   |           |   |   |   |   |-- sessions.cpython-312.pyc
|   |           |   |   |   |   |-- status_codes.cpython-312.pyc
|   |           |   |   |   |   |-- structures.cpython-312.pyc
|   |           |   |   |   |   `-- utils.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- __version__.py
|   |           |   |   |   |-- _internal_utils.py
|   |           |   |   |   |-- adapters.py
|   |           |   |   |   |-- api.py
|   |           |   |   |   |-- auth.py
|   |           |   |   |   |-- certs.py
|   |           |   |   |   |-- compat.py
|   |           |   |   |   |-- cookies.py
|   |           |   |   |   |-- exceptions.py
|   |           |   |   |   |-- help.py
|   |           |   |   |   |-- hooks.py
|   |           |   |   |   |-- models.py
|   |           |   |   |   |-- packages.py
|   |           |   |   |   |-- sessions.py
|   |           |   |   |   |-- status_codes.py
|   |           |   |   |   |-- structures.py
|   |           |   |   |   `-- utils.py
|   |           |   |   |-- resolvelib
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- providers.cpython-312.pyc
|   |           |   |   |   |   |-- reporters.cpython-312.pyc
|   |           |   |   |   |   `-- structs.cpython-312.pyc
|   |           |   |   |   |-- resolvers
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- abstract.cpython-312.pyc
|   |           |   |   |   |   |   |-- criterion.cpython-312.pyc
|   |           |   |   |   |   |   |-- exceptions.cpython-312.pyc
|   |           |   |   |   |   |   `-- resolution.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- abstract.py
|   |           |   |   |   |   |-- criterion.py
|   |           |   |   |   |   |-- exceptions.py
|   |           |   |   |   |   `-- resolution.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- providers.py
|   |           |   |   |   |-- py.typed
|   |           |   |   |   |-- reporters.py
|   |           |   |   |   `-- structs.py
|   |           |   |   |-- rich
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |   |   |-- _cell_widths.cpython-312.pyc
|   |           |   |   |   |   |-- _emoji_codes.cpython-312.pyc
|   |           |   |   |   |   |-- _emoji_replace.cpython-312.pyc
|   |           |   |   |   |   |-- _export_format.cpython-312.pyc
|   |           |   |   |   |   |-- _extension.cpython-312.pyc
|   |           |   |   |   |   |-- _fileno.cpython-312.pyc
|   |           |   |   |   |   |-- _inspect.cpython-312.pyc
|   |           |   |   |   |   |-- _log_render.cpython-312.pyc
|   |           |   |   |   |   |-- _loop.cpython-312.pyc
|   |           |   |   |   |   |-- _null_file.cpython-312.pyc
|   |           |   |   |   |   |-- _palettes.cpython-312.pyc
|   |           |   |   |   |   |-- _pick.cpython-312.pyc
|   |           |   |   |   |   |-- _ratio.cpython-312.pyc
|   |           |   |   |   |   |-- _spinners.cpython-312.pyc
|   |           |   |   |   |   |-- _stack.cpython-312.pyc
|   |           |   |   |   |   |-- _timer.cpython-312.pyc
|   |           |   |   |   |   |-- _win32_console.cpython-312.pyc
|   |           |   |   |   |   |-- _windows.cpython-312.pyc
|   |           |   |   |   |   |-- _windows_renderer.cpython-312.pyc
|   |           |   |   |   |   |-- _wrap.cpython-312.pyc
|   |           |   |   |   |   |-- abc.cpython-312.pyc
|   |           |   |   |   |   |-- align.cpython-312.pyc
|   |           |   |   |   |   |-- ansi.cpython-312.pyc
|   |           |   |   |   |   |-- bar.cpython-312.pyc
|   |           |   |   |   |   |-- box.cpython-312.pyc
|   |           |   |   |   |   |-- cells.cpython-312.pyc
|   |           |   |   |   |   |-- color.cpython-312.pyc
|   |           |   |   |   |   |-- color_triplet.cpython-312.pyc
|   |           |   |   |   |   |-- columns.cpython-312.pyc
|   |           |   |   |   |   |-- console.cpython-312.pyc
|   |           |   |   |   |   |-- constrain.cpython-312.pyc
|   |           |   |   |   |   |-- containers.cpython-312.pyc
|   |           |   |   |   |   |-- control.cpython-312.pyc
|   |           |   |   |   |   |-- default_styles.cpython-312.pyc
|   |           |   |   |   |   |-- diagnose.cpython-312.pyc
|   |           |   |   |   |   |-- emoji.cpython-312.pyc
|   |           |   |   |   |   |-- errors.cpython-312.pyc
|   |           |   |   |   |   |-- file_proxy.cpython-312.pyc
|   |           |   |   |   |   |-- filesize.cpython-312.pyc
|   |           |   |   |   |   |-- highlighter.cpython-312.pyc
|   |           |   |   |   |   |-- json.cpython-312.pyc
|   |           |   |   |   |   |-- jupyter.cpython-312.pyc
|   |           |   |   |   |   |-- layout.cpython-312.pyc
|   |           |   |   |   |   |-- live.cpython-312.pyc
|   |           |   |   |   |   |-- live_render.cpython-312.pyc
|   |           |   |   |   |   |-- logging.cpython-312.pyc
|   |           |   |   |   |   |-- markup.cpython-312.pyc
|   |           |   |   |   |   |-- measure.cpython-312.pyc
|   |           |   |   |   |   |-- padding.cpython-312.pyc
|   |           |   |   |   |   |-- pager.cpython-312.pyc
|   |           |   |   |   |   |-- palette.cpython-312.pyc
|   |           |   |   |   |   |-- panel.cpython-312.pyc
|   |           |   |   |   |   |-- pretty.cpython-312.pyc
|   |           |   |   |   |   |-- progress.cpython-312.pyc
|   |           |   |   |   |   |-- progress_bar.cpython-312.pyc
|   |           |   |   |   |   |-- prompt.cpython-312.pyc
|   |           |   |   |   |   |-- protocol.cpython-312.pyc
|   |           |   |   |   |   |-- region.cpython-312.pyc
|   |           |   |   |   |   |-- repr.cpython-312.pyc
|   |           |   |   |   |   |-- rule.cpython-312.pyc
|   |           |   |   |   |   |-- scope.cpython-312.pyc
|   |           |   |   |   |   |-- screen.cpython-312.pyc
|   |           |   |   |   |   |-- segment.cpython-312.pyc
|   |           |   |   |   |   |-- spinner.cpython-312.pyc
|   |           |   |   |   |   |-- status.cpython-312.pyc
|   |           |   |   |   |   |-- style.cpython-312.pyc
|   |           |   |   |   |   |-- styled.cpython-312.pyc
|   |           |   |   |   |   |-- syntax.cpython-312.pyc
|   |           |   |   |   |   |-- table.cpython-312.pyc
|   |           |   |   |   |   |-- terminal_theme.cpython-312.pyc
|   |           |   |   |   |   |-- text.cpython-312.pyc
|   |           |   |   |   |   |-- theme.cpython-312.pyc
|   |           |   |   |   |   |-- themes.cpython-312.pyc
|   |           |   |   |   |   `-- traceback.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- __main__.py
|   |           |   |   |   |-- _cell_widths.py
|   |           |   |   |   |-- _emoji_codes.py
|   |           |   |   |   |-- _emoji_replace.py
|   |           |   |   |   |-- _export_format.py
|   |           |   |   |   |-- _extension.py
|   |           |   |   |   |-- _fileno.py
|   |           |   |   |   |-- _inspect.py
|   |           |   |   |   |-- _log_render.py
|   |           |   |   |   |-- _loop.py
|   |           |   |   |   |-- _null_file.py
|   |           |   |   |   |-- _palettes.py
|   |           |   |   |   |-- _pick.py
|   |           |   |   |   |-- _ratio.py
|   |           |   |   |   |-- _spinners.py
|   |           |   |   |   |-- _stack.py
|   |           |   |   |   |-- _timer.py
|   |           |   |   |   |-- _win32_console.py
|   |           |   |   |   |-- _windows.py
|   |           |   |   |   |-- _windows_renderer.py
|   |           |   |   |   |-- _wrap.py
|   |           |   |   |   |-- abc.py
|   |           |   |   |   |-- align.py
|   |           |   |   |   |-- ansi.py
|   |           |   |   |   |-- bar.py
|   |           |   |   |   |-- box.py
|   |           |   |   |   |-- cells.py
|   |           |   |   |   |-- color.py
|   |           |   |   |   |-- color_triplet.py
|   |           |   |   |   |-- columns.py
|   |           |   |   |   |-- console.py
|   |           |   |   |   |-- constrain.py
|   |           |   |   |   |-- containers.py
|   |           |   |   |   |-- control.py
|   |           |   |   |   |-- default_styles.py
|   |           |   |   |   |-- diagnose.py
|   |           |   |   |   |-- emoji.py
|   |           |   |   |   |-- errors.py
|   |           |   |   |   |-- file_proxy.py
|   |           |   |   |   |-- filesize.py
|   |           |   |   |   |-- highlighter.py
|   |           |   |   |   |-- json.py
|   |           |   |   |   |-- jupyter.py
|   |           |   |   |   |-- layout.py
|   |           |   |   |   |-- live.py
|   |           |   |   |   |-- live_render.py
|   |           |   |   |   |-- logging.py
|   |           |   |   |   |-- markup.py
|   |           |   |   |   |-- measure.py
|   |           |   |   |   |-- padding.py
|   |           |   |   |   |-- pager.py
|   |           |   |   |   |-- palette.py
|   |           |   |   |   |-- panel.py
|   |           |   |   |   |-- pretty.py
|   |           |   |   |   |-- progress.py
|   |           |   |   |   |-- progress_bar.py
|   |           |   |   |   |-- prompt.py
|   |           |   |   |   |-- protocol.py
|   |           |   |   |   |-- py.typed
|   |           |   |   |   |-- region.py
|   |           |   |   |   |-- repr.py
|   |           |   |   |   |-- rule.py
|   |           |   |   |   |-- scope.py
|   |           |   |   |   |-- screen.py
|   |           |   |   |   |-- segment.py
|   |           |   |   |   |-- spinner.py
|   |           |   |   |   |-- status.py
|   |           |   |   |   |-- style.py
|   |           |   |   |   |-- styled.py
|   |           |   |   |   |-- syntax.py
|   |           |   |   |   |-- table.py
|   |           |   |   |   |-- terminal_theme.py
|   |           |   |   |   |-- text.py
|   |           |   |   |   |-- theme.py
|   |           |   |   |   |-- themes.py
|   |           |   |   |   |-- traceback.py
|   |           |   |   |   `-- tree.py
|   |           |   |   |-- tomli
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- _parser.py
|   |           |   |   |   |-- _re.py
|   |           |   |   |   |-- _types.py
|   |           |   |   |   `-- py.typed
|   |           |   |   |-- tomli_w
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- _writer.py
|   |           |   |   |   `-- py.typed
|   |           |   |   |-- truststore
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- _api.cpython-312.pyc
|   |           |   |   |   |   |-- _openssl.cpython-312.pyc
|   |           |   |   |   |   `-- _ssl_constants.cpython-312.pyc
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- _api.py
|   |           |   |   |   |-- _macos.py
|   |           |   |   |   |-- _openssl.py
|   |           |   |   |   |-- _ssl_constants.py
|   |           |   |   |   |-- _windows.py
|   |           |   |   |   `-- py.typed
|   |           |   |   |-- urllib3
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- _collections.cpython-312.pyc
|   |           |   |   |   |   |-- _version.cpython-312.pyc
|   |           |   |   |   |   |-- connection.cpython-312.pyc
|   |           |   |   |   |   |-- connectionpool.cpython-312.pyc
|   |           |   |   |   |   |-- exceptions.cpython-312.pyc
|   |           |   |   |   |   |-- fields.cpython-312.pyc
|   |           |   |   |   |   |-- filepost.cpython-312.pyc
|   |           |   |   |   |   |-- poolmanager.cpython-312.pyc
|   |           |   |   |   |   |-- request.cpython-312.pyc
|   |           |   |   |   |   `-- response.cpython-312.pyc
|   |           |   |   |   |-- contrib
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- _appengine_environ.cpython-312.pyc
|   |           |   |   |   |   |   `-- socks.cpython-312.pyc
|   |           |   |   |   |   |-- _securetransport
|   |           |   |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |   |-- bindings.py
|   |           |   |   |   |   |   `-- low_level.py
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- _appengine_environ.py
|   |           |   |   |   |   |-- appengine.py
|   |           |   |   |   |   |-- ntlmpool.py
|   |           |   |   |   |   |-- pyopenssl.py
|   |           |   |   |   |   |-- securetransport.py
|   |           |   |   |   |   `-- socks.py
|   |           |   |   |   |-- packages
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   `-- six.cpython-312.pyc
|   |           |   |   |   |   |-- backports
|   |           |   |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |   |-- makefile.py
|   |           |   |   |   |   |   `-- weakref_finalize.py
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   `-- six.py
|   |           |   |   |   |-- util
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |   |   |-- connection.cpython-312.pyc
|   |           |   |   |   |   |   |-- proxy.cpython-312.pyc
|   |           |   |   |   |   |   |-- queue.cpython-312.pyc
|   |           |   |   |   |   |   |-- request.cpython-312.pyc
|   |           |   |   |   |   |   |-- response.cpython-312.pyc
|   |           |   |   |   |   |   |-- retry.cpython-312.pyc
|   |           |   |   |   |   |   |-- ssl_.cpython-312.pyc
|   |           |   |   |   |   |   |-- ssl_match_hostname.cpython-312.pyc
|   |           |   |   |   |   |   |-- ssltransport.cpython-312.pyc
|   |           |   |   |   |   |   |-- timeout.cpython-312.pyc
|   |           |   |   |   |   |   |-- url.cpython-312.pyc
|   |           |   |   |   |   |   `-- wait.cpython-312.pyc
|   |           |   |   |   |   |-- __init__.py
|   |           |   |   |   |   |-- connection.py
|   |           |   |   |   |   |-- proxy.py
|   |           |   |   |   |   |-- queue.py
|   |           |   |   |   |   |-- request.py
|   |           |   |   |   |   |-- response.py
|   |           |   |   |   |   |-- retry.py
|   |           |   |   |   |   |-- ssl_.py
|   |           |   |   |   |   |-- ssl_match_hostname.py
|   |           |   |   |   |   |-- ssltransport.py
|   |           |   |   |   |   |-- timeout.py
|   |           |   |   |   |   |-- url.py
|   |           |   |   |   |   `-- wait.py
|   |           |   |   |   |-- __init__.py
|   |           |   |   |   |-- _collections.py
|   |           |   |   |   |-- _version.py
|   |           |   |   |   |-- connection.py
|   |           |   |   |   |-- connectionpool.py
|   |           |   |   |   |-- exceptions.py
|   |           |   |   |   |-- fields.py
|   |           |   |   |   |-- filepost.py
|   |           |   |   |   |-- poolmanager.py
|   |           |   |   |   |-- request.py
|   |           |   |   |   `-- response.py
|   |           |   |   |-- __init__.py
|   |           |   |   `-- vendor.txt
|   |           |   |-- __init__.py
|   |           |   |-- __main__.py
|   |           |   |-- __pip-runner__.py
|   |           |   `-- py.typed
|   |           |-- pip-25.2.dist-info
|   |           |   |-- licenses
|   |           |   |   |-- src
|   |           |   |   |   `-- pip
|   |           |   |   |       `-- _vendor
|   |           |   |   |           |-- cachecontrol
|   |           |   |   |           |   `-- LICENSE.txt
|   |           |   |   |           |-- certifi
|   |           |   |   |           |   `-- LICENSE
|   |           |   |   |           |-- dependency_groups
|   |           |   |   |           |   `-- LICENSE.txt
|   |           |   |   |           |-- distlib
|   |           |   |   |           |   `-- LICENSE.txt
|   |           |   |   |           |-- distro
|   |           |   |   |           |   `-- LICENSE
|   |           |   |   |           |-- idna
|   |           |   |   |           |   `-- LICENSE.md
|   |           |   |   |           |-- msgpack
|   |           |   |   |           |   `-- COPYING
|   |           |   |   |           |-- packaging
|   |           |   |   |           |   |-- LICENSE
|   |           |   |   |           |   |-- LICENSE.APACHE
|   |           |   |   |           |   `-- LICENSE.BSD
|   |           |   |   |           |-- pkg_resources
|   |           |   |   |           |   `-- LICENSE
|   |           |   |   |           |-- platformdirs
|   |           |   |   |           |   `-- LICENSE
|   |           |   |   |           |-- pygments
|   |           |   |   |           |   `-- LICENSE
|   |           |   |   |           |-- pyproject_hooks
|   |           |   |   |           |   `-- LICENSE
|   |           |   |   |           |-- requests
|   |           |   |   |           |   `-- LICENSE
|   |           |   |   |           |-- resolvelib
|   |           |   |   |           |   `-- LICENSE
|   |           |   |   |           |-- rich
|   |           |   |   |           |   `-- LICENSE
|   |           |   |   |           |-- tomli
|   |           |   |   |           |   |-- LICENSE
|   |           |   |   |           |   `-- LICENSE-HEADER
|   |           |   |   |           |-- tomli_w
|   |           |   |   |           |   `-- LICENSE
|   |           |   |   |           |-- truststore
|   |           |   |   |           |   `-- LICENSE
|   |           |   |   |           `-- urllib3
|   |           |   |   |               `-- LICENSE.txt
|   |           |   |   |-- AUTHORS.txt
|   |           |   |   `-- LICENSE.txt
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   |-- WHEEL
|   |           |   |-- entry_points.txt
|   |           |   `-- top_level.txt
|   |           |-- pluggy
|   |           |   |-- __pycache__
|   |           |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |-- _callers.cpython-312.pyc
|   |           |   |   |-- _hooks.cpython-312.pyc
|   |           |   |   |-- _manager.cpython-312.pyc
|   |           |   |   |-- _result.cpython-312.pyc
|   |           |   |   |-- _tracing.cpython-312.pyc
|   |           |   |   |-- _version.cpython-312.pyc
|   |           |   |   `-- _warnings.cpython-312.pyc
|   |           |   |-- __init__.py
|   |           |   |-- _callers.py
|   |           |   |-- _hooks.py
|   |           |   |-- _manager.py
|   |           |   |-- _result.py
|   |           |   |-- _tracing.py
|   |           |   |-- _version.py
|   |           |   |-- _warnings.py
|   |           |   `-- py.typed
|   |           |-- pluggy-1.6.0.dist-info
|   |           |   |-- licenses
|   |           |   |   `-- LICENSE
|   |           |   |-- INSTALLER
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   |-- WHEEL
|   |           |   `-- top_level.txt
|   |           |-- pygments
|   |           |   |-- __pycache__
|   |           |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |-- cmdline.cpython-312.pyc
|   |           |   |   |-- console.cpython-312.pyc
|   |           |   |   |-- filter.cpython-312.pyc
|   |           |   |   |-- formatter.cpython-312.pyc
|   |           |   |   |-- lexer.cpython-312.pyc
|   |           |   |   |-- modeline.cpython-312.pyc
|   |           |   |   |-- plugin.cpython-312.pyc
|   |           |   |   |-- regexopt.cpython-312.pyc
|   |           |   |   |-- scanner.cpython-312.pyc
|   |           |   |   |-- sphinxext.cpython-312.pyc
|   |           |   |   |-- style.cpython-312.pyc
|   |           |   |   |-- token.cpython-312.pyc
|   |           |   |   |-- unistring.cpython-312.pyc
|   |           |   |   `-- util.cpython-312.pyc
|   |           |   |-- filters
|   |           |   |   |-- __pycache__
|   |           |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   `-- __init__.py
|   |           |   |-- formatters
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _mapping.cpython-312.pyc
|   |           |   |   |   |-- bbcode.cpython-312.pyc
|   |           |   |   |   |-- groff.cpython-312.pyc
|   |           |   |   |   |-- html.cpython-312.pyc
|   |           |   |   |   |-- img.cpython-312.pyc
|   |           |   |   |   |-- irc.cpython-312.pyc
|   |           |   |   |   |-- latex.cpython-312.pyc
|   |           |   |   |   |-- other.cpython-312.pyc
|   |           |   |   |   |-- pangomarkup.cpython-312.pyc
|   |           |   |   |   |-- rtf.cpython-312.pyc
|   |           |   |   |   |-- svg.cpython-312.pyc
|   |           |   |   |   |-- terminal.cpython-312.pyc
|   |           |   |   |   `-- terminal256.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- _mapping.py
|   |           |   |   |-- bbcode.py
|   |           |   |   |-- groff.py
|   |           |   |   |-- html.py
|   |           |   |   |-- img.py
|   |           |   |   |-- irc.py
|   |           |   |   |-- latex.py
|   |           |   |   |-- other.py
|   |           |   |   |-- pangomarkup.py
|   |           |   |   |-- rtf.py
|   |           |   |   |-- svg.py
|   |           |   |   |-- terminal.py
|   |           |   |   `-- terminal256.py
|   |           |   |-- lexers
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _ada_builtins.cpython-312.pyc
|   |           |   |   |   |-- _asy_builtins.cpython-312.pyc
|   |           |   |   |   |-- _cl_builtins.cpython-312.pyc
|   |           |   |   |   |-- _cocoa_builtins.cpython-312.pyc
|   |           |   |   |   |-- _csound_builtins.cpython-312.pyc
|   |           |   |   |   |-- _css_builtins.cpython-312.pyc
|   |           |   |   |   |-- _googlesql_builtins.cpython-312.pyc
|   |           |   |   |   |-- _julia_builtins.cpython-312.pyc
|   |           |   |   |   |-- _lasso_builtins.cpython-312.pyc
|   |           |   |   |   |-- _lilypond_builtins.cpython-312.pyc
|   |           |   |   |   |-- _lua_builtins.cpython-312.pyc
|   |           |   |   |   |-- _luau_builtins.cpython-312.pyc
|   |           |   |   |   |-- _mapping.cpython-312.pyc
|   |           |   |   |   |-- _mql_builtins.cpython-312.pyc
|   |           |   |   |   |-- _mysql_builtins.cpython-312.pyc
|   |           |   |   |   |-- _openedge_builtins.cpython-312.pyc
|   |           |   |   |   |-- _php_builtins.cpython-312.pyc
|   |           |   |   |   |-- _postgres_builtins.cpython-312.pyc
|   |           |   |   |   |-- _qlik_builtins.cpython-312.pyc
|   |           |   |   |   |-- _scheme_builtins.cpython-312.pyc
|   |           |   |   |   |-- _scilab_builtins.cpython-312.pyc
|   |           |   |   |   |-- _sourcemod_builtins.cpython-312.pyc
|   |           |   |   |   |-- _sql_builtins.cpython-312.pyc
|   |           |   |   |   |-- _stan_builtins.cpython-312.pyc
|   |           |   |   |   |-- _stata_builtins.cpython-312.pyc
|   |           |   |   |   |-- _tsql_builtins.cpython-312.pyc
|   |           |   |   |   |-- _usd_builtins.cpython-312.pyc
|   |           |   |   |   |-- _vbscript_builtins.cpython-312.pyc
|   |           |   |   |   |-- _vim_builtins.cpython-312.pyc
|   |           |   |   |   |-- actionscript.cpython-312.pyc
|   |           |   |   |   |-- ada.cpython-312.pyc
|   |           |   |   |   |-- agile.cpython-312.pyc
|   |           |   |   |   |-- algebra.cpython-312.pyc
|   |           |   |   |   |-- ambient.cpython-312.pyc
|   |           |   |   |   |-- amdgpu.cpython-312.pyc
|   |           |   |   |   |-- ampl.cpython-312.pyc
|   |           |   |   |   |-- apdlexer.cpython-312.pyc
|   |           |   |   |   |-- apl.cpython-312.pyc
|   |           |   |   |   |-- archetype.cpython-312.pyc
|   |           |   |   |   |-- arrow.cpython-312.pyc
|   |           |   |   |   |-- arturo.cpython-312.pyc
|   |           |   |   |   |-- asc.cpython-312.pyc
|   |           |   |   |   |-- asm.cpython-312.pyc
|   |           |   |   |   |-- asn1.cpython-312.pyc
|   |           |   |   |   |-- automation.cpython-312.pyc
|   |           |   |   |   |-- bare.cpython-312.pyc
|   |           |   |   |   |-- basic.cpython-312.pyc
|   |           |   |   |   |-- bdd.cpython-312.pyc
|   |           |   |   |   |-- berry.cpython-312.pyc
|   |           |   |   |   |-- bibtex.cpython-312.pyc
|   |           |   |   |   |-- blueprint.cpython-312.pyc
|   |           |   |   |   |-- boa.cpython-312.pyc
|   |           |   |   |   |-- bqn.cpython-312.pyc
|   |           |   |   |   |-- business.cpython-312.pyc
|   |           |   |   |   |-- c_cpp.cpython-312.pyc
|   |           |   |   |   |-- c_like.cpython-312.pyc
|   |           |   |   |   |-- capnproto.cpython-312.pyc
|   |           |   |   |   |-- carbon.cpython-312.pyc
|   |           |   |   |   |-- cddl.cpython-312.pyc
|   |           |   |   |   |-- chapel.cpython-312.pyc
|   |           |   |   |   |-- clean.cpython-312.pyc
|   |           |   |   |   |-- codeql.cpython-312.pyc
|   |           |   |   |   |-- comal.cpython-312.pyc
|   |           |   |   |   |-- compiled.cpython-312.pyc
|   |           |   |   |   |-- configs.cpython-312.pyc
|   |           |   |   |   |-- console.cpython-312.pyc
|   |           |   |   |   |-- cplint.cpython-312.pyc
|   |           |   |   |   |-- crystal.cpython-312.pyc
|   |           |   |   |   |-- csound.cpython-312.pyc
|   |           |   |   |   |-- css.cpython-312.pyc
|   |           |   |   |   |-- d.cpython-312.pyc
|   |           |   |   |   |-- dalvik.cpython-312.pyc
|   |           |   |   |   |-- data.cpython-312.pyc
|   |           |   |   |   |-- dax.cpython-312.pyc
|   |           |   |   |   |-- devicetree.cpython-312.pyc
|   |           |   |   |   |-- diff.cpython-312.pyc
|   |           |   |   |   |-- dns.cpython-312.pyc
|   |           |   |   |   |-- dotnet.cpython-312.pyc
|   |           |   |   |   |-- dsls.cpython-312.pyc
|   |           |   |   |   |-- dylan.cpython-312.pyc
|   |           |   |   |   |-- ecl.cpython-312.pyc
|   |           |   |   |   |-- eiffel.cpython-312.pyc
|   |           |   |   |   |-- elm.cpython-312.pyc
|   |           |   |   |   |-- elpi.cpython-312.pyc
|   |           |   |   |   |-- email.cpython-312.pyc
|   |           |   |   |   |-- erlang.cpython-312.pyc
|   |           |   |   |   |-- esoteric.cpython-312.pyc
|   |           |   |   |   |-- ezhil.cpython-312.pyc
|   |           |   |   |   |-- factor.cpython-312.pyc
|   |           |   |   |   |-- fantom.cpython-312.pyc
|   |           |   |   |   |-- felix.cpython-312.pyc
|   |           |   |   |   |-- fift.cpython-312.pyc
|   |           |   |   |   |-- floscript.cpython-312.pyc
|   |           |   |   |   |-- forth.cpython-312.pyc
|   |           |   |   |   |-- fortran.cpython-312.pyc
|   |           |   |   |   |-- foxpro.cpython-312.pyc
|   |           |   |   |   |-- freefem.cpython-312.pyc
|   |           |   |   |   |-- func.cpython-312.pyc
|   |           |   |   |   |-- functional.cpython-312.pyc
|   |           |   |   |   |-- futhark.cpython-312.pyc
|   |           |   |   |   |-- gcodelexer.cpython-312.pyc
|   |           |   |   |   |-- gdscript.cpython-312.pyc
|   |           |   |   |   |-- gleam.cpython-312.pyc
|   |           |   |   |   |-- go.cpython-312.pyc
|   |           |   |   |   |-- grammar_notation.cpython-312.pyc
|   |           |   |   |   |-- graph.cpython-312.pyc
|   |           |   |   |   |-- graphics.cpython-312.pyc
|   |           |   |   |   |-- graphql.cpython-312.pyc
|   |           |   |   |   |-- graphviz.cpython-312.pyc
|   |           |   |   |   |-- gsql.cpython-312.pyc
|   |           |   |   |   |-- hare.cpython-312.pyc
|   |           |   |   |   |-- haskell.cpython-312.pyc
|   |           |   |   |   |-- haxe.cpython-312.pyc
|   |           |   |   |   |-- hdl.cpython-312.pyc
|   |           |   |   |   |-- hexdump.cpython-312.pyc
|   |           |   |   |   |-- html.cpython-312.pyc
|   |           |   |   |   |-- idl.cpython-312.pyc
|   |           |   |   |   |-- igor.cpython-312.pyc
|   |           |   |   |   |-- inferno.cpython-312.pyc
|   |           |   |   |   |-- installers.cpython-312.pyc
|   |           |   |   |   |-- int_fiction.cpython-312.pyc
|   |           |   |   |   |-- iolang.cpython-312.pyc
|   |           |   |   |   |-- j.cpython-312.pyc
|   |           |   |   |   |-- javascript.cpython-312.pyc
|   |           |   |   |   |-- jmespath.cpython-312.pyc
|   |           |   |   |   |-- jslt.cpython-312.pyc
|   |           |   |   |   |-- json5.cpython-312.pyc
|   |           |   |   |   |-- jsonnet.cpython-312.pyc
|   |           |   |   |   |-- jsx.cpython-312.pyc
|   |           |   |   |   |-- julia.cpython-312.pyc
|   |           |   |   |   |-- jvm.cpython-312.pyc
|   |           |   |   |   |-- kuin.cpython-312.pyc
|   |           |   |   |   |-- kusto.cpython-312.pyc
|   |           |   |   |   |-- ldap.cpython-312.pyc
|   |           |   |   |   |-- lean.cpython-312.pyc
|   |           |   |   |   |-- lilypond.cpython-312.pyc
|   |           |   |   |   |-- lisp.cpython-312.pyc
|   |           |   |   |   |-- macaulay2.cpython-312.pyc
|   |           |   |   |   |-- make.cpython-312.pyc
|   |           |   |   |   |-- maple.cpython-312.pyc
|   |           |   |   |   |-- markup.cpython-312.pyc
|   |           |   |   |   |-- math.cpython-312.pyc
|   |           |   |   |   |-- matlab.cpython-312.pyc
|   |           |   |   |   |-- maxima.cpython-312.pyc
|   |           |   |   |   |-- meson.cpython-312.pyc
|   |           |   |   |   |-- mime.cpython-312.pyc
|   |           |   |   |   |-- minecraft.cpython-312.pyc
|   |           |   |   |   |-- mips.cpython-312.pyc
|   |           |   |   |   |-- ml.cpython-312.pyc
|   |           |   |   |   |-- modeling.cpython-312.pyc
|   |           |   |   |   |-- modula2.cpython-312.pyc
|   |           |   |   |   |-- mojo.cpython-312.pyc
|   |           |   |   |   |-- monte.cpython-312.pyc
|   |           |   |   |   |-- mosel.cpython-312.pyc
|   |           |   |   |   |-- ncl.cpython-312.pyc
|   |           |   |   |   |-- nimrod.cpython-312.pyc
|   |           |   |   |   |-- nit.cpython-312.pyc
|   |           |   |   |   |-- nix.cpython-312.pyc
|   |           |   |   |   |-- numbair.cpython-312.pyc
|   |           |   |   |   |-- oberon.cpython-312.pyc
|   |           |   |   |   |-- objective.cpython-312.pyc
|   |           |   |   |   |-- ooc.cpython-312.pyc
|   |           |   |   |   |-- openscad.cpython-312.pyc
|   |           |   |   |   |-- other.cpython-312.pyc
|   |           |   |   |   |-- parasail.cpython-312.pyc
|   |           |   |   |   |-- parsers.cpython-312.pyc
|   |           |   |   |   |-- pascal.cpython-312.pyc
|   |           |   |   |   |-- pawn.cpython-312.pyc
|   |           |   |   |   |-- pddl.cpython-312.pyc
|   |           |   |   |   |-- perl.cpython-312.pyc
|   |           |   |   |   |-- phix.cpython-312.pyc
|   |           |   |   |   |-- php.cpython-312.pyc
|   |           |   |   |   |-- pointless.cpython-312.pyc
|   |           |   |   |   |-- pony.cpython-312.pyc
|   |           |   |   |   |-- praat.cpython-312.pyc
|   |           |   |   |   |-- procfile.cpython-312.pyc
|   |           |   |   |   |-- prolog.cpython-312.pyc
|   |           |   |   |   |-- promql.cpython-312.pyc
|   |           |   |   |   |-- prql.cpython-312.pyc
|   |           |   |   |   |-- ptx.cpython-312.pyc
|   |           |   |   |   |-- python.cpython-312.pyc
|   |           |   |   |   |-- q.cpython-312.pyc
|   |           |   |   |   |-- qlik.cpython-312.pyc
|   |           |   |   |   |-- qvt.cpython-312.pyc
|   |           |   |   |   |-- r.cpython-312.pyc
|   |           |   |   |   |-- rdf.cpython-312.pyc
|   |           |   |   |   |-- rebol.cpython-312.pyc
|   |           |   |   |   |-- rego.cpython-312.pyc
|   |           |   |   |   |-- resource.cpython-312.pyc
|   |           |   |   |   |-- ride.cpython-312.pyc
|   |           |   |   |   |-- rita.cpython-312.pyc
|   |           |   |   |   |-- rnc.cpython-312.pyc
|   |           |   |   |   |-- roboconf.cpython-312.pyc
|   |           |   |   |   |-- robotframework.cpython-312.pyc
|   |           |   |   |   |-- ruby.cpython-312.pyc
|   |           |   |   |   |-- rust.cpython-312.pyc
|   |           |   |   |   |-- sas.cpython-312.pyc
|   |           |   |   |   |-- savi.cpython-312.pyc
|   |           |   |   |   |-- scdoc.cpython-312.pyc
|   |           |   |   |   |-- scripting.cpython-312.pyc
|   |           |   |   |   |-- sgf.cpython-312.pyc
|   |           |   |   |   |-- shell.cpython-312.pyc
|   |           |   |   |   |-- sieve.cpython-312.pyc
|   |           |   |   |   |-- slash.cpython-312.pyc
|   |           |   |   |   |-- smalltalk.cpython-312.pyc
|   |           |   |   |   |-- smithy.cpython-312.pyc
|   |           |   |   |   |-- smv.cpython-312.pyc
|   |           |   |   |   |-- snobol.cpython-312.pyc
|   |           |   |   |   |-- solidity.cpython-312.pyc
|   |           |   |   |   |-- soong.cpython-312.pyc
|   |           |   |   |   |-- sophia.cpython-312.pyc
|   |           |   |   |   |-- special.cpython-312.pyc
|   |           |   |   |   |-- spice.cpython-312.pyc
|   |           |   |   |   |-- sql.cpython-312.pyc
|   |           |   |   |   |-- srcinfo.cpython-312.pyc
|   |           |   |   |   |-- stata.cpython-312.pyc
|   |           |   |   |   |-- supercollider.cpython-312.pyc
|   |           |   |   |   |-- tablegen.cpython-312.pyc
|   |           |   |   |   |-- tact.cpython-312.pyc
|   |           |   |   |   |-- tal.cpython-312.pyc
|   |           |   |   |   |-- tcl.cpython-312.pyc
|   |           |   |   |   |-- teal.cpython-312.pyc
|   |           |   |   |   |-- templates.cpython-312.pyc
|   |           |   |   |   |-- teraterm.cpython-312.pyc
|   |           |   |   |   |-- testing.cpython-312.pyc
|   |           |   |   |   |-- text.cpython-312.pyc
|   |           |   |   |   |-- textedit.cpython-312.pyc
|   |           |   |   |   |-- textfmts.cpython-312.pyc
|   |           |   |   |   |-- theorem.cpython-312.pyc
|   |           |   |   |   |-- thingsdb.cpython-312.pyc
|   |           |   |   |   |-- tlb.cpython-312.pyc
|   |           |   |   |   |-- tls.cpython-312.pyc
|   |           |   |   |   |-- tnt.cpython-312.pyc
|   |           |   |   |   |-- trafficscript.cpython-312.pyc
|   |           |   |   |   |-- typoscript.cpython-312.pyc
|   |           |   |   |   |-- typst.cpython-312.pyc
|   |           |   |   |   |-- ul4.cpython-312.pyc
|   |           |   |   |   |-- unicon.cpython-312.pyc
|   |           |   |   |   |-- urbi.cpython-312.pyc
|   |           |   |   |   |-- usd.cpython-312.pyc
|   |           |   |   |   |-- varnish.cpython-312.pyc
|   |           |   |   |   |-- verification.cpython-312.pyc
|   |           |   |   |   |-- verifpal.cpython-312.pyc
|   |           |   |   |   |-- vip.cpython-312.pyc
|   |           |   |   |   |-- vyper.cpython-312.pyc
|   |           |   |   |   |-- web.cpython-312.pyc
|   |           |   |   |   |-- webassembly.cpython-312.pyc
|   |           |   |   |   |-- webidl.cpython-312.pyc
|   |           |   |   |   |-- webmisc.cpython-312.pyc
|   |           |   |   |   |-- wgsl.cpython-312.pyc
|   |           |   |   |   |-- whiley.cpython-312.pyc
|   |           |   |   |   |-- wowtoc.cpython-312.pyc
|   |           |   |   |   |-- wren.cpython-312.pyc
|   |           |   |   |   |-- x10.cpython-312.pyc
|   |           |   |   |   |-- xorg.cpython-312.pyc
|   |           |   |   |   |-- yang.cpython-312.pyc
|   |           |   |   |   |-- yara.cpython-312.pyc
|   |           |   |   |   `-- zig.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- _ada_builtins.py
|   |           |   |   |-- _asy_builtins.py
|   |           |   |   |-- _cl_builtins.py
|   |           |   |   |-- _cocoa_builtins.py
|   |           |   |   |-- _csound_builtins.py
|   |           |   |   |-- _css_builtins.py
|   |           |   |   |-- _googlesql_builtins.py
|   |           |   |   |-- _julia_builtins.py
|   |           |   |   |-- _lasso_builtins.py
|   |           |   |   |-- _lilypond_builtins.py
|   |           |   |   |-- _lua_builtins.py
|   |           |   |   |-- _luau_builtins.py
|   |           |   |   |-- _mapping.py
|   |           |   |   |-- _mql_builtins.py
|   |           |   |   |-- _mysql_builtins.py
|   |           |   |   |-- _openedge_builtins.py
|   |           |   |   |-- _php_builtins.py
|   |           |   |   |-- _postgres_builtins.py
|   |           |   |   |-- _qlik_builtins.py
|   |           |   |   |-- _scheme_builtins.py
|   |           |   |   |-- _scilab_builtins.py
|   |           |   |   |-- _sourcemod_builtins.py
|   |           |   |   |-- _sql_builtins.py
|   |           |   |   |-- _stan_builtins.py
|   |           |   |   |-- _stata_builtins.py
|   |           |   |   |-- _tsql_builtins.py
|   |           |   |   |-- _usd_builtins.py
|   |           |   |   |-- _vbscript_builtins.py
|   |           |   |   |-- _vim_builtins.py
|   |           |   |   |-- actionscript.py
|   |           |   |   |-- ada.py
|   |           |   |   |-- agile.py
|   |           |   |   |-- algebra.py
|   |           |   |   |-- ambient.py
|   |           |   |   |-- amdgpu.py
|   |           |   |   |-- ampl.py
|   |           |   |   |-- apdlexer.py
|   |           |   |   |-- apl.py
|   |           |   |   |-- archetype.py
|   |           |   |   |-- arrow.py
|   |           |   |   |-- arturo.py
|   |           |   |   |-- asc.py
|   |           |   |   |-- asm.py
|   |           |   |   |-- asn1.py
|   |           |   |   |-- automation.py
|   |           |   |   |-- bare.py
|   |           |   |   |-- basic.py
|   |           |   |   |-- bdd.py
|   |           |   |   |-- berry.py
|   |           |   |   |-- bibtex.py
|   |           |   |   |-- blueprint.py
|   |           |   |   |-- boa.py
|   |           |   |   |-- bqn.py
|   |           |   |   |-- business.py
|   |           |   |   |-- c_cpp.py
|   |           |   |   |-- c_like.py
|   |           |   |   |-- capnproto.py
|   |           |   |   |-- carbon.py
|   |           |   |   |-- cddl.py
|   |           |   |   |-- chapel.py
|   |           |   |   |-- clean.py
|   |           |   |   |-- codeql.py
|   |           |   |   |-- comal.py
|   |           |   |   |-- compiled.py
|   |           |   |   |-- configs.py
|   |           |   |   |-- console.py
|   |           |   |   |-- cplint.py
|   |           |   |   |-- crystal.py
|   |           |   |   |-- csound.py
|   |           |   |   |-- css.py
|   |           |   |   |-- d.py
|   |           |   |   |-- dalvik.py
|   |           |   |   |-- data.py
|   |           |   |   |-- dax.py
|   |           |   |   |-- devicetree.py
|   |           |   |   |-- diff.py
|   |           |   |   |-- dns.py
|   |           |   |   |-- dotnet.py
|   |           |   |   |-- dsls.py
|   |           |   |   |-- dylan.py
|   |           |   |   |-- ecl.py
|   |           |   |   |-- eiffel.py
|   |           |   |   |-- elm.py
|   |           |   |   |-- elpi.py
|   |           |   |   |-- email.py
|   |           |   |   |-- erlang.py
|   |           |   |   |-- esoteric.py
|   |           |   |   |-- ezhil.py
|   |           |   |   |-- factor.py
|   |           |   |   |-- fantom.py
|   |           |   |   |-- felix.py
|   |           |   |   |-- fift.py
|   |           |   |   |-- floscript.py
|   |           |   |   |-- forth.py
|   |           |   |   |-- fortran.py
|   |           |   |   |-- foxpro.py
|   |           |   |   |-- freefem.py
|   |           |   |   |-- func.py
|   |           |   |   |-- functional.py
|   |           |   |   |-- futhark.py
|   |           |   |   |-- gcodelexer.py
|   |           |   |   |-- gdscript.py
|   |           |   |   |-- gleam.py
|   |           |   |   |-- go.py
|   |           |   |   |-- grammar_notation.py
|   |           |   |   |-- graph.py
|   |           |   |   |-- graphics.py
|   |           |   |   |-- graphql.py
|   |           |   |   |-- graphviz.py
|   |           |   |   |-- gsql.py
|   |           |   |   |-- hare.py
|   |           |   |   |-- haskell.py
|   |           |   |   |-- haxe.py
|   |           |   |   |-- hdl.py
|   |           |   |   |-- hexdump.py
|   |           |   |   |-- html.py
|   |           |   |   |-- idl.py
|   |           |   |   |-- igor.py
|   |           |   |   |-- inferno.py
|   |           |   |   |-- installers.py
|   |           |   |   |-- int_fiction.py
|   |           |   |   |-- iolang.py
|   |           |   |   |-- j.py
|   |           |   |   |-- javascript.py
|   |           |   |   |-- jmespath.py
|   |           |   |   |-- jslt.py
|   |           |   |   |-- json5.py
|   |           |   |   |-- jsonnet.py
|   |           |   |   |-- jsx.py
|   |           |   |   |-- julia.py
|   |           |   |   |-- jvm.py
|   |           |   |   |-- kuin.py
|   |           |   |   |-- kusto.py
|   |           |   |   |-- ldap.py
|   |           |   |   |-- lean.py
|   |           |   |   |-- lilypond.py
|   |           |   |   |-- lisp.py
|   |           |   |   |-- macaulay2.py
|   |           |   |   |-- make.py
|   |           |   |   |-- maple.py
|   |           |   |   |-- markup.py
|   |           |   |   |-- math.py
|   |           |   |   |-- matlab.py
|   |           |   |   |-- maxima.py
|   |           |   |   |-- meson.py
|   |           |   |   |-- mime.py
|   |           |   |   |-- minecraft.py
|   |           |   |   |-- mips.py
|   |           |   |   |-- ml.py
|   |           |   |   |-- modeling.py
|   |           |   |   |-- modula2.py
|   |           |   |   |-- mojo.py
|   |           |   |   |-- monte.py
|   |           |   |   |-- mosel.py
|   |           |   |   |-- ncl.py
|   |           |   |   |-- nimrod.py
|   |           |   |   |-- nit.py
|   |           |   |   |-- nix.py
|   |           |   |   |-- numbair.py
|   |           |   |   |-- oberon.py
|   |           |   |   |-- objective.py
|   |           |   |   |-- ooc.py
|   |           |   |   |-- openscad.py
|   |           |   |   |-- other.py
|   |           |   |   |-- parasail.py
|   |           |   |   |-- parsers.py
|   |           |   |   |-- pascal.py
|   |           |   |   |-- pawn.py
|   |           |   |   |-- pddl.py
|   |           |   |   |-- perl.py
|   |           |   |   |-- phix.py
|   |           |   |   |-- php.py
|   |           |   |   |-- pointless.py
|   |           |   |   |-- pony.py
|   |           |   |   |-- praat.py
|   |           |   |   |-- procfile.py
|   |           |   |   |-- prolog.py
|   |           |   |   |-- promql.py
|   |           |   |   |-- prql.py
|   |           |   |   |-- ptx.py
|   |           |   |   |-- python.py
|   |           |   |   |-- q.py
|   |           |   |   |-- qlik.py
|   |           |   |   |-- qvt.py
|   |           |   |   |-- r.py
|   |           |   |   |-- rdf.py
|   |           |   |   |-- rebol.py
|   |           |   |   |-- rego.py
|   |           |   |   |-- resource.py
|   |           |   |   |-- ride.py
|   |           |   |   |-- rita.py
|   |           |   |   |-- rnc.py
|   |           |   |   |-- roboconf.py
|   |           |   |   |-- robotframework.py
|   |           |   |   |-- ruby.py
|   |           |   |   |-- rust.py
|   |           |   |   |-- sas.py
|   |           |   |   |-- savi.py
|   |           |   |   |-- scdoc.py
|   |           |   |   |-- scripting.py
|   |           |   |   |-- sgf.py
|   |           |   |   |-- shell.py
|   |           |   |   |-- sieve.py
|   |           |   |   |-- slash.py
|   |           |   |   |-- smalltalk.py
|   |           |   |   |-- smithy.py
|   |           |   |   |-- smv.py
|   |           |   |   |-- snobol.py
|   |           |   |   |-- solidity.py
|   |           |   |   |-- soong.py
|   |           |   |   |-- sophia.py
|   |           |   |   |-- special.py
|   |           |   |   |-- spice.py
|   |           |   |   |-- sql.py
|   |           |   |   |-- srcinfo.py
|   |           |   |   |-- stata.py
|   |           |   |   |-- supercollider.py
|   |           |   |   |-- tablegen.py
|   |           |   |   |-- tact.py
|   |           |   |   |-- tal.py
|   |           |   |   |-- tcl.py
|   |           |   |   |-- teal.py
|   |           |   |   |-- templates.py
|   |           |   |   |-- teraterm.py
|   |           |   |   |-- testing.py
|   |           |   |   |-- text.py
|   |           |   |   |-- textedit.py
|   |           |   |   |-- textfmts.py
|   |           |   |   |-- theorem.py
|   |           |   |   |-- thingsdb.py
|   |           |   |   |-- tlb.py
|   |           |   |   |-- tls.py
|   |           |   |   |-- tnt.py
|   |           |   |   |-- trafficscript.py
|   |           |   |   |-- typoscript.py
|   |           |   |   |-- typst.py
|   |           |   |   |-- ul4.py
|   |           |   |   |-- unicon.py
|   |           |   |   |-- urbi.py
|   |           |   |   |-- usd.py
|   |           |   |   |-- varnish.py
|   |           |   |   |-- verification.py
|   |           |   |   |-- verifpal.py
|   |           |   |   |-- vip.py
|   |           |   |   |-- vyper.py
|   |           |   |   |-- web.py
|   |           |   |   |-- webassembly.py
|   |           |   |   |-- webidl.py
|   |           |   |   |-- webmisc.py
|   |           |   |   |-- wgsl.py
|   |           |   |   |-- whiley.py
|   |           |   |   |-- wowtoc.py
|   |           |   |   |-- wren.py
|   |           |   |   |-- x10.py
|   |           |   |   |-- xorg.py
|   |           |   |   |-- yang.py
|   |           |   |   |-- yara.py
|   |           |   |   `-- zig.py
|   |           |   |-- styles
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- _mapping.cpython-312.pyc
|   |           |   |   |   |-- abap.cpython-312.pyc
|   |           |   |   |   |-- algol.cpython-312.pyc
|   |           |   |   |   |-- algol_nu.cpython-312.pyc
|   |           |   |   |   |-- arduino.cpython-312.pyc
|   |           |   |   |   |-- autumn.cpython-312.pyc
|   |           |   |   |   |-- borland.cpython-312.pyc
|   |           |   |   |   |-- bw.cpython-312.pyc
|   |           |   |   |   |-- coffee.cpython-312.pyc
|   |           |   |   |   |-- colorful.cpython-312.pyc
|   |           |   |   |   |-- default.cpython-312.pyc
|   |           |   |   |   |-- dracula.cpython-312.pyc
|   |           |   |   |   |-- emacs.cpython-312.pyc
|   |           |   |   |   |-- friendly.cpython-312.pyc
|   |           |   |   |   |-- friendly_grayscale.cpython-312.pyc
|   |           |   |   |   |-- fruity.cpython-312.pyc
|   |           |   |   |   |-- gh_dark.cpython-312.pyc
|   |           |   |   |   |-- gruvbox.cpython-312.pyc
|   |           |   |   |   |-- igor.cpython-312.pyc
|   |           |   |   |   |-- inkpot.cpython-312.pyc
|   |           |   |   |   |-- lightbulb.cpython-312.pyc
|   |           |   |   |   |-- lilypond.cpython-312.pyc
|   |           |   |   |   |-- lovelace.cpython-312.pyc
|   |           |   |   |   |-- manni.cpython-312.pyc
|   |           |   |   |   |-- material.cpython-312.pyc
|   |           |   |   |   |-- monokai.cpython-312.pyc
|   |           |   |   |   |-- murphy.cpython-312.pyc
|   |           |   |   |   |-- native.cpython-312.pyc
|   |           |   |   |   |-- nord.cpython-312.pyc
|   |           |   |   |   |-- onedark.cpython-312.pyc
|   |           |   |   |   |-- paraiso_dark.cpython-312.pyc
|   |           |   |   |   |-- paraiso_light.cpython-312.pyc
|   |           |   |   |   |-- pastie.cpython-312.pyc
|   |           |   |   |   |-- perldoc.cpython-312.pyc
|   |           |   |   |   |-- rainbow_dash.cpython-312.pyc
|   |           |   |   |   |-- rrt.cpython-312.pyc
|   |           |   |   |   |-- sas.cpython-312.pyc
|   |           |   |   |   |-- solarized.cpython-312.pyc
|   |           |   |   |   |-- staroffice.cpython-312.pyc
|   |           |   |   |   |-- stata_dark.cpython-312.pyc
|   |           |   |   |   |-- stata_light.cpython-312.pyc
|   |           |   |   |   |-- tango.cpython-312.pyc
|   |           |   |   |   |-- trac.cpython-312.pyc
|   |           |   |   |   |-- vim.cpython-312.pyc
|   |           |   |   |   |-- vs.cpython-312.pyc
|   |           |   |   |   |-- xcode.cpython-312.pyc
|   |           |   |   |   `-- zenburn.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- _mapping.py
|   |           |   |   |-- abap.py
|   |           |   |   |-- algol.py
|   |           |   |   |-- algol_nu.py
|   |           |   |   |-- arduino.py
|   |           |   |   |-- autumn.py
|   |           |   |   |-- borland.py
|   |           |   |   |-- bw.py
|   |           |   |   |-- coffee.py
|   |           |   |   |-- colorful.py
|   |           |   |   |-- default.py
|   |           |   |   |-- dracula.py
|   |           |   |   |-- emacs.py
|   |           |   |   |-- friendly.py
|   |           |   |   |-- friendly_grayscale.py
|   |           |   |   |-- fruity.py
|   |           |   |   |-- gh_dark.py
|   |           |   |   |-- gruvbox.py
|   |           |   |   |-- igor.py
|   |           |   |   |-- inkpot.py
|   |           |   |   |-- lightbulb.py
|   |           |   |   |-- lilypond.py
|   |           |   |   |-- lovelace.py
|   |           |   |   |-- manni.py
|   |           |   |   |-- material.py
|   |           |   |   |-- monokai.py
|   |           |   |   |-- murphy.py
|   |           |   |   |-- native.py
|   |           |   |   |-- nord.py
|   |           |   |   |-- onedark.py
|   |           |   |   |-- paraiso_dark.py
|   |           |   |   |-- paraiso_light.py
|   |           |   |   |-- pastie.py
|   |           |   |   |-- perldoc.py
|   |           |   |   |-- rainbow_dash.py
|   |           |   |   |-- rrt.py
|   |           |   |   |-- sas.py
|   |           |   |   |-- solarized.py
|   |           |   |   |-- staroffice.py
|   |           |   |   |-- stata_dark.py
|   |           |   |   |-- stata_light.py
|   |           |   |   |-- tango.py
|   |           |   |   |-- trac.py
|   |           |   |   |-- vim.py
|   |           |   |   |-- vs.py
|   |           |   |   |-- xcode.py
|   |           |   |   `-- zenburn.py
|   |           |   |-- __init__.py
|   |           |   |-- __main__.py
|   |           |   |-- cmdline.py
|   |           |   |-- console.py
|   |           |   |-- filter.py
|   |           |   |-- formatter.py
|   |           |   |-- lexer.py
|   |           |   |-- modeline.py
|   |           |   |-- plugin.py
|   |           |   |-- regexopt.py
|   |           |   |-- scanner.py
|   |           |   |-- sphinxext.py
|   |           |   |-- style.py
|   |           |   |-- token.py
|   |           |   |-- unistring.py
|   |           |   `-- util.py
|   |           |-- pygments-2.19.2.dist-info
|   |           |   |-- licenses
|   |           |   |   |-- AUTHORS
|   |           |   |   `-- LICENSE
|   |           |   |-- INSTALLER
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   |-- WHEEL
|   |           |   `-- entry_points.txt
|   |           |-- pyparsing
|   |           |   |-- __pycache__
|   |           |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |-- actions.cpython-312.pyc
|   |           |   |   |-- common.cpython-312.pyc
|   |           |   |   |-- core.cpython-312.pyc
|   |           |   |   |-- exceptions.cpython-312.pyc
|   |           |   |   |-- helpers.cpython-312.pyc
|   |           |   |   |-- results.cpython-312.pyc
|   |           |   |   |-- testing.cpython-312.pyc
|   |           |   |   |-- unicode.cpython-312.pyc
|   |           |   |   `-- util.cpython-312.pyc
|   |           |   |-- diagram
|   |           |   |   |-- __pycache__
|   |           |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   `-- __init__.py
|   |           |   |-- tools
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   `-- cvt_pyparsing_pep8_names.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   `-- cvt_pyparsing_pep8_names.py
|   |           |   |-- __init__.py
|   |           |   |-- actions.py
|   |           |   |-- common.py
|   |           |   |-- core.py
|   |           |   |-- exceptions.py
|   |           |   |-- helpers.py
|   |           |   |-- py.typed
|   |           |   |-- results.py
|   |           |   |-- testing.py
|   |           |   |-- unicode.py
|   |           |   `-- util.py
|   |           |-- pyparsing-3.2.5.dist-info
|   |           |   |-- licenses
|   |           |   |   `-- LICENSE
|   |           |   |-- INSTALLER
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   `-- WHEEL
|   |           |-- pytest
|   |           |   |-- __pycache__
|   |           |   |   |-- __init__.cpython-312.pyc
|   |           |   |   `-- __main__.cpython-312.pyc
|   |           |   |-- __init__.py
|   |           |   |-- __main__.py
|   |           |   `-- py.typed
|   |           |-- pytest-8.4.2.dist-info
|   |           |   |-- licenses
|   |           |   |   |-- AUTHORS
|   |           |   |   `-- LICENSE
|   |           |   |-- INSTALLER
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   |-- REQUESTED
|   |           |   |-- WHEEL
|   |           |   |-- entry_points.txt
|   |           |   `-- top_level.txt
|   |           |-- python_dateutil-2.9.0.post0.dist-info
|   |           |   |-- INSTALLER
|   |           |   |-- LICENSE
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   |-- REQUESTED
|   |           |   |-- WHEEL
|   |           |   |-- top_level.txt
|   |           |   `-- zip-safe
|   |           |-- pytz
|   |           |   |-- __pycache__
|   |           |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |-- exceptions.cpython-312.pyc
|   |           |   |   |-- lazy.cpython-312.pyc
|   |           |   |   |-- reference.cpython-312.pyc
|   |           |   |   |-- tzfile.cpython-312.pyc
|   |           |   |   `-- tzinfo.cpython-312.pyc
|   |           |   |-- zoneinfo
|   |           |   |   |-- Africa
|   |           |   |   |   |-- Abidjan
|   |           |   |   |   |-- Accra
|   |           |   |   |   |-- Addis_Ababa
|   |           |   |   |   |-- Algiers
|   |           |   |   |   |-- Asmara
|   |           |   |   |   |-- Asmera
|   |           |   |   |   |-- Bamako
|   |           |   |   |   |-- Bangui
|   |           |   |   |   |-- Banjul
|   |           |   |   |   |-- Bissau
|   |           |   |   |   |-- Blantyre
|   |           |   |   |   |-- Brazzaville
|   |           |   |   |   |-- Bujumbura
|   |           |   |   |   |-- Cairo
|   |           |   |   |   |-- Casablanca
|   |           |   |   |   |-- Ceuta
|   |           |   |   |   |-- Conakry
|   |           |   |   |   |-- Dakar
|   |           |   |   |   |-- Dar_es_Salaam
|   |           |   |   |   |-- Djibouti
|   |           |   |   |   |-- Douala
|   |           |   |   |   |-- El_Aaiun
|   |           |   |   |   |-- Freetown
|   |           |   |   |   |-- Gaborone
|   |           |   |   |   |-- Harare
|   |           |   |   |   |-- Johannesburg
|   |           |   |   |   |-- Juba
|   |           |   |   |   |-- Kampala
|   |           |   |   |   |-- Khartoum
|   |           |   |   |   |-- Kigali
|   |           |   |   |   |-- Kinshasa
|   |           |   |   |   |-- Lagos
|   |           |   |   |   |-- Libreville
|   |           |   |   |   |-- Lome
|   |           |   |   |   |-- Luanda
|   |           |   |   |   |-- Lubumbashi
|   |           |   |   |   |-- Lusaka
|   |           |   |   |   |-- Malabo
|   |           |   |   |   |-- Maputo
|   |           |   |   |   |-- Maseru
|   |           |   |   |   |-- Mbabane
|   |           |   |   |   |-- Mogadishu
|   |           |   |   |   |-- Monrovia
|   |           |   |   |   |-- Nairobi
|   |           |   |   |   |-- Ndjamena
|   |           |   |   |   |-- Niamey
|   |           |   |   |   |-- Nouakchott
|   |           |   |   |   |-- Ouagadougou
|   |           |   |   |   |-- Porto-Novo
|   |           |   |   |   |-- Sao_Tome
|   |           |   |   |   |-- Timbuktu
|   |           |   |   |   |-- Tripoli
|   |           |   |   |   |-- Tunis
|   |           |   |   |   `-- Windhoek
|   |           |   |   |-- America
|   |           |   |   |   |-- Argentina
|   |           |   |   |   |   |-- Buenos_Aires
|   |           |   |   |   |   |-- Catamarca
|   |           |   |   |   |   |-- ComodRivadavia
|   |           |   |   |   |   |-- Cordoba
|   |           |   |   |   |   |-- Jujuy
|   |           |   |   |   |   |-- La_Rioja
|   |           |   |   |   |   |-- Mendoza
|   |           |   |   |   |   |-- Rio_Gallegos
|   |           |   |   |   |   |-- Salta
|   |           |   |   |   |   |-- San_Juan
|   |           |   |   |   |   |-- San_Luis
|   |           |   |   |   |   |-- Tucuman
|   |           |   |   |   |   `-- Ushuaia
|   |           |   |   |   |-- Indiana
|   |           |   |   |   |   |-- Indianapolis
|   |           |   |   |   |   |-- Knox
|   |           |   |   |   |   |-- Marengo
|   |           |   |   |   |   |-- Petersburg
|   |           |   |   |   |   |-- Tell_City
|   |           |   |   |   |   |-- Vevay
|   |           |   |   |   |   |-- Vincennes
|   |           |   |   |   |   `-- Winamac
|   |           |   |   |   |-- Kentucky
|   |           |   |   |   |   |-- Louisville
|   |           |   |   |   |   `-- Monticello
|   |           |   |   |   |-- North_Dakota
|   |           |   |   |   |   |-- Beulah
|   |           |   |   |   |   |-- Center
|   |           |   |   |   |   `-- New_Salem
|   |           |   |   |   |-- Adak
|   |           |   |   |   |-- Anchorage
|   |           |   |   |   |-- Anguilla
|   |           |   |   |   |-- Antigua
|   |           |   |   |   |-- Araguaina
|   |           |   |   |   |-- Aruba
|   |           |   |   |   |-- Asuncion
|   |           |   |   |   |-- Atikokan
|   |           |   |   |   |-- Atka
|   |           |   |   |   |-- Bahia
|   |           |   |   |   |-- Bahia_Banderas
|   |           |   |   |   |-- Barbados
|   |           |   |   |   |-- Belem
|   |           |   |   |   |-- Belize
|   |           |   |   |   |-- Blanc-Sablon
|   |           |   |   |   |-- Boa_Vista
|   |           |   |   |   |-- Bogota
|   |           |   |   |   |-- Boise
|   |           |   |   |   |-- Buenos_Aires
|   |           |   |   |   |-- Cambridge_Bay
|   |           |   |   |   |-- Campo_Grande
|   |           |   |   |   |-- Cancun
|   |           |   |   |   |-- Caracas
|   |           |   |   |   |-- Catamarca
|   |           |   |   |   |-- Cayenne
|   |           |   |   |   |-- Cayman
|   |           |   |   |   |-- Chicago
|   |           |   |   |   |-- Chihuahua
|   |           |   |   |   |-- Ciudad_Juarez
|   |           |   |   |   |-- Coral_Harbour
|   |           |   |   |   |-- Cordoba
|   |           |   |   |   |-- Costa_Rica
|   |           |   |   |   |-- Coyhaique
|   |           |   |   |   |-- Creston
|   |           |   |   |   |-- Cuiaba
|   |           |   |   |   |-- Curacao
|   |           |   |   |   |-- Danmarkshavn
|   |           |   |   |   |-- Dawson
|   |           |   |   |   |-- Dawson_Creek
|   |           |   |   |   |-- Denver
|   |           |   |   |   |-- Detroit
|   |           |   |   |   |-- Dominica
|   |           |   |   |   |-- Edmonton
|   |           |   |   |   |-- Eirunepe
|   |           |   |   |   |-- El_Salvador
|   |           |   |   |   |-- Ensenada
|   |           |   |   |   |-- Fort_Nelson
|   |           |   |   |   |-- Fort_Wayne
|   |           |   |   |   |-- Fortaleza
|   |           |   |   |   |-- Glace_Bay
|   |           |   |   |   |-- Godthab
|   |           |   |   |   |-- Goose_Bay
|   |           |   |   |   |-- Grand_Turk
|   |           |   |   |   |-- Grenada
|   |           |   |   |   |-- Guadeloupe
|   |           |   |   |   |-- Guatemala
|   |           |   |   |   |-- Guayaquil
|   |           |   |   |   |-- Guyana
|   |           |   |   |   |-- Halifax
|   |           |   |   |   |-- Havana
|   |           |   |   |   |-- Hermosillo
|   |           |   |   |   |-- Indianapolis
|   |           |   |   |   |-- Inuvik
|   |           |   |   |   |-- Iqaluit
|   |           |   |   |   |-- Jamaica
|   |           |   |   |   |-- Jujuy
|   |           |   |   |   |-- Juneau
|   |           |   |   |   |-- Knox_IN
|   |           |   |   |   |-- Kralendijk
|   |           |   |   |   |-- La_Paz
|   |           |   |   |   |-- Lima
|   |           |   |   |   |-- Los_Angeles
|   |           |   |   |   |-- Louisville
|   |           |   |   |   |-- Lower_Princes
|   |           |   |   |   |-- Maceio
|   |           |   |   |   |-- Managua
|   |           |   |   |   |-- Manaus
|   |           |   |   |   |-- Marigot
|   |           |   |   |   |-- Martinique
|   |           |   |   |   |-- Matamoros
|   |           |   |   |   |-- Mazatlan
|   |           |   |   |   |-- Mendoza
|   |           |   |   |   |-- Menominee
|   |           |   |   |   |-- Merida
|   |           |   |   |   |-- Metlakatla
|   |           |   |   |   |-- Mexico_City
|   |           |   |   |   |-- Miquelon
|   |           |   |   |   |-- Moncton
|   |           |   |   |   |-- Monterrey
|   |           |   |   |   |-- Montevideo
|   |           |   |   |   |-- Montreal
|   |           |   |   |   |-- Montserrat
|   |           |   |   |   |-- Nassau
|   |           |   |   |   |-- New_York
|   |           |   |   |   |-- Nipigon
|   |           |   |   |   |-- Nome
|   |           |   |   |   |-- Noronha
|   |           |   |   |   |-- Nuuk
|   |           |   |   |   |-- Ojinaga
|   |           |   |   |   |-- Panama
|   |           |   |   |   |-- Pangnirtung
|   |           |   |   |   |-- Paramaribo
|   |           |   |   |   |-- Phoenix
|   |           |   |   |   |-- Port-au-Prince
|   |           |   |   |   |-- Port_of_Spain
|   |           |   |   |   |-- Porto_Acre
|   |           |   |   |   |-- Porto_Velho
|   |           |   |   |   |-- Puerto_Rico
|   |           |   |   |   |-- Punta_Arenas
|   |           |   |   |   |-- Rainy_River
|   |           |   |   |   |-- Rankin_Inlet
|   |           |   |   |   |-- Recife
|   |           |   |   |   |-- Regina
|   |           |   |   |   |-- Resolute
|   |           |   |   |   |-- Rio_Branco
|   |           |   |   |   |-- Rosario
|   |           |   |   |   |-- Santa_Isabel
|   |           |   |   |   |-- Santarem
|   |           |   |   |   |-- Santiago
|   |           |   |   |   |-- Santo_Domingo
|   |           |   |   |   |-- Sao_Paulo
|   |           |   |   |   |-- Scoresbysund
|   |           |   |   |   |-- Shiprock
|   |           |   |   |   |-- Sitka
|   |           |   |   |   |-- St_Barthelemy
|   |           |   |   |   |-- St_Johns
|   |           |   |   |   |-- St_Kitts
|   |           |   |   |   |-- St_Lucia
|   |           |   |   |   |-- St_Thomas
|   |           |   |   |   |-- St_Vincent
|   |           |   |   |   |-- Swift_Current
|   |           |   |   |   |-- Tegucigalpa
|   |           |   |   |   |-- Thule
|   |           |   |   |   |-- Thunder_Bay
|   |           |   |   |   |-- Tijuana
|   |           |   |   |   |-- Toronto
|   |           |   |   |   |-- Tortola
|   |           |   |   |   |-- Vancouver
|   |           |   |   |   |-- Virgin
|   |           |   |   |   |-- Whitehorse
|   |           |   |   |   |-- Winnipeg
|   |           |   |   |   |-- Yakutat
|   |           |   |   |   `-- Yellowknife
|   |           |   |   |-- Antarctica
|   |           |   |   |   |-- Casey
|   |           |   |   |   |-- Davis
|   |           |   |   |   |-- DumontDUrville
|   |           |   |   |   |-- Macquarie
|   |           |   |   |   |-- Mawson
|   |           |   |   |   |-- McMurdo
|   |           |   |   |   |-- Palmer
|   |           |   |   |   |-- Rothera
|   |           |   |   |   |-- South_Pole
|   |           |   |   |   |-- Syowa
|   |           |   |   |   |-- Troll
|   |           |   |   |   `-- Vostok
|   |           |   |   |-- Arctic
|   |           |   |   |   `-- Longyearbyen
|   |           |   |   |-- Asia
|   |           |   |   |   |-- Aden
|   |           |   |   |   |-- Almaty
|   |           |   |   |   |-- Amman
|   |           |   |   |   |-- Anadyr
|   |           |   |   |   |-- Aqtau
|   |           |   |   |   |-- Aqtobe
|   |           |   |   |   |-- Ashgabat
|   |           |   |   |   |-- Ashkhabad
|   |           |   |   |   |-- Atyrau
|   |           |   |   |   |-- Baghdad
|   |           |   |   |   |-- Bahrain
|   |           |   |   |   |-- Baku
|   |           |   |   |   |-- Bangkok
|   |           |   |   |   |-- Barnaul
|   |           |   |   |   |-- Beirut
|   |           |   |   |   |-- Bishkek
|   |           |   |   |   |-- Brunei
|   |           |   |   |   |-- Calcutta
|   |           |   |   |   |-- Chita
|   |           |   |   |   |-- Choibalsan
|   |           |   |   |   |-- Chongqing
|   |           |   |   |   |-- Chungking
|   |           |   |   |   |-- Colombo
|   |           |   |   |   |-- Dacca
|   |           |   |   |   |-- Damascus
|   |           |   |   |   |-- Dhaka
|   |           |   |   |   |-- Dili
|   |           |   |   |   |-- Dubai
|   |           |   |   |   |-- Dushanbe
|   |           |   |   |   |-- Famagusta
|   |           |   |   |   |-- Gaza
|   |           |   |   |   |-- Harbin
|   |           |   |   |   |-- Hebron
|   |           |   |   |   |-- Ho_Chi_Minh
|   |           |   |   |   |-- Hong_Kong
|   |           |   |   |   |-- Hovd
|   |           |   |   |   |-- Irkutsk
|   |           |   |   |   |-- Istanbul
|   |           |   |   |   |-- Jakarta
|   |           |   |   |   |-- Jayapura
|   |           |   |   |   |-- Jerusalem
|   |           |   |   |   |-- Kabul
|   |           |   |   |   |-- Kamchatka
|   |           |   |   |   |-- Karachi
|   |           |   |   |   |-- Kashgar
|   |           |   |   |   |-- Kathmandu
|   |           |   |   |   |-- Katmandu
|   |           |   |   |   |-- Khandyga
|   |           |   |   |   |-- Kolkata
|   |           |   |   |   |-- Krasnoyarsk
|   |           |   |   |   |-- Kuala_Lumpur
|   |           |   |   |   |-- Kuching
|   |           |   |   |   |-- Kuwait
|   |           |   |   |   |-- Macao
|   |           |   |   |   |-- Macau
|   |           |   |   |   |-- Magadan
|   |           |   |   |   |-- Makassar
|   |           |   |   |   |-- Manila
|   |           |   |   |   |-- Muscat
|   |           |   |   |   |-- Nicosia
|   |           |   |   |   |-- Novokuznetsk
|   |           |   |   |   |-- Novosibirsk
|   |           |   |   |   |-- Omsk
|   |           |   |   |   |-- Oral
|   |           |   |   |   |-- Phnom_Penh
|   |           |   |   |   |-- Pontianak
|   |           |   |   |   |-- Pyongyang
|   |           |   |   |   |-- Qatar
|   |           |   |   |   |-- Qostanay
|   |           |   |   |   |-- Qyzylorda
|   |           |   |   |   |-- Rangoon
|   |           |   |   |   |-- Riyadh
|   |           |   |   |   |-- Saigon
|   |           |   |   |   |-- Sakhalin
|   |           |   |   |   |-- Samarkand
|   |           |   |   |   |-- Seoul
|   |           |   |   |   |-- Shanghai
|   |           |   |   |   |-- Singapore
|   |           |   |   |   |-- Srednekolymsk
|   |           |   |   |   |-- Taipei
|   |           |   |   |   |-- Tashkent
|   |           |   |   |   |-- Tbilisi
|   |           |   |   |   |-- Tehran
|   |           |   |   |   |-- Tel_Aviv
|   |           |   |   |   |-- Thimbu
|   |           |   |   |   |-- Thimphu
|   |           |   |   |   |-- Tokyo
|   |           |   |   |   |-- Tomsk
|   |           |   |   |   |-- Ujung_Pandang
|   |           |   |   |   |-- Ulaanbaatar
|   |           |   |   |   |-- Ulan_Bator
|   |           |   |   |   |-- Urumqi
|   |           |   |   |   |-- Ust-Nera
|   |           |   |   |   |-- Vientiane
|   |           |   |   |   |-- Vladivostok
|   |           |   |   |   |-- Yakutsk
|   |           |   |   |   |-- Yangon
|   |           |   |   |   |-- Yekaterinburg
|   |           |   |   |   `-- Yerevan
|   |           |   |   |-- Atlantic
|   |           |   |   |   |-- Azores
|   |           |   |   |   |-- Bermuda
|   |           |   |   |   |-- Canary
|   |           |   |   |   |-- Cape_Verde
|   |           |   |   |   |-- Faeroe
|   |           |   |   |   |-- Faroe
|   |           |   |   |   |-- Jan_Mayen
|   |           |   |   |   |-- Madeira
|   |           |   |   |   |-- Reykjavik
|   |           |   |   |   |-- South_Georgia
|   |           |   |   |   |-- St_Helena
|   |           |   |   |   `-- Stanley
|   |           |   |   |-- Australia
|   |           |   |   |   |-- ACT
|   |           |   |   |   |-- Adelaide
|   |           |   |   |   |-- Brisbane
|   |           |   |   |   |-- Broken_Hill
|   |           |   |   |   |-- Canberra
|   |           |   |   |   |-- Currie
|   |           |   |   |   |-- Darwin
|   |           |   |   |   |-- Eucla
|   |           |   |   |   |-- Hobart
|   |           |   |   |   |-- LHI
|   |           |   |   |   |-- Lindeman
|   |           |   |   |   |-- Lord_Howe
|   |           |   |   |   |-- Melbourne
|   |           |   |   |   |-- NSW
|   |           |   |   |   |-- North
|   |           |   |   |   |-- Perth
|   |           |   |   |   |-- Queensland
|   |           |   |   |   |-- South
|   |           |   |   |   |-- Sydney
|   |           |   |   |   |-- Tasmania
|   |           |   |   |   |-- Victoria
|   |           |   |   |   |-- West
|   |           |   |   |   `-- Yancowinna
|   |           |   |   |-- Brazil
|   |           |   |   |   |-- Acre
|   |           |   |   |   |-- DeNoronha
|   |           |   |   |   |-- East
|   |           |   |   |   `-- West
|   |           |   |   |-- Canada
|   |           |   |   |   |-- Atlantic
|   |           |   |   |   |-- Central
|   |           |   |   |   |-- Eastern
|   |           |   |   |   |-- Mountain
|   |           |   |   |   |-- Newfoundland
|   |           |   |   |   |-- Pacific
|   |           |   |   |   |-- Saskatchewan
|   |           |   |   |   `-- Yukon
|   |           |   |   |-- Chile
|   |           |   |   |   |-- Continental
|   |           |   |   |   `-- EasterIsland
|   |           |   |   |-- Etc
|   |           |   |   |   |-- GMT
|   |           |   |   |   |-- GMT+0
|   |           |   |   |   |-- GMT+1
|   |           |   |   |   |-- GMT+10
|   |           |   |   |   |-- GMT+11
|   |           |   |   |   |-- GMT+12
|   |           |   |   |   |-- GMT+2
|   |           |   |   |   |-- GMT+3
|   |           |   |   |   |-- GMT+4
|   |           |   |   |   |-- GMT+5
|   |           |   |   |   |-- GMT+6
|   |           |   |   |   |-- GMT+7
|   |           |   |   |   |-- GMT+8
|   |           |   |   |   |-- GMT+9
|   |           |   |   |   |-- GMT-0
|   |           |   |   |   |-- GMT-1
|   |           |   |   |   |-- GMT-10
|   |           |   |   |   |-- GMT-11
|   |           |   |   |   |-- GMT-12
|   |           |   |   |   |-- GMT-13
|   |           |   |   |   |-- GMT-14
|   |           |   |   |   |-- GMT-2
|   |           |   |   |   |-- GMT-3
|   |           |   |   |   |-- GMT-4
|   |           |   |   |   |-- GMT-5
|   |           |   |   |   |-- GMT-6
|   |           |   |   |   |-- GMT-7
|   |           |   |   |   |-- GMT-8
|   |           |   |   |   |-- GMT-9
|   |           |   |   |   |-- GMT0
|   |           |   |   |   |-- Greenwich
|   |           |   |   |   |-- UCT
|   |           |   |   |   |-- UTC
|   |           |   |   |   |-- Universal
|   |           |   |   |   `-- Zulu
|   |           |   |   |-- Europe
|   |           |   |   |   |-- Amsterdam
|   |           |   |   |   |-- Andorra
|   |           |   |   |   |-- Astrakhan
|   |           |   |   |   |-- Athens
|   |           |   |   |   |-- Belfast
|   |           |   |   |   |-- Belgrade
|   |           |   |   |   |-- Berlin
|   |           |   |   |   |-- Bratislava
|   |           |   |   |   |-- Brussels
|   |           |   |   |   |-- Bucharest
|   |           |   |   |   |-- Budapest
|   |           |   |   |   |-- Busingen
|   |           |   |   |   |-- Chisinau
|   |           |   |   |   |-- Copenhagen
|   |           |   |   |   |-- Dublin
|   |           |   |   |   |-- Gibraltar
|   |           |   |   |   |-- Guernsey
|   |           |   |   |   |-- Helsinki
|   |           |   |   |   |-- Isle_of_Man
|   |           |   |   |   |-- Istanbul
|   |           |   |   |   |-- Jersey
|   |           |   |   |   |-- Kaliningrad
|   |           |   |   |   |-- Kiev
|   |           |   |   |   |-- Kirov
|   |           |   |   |   |-- Kyiv
|   |           |   |   |   |-- Lisbon
|   |           |   |   |   |-- Ljubljana
|   |           |   |   |   |-- London
|   |           |   |   |   |-- Luxembourg
|   |           |   |   |   |-- Madrid
|   |           |   |   |   |-- Malta
|   |           |   |   |   |-- Mariehamn
|   |           |   |   |   |-- Minsk
|   |           |   |   |   |-- Monaco
|   |           |   |   |   |-- Moscow
|   |           |   |   |   |-- Nicosia
|   |           |   |   |   |-- Oslo
|   |           |   |   |   |-- Paris
|   |           |   |   |   |-- Podgorica
|   |           |   |   |   |-- Prague
|   |           |   |   |   |-- Riga
|   |           |   |   |   |-- Rome
|   |           |   |   |   |-- Samara
|   |           |   |   |   |-- San_Marino
|   |           |   |   |   |-- Sarajevo
|   |           |   |   |   |-- Saratov
|   |           |   |   |   |-- Simferopol
|   |           |   |   |   |-- Skopje
|   |           |   |   |   |-- Sofia
|   |           |   |   |   |-- Stockholm
|   |           |   |   |   |-- Tallinn
|   |           |   |   |   |-- Tirane
|   |           |   |   |   |-- Tiraspol
|   |           |   |   |   |-- Ulyanovsk
|   |           |   |   |   |-- Uzhgorod
|   |           |   |   |   |-- Vaduz
|   |           |   |   |   |-- Vatican
|   |           |   |   |   |-- Vienna
|   |           |   |   |   |-- Vilnius
|   |           |   |   |   |-- Volgograd
|   |           |   |   |   |-- Warsaw
|   |           |   |   |   |-- Zagreb
|   |           |   |   |   |-- Zaporozhye
|   |           |   |   |   `-- Zurich
|   |           |   |   |-- Indian
|   |           |   |   |   |-- Antananarivo
|   |           |   |   |   |-- Chagos
|   |           |   |   |   |-- Christmas
|   |           |   |   |   |-- Cocos
|   |           |   |   |   |-- Comoro
|   |           |   |   |   |-- Kerguelen
|   |           |   |   |   |-- Mahe
|   |           |   |   |   |-- Maldives
|   |           |   |   |   |-- Mauritius
|   |           |   |   |   |-- Mayotte
|   |           |   |   |   `-- Reunion
|   |           |   |   |-- Mexico
|   |           |   |   |   |-- BajaNorte
|   |           |   |   |   |-- BajaSur
|   |           |   |   |   `-- General
|   |           |   |   |-- Pacific
|   |           |   |   |   |-- Apia
|   |           |   |   |   |-- Auckland
|   |           |   |   |   |-- Bougainville
|   |           |   |   |   |-- Chatham
|   |           |   |   |   |-- Chuuk
|   |           |   |   |   |-- Easter
|   |           |   |   |   |-- Efate
|   |           |   |   |   |-- Enderbury
|   |           |   |   |   |-- Fakaofo
|   |           |   |   |   |-- Fiji
|   |           |   |   |   |-- Funafuti
|   |           |   |   |   |-- Galapagos
|   |           |   |   |   |-- Gambier
|   |           |   |   |   |-- Guadalcanal
|   |           |   |   |   |-- Guam
|   |           |   |   |   |-- Honolulu
|   |           |   |   |   |-- Johnston
|   |           |   |   |   |-- Kanton
|   |           |   |   |   |-- Kiritimati
|   |           |   |   |   |-- Kosrae
|   |           |   |   |   |-- Kwajalein
|   |           |   |   |   |-- Majuro
|   |           |   |   |   |-- Marquesas
|   |           |   |   |   |-- Midway
|   |           |   |   |   |-- Nauru
|   |           |   |   |   |-- Niue
|   |           |   |   |   |-- Norfolk
|   |           |   |   |   |-- Noumea
|   |           |   |   |   |-- Pago_Pago
|   |           |   |   |   |-- Palau
|   |           |   |   |   |-- Pitcairn
|   |           |   |   |   |-- Pohnpei
|   |           |   |   |   |-- Ponape
|   |           |   |   |   |-- Port_Moresby
|   |           |   |   |   |-- Rarotonga
|   |           |   |   |   |-- Saipan
|   |           |   |   |   |-- Samoa
|   |           |   |   |   |-- Tahiti
|   |           |   |   |   |-- Tarawa
|   |           |   |   |   |-- Tongatapu
|   |           |   |   |   |-- Truk
|   |           |   |   |   |-- Wake
|   |           |   |   |   |-- Wallis
|   |           |   |   |   `-- Yap
|   |           |   |   |-- US
|   |           |   |   |   |-- Alaska
|   |           |   |   |   |-- Aleutian
|   |           |   |   |   |-- Arizona
|   |           |   |   |   |-- Central
|   |           |   |   |   |-- East-Indiana
|   |           |   |   |   |-- Eastern
|   |           |   |   |   |-- Hawaii
|   |           |   |   |   |-- Indiana-Starke
|   |           |   |   |   |-- Michigan
|   |           |   |   |   |-- Mountain
|   |           |   |   |   |-- Pacific
|   |           |   |   |   `-- Samoa
|   |           |   |   |-- CET
|   |           |   |   |-- CST6CDT
|   |           |   |   |-- Cuba
|   |           |   |   |-- EET
|   |           |   |   |-- EST
|   |           |   |   |-- EST5EDT
|   |           |   |   |-- Egypt
|   |           |   |   |-- Eire
|   |           |   |   |-- Factory
|   |           |   |   |-- GB
|   |           |   |   |-- GB-Eire
|   |           |   |   |-- GMT
|   |           |   |   |-- GMT+0
|   |           |   |   |-- GMT-0
|   |           |   |   |-- GMT0
|   |           |   |   |-- Greenwich
|   |           |   |   |-- HST
|   |           |   |   |-- Hongkong
|   |           |   |   |-- Iceland
|   |           |   |   |-- Iran
|   |           |   |   |-- Israel
|   |           |   |   |-- Jamaica
|   |           |   |   |-- Japan
|   |           |   |   |-- Kwajalein
|   |           |   |   |-- Libya
|   |           |   |   |-- MET
|   |           |   |   |-- MST
|   |           |   |   |-- MST7MDT
|   |           |   |   |-- NZ
|   |           |   |   |-- NZ-CHAT
|   |           |   |   |-- Navajo
|   |           |   |   |-- PRC
|   |           |   |   |-- PST8PDT
|   |           |   |   |-- Poland
|   |           |   |   |-- Portugal
|   |           |   |   |-- ROC
|   |           |   |   |-- ROK
|   |           |   |   |-- Singapore
|   |           |   |   |-- Turkey
|   |           |   |   |-- UCT
|   |           |   |   |-- UTC
|   |           |   |   |-- Universal
|   |           |   |   |-- W-SU
|   |           |   |   |-- WET
|   |           |   |   |-- Zulu
|   |           |   |   |-- iso3166.tab
|   |           |   |   |-- leapseconds
|   |           |   |   |-- tzdata.zi
|   |           |   |   |-- zone.tab
|   |           |   |   |-- zone1970.tab
|   |           |   |   `-- zonenow.tab
|   |           |   |-- __init__.py
|   |           |   |-- exceptions.py
|   |           |   |-- lazy.py
|   |           |   |-- reference.py
|   |           |   |-- tzfile.py
|   |           |   `-- tzinfo.py
|   |           |-- pytz-2025.2.dist-info
|   |           |   |-- INSTALLER
|   |           |   |-- LICENSE.txt
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   |-- WHEEL
|   |           |   |-- top_level.txt
|   |           |   `-- zip-safe
|   |           |-- six-1.17.0.dist-info
|   |           |   |-- INSTALLER
|   |           |   |-- LICENSE
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   |-- WHEEL
|   |           |   `-- top_level.txt
|   |           |-- tqdm
|   |           |   |-- __pycache__
|   |           |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |-- __main__.cpython-312.pyc
|   |           |   |   |-- _dist_ver.cpython-312.pyc
|   |           |   |   |-- _main.cpython-312.pyc
|   |           |   |   |-- _monitor.cpython-312.pyc
|   |           |   |   |-- _tqdm.cpython-312.pyc
|   |           |   |   |-- _tqdm_gui.cpython-312.pyc
|   |           |   |   |-- _tqdm_notebook.cpython-312.pyc
|   |           |   |   |-- _tqdm_pandas.cpython-312.pyc
|   |           |   |   |-- _utils.cpython-312.pyc
|   |           |   |   |-- asyncio.cpython-312.pyc
|   |           |   |   |-- auto.cpython-312.pyc
|   |           |   |   |-- autonotebook.cpython-312.pyc
|   |           |   |   |-- cli.cpython-312.pyc
|   |           |   |   |-- dask.cpython-312.pyc
|   |           |   |   |-- gui.cpython-312.pyc
|   |           |   |   |-- keras.cpython-312.pyc
|   |           |   |   |-- notebook.cpython-312.pyc
|   |           |   |   |-- rich.cpython-312.pyc
|   |           |   |   |-- std.cpython-312.pyc
|   |           |   |   |-- tk.cpython-312.pyc
|   |           |   |   |-- utils.cpython-312.pyc
|   |           |   |   `-- version.cpython-312.pyc
|   |           |   |-- contrib
|   |           |   |   |-- __pycache__
|   |           |   |   |   |-- __init__.cpython-312.pyc
|   |           |   |   |   |-- bells.cpython-312.pyc
|   |           |   |   |   |-- concurrent.cpython-312.pyc
|   |           |   |   |   |-- discord.cpython-312.pyc
|   |           |   |   |   |-- itertools.cpython-312.pyc
|   |           |   |   |   |-- logging.cpython-312.pyc
|   |           |   |   |   |-- slack.cpython-312.pyc
|   |           |   |   |   |-- telegram.cpython-312.pyc
|   |           |   |   |   `-- utils_worker.cpython-312.pyc
|   |           |   |   |-- __init__.py
|   |           |   |   |-- bells.py
|   |           |   |   |-- concurrent.py
|   |           |   |   |-- discord.py
|   |           |   |   |-- itertools.py
|   |           |   |   |-- logging.py
|   |           |   |   |-- slack.py
|   |           |   |   |-- telegram.py
|   |           |   |   `-- utils_worker.py
|   |           |   |-- __init__.py
|   |           |   |-- __main__.py
|   |           |   |-- _dist_ver.py
|   |           |   |-- _main.py
|   |           |   |-- _monitor.py
|   |           |   |-- _tqdm.py
|   |           |   |-- _tqdm_gui.py
|   |           |   |-- _tqdm_notebook.py
|   |           |   |-- _tqdm_pandas.py
|   |           |   |-- _utils.py
|   |           |   |-- asyncio.py
|   |           |   |-- auto.py
|   |           |   |-- autonotebook.py
|   |           |   |-- cli.py
|   |           |   |-- completion.sh
|   |           |   |-- dask.py
|   |           |   |-- gui.py
|   |           |   |-- keras.py
|   |           |   |-- notebook.py
|   |           |   |-- rich.py
|   |           |   |-- std.py
|   |           |   |-- tk.py
|   |           |   |-- tqdm.1
|   |           |   |-- utils.py
|   |           |   `-- version.py
|   |           |-- tqdm-4.67.1.dist-info
|   |           |   |-- INSTALLER
|   |           |   |-- LICENCE
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   |-- REQUESTED
|   |           |   |-- WHEEL
|   |           |   |-- entry_points.txt
|   |           |   `-- top_level.txt
|   |           |-- tzdata
|   |           |   |-- __pycache__
|   |           |   |   `-- __init__.cpython-312.pyc
|   |           |   |-- zoneinfo
|   |           |   |   |-- Africa
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- Abidjan
|   |           |   |   |   |-- Accra
|   |           |   |   |   |-- Addis_Ababa
|   |           |   |   |   |-- Algiers
|   |           |   |   |   |-- Asmara
|   |           |   |   |   |-- Asmera
|   |           |   |   |   |-- Bamako
|   |           |   |   |   |-- Bangui
|   |           |   |   |   |-- Banjul
|   |           |   |   |   |-- Bissau
|   |           |   |   |   |-- Blantyre
|   |           |   |   |   |-- Brazzaville
|   |           |   |   |   |-- Bujumbura
|   |           |   |   |   |-- Cairo
|   |           |   |   |   |-- Casablanca
|   |           |   |   |   |-- Ceuta
|   |           |   |   |   |-- Conakry
|   |           |   |   |   |-- Dakar
|   |           |   |   |   |-- Dar_es_Salaam
|   |           |   |   |   |-- Djibouti
|   |           |   |   |   |-- Douala
|   |           |   |   |   |-- El_Aaiun
|   |           |   |   |   |-- Freetown
|   |           |   |   |   |-- Gaborone
|   |           |   |   |   |-- Harare
|   |           |   |   |   |-- Johannesburg
|   |           |   |   |   |-- Juba
|   |           |   |   |   |-- Kampala
|   |           |   |   |   |-- Khartoum
|   |           |   |   |   |-- Kigali
|   |           |   |   |   |-- Kinshasa
|   |           |   |   |   |-- Lagos
|   |           |   |   |   |-- Libreville
|   |           |   |   |   |-- Lome
|   |           |   |   |   |-- Luanda
|   |           |   |   |   |-- Lubumbashi
|   |           |   |   |   |-- Lusaka
|   |           |   |   |   |-- Malabo
|   |           |   |   |   |-- Maputo
|   |           |   |   |   |-- Maseru
|   |           |   |   |   |-- Mbabane
|   |           |   |   |   |-- Mogadishu
|   |           |   |   |   |-- Monrovia
|   |           |   |   |   |-- Nairobi
|   |           |   |   |   |-- Ndjamena
|   |           |   |   |   |-- Niamey
|   |           |   |   |   |-- Nouakchott
|   |           |   |   |   |-- Ouagadougou
|   |           |   |   |   |-- Porto-Novo
|   |           |   |   |   |-- Sao_Tome
|   |           |   |   |   |-- Timbuktu
|   |           |   |   |   |-- Tripoli
|   |           |   |   |   |-- Tunis
|   |           |   |   |   |-- Windhoek
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- America
|   |           |   |   |   |-- Argentina
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- Buenos_Aires
|   |           |   |   |   |   |-- Catamarca
|   |           |   |   |   |   |-- ComodRivadavia
|   |           |   |   |   |   |-- Cordoba
|   |           |   |   |   |   |-- Jujuy
|   |           |   |   |   |   |-- La_Rioja
|   |           |   |   |   |   |-- Mendoza
|   |           |   |   |   |   |-- Rio_Gallegos
|   |           |   |   |   |   |-- Salta
|   |           |   |   |   |   |-- San_Juan
|   |           |   |   |   |   |-- San_Luis
|   |           |   |   |   |   |-- Tucuman
|   |           |   |   |   |   |-- Ushuaia
|   |           |   |   |   |   `-- __init__.py
|   |           |   |   |   |-- Indiana
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- Indianapolis
|   |           |   |   |   |   |-- Knox
|   |           |   |   |   |   |-- Marengo
|   |           |   |   |   |   |-- Petersburg
|   |           |   |   |   |   |-- Tell_City
|   |           |   |   |   |   |-- Vevay
|   |           |   |   |   |   |-- Vincennes
|   |           |   |   |   |   |-- Winamac
|   |           |   |   |   |   `-- __init__.py
|   |           |   |   |   |-- Kentucky
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- Louisville
|   |           |   |   |   |   |-- Monticello
|   |           |   |   |   |   `-- __init__.py
|   |           |   |   |   |-- North_Dakota
|   |           |   |   |   |   |-- __pycache__
|   |           |   |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |   |-- Beulah
|   |           |   |   |   |   |-- Center
|   |           |   |   |   |   |-- New_Salem
|   |           |   |   |   |   `-- __init__.py
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- Adak
|   |           |   |   |   |-- Anchorage
|   |           |   |   |   |-- Anguilla
|   |           |   |   |   |-- Antigua
|   |           |   |   |   |-- Araguaina
|   |           |   |   |   |-- Aruba
|   |           |   |   |   |-- Asuncion
|   |           |   |   |   |-- Atikokan
|   |           |   |   |   |-- Atka
|   |           |   |   |   |-- Bahia
|   |           |   |   |   |-- Bahia_Banderas
|   |           |   |   |   |-- Barbados
|   |           |   |   |   |-- Belem
|   |           |   |   |   |-- Belize
|   |           |   |   |   |-- Blanc-Sablon
|   |           |   |   |   |-- Boa_Vista
|   |           |   |   |   |-- Bogota
|   |           |   |   |   |-- Boise
|   |           |   |   |   |-- Buenos_Aires
|   |           |   |   |   |-- Cambridge_Bay
|   |           |   |   |   |-- Campo_Grande
|   |           |   |   |   |-- Cancun
|   |           |   |   |   |-- Caracas
|   |           |   |   |   |-- Catamarca
|   |           |   |   |   |-- Cayenne
|   |           |   |   |   |-- Cayman
|   |           |   |   |   |-- Chicago
|   |           |   |   |   |-- Chihuahua
|   |           |   |   |   |-- Ciudad_Juarez
|   |           |   |   |   |-- Coral_Harbour
|   |           |   |   |   |-- Cordoba
|   |           |   |   |   |-- Costa_Rica
|   |           |   |   |   |-- Coyhaique
|   |           |   |   |   |-- Creston
|   |           |   |   |   |-- Cuiaba
|   |           |   |   |   |-- Curacao
|   |           |   |   |   |-- Danmarkshavn
|   |           |   |   |   |-- Dawson
|   |           |   |   |   |-- Dawson_Creek
|   |           |   |   |   |-- Denver
|   |           |   |   |   |-- Detroit
|   |           |   |   |   |-- Dominica
|   |           |   |   |   |-- Edmonton
|   |           |   |   |   |-- Eirunepe
|   |           |   |   |   |-- El_Salvador
|   |           |   |   |   |-- Ensenada
|   |           |   |   |   |-- Fort_Nelson
|   |           |   |   |   |-- Fort_Wayne
|   |           |   |   |   |-- Fortaleza
|   |           |   |   |   |-- Glace_Bay
|   |           |   |   |   |-- Godthab
|   |           |   |   |   |-- Goose_Bay
|   |           |   |   |   |-- Grand_Turk
|   |           |   |   |   |-- Grenada
|   |           |   |   |   |-- Guadeloupe
|   |           |   |   |   |-- Guatemala
|   |           |   |   |   |-- Guayaquil
|   |           |   |   |   |-- Guyana
|   |           |   |   |   |-- Halifax
|   |           |   |   |   |-- Havana
|   |           |   |   |   |-- Hermosillo
|   |           |   |   |   |-- Indianapolis
|   |           |   |   |   |-- Inuvik
|   |           |   |   |   |-- Iqaluit
|   |           |   |   |   |-- Jamaica
|   |           |   |   |   |-- Jujuy
|   |           |   |   |   |-- Juneau
|   |           |   |   |   |-- Knox_IN
|   |           |   |   |   |-- Kralendijk
|   |           |   |   |   |-- La_Paz
|   |           |   |   |   |-- Lima
|   |           |   |   |   |-- Los_Angeles
|   |           |   |   |   |-- Louisville
|   |           |   |   |   |-- Lower_Princes
|   |           |   |   |   |-- Maceio
|   |           |   |   |   |-- Managua
|   |           |   |   |   |-- Manaus
|   |           |   |   |   |-- Marigot
|   |           |   |   |   |-- Martinique
|   |           |   |   |   |-- Matamoros
|   |           |   |   |   |-- Mazatlan
|   |           |   |   |   |-- Mendoza
|   |           |   |   |   |-- Menominee
|   |           |   |   |   |-- Merida
|   |           |   |   |   |-- Metlakatla
|   |           |   |   |   |-- Mexico_City
|   |           |   |   |   |-- Miquelon
|   |           |   |   |   |-- Moncton
|   |           |   |   |   |-- Monterrey
|   |           |   |   |   |-- Montevideo
|   |           |   |   |   |-- Montreal
|   |           |   |   |   |-- Montserrat
|   |           |   |   |   |-- Nassau
|   |           |   |   |   |-- New_York
|   |           |   |   |   |-- Nipigon
|   |           |   |   |   |-- Nome
|   |           |   |   |   |-- Noronha
|   |           |   |   |   |-- Nuuk
|   |           |   |   |   |-- Ojinaga
|   |           |   |   |   |-- Panama
|   |           |   |   |   |-- Pangnirtung
|   |           |   |   |   |-- Paramaribo
|   |           |   |   |   |-- Phoenix
|   |           |   |   |   |-- Port-au-Prince
|   |           |   |   |   |-- Port_of_Spain
|   |           |   |   |   |-- Porto_Acre
|   |           |   |   |   |-- Porto_Velho
|   |           |   |   |   |-- Puerto_Rico
|   |           |   |   |   |-- Punta_Arenas
|   |           |   |   |   |-- Rainy_River
|   |           |   |   |   |-- Rankin_Inlet
|   |           |   |   |   |-- Recife
|   |           |   |   |   |-- Regina
|   |           |   |   |   |-- Resolute
|   |           |   |   |   |-- Rio_Branco
|   |           |   |   |   |-- Rosario
|   |           |   |   |   |-- Santa_Isabel
|   |           |   |   |   |-- Santarem
|   |           |   |   |   |-- Santiago
|   |           |   |   |   |-- Santo_Domingo
|   |           |   |   |   |-- Sao_Paulo
|   |           |   |   |   |-- Scoresbysund
|   |           |   |   |   |-- Shiprock
|   |           |   |   |   |-- Sitka
|   |           |   |   |   |-- St_Barthelemy
|   |           |   |   |   |-- St_Johns
|   |           |   |   |   |-- St_Kitts
|   |           |   |   |   |-- St_Lucia
|   |           |   |   |   |-- St_Thomas
|   |           |   |   |   |-- St_Vincent
|   |           |   |   |   |-- Swift_Current
|   |           |   |   |   |-- Tegucigalpa
|   |           |   |   |   |-- Thule
|   |           |   |   |   |-- Thunder_Bay
|   |           |   |   |   |-- Tijuana
|   |           |   |   |   |-- Toronto
|   |           |   |   |   |-- Tortola
|   |           |   |   |   |-- Vancouver
|   |           |   |   |   |-- Virgin
|   |           |   |   |   |-- Whitehorse
|   |           |   |   |   |-- Winnipeg
|   |           |   |   |   |-- Yakutat
|   |           |   |   |   |-- Yellowknife
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- Antarctica
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- Casey
|   |           |   |   |   |-- Davis
|   |           |   |   |   |-- DumontDUrville
|   |           |   |   |   |-- Macquarie
|   |           |   |   |   |-- Mawson
|   |           |   |   |   |-- McMurdo
|   |           |   |   |   |-- Palmer
|   |           |   |   |   |-- Rothera
|   |           |   |   |   |-- South_Pole
|   |           |   |   |   |-- Syowa
|   |           |   |   |   |-- Troll
|   |           |   |   |   |-- Vostok
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- Arctic
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- Longyearbyen
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- Asia
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- Aden
|   |           |   |   |   |-- Almaty
|   |           |   |   |   |-- Amman
|   |           |   |   |   |-- Anadyr
|   |           |   |   |   |-- Aqtau
|   |           |   |   |   |-- Aqtobe
|   |           |   |   |   |-- Ashgabat
|   |           |   |   |   |-- Ashkhabad
|   |           |   |   |   |-- Atyrau
|   |           |   |   |   |-- Baghdad
|   |           |   |   |   |-- Bahrain
|   |           |   |   |   |-- Baku
|   |           |   |   |   |-- Bangkok
|   |           |   |   |   |-- Barnaul
|   |           |   |   |   |-- Beirut
|   |           |   |   |   |-- Bishkek
|   |           |   |   |   |-- Brunei
|   |           |   |   |   |-- Calcutta
|   |           |   |   |   |-- Chita
|   |           |   |   |   |-- Choibalsan
|   |           |   |   |   |-- Chongqing
|   |           |   |   |   |-- Chungking
|   |           |   |   |   |-- Colombo
|   |           |   |   |   |-- Dacca
|   |           |   |   |   |-- Damascus
|   |           |   |   |   |-- Dhaka
|   |           |   |   |   |-- Dili
|   |           |   |   |   |-- Dubai
|   |           |   |   |   |-- Dushanbe
|   |           |   |   |   |-- Famagusta
|   |           |   |   |   |-- Gaza
|   |           |   |   |   |-- Harbin
|   |           |   |   |   |-- Hebron
|   |           |   |   |   |-- Ho_Chi_Minh
|   |           |   |   |   |-- Hong_Kong
|   |           |   |   |   |-- Hovd
|   |           |   |   |   |-- Irkutsk
|   |           |   |   |   |-- Istanbul
|   |           |   |   |   |-- Jakarta
|   |           |   |   |   |-- Jayapura
|   |           |   |   |   |-- Jerusalem
|   |           |   |   |   |-- Kabul
|   |           |   |   |   |-- Kamchatka
|   |           |   |   |   |-- Karachi
|   |           |   |   |   |-- Kashgar
|   |           |   |   |   |-- Kathmandu
|   |           |   |   |   |-- Katmandu
|   |           |   |   |   |-- Khandyga
|   |           |   |   |   |-- Kolkata
|   |           |   |   |   |-- Krasnoyarsk
|   |           |   |   |   |-- Kuala_Lumpur
|   |           |   |   |   |-- Kuching
|   |           |   |   |   |-- Kuwait
|   |           |   |   |   |-- Macao
|   |           |   |   |   |-- Macau
|   |           |   |   |   |-- Magadan
|   |           |   |   |   |-- Makassar
|   |           |   |   |   |-- Manila
|   |           |   |   |   |-- Muscat
|   |           |   |   |   |-- Nicosia
|   |           |   |   |   |-- Novokuznetsk
|   |           |   |   |   |-- Novosibirsk
|   |           |   |   |   |-- Omsk
|   |           |   |   |   |-- Oral
|   |           |   |   |   |-- Phnom_Penh
|   |           |   |   |   |-- Pontianak
|   |           |   |   |   |-- Pyongyang
|   |           |   |   |   |-- Qatar
|   |           |   |   |   |-- Qostanay
|   |           |   |   |   |-- Qyzylorda
|   |           |   |   |   |-- Rangoon
|   |           |   |   |   |-- Riyadh
|   |           |   |   |   |-- Saigon
|   |           |   |   |   |-- Sakhalin
|   |           |   |   |   |-- Samarkand
|   |           |   |   |   |-- Seoul
|   |           |   |   |   |-- Shanghai
|   |           |   |   |   |-- Singapore
|   |           |   |   |   |-- Srednekolymsk
|   |           |   |   |   |-- Taipei
|   |           |   |   |   |-- Tashkent
|   |           |   |   |   |-- Tbilisi
|   |           |   |   |   |-- Tehran
|   |           |   |   |   |-- Tel_Aviv
|   |           |   |   |   |-- Thimbu
|   |           |   |   |   |-- Thimphu
|   |           |   |   |   |-- Tokyo
|   |           |   |   |   |-- Tomsk
|   |           |   |   |   |-- Ujung_Pandang
|   |           |   |   |   |-- Ulaanbaatar
|   |           |   |   |   |-- Ulan_Bator
|   |           |   |   |   |-- Urumqi
|   |           |   |   |   |-- Ust-Nera
|   |           |   |   |   |-- Vientiane
|   |           |   |   |   |-- Vladivostok
|   |           |   |   |   |-- Yakutsk
|   |           |   |   |   |-- Yangon
|   |           |   |   |   |-- Yekaterinburg
|   |           |   |   |   |-- Yerevan
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- Atlantic
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- Azores
|   |           |   |   |   |-- Bermuda
|   |           |   |   |   |-- Canary
|   |           |   |   |   |-- Cape_Verde
|   |           |   |   |   |-- Faeroe
|   |           |   |   |   |-- Faroe
|   |           |   |   |   |-- Jan_Mayen
|   |           |   |   |   |-- Madeira
|   |           |   |   |   |-- Reykjavik
|   |           |   |   |   |-- South_Georgia
|   |           |   |   |   |-- St_Helena
|   |           |   |   |   |-- Stanley
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- Australia
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- ACT
|   |           |   |   |   |-- Adelaide
|   |           |   |   |   |-- Brisbane
|   |           |   |   |   |-- Broken_Hill
|   |           |   |   |   |-- Canberra
|   |           |   |   |   |-- Currie
|   |           |   |   |   |-- Darwin
|   |           |   |   |   |-- Eucla
|   |           |   |   |   |-- Hobart
|   |           |   |   |   |-- LHI
|   |           |   |   |   |-- Lindeman
|   |           |   |   |   |-- Lord_Howe
|   |           |   |   |   |-- Melbourne
|   |           |   |   |   |-- NSW
|   |           |   |   |   |-- North
|   |           |   |   |   |-- Perth
|   |           |   |   |   |-- Queensland
|   |           |   |   |   |-- South
|   |           |   |   |   |-- Sydney
|   |           |   |   |   |-- Tasmania
|   |           |   |   |   |-- Victoria
|   |           |   |   |   |-- West
|   |           |   |   |   |-- Yancowinna
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- Brazil
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- Acre
|   |           |   |   |   |-- DeNoronha
|   |           |   |   |   |-- East
|   |           |   |   |   |-- West
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- Canada
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- Atlantic
|   |           |   |   |   |-- Central
|   |           |   |   |   |-- Eastern
|   |           |   |   |   |-- Mountain
|   |           |   |   |   |-- Newfoundland
|   |           |   |   |   |-- Pacific
|   |           |   |   |   |-- Saskatchewan
|   |           |   |   |   |-- Yukon
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- Chile
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- Continental
|   |           |   |   |   |-- EasterIsland
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- Etc
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- GMT
|   |           |   |   |   |-- GMT+0
|   |           |   |   |   |-- GMT+1
|   |           |   |   |   |-- GMT+10
|   |           |   |   |   |-- GMT+11
|   |           |   |   |   |-- GMT+12
|   |           |   |   |   |-- GMT+2
|   |           |   |   |   |-- GMT+3
|   |           |   |   |   |-- GMT+4
|   |           |   |   |   |-- GMT+5
|   |           |   |   |   |-- GMT+6
|   |           |   |   |   |-- GMT+7
|   |           |   |   |   |-- GMT+8
|   |           |   |   |   |-- GMT+9
|   |           |   |   |   |-- GMT-0
|   |           |   |   |   |-- GMT-1
|   |           |   |   |   |-- GMT-10
|   |           |   |   |   |-- GMT-11
|   |           |   |   |   |-- GMT-12
|   |           |   |   |   |-- GMT-13
|   |           |   |   |   |-- GMT-14
|   |           |   |   |   |-- GMT-2
|   |           |   |   |   |-- GMT-3
|   |           |   |   |   |-- GMT-4
|   |           |   |   |   |-- GMT-5
|   |           |   |   |   |-- GMT-6
|   |           |   |   |   |-- GMT-7
|   |           |   |   |   |-- GMT-8
|   |           |   |   |   |-- GMT-9
|   |           |   |   |   |-- GMT0
|   |           |   |   |   |-- Greenwich
|   |           |   |   |   |-- UCT
|   |           |   |   |   |-- UTC
|   |           |   |   |   |-- Universal
|   |           |   |   |   |-- Zulu
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- Europe
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- Amsterdam
|   |           |   |   |   |-- Andorra
|   |           |   |   |   |-- Astrakhan
|   |           |   |   |   |-- Athens
|   |           |   |   |   |-- Belfast
|   |           |   |   |   |-- Belgrade
|   |           |   |   |   |-- Berlin
|   |           |   |   |   |-- Bratislava
|   |           |   |   |   |-- Brussels
|   |           |   |   |   |-- Bucharest
|   |           |   |   |   |-- Budapest
|   |           |   |   |   |-- Busingen
|   |           |   |   |   |-- Chisinau
|   |           |   |   |   |-- Copenhagen
|   |           |   |   |   |-- Dublin
|   |           |   |   |   |-- Gibraltar
|   |           |   |   |   |-- Guernsey
|   |           |   |   |   |-- Helsinki
|   |           |   |   |   |-- Isle_of_Man
|   |           |   |   |   |-- Istanbul
|   |           |   |   |   |-- Jersey
|   |           |   |   |   |-- Kaliningrad
|   |           |   |   |   |-- Kiev
|   |           |   |   |   |-- Kirov
|   |           |   |   |   |-- Kyiv
|   |           |   |   |   |-- Lisbon
|   |           |   |   |   |-- Ljubljana
|   |           |   |   |   |-- London
|   |           |   |   |   |-- Luxembourg
|   |           |   |   |   |-- Madrid
|   |           |   |   |   |-- Malta
|   |           |   |   |   |-- Mariehamn
|   |           |   |   |   |-- Minsk
|   |           |   |   |   |-- Monaco
|   |           |   |   |   |-- Moscow
|   |           |   |   |   |-- Nicosia
|   |           |   |   |   |-- Oslo
|   |           |   |   |   |-- Paris
|   |           |   |   |   |-- Podgorica
|   |           |   |   |   |-- Prague
|   |           |   |   |   |-- Riga
|   |           |   |   |   |-- Rome
|   |           |   |   |   |-- Samara
|   |           |   |   |   |-- San_Marino
|   |           |   |   |   |-- Sarajevo
|   |           |   |   |   |-- Saratov
|   |           |   |   |   |-- Simferopol
|   |           |   |   |   |-- Skopje
|   |           |   |   |   |-- Sofia
|   |           |   |   |   |-- Stockholm
|   |           |   |   |   |-- Tallinn
|   |           |   |   |   |-- Tirane
|   |           |   |   |   |-- Tiraspol
|   |           |   |   |   |-- Ulyanovsk
|   |           |   |   |   |-- Uzhgorod
|   |           |   |   |   |-- Vaduz
|   |           |   |   |   |-- Vatican
|   |           |   |   |   |-- Vienna
|   |           |   |   |   |-- Vilnius
|   |           |   |   |   |-- Volgograd
|   |           |   |   |   |-- Warsaw
|   |           |   |   |   |-- Zagreb
|   |           |   |   |   |-- Zaporozhye
|   |           |   |   |   |-- Zurich
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- Indian
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- Antananarivo
|   |           |   |   |   |-- Chagos
|   |           |   |   |   |-- Christmas
|   |           |   |   |   |-- Cocos
|   |           |   |   |   |-- Comoro
|   |           |   |   |   |-- Kerguelen
|   |           |   |   |   |-- Mahe
|   |           |   |   |   |-- Maldives
|   |           |   |   |   |-- Mauritius
|   |           |   |   |   |-- Mayotte
|   |           |   |   |   |-- Reunion
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- Mexico
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- BajaNorte
|   |           |   |   |   |-- BajaSur
|   |           |   |   |   |-- General
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- Pacific
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- Apia
|   |           |   |   |   |-- Auckland
|   |           |   |   |   |-- Bougainville
|   |           |   |   |   |-- Chatham
|   |           |   |   |   |-- Chuuk
|   |           |   |   |   |-- Easter
|   |           |   |   |   |-- Efate
|   |           |   |   |   |-- Enderbury
|   |           |   |   |   |-- Fakaofo
|   |           |   |   |   |-- Fiji
|   |           |   |   |   |-- Funafuti
|   |           |   |   |   |-- Galapagos
|   |           |   |   |   |-- Gambier
|   |           |   |   |   |-- Guadalcanal
|   |           |   |   |   |-- Guam
|   |           |   |   |   |-- Honolulu
|   |           |   |   |   |-- Johnston
|   |           |   |   |   |-- Kanton
|   |           |   |   |   |-- Kiritimati
|   |           |   |   |   |-- Kosrae
|   |           |   |   |   |-- Kwajalein
|   |           |   |   |   |-- Majuro
|   |           |   |   |   |-- Marquesas
|   |           |   |   |   |-- Midway
|   |           |   |   |   |-- Nauru
|   |           |   |   |   |-- Niue
|   |           |   |   |   |-- Norfolk
|   |           |   |   |   |-- Noumea
|   |           |   |   |   |-- Pago_Pago
|   |           |   |   |   |-- Palau
|   |           |   |   |   |-- Pitcairn
|   |           |   |   |   |-- Pohnpei
|   |           |   |   |   |-- Ponape
|   |           |   |   |   |-- Port_Moresby
|   |           |   |   |   |-- Rarotonga
|   |           |   |   |   |-- Saipan
|   |           |   |   |   |-- Samoa
|   |           |   |   |   |-- Tahiti
|   |           |   |   |   |-- Tarawa
|   |           |   |   |   |-- Tongatapu
|   |           |   |   |   |-- Truk
|   |           |   |   |   |-- Wake
|   |           |   |   |   |-- Wallis
|   |           |   |   |   |-- Yap
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- US
|   |           |   |   |   |-- __pycache__
|   |           |   |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |   |-- Alaska
|   |           |   |   |   |-- Aleutian
|   |           |   |   |   |-- Arizona
|   |           |   |   |   |-- Central
|   |           |   |   |   |-- East-Indiana
|   |           |   |   |   |-- Eastern
|   |           |   |   |   |-- Hawaii
|   |           |   |   |   |-- Indiana-Starke
|   |           |   |   |   |-- Michigan
|   |           |   |   |   |-- Mountain
|   |           |   |   |   |-- Pacific
|   |           |   |   |   |-- Samoa
|   |           |   |   |   `-- __init__.py
|   |           |   |   |-- __pycache__
|   |           |   |   |   `-- __init__.cpython-312.pyc
|   |           |   |   |-- CET
|   |           |   |   |-- CST6CDT
|   |           |   |   |-- Cuba
|   |           |   |   |-- EET
|   |           |   |   |-- EST
|   |           |   |   |-- EST5EDT
|   |           |   |   |-- Egypt
|   |           |   |   |-- Eire
|   |           |   |   |-- Factory
|   |           |   |   |-- GB
|   |           |   |   |-- GB-Eire
|   |           |   |   |-- GMT
|   |           |   |   |-- GMT+0
|   |           |   |   |-- GMT-0
|   |           |   |   |-- GMT0
|   |           |   |   |-- Greenwich
|   |           |   |   |-- HST
|   |           |   |   |-- Hongkong
|   |           |   |   |-- Iceland
|   |           |   |   |-- Iran
|   |           |   |   |-- Israel
|   |           |   |   |-- Jamaica
|   |           |   |   |-- Japan
|   |           |   |   |-- Kwajalein
|   |           |   |   |-- Libya
|   |           |   |   |-- MET
|   |           |   |   |-- MST
|   |           |   |   |-- MST7MDT
|   |           |   |   |-- NZ
|   |           |   |   |-- NZ-CHAT
|   |           |   |   |-- Navajo
|   |           |   |   |-- PRC
|   |           |   |   |-- PST8PDT
|   |           |   |   |-- Poland
|   |           |   |   |-- Portugal
|   |           |   |   |-- ROC
|   |           |   |   |-- ROK
|   |           |   |   |-- Singapore
|   |           |   |   |-- Turkey
|   |           |   |   |-- UCT
|   |           |   |   |-- UTC
|   |           |   |   |-- Universal
|   |           |   |   |-- W-SU
|   |           |   |   |-- WET
|   |           |   |   |-- Zulu
|   |           |   |   |-- __init__.py
|   |           |   |   |-- iso3166.tab
|   |           |   |   |-- leapseconds
|   |           |   |   |-- tzdata.zi
|   |           |   |   |-- zone.tab
|   |           |   |   |-- zone1970.tab
|   |           |   |   `-- zonenow.tab
|   |           |   |-- __init__.py
|   |           |   `-- zones
|   |           |-- tzdata-2025.2.dist-info
|   |           |   |-- licenses
|   |           |   |   |-- licenses
|   |           |   |   |   `-- LICENSE_APACHE
|   |           |   |   `-- LICENSE
|   |           |   |-- INSTALLER
|   |           |   |-- METADATA
|   |           |   |-- RECORD
|   |           |   |-- WHEEL
|   |           |   `-- top_level.txt
|   |           |-- py.py
|   |           |-- pylab.py
|   |           `-- six.py
|   |-- share
|   |   `-- man
|   |       `-- man1
|   |           `-- ttx.1
|   `-- pyvenv.cfg
|-- Agents
|   `-- issue_auto_solver.py
|-- config
|   `-- roster
|       |-- roster.csv
|       `-- roster_sample.csv
|-- docs
|   |-- DEVELOPMENT_FLOW.md
|   |-- DEVELOPMENT_WORKFLOW.md
|   |-- ENVIRONMENT_SETUP.md
|   |-- GUI_implementation.md
|   |-- GUI_requirements.md
|   |-- JAPANESE_SUPPORT.md
|   |-- SEGMENT_ROUNDS_DOCUMENTATION.md
|   `-- minimap_pipeline_worklog.md
|-- mapsight
|   |-- analysis
|   |   |-- __pycache__
|   |   |   |-- __init__.cpython-312.pyc
|   |   |   `-- player_tracking.cpython-312.pyc
|   |   |-- __init__.py
|   |   `-- player_tracking.py
|   `-- schemas
|       `-- positions.py
|-- notebook
|   |-- __init__.py
|   `-- colab_pipeline.py
|-- schemas
|   `-- player_position.schema.json
|-- screenshot
|   |-- sample
|   |   |-- frame_00559.jpg
|   |   `-- frame_01387.jpg
|   |-- connect_wsl.png
|   `-- スクリーンショット 2025-10-01 135237.png
|-- scripts
|   `-- issue_auto_solver.py
|-- src
|   |-- __pycache__
|   |   |-- clean_same_frames.cpython-312.pyc
|   |   `-- segment_rounds.cpython-312.pyc
|   |-- gui
|   |   |-- main.py
|   |   `-- styles.py
|   |-- check_env.py
|   |-- clean_same_frames.py
|   |-- crop_minimap.py
|   |-- segment_rounds.py
|   |-- segment_rounds_updated.py
|   `-- utils.py
|-- tests
|   |-- __pycache__
|   |   |-- test_clean_same_frames.cpython-312-pytest-8.3.5.pyc
|   |   |-- test_clean_same_frames.cpython-312-pytest-8.4.2.pyc
|   |   |-- test_player_tracking.cpython-312-pytest-8.3.5.pyc
|   |   |-- test_player_tracking.cpython-312-pytest-8.4.2.pyc
|   |   |-- test_segment_rounds.cpython-312-pytest-8.3.5.pyc
|   |   `-- test_segment_rounds.cpython-312-pytest-8.4.2.pyc
|   |-- sample
|   |   `-- test_detect.py
|   |-- test_clean_same_frames.py
|   |-- test_player_tracking.py
|   `-- test_segment_rounds.py
|-- .gitignore
|-- .markdownlint.json
|-- AGENTS.md
|-- MapSight_AI_Colab.ipynb
|-- PROJECT_STATUS.md
|-- QUICK_GUIDE.md
|-- README.md
|-- TREE.md
|-- config.yaml
|-- erangel_players.json
|-- extract_frames.sh
|-- idea.md
|-- requirements.txt
|-- survey.md
|-- データ設計.md
`-- 作業メモ.md

907 directories, 9108 files
```
<!-- DIR-END -->

## 動画URLからフレーム抽出  

MapSight_AI/data でコマンド実行．
コマンド例:
./extract_frames.sh "https://www.youtube.com/watch?v=tkbV9EJPak4"

・fps=2 → 0.5 s ごとに 1 枚（後で変更可能） # 0.5に変更済み
・生成先 data/frames/<公開日>/ は後段スクリプトが再帰検索します。
・画質を保ちたい場合は -q:v 2（2-31、数字が小さいほど高画質）。

## githubの開発フロー早わかり・説明

### Workflow (for my future self)

```text
1. Create an Issue (task / bug / log)
2. Move it to **In Progress** on Projects
3. Commit with `feat: ...  #123`
4. Open PR, merge -> Done (auto-closed)

```

まとめ

```text
    Issues = タスク＋作業ログ

    Projects = カンバンで見える化

    Actions（任意） = 毎日まとめてログ

    これだけで GitHub 内でタスク管理／履歴／振り返りが完結

    後からチームが増えても、そのままスケールアップできる

```

### commit テンプレ

```text
<type>(scope): <短い概要>  #<Issue番号>

type = feat | fix | docs | refactor | chore | test  
scope = オプション: モジュール名や機能名  

<例>
feat(map): add heatmap aggregation logic  #23
fix(ml): prevent NaN in MLP loss          #45
```

### プルリクのテンプレ

```text
概要 / Purpose
<!-- 何を・なぜ -->

🔗 関連 Issue
Fixes #123  <!-- 自動 Close したい場合は Fixes/Closes キーワード -->

✅ チェックリスト
- [ ] ビルドが通る
- [ ] 仕様書 / docs 更新
```

## 🌱 Development Workflow

1. **Issue を作る** (Task/Bug/Log)
2. **Projects の Todo** に置く
3. **branch**:`feature/<short-desc>` → コード
4. `feat: ...  #issue` で commit
5. PR → Merge → Projects Done (auto-archive)

👉 [Backlog Board](https://github.com/<user>/<repo>/projects/1) で全タスクを確認

## データ取得の流れ

仮想環境:pubgmapenvの中で

1. extract_frames.sh に対象URLを渡して実行(data/framesに画像データが生成される)
2. crop_minimap.pyを実行（対象ディレクトリの箇所を適宜変更）
3. clean_same_frames.pyを実行
4. segment_rounds.pyを実行

この段階でラウンドごとにマップ画像が保存される．（まだ不必要なデータが含まれている）
