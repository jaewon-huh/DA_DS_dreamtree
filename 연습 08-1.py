import pymysql

### 데이터 조회 프로그램 select

# 전역 변수 선언
conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""   # 사용할 변수들  
row = None 

# 메인 코드  (mysql 연결 및 커서생성)
conn = pymysql.connect(host='127.0.0.1', user='root', password='woal00', db='soloDB', charset='utf8')
cur = conn.cursor()

cur.execute("SELECT * FROM userTable")    # 테이블 조회 , 결과는 cur 변수에 저장 

print("사용자ID      사용자이름        이메일          출생년도")
print("---------------------------------------------------------")

while (True) :
    row = cur.fetchone()        # 한 행씩 추출한 데이터를 row에
                                # row 변수에 튜플형식으로 행 데이터가 저장됨 
    if row == None :            # 더 이상 읽을 행 x
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%5s   %15s  %20s %d" %(data1, data2, data3, data4))

conn.close()    