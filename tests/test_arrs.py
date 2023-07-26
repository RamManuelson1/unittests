import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])

    def test_slice_with_negative_start_index(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -3, 4), [3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -2), [4, 5])

    def test_slice_with_negative_end_index(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 1, -1), [2, 3, 4])

    def test_slice_with_negative_indices_out_of_range(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -7, -6), [])

    def test_slice_with_start_index_greater_than_end_index(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 3, 1), [])

    def test_slice_with_end_index_equal_to_start_index(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 2, 2), [])

    def test_slice_with_end_index_greater_than_length(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 2, 10), [3, 4, 5])
    def test_slice_with_default_arguments(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(arrs.my_slice([]), [])