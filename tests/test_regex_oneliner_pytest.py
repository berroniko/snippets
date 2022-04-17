from snippets.regex_oneliner import regex_oneliner


def test_number_after_str():
    string = 'abckeidasdf45'
    result = regex_oneliner(string)
    assert "45" == result


def test_number_at_beginning():
    string = '45abckeidasdf'
    result = regex_oneliner(string)
    assert result is None

