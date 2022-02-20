import unittest

from regex_oneliner import regex_oneliner


class RegexTest(unittest.TestCase):

    def test_number_after_str(self):
        string = 'abckeidasdf45'
        result = regex_oneliner(string)
        self.assertEqual('45', result)

    def test_number_after_dot(self):
        string = 'abckeidasdf34.45'
        result = regex_oneliner(string)
        self.assertEqual('45', result)

    def test_no_number(self):
        string = 'abckeidasdf'
        result = regex_oneliner(string)
        self.assertEqual(None, result)
