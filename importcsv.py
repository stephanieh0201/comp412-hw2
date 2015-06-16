import csv

def PovertyParser():
    with open('Health_Indicators.csv', 'rb') as csvfile:
        datafile = csv.reader(csvfile, delimiter=' ', quotechar='|')
  
    # get headers of columns
        for row in csvfile.readlines():
            column = row.split(',')
            header1 = column[0]
    	    header24 = column[23]
            print "Data is for " + header1 + " and " + header24
            break
        csvfile.seek(0)
        csvfile.next()
   

    # store data in dictionary
        PovertyDict = {}
        for row in csvfile:
    	    column = row.split(',')
            data1 = column[0]
    	    data24 = column[23]
    	    PovertyDict[data1] = data24

    # print poverty data to screen    
        return PovertyDict

#Importing Life Expectancy data by community area
def LifeExpecParser():
    with open('Life_Expectancy.csv', 'rb') as csvfile:
        datafile = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
        # get headers of columns
        for row in csvfile.readlines():
            column = row.split(',')
            lifeheader1 = column[0]
    	    lifeheader9 = column[8]
            print "Data is for " + lifeheader1 + " and " + lifeheader9
            break
        csvfile.seek(0)
        csvfile.next()

        # store data in dictionary
        LifeDict= {}
        for row in csvfile:
    	    column = row.split(',')
            lifedata1 = column[0]
    	    lifedata9 = column[8]
    	    LifeDict[lifedata1] = lifedata9
        del LifeDict['']    
        return LifeDict

    combined = {}
    
    print LifeDict["77"] + PovertyDict["77"]
 
    #for key, value in LifeDict.items:
     #   print value + "&" + key + ": Life-" + LifeDict[key]  + " ----  Pov-" + PovertyDict[key]  