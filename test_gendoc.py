import unittest
import gendoc


class Testgendoc(unittest.TestCase):

    def test_gendoc(self):
        gendoc.gendoc("./config.json")


if __name__ == '__main__':
    unittest.main()
