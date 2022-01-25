DROP DATABASE IF EXISTS naver_db;
CREATE DATABASE naver_db;

-- 테이블 생성 
USE naver_db;
D
DROP TABLE IF EXISTS buy;
CREATE TABLE buy
(num INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 mem_id CHAR(8) NOT NULL,
 prod_name VARCHAR(10) NOT NULL, 
 group_name CHAR(4) NULL,
 price INT UNSIGNED NOT NULL,
 amount SMALLINT UNSIGNED NOT NULL,
 FOREIGN KEY(mem_id) REFERENCES member(mem_id) -- 마지막에 외래키 지정 
 );
 
SELECT * FROM member;
SELECT * FROM buy;

-- 데이터 입력하기 
INSERT INTO member VALUES ('TWC', '트와이스', 9 , '서울', '02', '11111111', 167, '2015-10-19');
INSERT INTO member VALUES('BLK', '블랙핑크', 4, '경남', '055', '22222222', 163, '2016-8-8');
INSERT INTO member VALUES('WMN', '여자친구', 6, '경기', '031', '33333333', 166, '2015-1-15');


INSERT INTO buy VALUES( NULL, 'BLK', '지갑', NULL, 30, 2);
INSERT INTO buy VALUES( NULL, 'BLK', '맥북프로', '디지털', 1000, 1);
INSERT INTO buy VALUES( NULL, 'APN', '아이폰', '디지털', 200, 1);


-- 테이블 제약조건 
 USE naver_db;
 DESCRIBE member;

DROP TABLE IF EXISTS buy, member;
CREATE TABLE member
( mem_id CHAR(8) NOT NULL,
  mem_name VARCHAR(10) NOT NULL, 
  height TINYINT UNSIGNED NOT NULL,
  PRIMARY KEY(mem_id)
);
 DESCRIBE member;
 -- alter table
 DROP TABLE IF EXISTS member;
 CREATE TABLE member
(mem_id CHAR(8) NOT NULL,
 mem_name VARCHAR(10) NOT NULL, 
 height TINYINT UNSIGNED NOT NULL
);
ALTER TABLE member
	ADD CONSTRAINT
    PRIMARY KEY(mem_id);
 DESCRIBE member;    

-- 외래 키 
DROP TABLE IF EXISTS buy, member;
CREATE TABLE member 
( mem_id  CHAR(8) NOT NULL PRIMARY KEY, 
  mem_name    VARCHAR(10) NOT NULL, 
  height      TINYINT UNSIGNED NULL
);
CREATE TABLE buy 
(  num         INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
   mem_id      CHAR(8) NOT NULL, 
   prod_name     CHAR(6) NOT NULL, 
   FOREIGN KEY(mem_id) REFERENCES member(mem_id)
);

DROP TABLE IF EXISTS buy;
CREATE TABLE buy 
(  num         INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
   mem_id      CHAR(8) NOT NULL, 
   prod_name     CHAR(6) NOT NULL
);
ALTER TABLE buy
	ADD CONSTRAINT 
	FOREIGN KEY (mem_id)
    REFERENCES member (mem_id);
    
-- 기준 테이블의 열이 변경 ON UPDATE CASCADE
INSERT INTO member VALUES('BLK', '블랙핑크', 163);
INSERT INTO buy VALUES(NULL, 'BLK', '지갑');
INSERT INTO buy VALUES(NULL, 'BLK', '맥북');

SELECT M.mem_id, M.mem_name, B.prod_name
	FROM buy B
		INNER JOIN member M
		ON B.mem_id = M.mem_id ;
        
UPDATE member
	SET mem_id = 'PINK'
    WHERE mem_id = 'BLK' ;
    
DELETE FROM member WHERE mem_id = 'BLK';

