
'''
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('misterhay', "us63tb9s86")
'''

'''
dictionaryOfLists = dict(
  listSchoolExcellence='School Mark % Exc',
  listSchoolAcceptable = 'School Mark % Acc',
  listSchoolMark = 'School Average %',
  listExamExcellence = 'Exam Mark % Exc',
  listExamAcceptable = 'Exam Mark % Acc',
  listExamAverage = 'Exam Average %',
  listFinalExcellence = 'Final Mark % Exc',
  listFinalAcceptable = 'Final Mark % Acc',
  listFinalMark = 'Final Average %')
'''

'''
English Lang Arts 30-2
English Lang Arts 30-1
Biology 30
Chemistry 30
Social Studies 30-1
Social Studies 30-2
Mathematics 30-1
Mathematics 30-2
Physics 30
Science 30
French Lang Arts 30-1
'''

import csv

#listYears = [2010, 2011, 2012, 2013, 2014]
#listYears = ['2010', '2011', '2012', '2013', '2014']
listSchoolExcellence = [] # School Mark % Exc
listSchoolAcceptable = [] # School Mark % Acc
listSchoolMark = [] # School Average %
listExamExcellence = [] # Exam Mark % Exc
listExamAcceptable = [] # Exam Mark % Acc
listExamAverage = [] # Exam Average %
listFinalExcellence = [] # Final Mark % Exc
listFinalAcceptable = [] # Final Mark % Acc
listFinalMark = [] # Final Average %

# read row index 0 to get locations of interest
csvFile = open('Diploma Multiyear Results - Whole Year (all schools).csv', 'rb')
csvReader = csv.reader(csvFile)
for index, row in enumerate(csvReader):
    if index == 0:
        for index, cell in enumerate(row):
            if cell.find('School Mark % Exc') != -1:
                listSchoolExcellence.append(index)
            if cell.find('School Mark % Acc') != -1:
                listSchoolAcceptable.append(index)
            if cell.find('School Average %') != -1:
                listSchoolMark.append(index)
            if cell.find('Exam Mark % Exc') != -1:
                listExamExcellence.append(index)
            if cell.find('Exam Mark % Acc') != -1:
                listExamAcceptable.append(index)
            if cell.find('Exam Average %') != -1:
                listExamAverage.append(index)
            if cell.find('Final Mark % Exc') != -1:
                listFinalExcellence.append(index)
            if cell.find('Final Mark % Acc') != -1:
                listFinalAcceptable.append(index)
            if cell.find('Final Average %') != -1:
                listFinalMark.append(index)
csvFile.close()

import os
def createCsv(course, label, data, which): # which should be 'ea' Excellence/Acceptable or 'ce' Course/Exam
    fileName = course.replace(" ", "") + which + '.csv' # replace spaces with nothing, add extension
    csvFile = open(fileName, 'a') # open for appending
    if os.stat(fileName).st_size == 0: # if the file is blank
        print 'writing column headings'
        csvFile.write(course)
        listYears = ['2010', '2011', '2012', '2013', '2014']
        for year in listYears:
            csvFile.write(',')
            csvFile.write(year)
        csvFile.write('\n')
    csvFile.write(label)
    for value in data:
        csvFile.write(',')
        if value == 'N/A':
            value = 'null' # so that Highcharts displays properly
        csvFile.write(value)
    csvFile.write('\n')
    csvFile.close()

def thValue(row, listOf):
    newList = []
    newList.append(row[listOf[0]])
    newList.append(row[listOf[1]])
    newList.append(row[listOf[2]])
    newList.append(row[listOf[3]])
    newList.append(row[listOf[4]])
    return newList

'''
def forEachCategory(row):
    print 'School Mark % Exc'
    thValue(row, listSchoolExcellence)
    print 'School Mark % Acc'
    thValue(row, listSchoolAcceptable)
    #print 'School Average %'
    #thValue(row, listSchoolMark)
    print 'Exam Mark % Exc'
    thValue(row, listExamExcellence)
    print 'Exam Mark % Acc'
    thValue(row, listExamAcceptable)
    #print 'Exam Average %'
    #thValue(row, listExamAverage)
    #print 'Final Mark % Exc'
    print thValue(row, listFinalExcellence)
    #print 'Final Mark % Acc'
    print thValue(row, listFinalAcceptable)
    #print 'Final Average %'
    #thValue(row, listFinalMark)
'''

csvFile = open('Diploma Multiyear Results - Whole Year (all schools).csv', 'rb')
csvReader = csv.reader(csvFile)
for index, row in enumerate(csvReader):
    course = row[0]
    school = row[3]
    if school == '401':
        school = '0401' # because the spreadsheet stripped the leading zero
    if index != 0:
    #if course == 'Physics 30':
        print 'School:', school
        #print row[listSchoolExcellence[0]], row[listSchoolExcellence[1]], row[listSchoolExcellence[2]], row[listSchoolExcellence[3]], row[listSchoolExcellence[4]]
        #forEachCategory(row)
        finalExcellence = thValue(row, listFinalExcellence)
        finalAcceptable = thValue(row, listFinalAcceptable)
        #print finalExcellence
        #print finalAcceptable
        labelExcellence = str(school) + ' % Excellence'
        labelAcceptable = str(school) + ' % Acceptable'
        createCsv(course, labelExcellence, finalExcellence, 'ea')
        createCsv(course, labelAcceptable, finalAcceptable, 'ea')
        finalCourse = thValue(row, listSchoolMark)
        finalExam = thValue(row, listExamAverage)
        labelCourse = str(school) + ' Course Mark'
        labelExam = str(school) + ' Exam Mark'
        print labelCourse, finalCourse
        print labelExam, finalExam
        createCsv(course, labelCourse, finalCourse, 'ce')
        createCsv(course, labelExam, finalExam, 'ce')
csvFile.close()
