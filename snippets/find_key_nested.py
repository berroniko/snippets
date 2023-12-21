from typing import List, Generator


#  https://stackoverflow.com/questions/9807634/find-all-occurrences-of-a-key-in-nested-dictionaries-and-lists

def gen_dict_extract(key: str, var: dict | List[dict]) -> Generator:
    """Extract all occurrences of a keyword in a nested dictionary that may include lists of dictionaries.

    Args:
        var: the dictionary to be searched
        key: the key being searched for

    Returns:
        generator yielding all values related to the key
    """
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result
