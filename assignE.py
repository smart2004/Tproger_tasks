import unittest

a = 1
b = 2
c = 3
d = -4
e = 5
f = 6
g = 7
h = -8

def add(x, y):
    return(x + y)

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(a, b), c)

    def test_add_negative_numbers(self):
        self.assertEqual(add(d, d), h)

if __name__ == '__main__':
    unittest.main()
