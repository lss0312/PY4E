# sql
# establish a table use SQLlit
CREATE TABLE Users(
	name VARCHAR(128)
	email VARCHAR(128)
	)
# VARCHAR means the longest lenth that stored in the database 
# SQL insert data
INSERT INTO Users (name,email) VALUES('Kristin','kf@umich.edu')
# delet
DELETE FROM Users WHERE email='df@123.com'
# update 
UPADTE Users SET name='Charles' WHERE email ='sally@163.com'
# retrieve records
SELECT*FROM Users WHERE email=''
# order by some certain attributes
SELECT*FROM Users ORDER BY email

# use python to read database and do some calculating
import sqlite3
conn = squlite3.connect('emaildb.sqlite')# used to make a connection to the database file
cur = conn.cursor()#read the file
cur.execute(''' DROP TABLE IF EXISTS Counts''')
cur.execute('''CREATE TABLE Counst(email TEXT, count INTERGER)''') # create a new table

fname = input('Enter file name:')
if (len(fname) < 1):
	fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
	if not line.startwith('From：'):
		continue
	pieces = line.split()
	email = pieces[1]
	cur.execute('SELECT count FROM Counts WHERE email = ?',(email,))
	row = cur.fetchone()
	if row is None:
		cur.execute('''INSERT INTO Counts (email,count)) VALUE (?,1)'''(email,))
	else:
	    cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',(email,))
	conn.commit()	

	sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
	for row in cur.execute(sqlstr):
		print(str(row[0],row[1]))