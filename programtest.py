import unittest
from importcsv import *


class ProgramTest(unittest.TestCase):
   # def test_no_data(filename)
    def testAverageWrong(self):
        prog=Program()
        test1 ={1:2,3:4,5:6}
        avg=Program.Average(prog, test1)
        self.assertNotEqual(avg, 9)

    def testAverageRight(self):
    	prog=Program()
        test1 ={7:8,9:10,11:12}
        avg=Program.Average(prog, test1)
        self.assertEqual(avg, 10)

    def testPearsonRight(self):
    	prog=Program()
    	test1= {1:1, 2:2, 3:3}
    	test2= {1:1, 2:2, 3:3}
    	output=Program.Pearson(prog, test1, test2)
    	self.assertEqual(output, 1)

    def testDictsSameSize(self):
        prog=Program()
        d1= prog.Parser('Health_Indicators.csv', 0, 23)
        d2= prog.Parser('Life_Expectancy.csv', 0, 8)
        l1=len(d1)
        l2=len(d2)
        self.assertEqual(l1,l2)

    #def testMatchingKeys(self):
    #	prog=Program()
    #	d1= prog.Parser('Health_Indicators.csv', 0, 23)
    #	d2= prog.Parser('Life_Expectancy.csv', 0, 8)
     #   for k, v in d1.iteritems():
      #  	assert 


    #def testPearsonWrong(self):


if __name__ == '__main__':
    unittest.main()