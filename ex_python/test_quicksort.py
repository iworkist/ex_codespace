import unittest
from quicksort import quicksort

class TestQuicksort(unittest.TestCase):
    def test_quicksort(self):
        self.assertEqual(quicksort([1, 3, 5, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()

# $ python3 -m unittest test_quicksort.py

        
