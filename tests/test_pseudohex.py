import unittest

from pseudohex import Pseudohex


class test_pseudohex(unittest.TestCase):
    def test_int(self):
        p = Pseudohex()
        self.assertEquals(0, int(p))

    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            p = Pseudohex('@')
        with self.assertRaises(ValueError):
            p = Pseudohex(99)

    def test_str(self):
        p = Pseudohex(12)
        self.assertEquals('C', str(p))

    def test_equality(self):
        p = Pseudohex(6)
        self.assertTrue(p == 6)
        self.assertFalse(p == 7)
        self.assertTrue(p == '6')
        self.assertFalse(p == '7')

    def test_inequality(self):
        p = Pseudohex(7)
        self.assertTrue(p != 6)
        self.assertFalse(p != 7)
        self.assertTrue(p != '6')
        self.assertFalse(p != '7')

    def test_no_negative(self):
        with self.assertRaises(ValueError):
            p = Pseudohex(-1)
