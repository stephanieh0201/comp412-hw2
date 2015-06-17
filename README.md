# comp412-hw2
Project: Analyzing the Effect of Percent of People Living in Poverty on Life Expectancy of Chicago Community Areas.
Created by: Stephanie Verlingo
Loyola University, COMP 412 Homework Assignment 2

This is a python project analyzing Chicago city data to determine if there is a coorelation between number of people living in poverty vs. life expectancy. This will be determined by using a Pearson Correlation Coefficient.

Data:

Data was obtained from the City of Chicago Data Portal (https://data.cityofchicago.org/).
Specific data sets used were:

1. Public Health Statistics - Life Expectancy by Community Area (Data for Community Area: Life Expectancy in Years) (https://data.cityofchicago.org/Health-Human-Services/Public-Health-Statistics-Life-Expectancy-By-Commun/qjr3-bm53)
2. Public Health Statistics - Selected Public Health Indicators by Community Area (Data for Community Area: Percent of Population Living in Poverty) (https://data.cityofchicago.org/Health-Human-Services/Public-Health-Statistics-Selected-public-health-in/iqnk-2tcu)

Methods:

Using Python language, methods were developed. Methods include: 
 def GetHeader(self, filename, column1, column2)
 def Parser(self, filename, column1, column2) 
 def Average (self, Dict)
 def Pearson (self, Dict1, Dict2)
 def CorrelationStrength(self, coefficient)

UnitTests:

Unit test are being developed to ensure program is running efficiently.

Data Analysis:

1. The two csv data files are parsed into two separate dictionaries. Data is identified by a community area number which is consistent across the two files.
2. Pearson Correlation is run on the two data sets, matching the Life Expectancy with the Perecent of People in Poverty by the Community Area.
3. The correlation coefficient is analyzed to determine what type of relationship the two variables have with each other, and and displayed to the screen.

