import unittest
from example import Examples


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This will run once before all the methods")

    @classmethod
    def tearDownClass(cls):
        print("This will run once before all the methods")


    def setUp(self):
        print("This will run Before Every Method")

    def tearDown(self):
        print("This will run After Every Method")

    def test_add(self):
        result = Examples.add(self, 10, 20)
        self.assertEqual(result, 30)
        self.assertEqual(Examples.add(self, 20, 30), 50)


    def test_sub(self):
        result = Examples.sub(self, 20, 10)
        self.assertEqual(result, 10)
        self.assertEqual(Examples.sub(self, 30, 20), 10)








if __name__ == '__main__':
    unittest.main()
