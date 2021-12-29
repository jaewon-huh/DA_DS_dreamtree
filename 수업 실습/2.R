#데이터 열기 
trade <- read.csv("trade_dataset.csv", header = T)
trade <- read.csv(file.choose(), header = T)

#데이터 탐색
trade
head(trade)
tail(trade)


# 연산자 활용

x <- c(10, 20, 30, 40)
x
x[x < 30]
x[(x >= 10 & x < 40)]
x[!(x >= 10 & x < 40)] #부정 

# 열과 행으로 찾기
trade[1:5, 2:4]
trade[,1:3] # 1~3 열
trade[, c(1,3)] # 1,3열
trade[2:6,]
trade[5, 4]

# 변수명으로 찾기 
trade$Commodity[1:10]
names(trade)

# subset(데이터, 조건식 , 인자(열) ) :특정 조건 만족하는 데이터 찾기
subset(trade, Reporter.ISO == "KOR", select = "Trade.Flow")
trade_kor <- subset(trade, Reporter.ISO == "KOR") # 별도의 객체로 저장
trade_kor

# 데이터 유형 확인
class(trade)
class(trade$癤풷ear) # 첫 열이 깨짐 
class(trade$Trade.Flow)

trade <- read.csv("trade_dataset.csv", header = T, stringsAsFactors = F)
# 문자가 들어있는 열의 파일 불러올때 
class(trade$Trade.Flow)

# factor 요인(범주) 생성
eyes <- c("hazel", "brown", "black", "brown")
eyes # 값
eyes_factor <- factor(eyes)
eyes_factor # 범주 

eyes_factor <-factor(eyes, levels = c("black", "brown", "hazel", "blue")) # 범주 정의
eyes_factor

eyes_factor2 <- factor(eyes, levels = c("black", "brown")) # 범주를 2개만 
eyes_factor2

levels(eyes_factor) #범주만 

#ordered() : 순서가 있는 범주주
pain <- ordered(c("low", "medium", "medium", "high"),
                levels = c("low", "medium", "high")) # 지정
pain
# 요인 탐색
eyes_factor[1:3]
eyes_factor[pain > "medium"]
pain[eyes_factor == "brown"]
pain[eyes_factor != "black"]

eyes_factor == "black"
eyes_factor < "black" # 서열 x
pain <= "medium"


#데이터 저장 
trade_kor <- subset(trade, Reporter.ISO == "KOR")
dim(trade) # 행과 열 개수 확인 
dim(trade_kor)
# write.csv(객체명, file = "파일명.형식")
write.csv(trade_kor, file = "trade_kor.csv") 
# save(객체명, file = "파일명") : R 포멧으로 저장
save(trade_kor, file = "trade_kor")
rm(trade_kor) # 데이터 삭제 

load(file = "trade_kor")
