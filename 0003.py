from uuid import uuid1
import redis

i = 0
sn = set()
while i < 200:
    i+=1
    tmp = uuid1()
    sn.add(tmp)
try:
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set('sn', sn)
    print r.get('sn')
    r.delete('sn')
except:
    print 'Error'
