#  원자 벡터  : 일차원 벡터 
die <- c(1,2,3,4,5,6)
is.vector(die)
length(die)
class(die)

int <- 1L # 정수형 : 숫자뒤 대문자L 
text <- " ace" # 문자형 : " "
int <- c(1L,5L)
sum(int)
# 실수형 double
die <- c(1,2,3,4,5,6)
typeof(die)
sqrt(2)^2 -2 # 부동소수점 오차 
# 논리형 logical
3>4
typeof(3>4)
# 복소수형 complex , i , 원시형 raw raw(n)

# 스페이드 로열 플러시 
hand <- c("ace", "king", "queen", "jack", "ten") #카드 이름 저장 
hand

# 속성 : 벡터에 붙일 수 있는 정보 ( 이름 names , 차원 dim, 클래스 class) , 열?
attributes(die)

# 이름 name 
names(die) <- c("one", "two", "three", "four", "five", "six")
names(die)
attributes(die)
die
die + 1 # 이름은 실제 벡터 값에 영향 x, 
names(die) <- c("uno", "dos", "tres", "cuatro", "cinco", "seis") # 새로 할당 
die
names(die) <- NULL # 이름 지우기 
die

# 차원 dim -> 원자 벡터를 n차원 배열로 변경
dim(die) <-c(2,3) # 2행 3열
die
dim(die) <-c(1,2,3) # 3차원 하이퍼 큐브 1행 2열 , 3슬라이스 
die

# 행렬  matrix(값, 행의수 ,열의수 , byrow = T 행 중심 입력)
m <- matrix(die, nrow=2, ncol=3)
m <- matrix(die,2,3)
m
m <- matrix(die, 2, byrow = T)
m

?matrix  
#dimnames= : 행과 열의 이름 지정 = rownames(mdat) <-c("row1", "row2")  
mdat <- matrix(c(1,2,3, 11,12,13), nrow = 2, ncol = 3, byrow = TRUE,
               dimnames = list(c("row1", "row2"),
                               c("C.1", "C.2", "C.3"))) 
mdat
row.names(mdat)

# 배열 array =(값 , dim = c(행,열, 슬라이스) )
ar <- array(c(11:14, 21:24, 31:34), dim = c(2, 2, 3))
ar

hand1 <-c("ace", "king", "queen", "jack", "ten",
          "spades", "spades", "spades", "spades", "spades")
hand1
matrix(hand1, ncol=2 )
dim(hand1) <-c(5,2)
hand1
hand2 <-c("ace", "spades", "king", "spades", "queen", "spades", "jack", "spades", "ten", "spades")
matrix(hand2, ncol =2 , byrow =T)

# 클래스 class 
# 객체의 차원을 바꾸면 객체의 자료형은 변하지 않으나 , 클래스 속성은 변화 
dim(die) <-c(2,3)
typeof(die)
class(die) # numeric에서 matrix 로 (속성이니까)
attributes(die)

# 날짜   
now <- Sys.time()
now
typeof(now)
class(now)
unclass(now) #클래스 속성을 지워 벡터 확인 
# 실수형 벡터에 시간 클래스를 부여해 시간을 다루는 중이라고 알려줄 수 있음.

# 요인 클래스 factor : 범주형 정보 저장 (남,녀)
gender <- factor(c("male","female","male","female"))
gender
attributes(gender)

# ace, heart, 1을 가지는 카드
card <- c("ace", "hearts", 1)
card # 벡터는 하나의 자료형만 따라서 문자열로 변환함 
# 강제변환 논리 -> 숫자형 -> 문자형 
sum(c(T,T,F,F)) # sum(c(1,1,0,0))
as.character(1)
as.logical(1)
as.numeric(F)

# 리스트 객체 list() : 한 벡터에 다양한 자료형가능 , R 객체들을 그룹화
list1 <- list(100:130 , "R", list(T,F))
list1
# ace, heart, 1 을 가지는 게임용 카드 
card  <- list("ace", "hearts", 1)
card
# 데이터 프레임 data.frame(var1, var2, var3 ...)
df <- data.frame(face = c("ace","two","six"),
                 suit = c("clubs", "clubs", "clubs"),
                 value = c(1,2,3))
df
typeof(df) # df의 자료형은 list
class(df) # 클래스 = data.frame 를 같는 리스트 
str(df)
# 데이터 불러오기 
deck <- read.csv("card.csv", header = T)
head(deck)
getwd()
write.csv(deck,file ="card.csv", row.names = F)
