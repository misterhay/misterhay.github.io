# create html files for each school from master csv
# build a graph for each school

import csv
import os
from random import randint # for randomly choosing a dashStyle

school_name_dictionary = {
'0401':'Vegreville Next Step III Outreach School',
'1221':'Lakeland Ridge School',
'1233':'NSonline',
'1234':'EIPS Home Education',
'1362':'EIPS Centre for Educational Alternatives',
'1367':'Strathcona Christian Academy Elementary School',
'1599':'Elk Island Youth Ranch Learning Centre',
'1752':'Rudolph Hennig Junior High School',
'1753':'Ecole Parc Elementaire',
'3301':'Ardrossan Junior Senior High School',
'3303':'Ecole Elementaire Ardrossan Elementary School',
'3304':'Uncas Elementary School',
'3307':'Sherwood Park Next Step I Outreach School',
'3310':'Fort Saskatchewan Next Step II Outreach School',
'3311':'Fort Saskatchewan High School',
'3313':'Fort Saskatchewan Elementary School',
'3316':'Win Ferguson Community School',
'3318':'Ministik School',
'3321':'F. R. Haythorne School',
'3322':'Salisbury Composite High School',
'3323':'Sherwood Heights Junior High School',
'3324':'Brentwood School',
'3325':'Ecole Campbelltown School',
'3326':'Pine Street School',
'3328':'Westboro Elementary School',
'3329':'Mills Haven Elementary School',
'3330':'Clover Bar Junior High School',
'3331':'Wye School',
'3332':'Castle School',
'3333':'Glen Allan Elementary School',
'3334':'Wes Hosford School',
'3335':'Fultonvale Elementary Junior High School',
'3336':'Woodbridge Farms School',
'3339':'Salisbury Composite (Evening)',
'3340':'Bev Facey Community High School',
'3341':'James Mowat School',
'3395':'Strathcona Christian Academy',
'3397':'Fort Saskatchewan Christian School',
'3401':'Andrew School',
'3404':'Lamont High School',
'3405':'Lamont Elementary School',
'3406':'Mundare School',
'3409':'Bruderheim Community School',
'3610':'Vegreville Composite High School',
'3611':'A. L. Horton Elementary School',
'3615':'Pleasant Ridge Colony School'}

dashStyles = ['Solid','ShortDash','ShortDot','ShortDashDot','ShortDashDotDot','Dot','Dash','LongDash','DashDot','LongDashDot','LongDashDotDot']
#dash = dashStyles[randint(0,10)]
#print dash

def makeHeader(school):
    school_name = school_name_dictionary[school]
    print "Making header for", school_name
    htmlFile = open(school + '.html', "a") # open for appending
    htmlFile.write('<!DOCTYPE HTML><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n')
    htmlFile.write("<title>Provincial Testing Results - " + school_name + " - " + school + "</title>\n")
    htmlFile.write('<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>\n')
    htmlFile.write('<style type="text/css">${demo.css}</style>\n')
    htmlFile.write('<script type="text/javascript">$(function () {\n')
    htmlFile.write("$('#container').highcharts({\n")
    htmlFile.write("title: {text: 'EIPS Provincial Testing Results', x: -20},\n")
    htmlFile.write("subtitle: {text: '" + school_name + " - " + school + "', x: -20},\n")
    htmlFile.write("exporting: {filename: '2014_Provincial_Testing_Chart_" + school_name + "'},\n")
    htmlFile.write("credits: {enabled: false},\n")
    htmlFile.write("xAxis: {categories: [2010, 2011, 2012, 2013, 2014]},\n")
    htmlFile.write("yAxis: {title: {text: '%'}},\n")
    htmlFile.write("tooltip: {valueSuffix: '%'},\n")
    htmlFile.write("legend: {layout: 'horizontal',align: 'center',verticalAlign: 'bottom',borderWidth: 0},\n")
    htmlFile.write("series: [")
    htmlFile.close()

