import csv, math

def Parser(filename, column1, column2):
    with open(filename, 'rb') as csvfile:
        datafile = csv.reader(csvfile, delimiter=' ', quotechar='|')
  
    # get headers of columns
        for row in csvfile.readlines():
            column = row.split(',')
            header1 = column[column1]
            header2 = column[column2]
            print "Data is for " + header1 + " and " + header2
            break
        csvfile.seek(0)
        csvfile.next()
   

    # store data in dictionary
        Dict = {}
        for row in csvfile:
            column = row.split(',')
            data1 = column[column1]
            data2 = column[column2]
            Dict[(data1)] = (data2)
        if '' in Dict.keys():
            del Dict['']
                # print poverty data to screen 
        Dict = {int(k):float(v) for k, v in Dict.items()}

        return Dict

def CombineData(Dict1, Dict2):
    combine = {}
    for k in Dict1:
        combine[Dict1[k]]=Dict2[k]
    return combine

def AveragePov(Dict):
    sum = 0
    for key in Dict:
        sum = sum + key
    average = sum/len(Dict)
    return average

def AverageLife(Dict):
    sum=0
    for k, v in Dict.iteritems():
        sum= sum + v
    average= sum/len(Dict)
    return average

#def Correlation(Dict):
    


PovDict =  Parser ('Health_Indicators.csv', 0, 23)
LifeDict = Parser ('Life_Expectancy.csv', 0, 8)
DictComb = CombineData(PovDict, LifeDict)
print AveragePov(DictComb)
print AverageLife(DictComb)
