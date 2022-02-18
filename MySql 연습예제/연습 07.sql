USE market_db;
DROP PROCEDURE IF EXISTS user_proc;
DELIMITER $$
CREATE PROCEDURE user_proc()
BEGIN
	SELECT * FROM member;
END $$ 
DELIMITER ;
CALL user_proc();

-- 매개변수 사용 
DROP PROCEDURE IF EXISTS user_proc1;
DELIMITER $$
CREATE PROCEDURE user_proc1(IN userName VARCHAR(10))
BEGIN
	SELECT * FROM member WHERE mem_name = userName;
END $$ 
DELIMITER ;

CALL user_proc1('에이핑크');

DROP PROCEDURE IF EXISTS user_proc2;
DELIMITER $$
CREATE PROCEDURE user_proc2(
	IN userNumber INT,
    IN userHeight INT)
BEGIN
	SELECT * FROM member 
    WHERE mem_number > userNumber AND height > userHeight;
END $$ 
DELIMITER ;

CALL user_proc2(6, 165);


DROP PROCEDURE IF EXISTS user_proc3;
DELIMITER $$
CREATE PROCEDURE user_proc3(
    IN txtValue CHAR(10),
    OUT outValue INT     )
BEGIN
  INSERT INTO noTable VALUES(NULL,txtValue);
  SELECT MAX(id) INTO outValue FROM noTable; 
END $$
DELIMITER ;

DESC noTable;


CREATE TABLE IF NOT EXISTS noTable(
    id INT AUTO_INCREMENT PRIMARY KEY, 
    txt CHAR(10)
);

CALL user_proc3 ('테스트1', @myValue);
SELECT CONCAT('입력된 ID 값 ==>', @myValue);

DROP PROCEDURE IF EXISTS ifelse_proc;
DELIMITER $$
CREATE PROCEDURE ifelse_proc(
    IN memName VARCHAR(10)
)
BEGIN
    DECLARE debutYear INT; -- 변수 선언
    SELECT YEAR(debut_date) into debutYear FROM member -- 멤버 t의 데뷔년도를 debutYear에 지정 
        WHERE mem_name = memName;
    IF (debutYear >= 2015) THEN
            SELECT '신인 가수네요. 화이팅 하세요.' AS '메시지';
    ELSE
            SELECT '고참 가수네요. 그동안 수고하셨어요.'AS '메시지';
    END IF;
END $$
DELIMITER ;

CALL ifelse_proc('블랙핑크');

-- 커서 
-- 그룹별 평균 인원수 계산

USE market_db;
DROP PROCEDURE IF EXISTS cursor_proc;

DELIMITER $$
CREATE PROCEDURE cursor_proc()
BEGIN
	DECLARE memNumber INT; 	 		-- 회원당 인원수
    DECLARE cnt INT DEFAULT 0 ;		-- 읽은 행 수 
    DECLARE totNumber INT DEFAULT 0 ;	-- 전체 인원수
    DECLARE endOfRow BOOLEAN DEFAULT FALSE;  	-- 행의 끝을 파악 
    
    DECLARE memberCuror CURSOR FOR
		SELECT mem_number FROM member; -- 커서 선언 : 회원수를 가져옴
	
	DECLARE CONTINUE HANDLER -- 행의 끝이면 endOfRow 변수에 TRUE를 대입 
        FOR NOT FOUND SET endOfRow = TRUE;

    OPEN memberCuror;  -- 커서 열기

    cursor_loop: LOOP
        FETCH  memberCuror INTO memNumber;  -- 한행씩 읽어오기 

        IF endOfRow THEN  		-- endofRow = T면 루프 탈출
            LEAVE cursor_loop;
        END IF;

        SET cnt = cnt + 1;				-- 행 하나 읽었으니 읽은 행수 +1
        SET totNumber = totNumber + memNumber;   --   인원 합은 = 기존 + 인원수
    END LOOP cursor_loop;

    SELECT (totNumber/cnt) AS '회원의 평균 인원 수';		-- 전체 인원 / 전체 회원수(행수)

    CLOSE memberCuror; 	-- 커서 닫기
END $$ 		-- 프로시저 닫기 
DELIMITER ;

CALL cursor_proc(); -- 프로시저 호출 


-- 트리거 
USE market_db;
CREATE TABLE IF NOT EXISTS trigger_table (id INT, txt VARCHAR(10));
INSERT INTO trigger_table VALUES(1, '레드벨벳');
INSERT INTO trigger_table VALUES(2, '잇지');
INSERT INTO trigger_table VALUES(3, '블랙핑크');

DELIMITER $$
CREATE TRIGGER myTrigger
	AFTER DELETE
    ON trigger_table
    FOR EACH ROW
BEGIN
	SET @msg = '가수 그룹이 삭제됨';	 -- 트리거 실행시 작동될 코드 
    
END $$
DELIMITER ; 

SET @msg = '';

DELETE FROM trigger_table WHERE id = 3 ;
SELECT @msg; 


--- USE market_db;
CREATE TABLE singer 
(SELECT mem_id , mem_name , mem_number, addr FROM member);  -- 테이블을 복사해 새로운 테이블 

-- 백업 테이블 
DROP TABLE IF EXISTS backup_singer; 
CREATE TABLE backup_singer
( mem_id  		CHAR(8) NOT NULL , 
  mem_name    	VARCHAR(10) NOT NULL, 
  mem_number    INT NOT NULL, 
  addr	  		CHAR(2) NOT NULL,
  modType CHAR(2), -- 변경된 타입 (수정 OR 삭제)
  modDate DATE, 	  -- 변경된 날짜
  modUSer VARCHAR(30) -- 변경한 사용자
);

-- UPDATE 트리거 
DROP TRIGGER IF EXISTS singer_updateTrg;
DELIMITER $$
CREATE TRIGGER singer_updateTrg
	AFTER UPDATE
    ON singer 			-- singer 테이블이 수정되면  
    FOR EACH ROW
BEGIN
	INSERT INTO backup_singer VALUES(OLD.mem_id, OLD.mem_name , OLD.mem_number, 
		OLD.addr, '수정', CURDATE(), CURRENT_USER() );
END $$
DELIMITER ;        
-- DELETE 트리거 
DROP TRIGGER IF EXISTS singer_deleteTrg;
DELIMITER $$
CREATE TRIGGER singer_deleteTrg
	AFTER DELETE
    ON singer
    FOR EACH ROW
BEGIN
	INSERT INTO backup_singer VALUES(OLD.mem_id, OLD.mem_name , OLD.mem_number, 
		OLD.addr, '삭제', CURDATE(), CURRENT_USER() );
END $$
DELIMITER ;        

UPDATE singer SET addr= '영국' WHERE mem_id ='BLK' ; 
DELETE FROM singer WHERE mem_number >= 7;

SELECT * FROM singer;
SELECT * FROM backup_singer;

TRUNCATE TABLE singer; 
SELECT * FROM backup_singer;