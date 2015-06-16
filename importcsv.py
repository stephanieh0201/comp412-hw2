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
        if '' in Dict.keys():
            del Dict['']
                # print poverty data to screen    
        return Dict

def CombineData(Dict1, Dict2):
    combine = {}
    olddata=[Dict1, Dict2]
    for k in Dict1:
        combine[Dict1[k]]=Dict2[k]
    return combine
    


PovDict =  Parser ('Health_Indicators.csv', 0, 23)
LifeDict = Parser ('Life_Expectancy.csv', 0, 8)
ListComb = CombineData(PovDict, LifeDict)


