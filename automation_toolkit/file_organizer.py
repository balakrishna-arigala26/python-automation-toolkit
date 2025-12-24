from pathlib import Path


def organize_file(source: Path, target_dir: Path) -> Path:
    """
    Move a file into the target directory.
    Creates target directory if it does not exist.
    Overwrites existing file with the same name.
    """
    if not source.exists():
        raise FileNotFoundError(f"{source} does not exist")

    target_dir.mkdir(parents=True, exist_ok=True)

    target_file = target_dir / source.name
    target_file.write_text(source.read_text())

    return target_file
