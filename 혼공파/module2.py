import sys #시스템과 관련된 정보 
print(sys.version)
#명령 매개변수 
print(sys.argv)

import datetime #날짜 및 시간과 관련된 모듈 
now = datetime.datetime.now()
print(now.year)
print(now.month) #python에서 month는 1~12, 다른 프로그래밍 : 0~11
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
from datetime import datetime
now = datetime.now()        #기준을 now()가 아닌 특정시간 (2010,3,1,1,1,1,)으로 설정 가능 
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

import time #'시간'과 관련된 기능을 다룰때 
print("A")
time.sleep(3) # 특정시간동안 코드진행 정지 , 매개변수에 정지하고 싶은 시간 초단위 
print("3초뒤에 B가 출력되었습니다.")

#urllib 모듈 : url library, 인터넷 주소를 활용할때 사용하는 라이브러리
from urllib import request
#urlopen으로 구글의 메인페이지를 읽습니다.
target = request.urlopen("https://www.google.co.kr/")
output = target.read() 
print(output[:100])
# 스크래핑? 크롤링 ? 