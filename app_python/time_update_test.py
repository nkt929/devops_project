import unittest
from time import sleep
from main import get_time


class MyTestCase(unittest.TestCase):
    def test_something(self):
        str_1 = get_time()
        sleep(2)
        str_2 = get_time()
        self.assertNotEqual(str_1, str_2)


if __name__ == '__main__':
    unittest.main()
