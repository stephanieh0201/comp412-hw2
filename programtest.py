import unittest
from importcsv import *


class ProgramTest(unittest.TestCase):
   # def test_no_data(filename)
    #def testFileNotExist(self):
     #   prog=Program()
      #  d = Program.Parser(prog, 'notfile.csv', 1,2)
       # self.fail(d)
    def testCorrectData(self):
        """Testing that Parser() is importing correct data for specific community area 
        (testing area 1)"""
        prog=Program()
        d1= prog.Parser('Health_Indicators.csv', 0, 23)
        d2= prog.Parser('Life_Expectancy.csv', 0, 8)
        data = [d1[1],d2[1]]
        self.assertItemsEqual(data,[22.7, 77.3])

    def testAverageRight(self):
        """This is testing the Average() method from Program to ensure it is calulating
        the average of the values of a dictionary correctly. Testing mean of 8,10,12 (mean=10) """
    	prog=Program()
        test1 ={7:8,9:10,11:12}
        avg=Program.Average(prog, test1)
        self.assertEqual(avg, 10)

    def testPearsonRight(self):
        """Testing to check if Pearson() calculation is working correctly. Two dictionaries 
        same values should give a coefficient of 1"""
    	prog=Program()
    	test1= {1:1, 2:2, 3:3}
    	test2= {1:1, 2:2, 3:3}
    	output=Program.Pearson(prog, test1, test2)
    	self.assertEqual(output, 1)

    def testDictsSameSize(self):
        """Testing to see if the two dictionaries created from Parser() from the two
        chicago data csv files are the same lenghth."""
        prog=Program()
        d1= prog.Parser('Health_Indicators.csv', 0, 23)
        d2= prog.Parser('Life_Expectancy.csv', 0, 8)
        l1=len(d1)
        l2=len(d2)
        self.assertEqual(l1,l2)

    def testDictKeysMatch(self):
        """Testing the two dictionaries created by Parser() from the Chicago datacsv 
        files to determine that keys in one dictionary match the other"""
        prog=Program()
        d1= prog.Parser('Health_Indicators.csv', 0, 23)
        d2= prog.Parser('Life_Expectancy.csv', 0, 8)
        self.assertItemsEqual(d1.keys(),d2.keys())
        #for k in d1:
         #   assert(k in d2)



if __name__ == '__main__':
    unittest.main()