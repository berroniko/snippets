from snippets.access_large_csv import access_large_csv


def test_return_column():
    filename = "./tests/test_data/ACWI.csv"
    csv_gen = access_large_csv(filename, "Close")
    result = next(csv_gen)
    assert result == str(50.099998)
