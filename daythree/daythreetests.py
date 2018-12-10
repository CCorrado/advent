import unittest

from daythree.daythree import get_result


class DayThreeTests(unittest.TestCase):

    def test_one(self):
        self.assertEqual(4, get_result("testdata1"))
