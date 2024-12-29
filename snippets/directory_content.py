from pathlib import Path
from typing import List


def directory_content(kind: str = 'file', filepath: Path | str | None = None) -> List[Path]:
    """get content of a directory.

    Only the contents of the directory itself is returned, not the contents of any subdirectories

    Args:
        filepath (optional): Path to the directory, default is current working directory
        kind (str): 'file' (default) for files
                    'dir' for directories
                    'all' for files and directories
                    or a search pattern as '*.py'

    Returns:
        List[Path]: Content of the specified kind.
    """
    result = []

    d = Path(filepath) if filepath else Path.cwd()

    if kind in ['file', 'dir', 'all']:
        result = [
            elem for elem in d.iterdir()
            if (elem.is_file() and kind in ['file', 'all']) or (elem.is_dir() and kind in ['dir', 'all'])
        ]
    else:
        result = list(d.glob(kind))

    return sorted(result)


if __name__ == '__main__':
    import pprint
    print(Path.cwd())

    dir_path = r"./snippets"
    pprint.pprint(directory_content(filepath=dir_path, kind="s*"))

    pprint.pprint(directory_content(kind="s*"))


