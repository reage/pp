from uuid import uuid1
import MySQLdb

i = 0
sn = set()
while i < 200:
    i+=1
    tmp = uuid1()
    sn.add(tmp)
