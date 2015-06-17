comp412-hw2
#Project: Analyzing the Effect of Percent of People Living in Poverty on Life Expectancy of Chicago Community Areas.
Created by: Stephanie Verlingo
Loyola University of Chicago, COMP 412 Homework Assignment 2


#Challenge/Background:

This project was created to determine if there is a relationship/correlation between the number people living in poverty vs the life expectancy of a community area by using data from the city of Chicago Data Portal
- Question: Does a community area's life expectancy go down if more people are living in poverty? 
- Statistical Analysis: Pearson Correlation
- Language used: Python

#Data:

Data was obtained from the City of Chicago Data Portal (https://data.cityofchicago.org/).
Specific data sets used were:

1. Public Health Statistics - Life Expectancy by Community Area (Data for Community Area: Life Expectancy in Years) (https://data.cityofchicago.org/Health-Human-Services/Public-Health-Statistics-Life-Expectancy-By-Commun/qjr3-bm53)
 - Saved as Life_Expectancy.csv
 - This file contains the data on life expectancy in years per community area.
2. Public Health Statistics - Selected Public Health Indicators by Community Area (Data for Community Area: Percent of Population Living in Poverty) (https://data.cityofchicago.org/Health-Human-Services/Public-Health-Statistics-Selected-public-health-in/iqnk-2tcu) 
 - Saved as Health_Indicators.csv
 - This file contains the data on percent of people living in poverty per community area.
To Note: These data sets have community areas consistently numbered 1 through 77 across the Chicago area.

#Methods:

Using Python language, methods were developed. 
Methods are found in program.py
Methods include: 
- def Parser(self, filename, column1, column2) 
- def Average (self, Dict)
- def Pearson (self, Dict1, Dict2)
- def CorrelationStrength(self, coefficient)

#UnitTests:

Unit tests were developed to ensure program is running efficiently. 
Unit tests are found in programtest.py
12 Tests run in .009s. 
Tests Include:
- def testFileExists()
- def testCorrectColumnsHealth()
- def testCorrectColumnsLife()
- def testCorrectData()
- def testDictsSameSize()
- def testNumberMatchesArea()
- def testDictKeysMatch()
- def testAverageRight()
- def testPearsonRight()
- def testPearsonMatchExcel()
- def testCoefficientInRange()
- def testCoefficientOutput()

#Data Analysis:

1. The two csv data files are parsed into two separate dictionaries. Data is identified by a community area number which is consistent across the two files.
2. Pearson Correlation is run on the two data sets, matching the Life Expectancy with the Percent of People in Poverty by the Community Area.
3. The correlation coefficient is analyzed to determine what type of relationship the two variables have with each other, and and displayed to the screen.

#Results:

- Results are displayed in the output of executed program.py. 
- Pearson Correlation Coefficient was determined to be approximately -.66.
- This indicates a strong negative correlation between the two variables.
- As the percentage of people living in poverty in a community area goes up, the life expectancy goes down. 
- To note: Correlation does not imply causation.
