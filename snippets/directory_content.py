from pathlib import Path
from typing import List


def directory_content(filepath=Path.cwd(), kind: str = 'file') -> List:
    """get content of a directory.

    Only the contents of the directory itself is returned, not the contents of any subdirectories

    Args:
        filepath (optional): Path to the directory, default is current working directory
        kind (str): 'file' (default) for files
                    'dir' for directories
                    'all' for files and directories
                    or a search pattern as '*.py'

    Returns:
        List: Content of the specified kind
    """
    result = []

    d = Path(filepath)

    if kind in ['file', 'dir', 'all']:
        for elem in d.iterdir():
            if elem.is_file() and (kind == 'file' or kind == 'all'):
                result.append(elem)
            if elem.is_dir() and (kind == 'dir' or kind == 'all'):
                result.append(elem)
    else:
        result = d.glob(kind)
    return sorted(result)


if __name__ == '__main__':
    import pprint

    dir_path = r'../snippets'''
    pprint.pprint(directory_content(filepath=dir_path, kind="g*"))
