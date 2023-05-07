import csv


def access_large_csv(filepath: str,
                     fieldname: str) -> str:
    """Yields elements from csv-file.

    Opens csv-file and provides the content as a generator yielding the elements of the column `fieldname`.
    It is able to handle files larger than the available memory.

    Args:
        filepath : path to the file to be read
        fieldname : key of the column to be returned

    Yields:
        Elements of the selected columns. One row per call
    """

    with open(filepath) as f:
        content = csv.reader(f)
        header = next(content)  # the first line of content

        if fieldname in header:
            pos = header.index(fieldname)  # the position of fieldname in header
        else:
            print(f"{fieldname} does not exist in file {filepath}")
            print(f"header: {header}")
        while True:
            try:
                yield next(content)[pos]
            except StopIteration:
                break


if __name__ == '__main__':

    # load data
    file = "../tests/test_data/ACWI.csv"

    # access using next()
    csv_gen = access_large_csv(file, "Close")
    while False:
        try:
            print(next(csv_gen))
        except StopIteration:
            break

    # or by send
    csv_gen = access_large_csv(file, "Close")
    while True:
        try:
            print(csv_gen.send(None))
        except StopIteration:
            break

    # or by loop
    while False:
        for index, _ in zip(access_large_csv(file, "Close"), range(5)):  # range only defines the end of the loop
            print(index)

    while False:  # without range all rows are printed
        for i in access_large_csv(file, "Close"):
            print(i)
