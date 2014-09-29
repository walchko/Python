#!/usr/bin/env python


import sqlite3 as lite
import sys

def getTableNames(con):
	with con:
		cur = con.cursor()    
		cur.execute("SELECT name FROM sqlite_master WHERE type='table'")

		rows = cur.fetchall()
		r = list()

		for row in rows:
			#print row[0]
			r.append(row[0])
		
		return r

def printTable(con,tablename):
	if tablename == 'oui':
		return
		
	cur = con.cursor()
	comm = "SELECT * FROM %s" % tablename    
	cur.execute(comm)
	
	rows = cur.fetchall()
	
	print 'Table: ',tablename
	for row in rows:
		print row

def main():
	con = lite.connect('db')
	
	tn = getTableNames(con)
	#print tn
	
	for i in tn:
		printTable(con,i)
	
	con.close()




if __name__ == '__main__':
    main()