def addToBody(school, label, datalist):
    #if label.find('EIPS') != -1: # if EIPS exists anywhere in it
    #    color = 'green'
    #if label.find('Prov') != -1:
    #    color = 'red'
    #else:
    #    color = 'blue'
    if label.find('Excellence') != -1:
        marker = 'square'
    if label.find('Acceptable') != -1:
        marker = 'triangle'
    if label.find('Mark') != -1:
        marker = 'circle'
    if label.find('Exam') != -1:
        marker = 'triangle-down'

    htmlFile = open(school + '.html', "a")
    htmlFile.write("{name: '" + label + "',\n")
    htmlFile.write("id: '" + label + "',\n")
    htmlFile.write("data: [")
    for value in datalist:
        htmlFile.write(value)
        htmlFile.write(",")
    htmlFile.write("],\n")
    htmlFile.write("dashStyle: '" + dashStyles[randint(0,10)] + "',") # choose a random dash style
    #htmlFile.write("color: '" + color + "',\n")
    htmlFile.write("marker: {symbol: '" + marker + "'}\n")
    htmlFile.write(", visible: false\n")
    htmlFile.write("},\n")
    htmlFile.close()

def makeFooter(school):
    htmlFile = open(school+'.html', 'a') # open for appending

    # add the EIPS and Prov stuff
    dataSourceName = open('bestFileWithEIPS_Prov_Schools.csv', 'rb')
    csvReader = csv.reader(dataSourceName)
    for row in csvReader:
        course = row[0]
        form = row[1]
        language = row[2]
        #school = row[3] # we're not going to change the value of the school variable
        datatype = row[4]
        year1 = row[5]
        year2 = row[6]
        year3 = row[7]
        year4 = row[8]
        year5 = row[9]
        if row[3] == 'Prov' or school == 'EIPS':
            label = row[3] + ' ' + course + ' ' + '' + form + ' ' + language + ' ' + datatype
            datalist = [year1, year2, year3, year4, year5]
            addToBody(school, label, datalist)
    # done adding the EIPS and Prov stuff

    htmlFile.write("]\n")
    htmlFile.write("});});\n")
    #htmlFile.write("var chart = $('#container').highcharts(),\n")
    htmlFile.write("</script></head><body>\n")
    htmlFile.write('<script src="js/highcharts.js"></script>\n')
    htmlFile.write('<script src="js/modules/exporting.js"></script>\n')
    htmlFile.write('<div id="container" style="min-width: 310px; height: 750px; margin: 0 auto"></div>\n')
    htmlFile.write('</body></html>\n')
    htmlFile.close()

def createHtml(xaxis, course, form, language, school, datatype, year1, year2, year3, year4, year5):
    #print xaxis
    filename = school + '.html'
    htmlFile = open(filename, 'a') # open for appending
    if os.stat(filename).st_size == 0: # if the file is empty
        makeHeader(school)
    # remember to include EIPS and Prov in each document
    label = school + ' ' + course + ' ' + datatype
    datalist = [year1, year2, year3, year4, year5]
    if form != '':
        label = school + ' ' + course + ' ' + '' + form + ' ' + language + ' ' + datatype
    addToBody(school, label, datalist)
    htmlFile.close()

schoollist = []
dataSourceName = open('bestFileWithEIPS_Prov_Schools.csv', 'rb')
csvReader = csv.reader(dataSourceName)
for index, row in enumerate(csvReader):
    if index == 0:
        xaxis = [row[5], row[6], row[7], row[8], row[9]]
        #print xaxis
    if index != 0:
        course = row[0]
        form = row[1]
        language = row[2]
        school = row[3]
        datatype = row[4]
        year1 = row[5]
        year2 = row[6]
        year3 = row[7]
        year4 = row[8]
        year5 = row[9]
        if school != 'Prov' and school != 'EIPS':
        #if school == '3610':
            if school in schoollist:
                pass
            else:
                schoollist.append(school)
            #label = school + ' ' + course + ' ' + '' + form + ' ' + language + ' ' + datatype
            createHtml(xaxis, course, form, language, school, datatype, year1, year2, year3, year4, year5)

#print schoollist
for school in schoollist:
    makeFooter(school)

##Science 6 (Fr)
##Science 9 (Fr)
##Mathematics 6 (Fr)
##Mathematics 9 (Fr)
##Mathematics 3 (Fr)
##Social Studies (Fr) 6
##Social Studies (Fr) 9
##English Language Arts 6
##French Language Arts 6
##Mathematics 6
##Science 6
##Social Studies 6
##English Language Arts 9
##French Language Arts 9
##English Lang Arts 9 KAE
##Mathematics 9
##Mathematics 9 KAE
##Science 9
##Science 9 KAE
##Social Studies 9
##Social Studies 9 KAE
##English Language Arts 3
##Mathematics 3
##French Language Arts 3
##'''