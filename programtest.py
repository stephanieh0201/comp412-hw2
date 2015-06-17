import unittest
from importcsv import *


class ProgramTest(unittest.TestCase):
   # def test_no_data(filename)
    prog = Program()
    test1 ={[1,2],[3,4]}
    test2 = {[5,6],[7,8],[9,10]}
    def test_dictSameSize(self):

        self.assertTrue(len(test1) == len(test2))

if __name__ == '__main__':
    unittest.main()