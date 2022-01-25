USE market_db;
SELECT addr,height 키,debut_date "데뷔 일자"
FROM member ;

SELECT * FROM member WHERE mem_name = '블랙핑크' ; 
SELECT * FROM member WHERE mem_number = 4 ; 

SELECT * FROM member WHERE height <= 162 ;

SELECT * FROM member WHERE height >= 165 AND mem_number > 6 ; 
SELECT * FROM member WHERE height >= 165 or mem_number > 6 ; 

SELECT * FROM member WHERE mem_name LIKE '우%'; -- 아아이아 
SELECT * FROM member WHERE mem_name LIKE '__핑크';

USE market_db;
CREATE TABLE hongong1 (toy_id  INT , toy_name CHAR(4), age INT); 
INSERT INTO hongong1  VALUES (1, '우디', 25);

INSERT INTO hongong1 (toy_id , toy_name) VALUES (2, '버즈');

select * FROM hongong1;

CREATE TABLE hongong2 ( 
   toy_id  INT AUTO_INCREMENT PRIMARY KEY, 
   toy_name CHAR(4), 
   age INT);

INSERT INTO hongong2 VALUES (NULL, '보핍', 25);
INSERT INTO hongong2 VALUES (NULL, '슬링키', 22);
INSERT INTO hongong2 VALUES (NULL, '렉스', 21);
SELECT * FROM hongong2;

SELECT last_insert_id();

ALTER TABLE hongong2 auto_increment =100;
INSERT INTO hongong2 VALUES (NULL, '재원', 25);
SELECT * FROM hongong2;

CREATE TABLE hongong3 (
	toy_id  INT AUTO_INCREMENT PRIMARY KEY, 
    toy_name CHAR(4), 
	age INT);
ALTER TABLE hongong3 auto_increment =1000;
SET @@auto_increment_increment =3 ; 

INSERT INTO hongong3 VALUES (NULL, '토마스', 20);
INSERT INTO hongong3 VALUES (NULL, '제임스', 23);
INSERT INTO hongong3 VALUES (NULL, '고든', 25);
SELECT * FROM hongong3;

INSERT INTO hongong3 VALUES (NULL, '고든', 25), (NULL, '고든', 25), (NULL, '고든', 25) ;

SELECT COUNT(*) FROM world.city;  
desc world.city;

SELECT * FROM world.city LIMIT 5;
-- 가져오고 싶어 

CREATE TABLE city_popul (
 city_name CHAR(35),
 population INT);

SELECT * FROM city_popul ;

INSERT INTO city_popul
	SELECT Name, Population FROM world.city ;
    
SELECT * FROM city_popul WHERE city_name = 'Seoul';
UPDATE city_popul
	SET city_name = '서울'
    WHERE city_name = 'Seoul';
    
SELECT * FROM city_popul WHERE city_name = '서울';    

UPDATE city_popul
	SET city_name = '뉴욕' , population = 0 
    WHERE city_name = 'New York';

SELECT * FROM city_popul WHERE city_name = '뉴욕';    

-- WHERE 없이 : 전체 테이블 변경 (단위 변경)
UPDATE city_popul
	SET population = population / 10000 ;
SELECT * FROM city_popul LIMIT 5; 

DELETE FROM city_popul
	WHERE city_name LIKE 'New%' ;


USE market_db;
CREATE TABLE hongong4 (
tinyint_col TINYINT,
smallint_col SMALLINT,
int_col 	INT,
bigint_col	BIGINT);

INSERT INTO hongong4 VALUES (127,32767, 212313131,90000000000000);
INSERT INTO hongong4 VALUES (128,32768, 212313131,90000000000000);


DROP TABLE IF EXISTS buy, member;
CREATE TABLE member -- 회원 테이블
( mem_id      CHAR(8) NOT NULL PRIMARY KEY, -- 회원 아이디(PK)
  mem_name      VARCHAR(10) NOT NULL, -- 이름
  mem_number    INT NOT NULL,  -- 인원수
  addr          CHAR(2) NOT NULL, -- 주소(경기,서울,경남 식으로 2글자만입력)
  phone1        CHAR(3), -- 연락처의 국번(02, 031, 055 등)
  phone2        CHAR(8), -- 연락처의 나머지 전화번호(하이픈제외)
  height        SMALLINT,  -- 평균 키
  debut_date    DATE  -- 데뷔 일자
);

