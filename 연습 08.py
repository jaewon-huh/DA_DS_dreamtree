# cur.execute("CREATE TABLE usertable (id char(4), username char(15),
#                  email char(20), birthYear int)")
# cur.execute("INSER INTO usertable VALUES (' ' , ' ' ~ )")

import pymysql

### 데이터 입력 프로그램 

# 전역 변수 선언
conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""   # 사용할 변수들  
sql=""  

# 메인 코드  (mysql 연결 및 커서생성)
conn = pymysql.connect(host='127.0.0.1', user='root', password='woal00', db='soloDB', charset='utf8')
cur = conn.cursor()

#데이터 입력 
while (True) :
    data1 = input("사용자 id =>")
    if data1 == "" :
        break           # 입력하지 않으면 break
    data2 = input('사용자 이름 =>')
    data3 = input('사용자 이메일 =>')
    data4 = input('사용자 출생년도 =>')
    #(id char(4), username char(15)  , email char(20), birthYear int)")
    sql = "INSERT INTO userTable VALUES('" +data1 +"' ,'" +data2 +"', '" +data3 +"'," +data4 +")"
    cur.execute(sql)        
# 커밋 및 종료 
conn.commit()
conn.close()

### 데이터 조회 