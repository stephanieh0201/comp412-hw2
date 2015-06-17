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
        print len(Dict)
        return Dict

def CombineData(Dict1, Dict2):
    combine = {}
    for k in Dict1:
        combine[Dict1[k]]=Dict2[k]
    return combine

#def AveragePov(Dict):
 #   assert len(Dict) > 0
  #  sum = 0
   # for key in Dict:
    #    sum = sum + key
    #average = float(sum/len(Dict))
    #return average

def Average(Dict):
    assert len(Dict) > 0
    sum=0
    for k, v in Dict.iteritems():
        sum= sum + v
    average= float(sum/len(Dict))
    return average

def Pearson(Dict1, Dict2):
    n=len(Dict1)
    assert len(Dict1) == len(Dict2)
    assert n>0
    print n
    AvgPov=Average(Dict1)
    AvgLife=Average(Dict2)
    DiffProd=0
    PovDiff2=0
    LifeDiff2=0

    for k in Dict1:
        PovDiff = Dict1[k] - AvgPov
        LifeDiff= Dict2[k] - AvgLife
        DiffProd += PovDiff * LifeDiff
        PovDiff2 += PovDiff * PovDiff
        LifeDiff2 += LifeDiff * LifeDiff
    return DiffProd/math.sqrt(PovDiff2 * LifeDiff2)


PovDict =  Parser ('Health_Indicators.csv', 0, 23)
LifeDict = Parser ('Life_Expectancy.csv', 0, 8)
#DictComb = CombineData(PovDict, LifeDict)
#print DictComb
print "-------------"
print Average(PovDict)
print Average(LifeDict)
print Pearson(PovDict, LifeDict)