DROP TABLE IF EXISTS member;
CREATE TABLE member -- 회원 테이블
( mem_id      CHAR(8) NOT NULL PRIMARY KEY, -- 회원 아이디(PK)
  mem_name      VARCHAR(10) NOT NULL, -- 이름
  mem_number    TINYINT  NOT NULL,  -- 인원수
  addr          CHAR(2) NOT NULL, -- 주소(경기,서울,경남 식으로 2글자만입력)
  phone1        CHAR(3), -- 연락처의 국번(02, 031, 055 등)
  phone2        CHAR(8), -- 연락처의 나머지 전화번호(하이픈제외)
  height        TINYINT UNSIGNED,  -- 평균 키
  debut_date    DATE  -- 데뷔 일자
);

-- 변수 사용 
SET @count = 3 ; 
SELECT mem_name, height FROM member ORDER BY height LIMIT @count;  

SET @count = 3 ; 
PREPARE mysql FROM 'SELECT mem_name, height FROM member ORDER BY height LIMIT ?';
EXECUTE mysql USING @count; 

-- 형 변환 
SELECT AVG(price) FROM buy;

SELECT CAST(AVG(price) AS SIGNED) FROM buy;
SELECT CONVERT(AVG(price) , SIGNED) FROM buy;

SELECT CAST('2022$12$12' AS DATE);
SELECT CAST('2022/12/12' AS DATE);
SELECT CAST('2022%12%12' AS DATE);
SELECT CAST('2022@12@12' AS DATE);

SELECT * FROM buy ;

SELECT num, CONCAT(CAST(price AS CHAR) , 'X' , CAST(amount AS CHAR), '=') '가격X구매액' , 
price*amount '구매액' 
FROM buy ; 

-- 암시적 
SELECT '100' + '200' ;
SELECT CONCAT( '100', '200') ;
SELECT CONCAT (100, '200') ; -- 100200

SELECT 'SQL' +'Server' ;

USE market_db;
SELECT *
	FROM buy
		INNER JOIN member
		ON buy.mem_id = member.mem_id 
	WHERE buy.mem_id = 'GRL';
SELECT *
	FROM buy
		INNER JOIN member
		ON buy.mem_id = member.mem_id ;    
        
 -- 간결한 표현 
 SELECT mem_id, mem_name, prod_name, addr, CONCAT(phone1 , phone2) "연락처"
	FROM buy
		INNER JOIN member
		ON buy.mem_id = member.mem_id ;  	
        
SELECT buy.mem_id, mem_name, prod_name, addr, CONCAT(phone1 , phone2) "연락처"
	FROM buy
		INNER JOIN member
		ON buy.mem_id = member.mem_id ;         

SELECT B.mem_id, M.mem_name, B.prod_name, M.addr, 
		 CONCAT(M.phone1 , M.phone2) "연락처"
	FROM buy B
		INNER JOIN member M
		ON B.mem_id = M.mem_id ;   
 
-- 내부조인 두 테이블 모두 있는 내용만 , 
-- 구매기록 있는 회원 목록 (중복 X)
SELECT distinct M.mem_id, M.mem_name, M.addr, 
		 CONCAT(M.phone1 , M.phone2) "연락처"
	FROM buy B
		INNER JOIN member M
		ON B.mem_id = M.mem_id ;   
        
 -- 외부 조인 (한쪽만)
SELECT M.mem_id, M.mem_name, B.prod_name, M.addr, 
		 CONCAT(M.phone1 , M.phone2) "연락처"
	FROM member M
		LEFT OUTER JOIN buy B
		ON M.mem_id = B.mem_id ; 
        
SELECT DISTINCT M.mem_id, M.mem_name, M.addr, 
		 CONCAT(M.phone1 , M.phone2) "연락처"   -- 전체 회원 목록
	FROM member M
		LEFT OUTER JOIN buy B
		ON M.mem_id = B.mem_id ;   
        
-- 구매기록 없는 회원만 
SELECT M.mem_id, M.mem_name, M.addr, 
		 CONCAT(M.phone1 , M.phone2) "연락처"
	FROM member M
		LEFT OUTER JOIN buy B
		ON M.mem_id = B.mem_id 
    WHERE B.prod_name IS NULL ;    
    
