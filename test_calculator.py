import unittest
from calculator import multiply

class TestSomething(unittest.TestCase):
	def test_multiply(self):
		self.assertEqual(4, multiply(2,2))

if __name__ == '__main__':
	unittest.main()



