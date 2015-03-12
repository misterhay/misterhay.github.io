import csv

def makeHeader(course, which): # which should be 'ea' Excellence/Acceptable or 'ce' Course/Exam
    print "Making header for", course
    fileName = course.replace(" ", "") + which + ".html" # replace spaces with nothing, add extension
    htmlFile = open(fileName, "a") # open for appending
    htmlFile.write('<!DOCTYPE HTML><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n')
    htmlFile.write("<title>Provincial Testing Results - EIPS " + course + "</title>\n")
    htmlFile.write('<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>\n')
    htmlFile.write('<style type="text/css">${demo.css}</style>\n')
    htmlFile.write('<script type="text/javascript">$(function () {\n')
    htmlFile.write("$('#container').highcharts({\n")
    htmlFile.write("title: {text: '" + course + "', x: -20},\n")
    htmlFile.write("subtitle: {text: 'EIPS Provincial Testing Results', x: -20},\n")
    htmlFile.write("exporting: {filename: 'Provincial_Testing_Chart" + course + "'},\n")
    htmlFile.write("credits: {enabled: false},\n")
    htmlFile.write("xAxis: {categories: [2010, 2011, 2012, 2013, 2014]},\n")
    htmlFile.write("yAxis: {title: {text: '%'}},\n")
    htmlFile.write("tooltip: {valueSuffix: '%'},\n")
    htmlFile.write("legend: {layout: 'vertical',align: 'right',verticalAlign: 'bottom',borderWidth: 0},\n")
    htmlFile.write("series: [")
    htmlFile.close()

def addSeries(course, name, data, which):
    fileName = course.replace(" ", "") + which +  ".html" # replace spaces with nothing, add extension
    htmlFile = open(fileName, 'a') # open for appending
    if name.find('Alberta') != -1:
        color = 'red'
    elif name.find('EIPS') != -1:
        color = 'green'
    else:
        color = 'blue'
    if name.find('Excellence') != -1 or name.find('Course') != -1:
        marker = 'square'
    else:
        marker = 'circle'
    htmlFile.write("{name: '" + name + "',\n")
    htmlFile.write("id: '" + name + "',\n")
    htmlFile.write("data: [")
    for value in data:
        htmlFile.write(value)
        htmlFile.write(",")
    htmlFile.write("],\n")
    htmlFile.write("color: '" + color + "',\n")
    htmlFile.write("marker: {symbol: '" + marker + "'}\n")
    if name.find('Alberta') == -1:
        if name.find('EIPS') == -1:
            htmlFile.write(", visible: false\n")
    htmlFile.write("},\n")

def makeFooter(course, schoolLabelList, schoolList, which):
    fileName = course.replace(" ", "") + which + ".html" # replace spaces with nothing, add extension
    htmlFile = open(fileName, 'a') # open for appending
    htmlFile.write("]\n")
    htmlFile.write("});\n")
    htmlFile.write("var chart = $('#container').highcharts(),\n")
    htmlFile.write("\n")
    if which == 'ea':
        buttonE = " % Excellence'"
        buttonA = " % Acceptable'"
    if which == 'ce':
        buttonE = " Course Mark'"
        buttonA = " Exam Mark'"

    # now make buttons for each school, including Alberta and EIPS
    for school in schoolList:
        htmlFile.write("$button" + school + " = $('#button" + school + "');\n")
        htmlFile.write("$button" + school + ".click(function () {\n")
        htmlFile.write("if (chart.get('" + school + buttonE + ").visible) {\n")
        htmlFile.write("chart.get('" + school + buttonE + ").hide();\n")
        htmlFile.write("chart.get('" + school + buttonA + ").hide();\n")
        htmlFile.write("$button" + school + ".html('Show " + school + "');\n")
        htmlFile.write("} else {\n")
        htmlFile.write("chart.get('" + school + buttonE + ").show();\n")
        htmlFile.write("chart.get('" + school + buttonA + ").show();\n")
        htmlFile.write("$button" + school + ".html('Hide " + school + "');\n")
        htmlFile.write("}});\n")
        htmlFile.write("\n")

    # a show all button
    htmlFile.write("$buttonAll = $('#buttonAll');\n")
    htmlFile.write("$buttonAll.click(function () {\n")
    htmlFile.write("if (chart.get('Alberta" + buttonE + ").visible) {\n")
    for schoolLabel in schoolLabelList:
        htmlFile.write("chart.get('" + schoolLabel + "').hide();\n")
    for school in schoolList:
        htmlFile.write("$button" + school + ".html('Show " + school + "');\n")
    htmlFile.write("$buttonAll.html('Show All');\n")
    htmlFile.write("} else {\n")
    for schoolLabel in schoolLabelList:
        htmlFile.write("chart.get('" + schoolLabel + "').show();\n")
    for school in schoolList:
        htmlFile.write("$button" + school + ".html('Hide " + school + "');\n")
    htmlFile.write("$buttonAll.html('Hide All');\n")
    htmlFile.write("}});\n")
    htmlFile.write("});\n")
    htmlFile.write("</script></head><body>\n")
    htmlFile.write('<script src="js/highcharts.js"></script>\n')
    htmlFile.write('<script src="js/modules/exporting.js"></script>\n')
    htmlFile.write('<div id="container" style="min-width: 310px; height: 600px; margin: 0 auto"></div>\n')

    for school in schoolList:
        if school == 'Alberta':
            pass
        elif school == 'EIPS':
            pass
        else:
            htmlFile.write('<button id="button' + school + '" class="autocompare">Show ' + school + '</button>\n')
    htmlFile.write('<button id="buttonEIPS" class="autocompare">Hide EIPS</button>\n')
    htmlFile.write('<button id="buttonAlberta" class="autocompare">Hide Alberta</button>\n')
    htmlFile.write('<button id="buttonAll" class="autocompare">Hide All</button>\n')

    # and add the school list from a text file full of html
    footerTextFile = open('footerSchoolList.txt', 'r')
    htmlFile.write(footerTextFile.read())
    htmlFile.write('</body></html>\n')

#htmlFile.write("\n")
#htmlFile.write('\n')

courseList = ['Biology 30',
              'Chemistry 30',
              'English Lang Arts 30-2',
              'English Lang Arts 30-1',
              'Social Studies 30-1',
              'Social Studies 30-2',
              'Mathematics 30-1',
              'Mathematics 30-2',
              'Physics 30',
              'Science 30',
              'French Lang Arts 30-1']

schoolList = ['3610',
              '3395',
              '3307',
              '3322',
              '3339',
              '3404',
              '3310',
              '3311',
              '3340',
              '3301',
              '3401',
              'EIPS',
              'Alberta']

schoolLabelList = [] # empty, but we'll build it from the above list
for school in schoolList:
    schoolLabelList.append(str(school) + ' Course Mark')
    schoolLabelList.append(str(school) + ' Exam Mar')

'''
csvFileName = 'Physics30.csv'
course = 'Physics 30'
'''
def makeHtml(which):
    for course in courseList:
        csvFileName = course.replace(" ", "") + which + '.csv'
        csvFile = open(csvFileName, 'rb')
        csvReader = csv.reader(csvFile)
        makeHeader(course, which)

        for index, row in enumerate(csvReader):
            if index != 0:
                name = row[0]
                data = [row[1], row[2], row[3], row[4], row[5]]
                print course
                #print name, data
                addSeries(course, name, data, which)
        csvFile.close()

        makeFooter(course, schoolLabelList, schoolList, which)

makeHtml('ea')
makeHtml('ce')

#makeHeader(course)
#addSeries(course, name, data)
#makeFooter(course, schoolLabelList, schoolList)
