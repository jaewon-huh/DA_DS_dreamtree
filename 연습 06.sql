USE market_db;
CREATE TABLE table1  (
    col1  INT  PRIMARY KEY,
    col2  INT,
    col3  INT
);
SHOW INDEX FROM table1;

CREATE TABLE table2 (
	col1 INT PRIMARY KEY,
    col2 INT UNIQUE,
    col3 INT UNIQUE
    );
SHOW INDEX FROM table2;

-- 자동으로 정렬되는 클러스터형 인덱스 
USE market_db; 
DROP TABLE IF EXISTS buy,member ;
CREATE TABLE member
( mem_id CHAR(8),
  mem_name    VARCHAR(10),
  mem_number  INT ,  
  addr        CHAR(2)  
 );
INSERT INTO member VALUES('TWC', '트와이스', 9, '서울');
INSERT INTO member VALUES('BLK', '블랙핑크', 4, '경남');
INSERT INTO member VALUES('WMN', '여자친구', 6, '경기');
INSERT INTO member VALUES('OMY', '오마이걸', 7, '서울');
SELECT * FROM member; -- primiary 키 지정 전 정렬 안됨 

ALTER TABLE member
	ADD CONSTRAINT
    PRIMARY KEY(mem_id);
SELECT* FROM member ; 

-- mem_name 을 primary key로 
ALTER TABLE member DROP PRIMARY KEY;

ALTER TABLE member
	ADD CONSTRAINT
    PRIMARY KEY(mem_name);
SELECT* FROM member ;

INSERT INTO member VALUES('GRL' , '소녀시대' , 8 , '서울'); -- 데이터 추가시 알아서 기준에 맞게 정렬 됨 
SELECT* FROM member ;


-- 보조 인덱스 Unique 자동정렬 x
DROP TABLE IF EXISTS member ;
CREATE TABLE member
( mem_id 	  CHAR(8),
  mem_name    VARCHAR(10),
  mem_number  INT ,  
  addr        CHAR(2)  
 );
 
INSERT INTO member VALUES('TWC', '트와이스', 9, '서울');
INSERT INTO member VALUES('BLK', '블랙핑크', 4, '경남');
INSERT INTO member VALUES('WMN', '여자친구', 6, '경기');
INSERT INTO member VALUES('OMY', '오마이걸', 7, '서울');
SELECT * FROM member; 

ALTER TABLE member 
	ADD CONSTRAINT
    UNIQUE (mem_id);
SELECT * FROM member;  -- 내용이나 순서 변경 x 

ALTER TABLE member 
	ADD CONSTRAINT
    UNIQUE (mem_name);
SELECT * FROM member;  -- 내용이나 순서 변경 x 
INSERT INTO member VALUES('GRL' , '소녀시대' , 8 , '서울'); -- 데이터 추가시 알아서 기준에 맞게 정렬 됨 
SELECT* FROM member ;

-- 인덱스의 내부 작동 
USE market_db;
CREATE TABLE cluster  -- 클러스터형 테이블 
( mem_id      CHAR(8) , 
  mem_name    VARCHAR(10)
 );
INSERT INTO cluster VALUES('TWC', '트와이스');
INSERT INTO cluster VALUES('BLK', '블랙핑크');
INSERT INTO cluster VALUES('WMN', '여자친구');
INSERT INTO cluster VALUES('OMY', '오마이걸');
INSERT INTO cluster VALUES('GRL', '소녀시대');
INSERT INTO cluster VALUES('ITZ', '잇지');
INSERT INTO cluster VALUES('RED', '레드벨벳');
INSERT INTO cluster VALUES('APN', '에이핑크');
INSERT INTO cluster VALUES('SPC', '우주소녀');
INSERT INTO cluster VALUES('MMU', '마마무');

SELECT * FROM cluster;

-- 인덱스 지정 
ALTER TABLE cluster 
	ADD CONSTRAINT
    PRIMARY KEY(mem_id);
SELECT * FROM cluster;

USE market_db;
CREATE TABLE second  -- 보조 인덱스 테이블 
( mem_id      CHAR(8) , 
  mem_name    VARCHAR(10)
 );
INSERT INTO second VALUES('TWC', '트와이스');
INSERT INTO second VALUES('BLK', '블랙핑크');
INSERT INTO second VALUES('WMN', '여자친구');
INSERT INTO second VALUES('OMY', '오마이걸');
INSERT INTO second VALUES('GRL', '소녀시대');
INSERT INTO second VALUES('ITZ', '잇지');
INSERT INTO second VALUES('RED', '레드벨벳');
INSERT INTO second VALUES('APN', '에이핑크');
INSERT INTO second VALUES('SPC', '우주소녀');
INSERT INTO second VALUES('MMU', '마마무');

ALTER TABLE second
    ADD CONSTRAINT 
    UNIQUE (mem_id);

SELECT * FROM second;


-- 인덱스 생성 및 제거 
USE market_db;
SELECT * FROM member;

SHOW INDEX FROM member; 
SHOW TABLE STATUS LIKE 'member';

-- 보조인덱스 생성
CREATE INDEX idx_member_addr -- 멤버 테이블의 addr 열에 지정된 인덱스 
	 ON member(addr);

SHOW INDEX FROM member; 
ANALYZE TABLE member;
SHOW TABLE STATUS LIKE 'member';


CREATE UNIQUE INDEX idx_member_mem_name
    ON member (mem_name);
ANALYZE TABLE member;

SHOW INDEX FROM member; 
SHOW TABLE STATUS LIKE 'member';
    
-- 인덱스 활용
SELECT * FROM member ; -- EXECUTION PLAN FULL TABLE SCAN
SELECT mem_id, mem_name, addr FROM member ;

SELECT mem_id, mem_name, addr 
	FROM member 
    WHERE mem_name = '에이핑크';
	
    
CREATE INDEX idx_member_mem_number
    ON member (mem_number);
ANALYZE TABLE member; -- 인덱스 적용

SELECT mem_name, mem_number
	FROM member
    WHERE mem_number >= 7 ;
    

SELECT mem_name, mem_number
	FROM member
    WHERE mem_number >= 1;
    
SELECT mem_name, mem_number
	FROM member
    WHERE mem_number*2 >= 14;
    
SELECT mem_name, mem_number
	FROM member
    WHERE mem_number >= 14/2 ; 
SELECT mem_id, mem_name
	FROM member
	WHERE height >162; 

-- 인덱스 제거
SHOW INDEX FROM member;

DROP INDEX idx_member_mem_name ON member;
DROP INDEX idx_member_addr ON member;
DROP INDEX idx_member_mem_number ON member;
 
ALTER TABLE member 
    DROP PRIMARY KEY;

SELECT table_name, constraint_name
    FROM information_schema.referential_constraints
    WHERE constraint_schema = 'market_db';
