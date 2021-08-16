import unittest
from hw21 import merge


class TestMerge(unittest.TestCase):
    def test_size_0(self):
        self.assertEqual(list(merge((x for x in range(0)), (y for y in range(0)))), [])

    def test_2(self):
        self.assertEqual(list(merge((x for x in range(1,4)),(x for x in range(2,5)))), [1, 2, 2, 3, 3, 4])

    def test_3(self):
        self.assertEqual(list(merge((x for x in range(11, 25, 3) if not x),
                                    (x for x in range(13, 24, 2)))),
                         [13, 15, 17, 19, 21, 23])

    def test_4(self):
        self.assertEqual(list(merge((a for a in range(20)), (b for b in range(10)))),
                         [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8,
                          8, 9, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

