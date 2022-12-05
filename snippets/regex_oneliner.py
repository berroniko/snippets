import re


def regex_oneliner(string):
    """Short version of regex application.

    Example:
        Extract numbers at the end of a string.

        >>> regex_oneliner("asldkj1.23")
        "23"
    """
    res = re.search(r'(\d+)$', string)  # numbers at end of string

    if res:
        return res.group()
    else:
        return None


if "__name__" == "__main__":
    string = 'abckeid_34.5'
    print(regex_oneliner(string))
