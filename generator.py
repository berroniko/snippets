import csv

# load data
file = "data/ACWI.csv"


def access_large_csv(filepath, fieldname):
    """opens csv file on filepath, provides the content as a generator yielding the elements of fieldname
    it is thus able to handle files larger than the available memory"""
    with open(file) as f:
        content = csv.reader(f)
        # header is the first line of content
        header = next(content)
        # print(header)
        # find the position of fieldname in header
        if fieldname in header:
            pos = header.index(fieldname)
        else:
            print("{} does not exist in file {}".format(fieldname, filepath))
            print('header: ', header)
        while True:
            try:
                yield next(content)[pos]
            except StopIteration:
                break


if __name__ == '__main__':

    # access using next()
    csv_gen = access_large_csv(file, "Close")
    while True:
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
    # for index, _ in zip(access_large_csv(file, "Close"), range(5)):  # range only defines the end of the loop
    #     print(index)

    for i in access_large_csv(file, "Close"):
        print(i)