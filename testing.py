import unittest

def add(a,b):
    return a+b
def multiply(a,b):
    return a*b

class TestAPI(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10,20),30)
    def test_multiply(self):
        self.assertEqual(multiply(10,5),50)
    def test_negative(self):
        self.assertEqual(add(10,-20),-10)
    def test_zero(self):
        self.assertEqual(multiply(10,0),0)

if __name__=="__main__":
    unittest.main()