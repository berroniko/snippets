import pytest
import os
import json
import pprint
import sys
sys.path.append(".")
from snippets.json_plugin import jsonPlugin


class TestJsonPlugin:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.plugin = jsonPlugin()
        self.test_file = 'test.json'
        self.test_data = {"key": "value"}
        yield
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read_json(self):
        with open(self.test_file, 'w') as f:
            json.dump(self.test_data, f)
        result = self.plugin.read_json(self.test_file)
        assert result == self.test_data

    def test_write_json(self):
        self.plugin.write_json(self.test_file, self.test_data)
        with open(self.test_file) as f:
            result = json.load(f)
        assert result == self.test_data

    def test_append_data_to_file(self):
        initial_data = [{"key1": "value1"}]
        append_data = {"key2": "value2"}
        expected_data = initial_data + [append_data]

        with open(self.test_file, 'w') as f:
            json.dump(initial_data, f)

        result = self.plugin.append_data_to_file(self.test_file, append_data)
        assert result == expected_data


if __name__ == '__main__':
    pytest.main(['-v', __file__])
