import unittest

from dayone.dayone import get_result


class DayOneTests(unittest.TestCase):

    def test_one(self):
        self.assertEqual(0, get_result("testdata1"))

    def test_two(self):
        self.assertEqual(10, get_result("testdata2"))

    def test_three(self):
        self.assertEqual(5, get_result("testdata3"))

    def test_four(self):
        self.assertEqual(14, get_result("testdata4"))
