import pytest

from automation_toolkit.file_organizer import organize_file


def test_organize_file_creates_target_dir(tmp_path):
    src = tmp_path / "sample.txt"
    src.write_text("hello")

    target_dir = tmp_path / "organized"

    result = organize_file(src, target_dir)

    assert result.exists()
    assert result.parent == target_dir
    assert result.read_text() == "hello"


def test_organize_file_existing_file(tmp_path):
    src = tmp_path / "sample.txt"
    src.write_text("new")

    target_dir = tmp_path / "organized"
    target_dir.mkdir()

    existing = target_dir / "sample.txt"
    existing.write_text("old")

    result = organize_file(src, target_dir)

    assert result.exists()
    assert result.read_text() == "new"


def test_organize_file_missing_source(tmp_path):
    missing_file = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError):
        organize_file(missing_file, tmp_path / "out")
