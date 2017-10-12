# Author: Karim and Jeremy
# Course: TCMG 476
# Date: 10/12/2017
# This is a python program that should check this log (file.https://s3.amazonaws.com/tcmg412-fall2016/http_access_log)

def main () :
	f = open('http_access_log', 'r')
	count = 0
	allLine = []
 

	for line in f: 
		count += 1
		allLine.append(line)
	print ("1. How many total request were made in the time period represented in the log?")
	print  len(allLine)
	
main()
