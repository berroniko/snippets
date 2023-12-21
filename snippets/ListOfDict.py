import json
from typing import List

# import pandas as pd
from abc import ABCMeta
from pathlib import Path


class ListOfDictContainer(metaclass=ABCMeta):
    def __init__(self, filepath: Path, alternative_keys: dict = None):
        """Baseclass to handle lists of dictionaries
        Args:
            filepath (Path): Path to the json-file storing the list of dicts
            alternative_keys (Dict, optional): Dictionary in the format { alternative_key: valid_key }
            """
        self.alternative_keys = alternative_keys
        self.filepath = filepath
        with open(self.filepath) as f:
            self.data = json.load(f)

    def __iter__(self):
        """make the content of the class iterable"""
        return iter(self.data)

    def __len__(self):
        """return the number of entries"""
        return len(self.data)

    def _clean_data(self, data):
        return data

    def _unique_keys(self, data):
        """change keys to predefined keys"""
        unique = []
        for elem in data:
            unique_elem = {self.alternative_keys.get(k, k.strip("'")): v for k, v in elem.items()}
            unique.append(unique_elem)
        return unique

    def save(self, path_to_file: Path = None):
        """save the current dataset to a json file
        Args:
            path_to_file (Path, optional): Defaults to the standard filepath of the class
        """
        _filepath = path_to_file or self.filepath
        with open(_filepath, 'w') as f:
            json.dump(self.data, f)
            # logging.info(f"data saved to {self.filepath}")

    # def update_from_excel(self, path_to_excel: Path) -> None:
    #     """update both the json file and instance of the classe from an Excel sheet."""
    #     df = pd.read_excel(path_to_excel)
    #     raw_data = df.to_dict(orient='records')
    #     self.update_from_upload(data=raw_data)

    def update_from_file(self, path_to_file: Path) -> None:
        """update both the json file and instance of the classe from a file (.json)."""
        with open(path_to_file) as f:
            raw_data = json.load(f)
        self.update_from_upload(data=raw_data)

    def update_from_upload(self, data) -> None:
        """update both the json file and instance of the classe from a dataset."""
        unique_data = self._unique_keys(data=data) if self.alternative_keys else data
        self.data = self._clean_data(unique_data)
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f)
            # logging.info(f"ListOfDictContainer.update_from_upload() data saved to {self.filepath}")

    def get_entries(self, key, value):
        """get all entries with a given key value pair"""
        results = []
        for entry in self.data:
            if str(entry.get(key)) == str(value):
                results.append(entry)
        return results

    def get_entries_partial(self, key, expression):
        """get all entries with the expression being part of the key's value"""
        results = []
        for entry in self.data:
            if expression in entry.get(key):
                results.append(entry)
        return results

    def find(self, search: dict, display: dict = None) -> List[dict]:
        """retrieve dictionary in a list of dicts that contains given key value pair(s)

        A mongo-like search function that searches data (a list of dictionaries),
        returns a list with all elements in data that fulfill the key value pairs in the search dictionary
        and if the optional display dictionary is specified, return keys with value 1 or all those not 0

        Args:
            search: key value pairs that must be contained
            display: optional, extract keys from the retrieved dictionary to be returned

        Returns:
            list of dictionaries fulfilling search and display criteria

        Example:
            find_in_list_of_dict(search: {'ID': '1EC21030423', "nombreFactura": "IMM HARMONIE CREAM 50ML"},
                                display: {"presentacionComercial": 1})
            [{"presentacionComercial": "COS-512498"}]
        """

        results = []
        for elem in (dict(line) for line in self.data):
            if all([elem.get(k, None) == v for k, v in search.items()]):
                if display:
                    if sum(display.values()) > 0:  # display has elements with 1, defining what to show
                        reduced_elem = {k: v for k, v in elem.items() if display.get(k, None) == 1}
                    else:  # display has elements with 0, thus defining what not to show
                        reduced_elem = {k: v for k, v in elem.items() if display.get(k, None) != 0}
                    results.append(reduced_elem)
                else:
                    results.append(elem)
        return results
