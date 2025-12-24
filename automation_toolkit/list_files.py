from pathlib import Path
from typing import List, Optional


def list_files(directory: Path, extension: Optional[str] = None) -> List[Path]:
    """
    List files in a directory.
    Optionally filter by file extension.
    """
    if not directory.exists():
        return []

    files = []

    for item in directory.iterdir():
        if item.is_file():
            if extension is None or item.suffix == extension:
                files.append(item)

    return files
