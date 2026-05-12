import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from data_dirs import create_scrim, create_tournament


def test_create_scrim(tmp_path: Path) -> None:
    d = create_scrim("2024/05/06", rounds=2, root=tmp_path)
    assert (d / "Round1").is_dir()
    assert (d / "Round2").is_dir()


def test_create_tournament(tmp_path: Path) -> None:
    t = create_tournament("PMGC2024", root=tmp_path)
    assert t.is_dir()
