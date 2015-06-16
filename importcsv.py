import csv

def Parser(filename, column1, column2):
    with open(filename, 'rb') as csvfile:
        datafile = csv.reader(csvfile, delimiter=' ', quotechar='|')
  
    # get headers of columns
        for row in csvfile.readlines():
            column = row.split(',')
            header1 = column[column1]
            header24 = column[column2]
            print "Data is for " + header1 + " and " + header24
            break
        csvfile.seek(0)
        csvfile.next()
   

    # store data in dictionary
        Dict = {}
        for row in csvfile:
            column = row.split(',')
            data1 = column[column1]
            data24 = column[column2]
            Dict[data1] = data24

    # print poverty data to screen    
        return Dict

def CompareData(PovertyDict):
    for key in PovertyDict:
        print key


PovDict =  Parser ('Health_Indicators.csv', 0, 23)
LifeDict = Parser ('Life_Expectancy.csv', 0, 8)
del LifeDict['']
CompareData(LifeDict)
