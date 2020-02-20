#!/usr/bin/python3
"""Unittest for teh console"""


import unittest
import pep8


class Test_Console(unittest.TestCase):
    """Cases"""

    def test_pep8(self):
        """Test pep8 style"""
        pep8st = pep8.StyleGuide(quiet=True)
        res = pep8st.check_files(['console.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == "__main__":
    unittest.main()
