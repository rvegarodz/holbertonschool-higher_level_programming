import unittest

class TestMaxInteger(unittest.TestCase):
    def runTest(self):
        self.assertEqual(max_integer([1, 7, 3, 5]), 7)