DROP TABLE IF EXISTS buy;
CREATE TABLE buy 
(  num         INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
   mem_id      CHAR(8) NOT NULL, 
   prod_name     CHAR(6) NOT NULL
);
ALTER TABLE buy
	ADD CONSTRAINT
    FOREIGN KEY(mem_id) REFERENCES member(mem_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE; 
    
INSERT INTO buy VALUES(NULL, 'BLK', '지갑');
INSERT INTO buy VALUES(NULL, 'BLK', '맥북');    
    
UPDATE member
	SET mem_id = 'PINK'
    WHERE mem_id = 'BLK' ;
    
SELECT *  FROM buy; 

SELECT M.mem_id, M.mem_name, B.prod_name
	FROM buy B
		INNER JOIN member M
		ON B.mem_id = M.mem_id ;
        
    
DELETE FROM member WHERE mem_id = 'PINK';
SELECT *  FROM buy;  

-- 고유키 
DROP TABLE IF EXISTS buy, member;
CREATE TABLE member 
( mem_id  CHAR(8) NOT NULL PRIMARY KEY, 
  mem_name    VARCHAR(10) NOT NULL, 
  height      TINYINT UNSIGNED NULL,
  email		CHAR(30) NULL UNIQUE
);

INSERT INTO member VALUES('BLK', '블랙핑크', 163, 'pink@gmail.com');
INSERT INTO member VALUES('TWC', '트와이스', 167, NULL);
INSERT INTO member VALUES('APN', '에이핑크', 164, 'pink@gmail.com');

SELECT * FROM member;


DROP TABLE IF EXISTS member;
CREATE TABLE member 
( mem_id  CHAR(8) NOT NULL PRIMARY KEY, 
  mem_name    VARCHAR(10) NOT NULL, 
  height      TINYINT UNSIGNED NULL CHECK(height >= 100),
  phone1	CHAR(3)	NULL
);

INSERT INTO member VALUES('BLK', '블랙핑크', 163, NULL);
INSERT INTO member VALUES('TWC', '트와이스', 99, NULL); -- 에러 

ALTER TABLE member 
	ADD CONSTRAINT
    CHECK(phone1 IN('02', '031', '032', '054', '055', '061'));
    
INSERT INTO member VALUES('TWC', '트와이스', 167, '02'); 
INSERT INTO member VALUES('OMY', '오마이걸', 182, '010');     

SELECT * FROM member; 


DROP TABLE IF EXISTS member;
CREATE TABLE member 
( mem_id  CHAR(8) NOT NULL PRIMARY KEY, 
  mem_name    VARCHAR(10) NOT NULL, 
  height      TINYINT UNSIGNED NULL DEFAULT 160,
  phone1	CHAR(3)	NULL
);
ALTER TABLE member
	ALTER COLUMN phone1 SET DEFAULT '02';
    
INSERT INTO member VALUES('RED', '레드벨벳', 152, '031');
INSERT INTO member VALUES('SPC', '우주소녀', default, default);

SELECT * FROM member; 


-- 뷰 
USE market_db;
SELECT mem_id, mem_name, addr FROM member; -- select 문의 결과 

CREATE VIEW v_member
AS 
	SELECT mem_id, mem_name, addr FROM member;
	
SELECT * FROM v_member;     
SELECT mem_id, addr FROM v_member
	WHERE addr IN('서울', '경기');
    
SELECT B.mem_id, M.mem_name, B.prod_name, M.addr, 
        CONCAT(M.phone1, M.phone2) '연락처' 
   FROM buy B
     INNER JOIN member M
     ON B.mem_id = M.mem_id;

CREATE VIEW v_memberbuy
AS
    SELECT B.mem_id, M.mem_name, B.prod_name, M.addr, 
            CONCAT(M.phone1, M.phone2) '연락처' 
       FROM buy B
         INNER JOIN member M
         ON B.mem_id = M.mem_id;
         
SELECT * FROM v_memberbuy; 

USE market_db;
CREATE VIEW v_viewtest
AS
	SELECT B.mem_id "Member ID", M.mem_name AS "Member Name",
			B.prod_name "Product Name", CONCAT(M.phone1, M.phone2) AS "Office Phone"
		FROM buy B
			INNER JOIN member M 
            ON B.mem_id = M.mem_id;
            
 SELECT DISTInCT mem_id FROM buy ;
 SELECT DISTINCT `Member ID`, `Member Name`
	FROM v_viewtest ;  -- 구매자 목록 
    
CREATE OR REPLACE VIEW v_viewtest2 
AS 
	SELECT mem_id, mem_name, addr FROM member; 
    
DESCRIBE v_viewtest2; 
DESCRIBE member;

SHOW CREATE VIEW v_viewtest2;

UPDATE v_member SET addr = '부산' WHERE mem_id='BLK' ;

INSERT INTO v_member(mem_id, mem_name, addr) VALUES('BTS','방탄소년단','경기') ;
DESCRIBE member;

CREATE VIEW v_height167
AS
	SELECT * FROM member WHERE height >=167;
    
SELECT * FROM v_height167;
DELETE FROM v_height167 WHERE height < 167;

-- 데이터 입력 
INSERT INTO v_height167 VALUES('TRA' , '티아라', 6 , '서울', NULL, NULL, 156, '2005-01=01'); 

ALTER VIEW v_height167
AS
	SELECT * FROM member WHERE height >=167
			 WITH CHECK OPTION;  -- 167 이상의 데이터만 입력되도록 
             
INSERT INTO v_height167 VALUES('TRA' , '티아라', 6 , '서울', NULL, NULL, 156, '2005-01=01'); -- CHECK OPTION FAILED