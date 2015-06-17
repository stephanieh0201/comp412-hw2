import csv, math, os.path
class Program:
    """This class was developed to import data from a csv file into a dictionary
    and then utilize two separate dictionaries with matching keys in order to determine
    the Pearson Correlation Coefficient."""


    def Parser(self, filename, column1, column2):
        """Returns a dictionary with data (int format) from two specified columns of 
        a csv file assuming first row is a header row. Removes any k/v pairs that have 
        empty keys."""
        fileExists = os.path.isfile(filename)
        if fileExists:
            with open(filename, 'rb') as csvfile:
                datafile = csv.reader(csvfile, delimiter=' ', quotechar='|')
  
            # get headers of columns
                for row in csvfile.readlines():
                    column = row.split(',')
                    header1 = column[column1]
                    header2 = column[column2]
                    break
                csvfile.seek(0) # return to beginning of csv file 
                csvfile.next() # set up position in file to read data (skip header row)
   

            # storing data in dictionary
                Dict = {}
                for row in csvfile:
                    column = row.split(',')
                    data1 = column[column1]
                    data2 = column[column2]
                    Dict[(data1)] = (data2)
                if '' in Dict.keys(): #removing empty keys
                    del Dict['']
                Dict = {int(k):float(v) for k, v in Dict.items()} #cast items from string to int/float
                return Dict
        else: 
            print "Parser Error: File " + filename + " does not exist."

    def Average(self, Dict):
        """Returns the mean of a given dictionary using the values"""

        if len(Dict) > 0: #ensure dictionary contains items
            sum=0 
            for k, v in Dict.iteritems():
                sum += v
            average= float(sum/len(Dict))
            return average
        else:
            print "Average Error: Dictionary has no data."

    def Pearson(self, Dict1, Dict2):
        """Returns the Pearson Correlation Coefficient given two dictionaries.
        Correlation will be determined by matching keys across the two dictionaries
        and using the corresponding value pairs for the x and y data sets."""

        if len(Dict1)>0:
            if len(Dict1) == len(Dict2):
                n=len(Dict1)
                AvgPov=self.Average(Dict1)
                AvgLife= self.Average(Dict2)
                DiffProd=0
                PovDiff2=0
                LifeDiff2=0

                for k in Dict1:
                    PovDiff = Dict1[k] - AvgPov
                    LifeDiff = Dict2[k] - AvgLife
                    DiffProd += PovDiff * LifeDiff
                    PovDiff2 += PovDiff * PovDiff
                    LifeDiff2 += LifeDiff * LifeDiff
                return DiffProd/math.sqrt(PovDiff2 * LifeDiff2)
            else:
                print "Pearson Calculation Error: The two dictionaries are different sizes."
        else: 
            print "Pearson Calculation Error: No data in given file"

    def CorrelationStrength(self, coefficient):
        if  .70 <= coefficient <= 1.0:
            return "Very strong positive relationship"
        elif .40 <= coefficient < .70:
            return "Strong positive relationship"
        elif .30 <= coefficient < .40:
            return "Moderate positive relationship"
        elif .20 <= coefficient < .30:
            return "Weak positive relationship"
        elif -.19 <= coefficient < .20:
            return "No/negligible relationship"
        elif -.30 <= coefficient < -.20:
            return "Weak negative relationship"
        elif -.40 <= coefficient < -.30:
            return "Moderate negative relationship"
        elif -.70 <= coefficient < -.40:
            return "Strong negative relationship"
        elif -1.0 <= coefficient <= -.70:
            return "Very strong negative relationship"
        else:
            print "Correlation Strength Error: Coefficient out of range."
        


if __name__ == '__main__':
    prog = Program()
    print "Chicago city data is being analyzed to determine if there is a correlation between the percent of residents living in poverty in a community area vs life expectancy of that area."
    print ""
    print "Importing data from external files and loading into data dictionaries..."
    PovDict =  prog.Parser ('Health_Indicators.csv', 0, 23)
    LifeDict = prog.Parser ('Life_Expectancy.csv', 0, 8)
    print ""
    print "Calculating the pearson correlation coefficient..."
    print ""
    value = prog.Pearson(PovDict, LifeDict)
    print "Pearson Correlation Coefficient: " + str(value)
    print ""
    print "This indicates there is a " + prog.CorrelationStrength(value) + " between percent of residents living in poverty vs. life expectancy."