import json
from typing import Any


class jsonPlugin:
    def read_json(self, filename):
        with open(filename) as f:
            return json.load(f)

    def write_json(self, filename, data):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def append_data_to_file(self, filename: str, data: Any):
        """Append data to existing json - file.

        The content of the file needs to be a list, data will be appended as new entry to the list

        Args:
            filename: the file to be updated
            data: the data to append

        Returns:
            data_json: data as stored to filename
        """

        try:
            data_json = self.read_json(filename)
        except FileNotFoundError as err:
            print(f'{err}')
            print(f'{filename} created \n')
            data_json = []
        data_json.append(data)
        self.write_json(filename, data_json)

        return data_json
