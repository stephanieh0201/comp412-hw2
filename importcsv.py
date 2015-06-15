import csv
with open('C:\Users\Stephanie\Documents\GitHub\comp412-hw2\Health_Indicators.csv', 'rb') as csvfile:
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
    PovertyDict= {}
    for row in csvfile:
    	column = row.split(',')
        data1 = column[0]
    	data24 = column[23]
    	PovertyDict[data1] = data24

    # print poverty data to screen    
    print len(PovertyDict)
    print PovertyDict.viewitems()
    print "--------------------------------------"

#Importing Life Expectancy data by community area
with open('C:\Users\Stephanie\Documents\GitHub\comp412-hw2\Life_Expectancy.csv', 'rb') as csvfile:
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

    # print life expectancy data to screen
    print len(LifeDict)
    print LifeDict.viewitems()

    combined = {}

    for key in LifeDict:
        x=0
        pov = PovertyDict[x]
        life = LifeDict[x]
        combined[pov]=life
        x=x+1
    print combined.viewitems()