-- CROSS JOIN
SELECT *
	FROM buy
		CROSS JOIN member; 
        
SELECT COUNT(*) "데이터 개수"
	FROM sakila.inventory
		CROSS JOIN world.city;
        
-- 실제 대용량 테이블 만들기 
CREATE TABLE cross_table
	SELECT *
		FROM sakila.actor
			CROSS JOIN world.country; 
            
SELECT * FROM cross_table LIMIT 5 ; 

-- 자체조인 (1개 테이블 , 회사 조직관계)

USE market_db;
CREATE TABLE emp_table (emp CHAR(4), manager CHAR(4), phone VARCHAR(8));

INSERT INTO emp_table VALUES('대표', NULL, '0000');
INSERT INTO emp_table VALUES('영업이사', '대표', '1111');
INSERT INTO emp_table VALUES('관리이사', '대표', '2222');
INSERT INTO emp_table VALUES('정보이사', '대표', '3333');
INSERT INTO emp_table VALUES('영업과장', '영업이사', '1111-1');
INSERT INTO emp_table VALUES('경리부장', '관리이사', '2222-1');
INSERT INTO emp_table VALUES('인사부장', '관리이사', '2222-2');
INSERT INTO emp_table VALUES('개발팀장', '정보이사', '3333-1');
INSERT INTO emp_table VALUES('개발주임', '정보이사', '3333-1-1');

SELECT * FROM emp_table ; 
-- 경리부장의 직속상관의 연락처 
SELECT A.emp "직원" , B.emp "직속상관" ,B.phone "연락처"
	FROM emp_table A
		INNER JOIN emp_table B 
		ON A.manager = B.emp 
    WHERE A.emp = '경리부장' ;
    
-- 4-3 SQL 프로그래밍 

DROP PROCEDURE IF EXISTS ifproc1;
DELIMITER $$
CREATE PROCEDURE ifproc1()
BEGIN
	IF 100 = 100 THEN
		SELECT '100은 100과 같다';
	END IF;
END $$
DELIMITER ;
CALL ifproc1();

DROP PROCEDURE IF EXISTS ifproc2;
DELIMITER $$
CREATE PROCEDURE ifproc2()
BEGIN
	DECLARE myNum INT;
    SET myNum = 200;
    IF myNum = 100 THEN
		SELECT 'myNum은 100';
	else
		SELECT 'myNum은 100 아님';
    END IF;
END $$
DELIMITER ;
CALL ifproc2();

-- 에이핑크 APN 데뷔일자 5년 지남 ?
DROP PROCEDURE IF EXISTS ifproc3;
DELIMITER $$
CREATE PROCEDURE ifproc3()
BEGIN
	DECLARE debutDate DATE;  -- 데뷔일
    DECLARE curDate DATE;	 -- 오늘 
    DECLARE days INT;		 -- 활동일
    
    SELECT debut_date INTO debutDate
		FROM market_db.member 
        WHERE mem_id = 'APN';  	-- debutdate 변수 설정
    SET curDate = CURRENT_DATE(); 	-- 오늘 
    SET days = DATEDIFF(curDate, debutDate); -- 날짜차이 (일 단위)
    
    IF (days/365) >= 5 THEN -- 활동일이 5년 이상 
		SELECT CONCAT('데뷔한지', days, '일이 지났습니다 ㅊㅋㅊㅋ');
	else
		SELECT CONCAT('데뷔한지', days, '일이 지났습니다 ㅍㅇㅌ');
    END IF;
END $$
DELIMITER ;
CALL ifproc3();

-- CASE 믄 CASE WHEN THEN ELSE END CASE; 
DROP PROCEDURE IF EXISTS caseProc;
DELIMITER $$
CREATE PROCEDURE caseProc()
BEGIN
	DECLARE point INT;
    DECLARE credit CHAR(1);
    SET point = 82;
   
   CASE
	WHEN point >= 90 THEN
		SET credit = 'A';
    WHEN point >= 80 THEN
		SET credit = 'B';
    WHEN point >= 70 THEN
		SET credit = 'C';
    WHEN point >= 60 THEN
		SET credit = 'D';
    ELSE
		SET credit = 'F'; 
    END CASE;
    SELECT CONCAT('점수 ==>', point), CONCAT('학점 ==>', credit);
