import unittest
from hw23 import n_arr


class TestNarr(unittest.TestCase):
    def test_size_0(self):
        self.assertEqual(n_arr([]), [])

    def test_size_4(self):
        self.assertEqual(n_arr([4]), ['""', '""', '""', '""'])

    def test_size_2_3(self):
        self.assertEqual(n_arr([2, 2]), [['""', '""'], ['""', '""']])

    def test_size_2_3_4(self):
        self.assertEqual(n_arr([2, 3, 4]), [[['""', '""'], ['""', '""'], ['""', '""']],
                                            [['""', '""'], ['""', '""'], ['""', '""']],
                                            [['""', '""'], ['""', '""'], ['""', '""']],
                                            [['""', '""'], ['""', '""'], ['""', '""']]])

    def test_unique(self):
        res = n_arr([2, 3, 4])
        res[0][0][0] = 22
        self.assertNotEqual(res[0][1][0], 22)
