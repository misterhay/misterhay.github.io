#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      david hay
#
# Created:     22-06-2015
# Copyright:   (c) david hay 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import csv

def main():
    dataSourceName = open('bestFileWithEIPS_Prov_Schools.csv', 'rb')
    csvReader = csv.reader(dataSourceName)
    for row in csvReader:
        course = row[0]
        form = row[1]
        language = row[2]
        school = row[3] # we're not going to change the value of the school variable
        datatype = row[4]
        year1 = row[5]
        year2 = row[6]
        year3 = row[7]
        year4 = row[8]
        year5 = row[9]
        if row[3] == 'Prov' or row[3] == 'EIPS':
            print row[3]

if __name__ == '__main__':
    main()
