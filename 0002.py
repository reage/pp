from uuid import uuid1
import MySQLdb

i = 0
sn = set()
while i < 200:
    i+=1
    tmp = uuid1()
    sn.add(tmp)
try:
    db = MySQLdb.connect("localhost", "root", "", "py")

    cursor = db.cursor()
    for item in sn: 
        cursor.execute("INSERT INTO sn(ser) VALUES ('%s')" % str(item))
        db.commit()
except:
    print 'Error'
