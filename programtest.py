import unittest, os.path
from importcsv import *


class ProgramTest(unittest.TestCase):
    #def test_no_data(filename):
    def testFileNotExist(self):
        """Testing the two csv data files used in program exist."""
        assert os.path.exists('Health_Indicators.csv')
        assert os.path.exists('Life_Expectancy.csv')
        

    def testCorrectColumnsHealth(self):
        """Testing the Poverty Data Dictionary created by Parser() from Health_Indicators
        contains data from the necessary columns in the data csv file."""
        prog=Program()
        with open('Health_Indicators.csv', 'rb') as csvfile:
                datafile = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in csvfile.readlines():
                    column = row.split(',')
                    header1 = column[0]
                    header2 = column[23]
                    break
                self.assertEqual(header1, "Community Area")
                self.assertEqual(header2, "Below Poverty Level")


    def testCorrectColumnsLife(self):
        """Testing that Life Expectancy Dictionary created by Parser() contains data
        from the necessary columns in the data csv file."""
        prog=Program()
        with open('Life_Expectancy.csv', 'rb') as csvfile:
                datafile = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in csvfile.readlines():
                    column = row.split(',')
                    header1 = column[0]
                    header2 = column[8]
                    break
                self.assertEqual(header1, "Community Area Number")
                self.assertEqual(header2, "2010 Life Expectancy")

    def testCorrectData(self):
        """Testing that Parser() is importing correct data for specific community area."""
        prog=Program()
        d1= prog.Parser('Health_Indicators.csv', 0, 23)
        d2= prog.Parser('Life_Expectancy.csv', 0, 8)
        data1 = [d1[1], d2[1]]
        data2 = [d1[25], d2[25]]
        data3 = [d1[68], d2[68]]
        data4 = [d1[77], d2[77]]
        self.assertItemsEqual(data1, [22.7, 77.3])
        self.assertItemsEqual(data2, [27, 71.9])
        self.assertItemsEqual(data3, [42.2, 70.7])
        self.assertItemsEqual(data4, [16.6, 79.8])

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

    def testAverageRight(self):
        """Testing the Average() method from Program to ensure it is calulating
        the average of the values of a dictionary correctly. Testing mean of 8,10,12 (mean=10) """
        prog=Program()
        test1 ={7:8,9:10,11:12}
        avg=Program.Average(prog, test1)
        self.assertEqual(avg, 10)

    def testPearsonRight(self):
        """Testing to check if Pearson() calculation is working correctly. Two dictionaries 
        same values should give a coefficient of 1."""
        prog=Program()
        test1= {1:1, 2:2, 3:3}
        test2= {1:1, 2:2, 3:3}
        output=Program.Pearson(prog, test1, test2)
        self.assertEqual(output, 1)
       

    def testPearsonMatchExcel(self):
        """Testing to see if the program's Pearson() method calculates a similar value
        as the correlation function in excel"""
        prog=Program()
        d1= prog.Parser('Health_Indicators.csv', 0, 23)
        d2= prog.Parser('Life_Expectancy.csv', 0, 8)
        Progvalue = prog.Pearson(d1,d2)
        Excelvalue= -0.662362134530488
        self.assertAlmostEqual(Progvalue, Excelvalue)

    def testCoefficientInRange(self):
        """Testing that Pearson Coefficient is in range"""
        prog=Program()
        d1= prog.Parser('Health_Indicators.csv', 0, 23)
        d2= prog.Parser('Life_Expectancy.csv', 0, 8)
        value = prog.Pearson(d1,d2)
        self.assertGreaterEqual(value, -1)
        self.assertLessEqual(value, 1)


if __name__ == '__main__':
    unittest.main()