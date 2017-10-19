# Author: Karim and Jeremy
# Course: TCMG 476
# Date: 10/19/2017
# This is a python program that should check this log (file.https://s3.amazonaws.com/tcmg412-fall2016/http_access_log)

from datetime import datetime


def question_1 () :
	f = open('http_access_log', 'r')
	count = 0
	allLine = []

	for line in f:
		count += 1
		allLine.append(line)


	print ("1. How many total request were made in the time period represented in the log?")
	print len(allLine)
	print " "
def question_2 ():
	f = open('http_access_log', 'r')
        count = 0

        by_weekday = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
	by_month = {1: 0, 2: 0, 3: 0, 3: 0, 4: 0, 5: 0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

        for line in f:
                count += 1
                split_data = line.split()

                try:
                        str_date = line.split()[3][1:].split(':')[0]
                except:
                        pass
                date = datetime.strptime( str_date, "%d/%b/%Y" )
                by_weekday[date.weekday()] += 1
		by_month[date.month] += 1

       	print ("2. How many requests were made on each day?")
	print 'Monday:   ', by_weekday[0]
	print 'Tuesday:  ', by_weekday[1]
	print 'Wednesday:', by_weekday[2]
	print 'Thursday: ', by_weekday[3]
	print 'Friday:   ', by_weekday[4]
	print 'Saturday: ', by_weekday[5]
	print 'Sunday:   ', by_weekday[6]
	print " "

	print ("How many requests were made on each month?")
	print 'Jan:   ', by_month[1]
	print 'Feb:   ', by_month[2]
	print 'Mar:   ', by_month[3]
	print 'Apr:   ', by_month[4]
	print 'May:   ', by_month[5]
	print 'Jun:   ', by_month[6]
	print 'Jul:   ', by_month[7]
	print 'Aug:   ', by_month[8]
	print 'Sep:   ', by_month[9]
	print 'Oct:   ', by_month[10]
	print 'Nov:   ', by_month[11]
	print 'Dec:   ', by_month[12]
	print " "

question_1()
question_2()

