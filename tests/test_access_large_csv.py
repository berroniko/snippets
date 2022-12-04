import unittest

from snippets.access_large_csv import access_large_csv

class TestGenerator(unittest.TestCase):

    def setUp(self):
        self.file = "test_data/ACWI.csv"

    def test_return_column(self):
        csv_gen = access_large_csv(self.file, "Close")
        result = next(csv_gen)
        self.assertEqual(result, str(50.099998))


if __name__ == '__main__':
    unittest.main()