END $$
DELIMITER ;
CALL caseProc();

-- 회원 총 구매액에 따른 구매등급
SELECT mem_id, SUM(price*amount) "총 구매액"
	FROM  buy
    GROUP BY mem_id
    ORDER BY SUM(price*amount) DESC;
-- 멤버 이름도 표시 

SELECT B.mem_id, M.mem_name, SUM(price*amount) "총 구매액"
	FROM buy B 
		INNER JOIN member M 
		ON B.mem_id = M.mem_id
    GROUP BY B.mem_id
    ORDER BY SUM(price*amount) DESC;
    
SELECT M.mem_id, M.mem_name, SUM(price*amount) "총 구매액"
	FROM buy B 
		RIGHT OUTER JOIN member M 
		ON B.mem_id = M.mem_id
    GROUP BY M.mem_id
    ORDER BY SUM(price*amount) DESC;
    
CASE 
	WHEN (총 구매액 >= 1500) THEN '최우수고객'
	WHEN (총 구매액 >= 1000) THEN '우수고객'
	WHEN (총 구매액 >= 1) THEN '일반고객'	
    ELSE '유령고객'
END 


SELECT M.mem_id, M.mem_name, SUM(price*amount) "총 구매액",
	CASE 
		WHEN ( SUM(price*amount) >= 1500) THEN '최우수고객'
		WHEN ( SUM(price*amount) >= 1000) THEN '우수고객'
		WHEN ( SUM(price*amount) >= 1) THEN '일반고객'	
		ELSE '유령고객'
	END "회원등급"
	FROM buy B 
		RIGHT OUTER JOIN member M 
		ON B.mem_id = M.mem_id
    GROUP BY M.mem_id
    ORDER BY SUM(price*amount) DESC;

-- WHILE 조건문 
   
DROP PROCEDURE IF EXISTS whileProc; 
DELIMITER $$
CREATE PROCEDURE whileProc()
BEGIN
    DECLARE i INT; -- 1에서 100까지 증가할 변수
    DECLARE hap INT; -- 더한 값을 누적할 변수
    SET i = 1;
    SET hap = 0;

    WHILE (i <= 100) DO
        SET hap = hap + i;  -- hap의 원래의 값에 i를 더해서 다시 hap에 넣으라는 의미
        SET i = i + 1;      -- i의 원래의 값에 1을 더해서 다시 i에 넣으라는 의미
    END WHILE;

    SELECT '1부터 100까지의 합 ==>', hap;   
END $$
DELIMITER ;
CALL whileProc();


-- ITERATE & LEAVE
 
DROP PROCEDURE IF EXISTS whileProc2;
DELIMITER $$
CREATE PROCEDURE whileProc2()
BEGIN
	DECLARE i INT; -- 1에서 100까지 증가할 변수
    DECLARE hap INT; -- 더한 값을 누적할 변수
    SET i = 1;
    SET hap = 0;

    mywhile:  	-- while 문 레이블 지정 
	WHILE (i <= 100 ) DO -- 1
        IF (i%4 =0) THEN
			SET i = i + 1;    
			ITERATE mywhile;
        END IF;
		SET hap = hap + i;  -- 0+1= 1, 
        IF (hap > 1000) THEN
			LEAVE mywhile;
		END IF;
		SET i = i + 1;
	END WHILE;
    SELECT '1부터 100까지의 합(4의 배수 제외), 1000 넘으면 종료 ==>' , hap;
END $$
DELIMITER ; 
CALL whileProc2();    


END $$
DELIMITER ;
CALL whileProc2();

USE market_db;
PREPARE myQuery FROM 'SELECT * FROM member WHERE mem_id = "BLK"';
EXECUTE myQuery ; 
DEALLOCATE PREPARE myQuery;

DROP TABLE IF EXISTS gate_table;
CREATE TABLE gate_table (id INT AUTO_INCREMENT PRIMARY KEY, 
						 entry_time DATETIME);
SET @curDate = current_timestamp();

PREPARE myQuery FROM 'INSERT INTO gate_table VALUES (NULL, ?)';
execute myQuery USING @curDate;
deallocate prepare myQuery;

SELECT* FROM gate_table;