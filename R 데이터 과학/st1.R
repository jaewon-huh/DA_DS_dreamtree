# 처음의 값을 리턴,  처음의 값 4 
4 + 2   # 2를 더한다
(4 + 2) * 3 # 더한 값에 3을 곱한다 
((4 + 2) * 3 ) - 6 # 곱한 값에서 6을 뺀다 
(((4 + 2) * 3 ) - 6) / 3  # 그 값을 3으로 나눈다 . 

#객체 생성 
1:6
die <- 1: 6  # 주사위 생성 
die
ls() # 현재 사용하고 있는 객체 이름 보기 
# R은 원소 단위 실행 
#(벡터를 일치시킨 뒤 원소들을 짝지어 원소별로 계산)
die -1 
die /2 
die * die 
# recyling (짧은 벡터를 긴 쪽 벡터 크기 만큼 반복 )
die + 1:2 
die + 1:4 # 배수관계 x 6: 4

# 함수 
round(3.14)  # 반올림
factorial(3) # 팩토리얼 ! 
mean(1:6)
mean(die)
round(mean(die)) # 안쪽 함수부터 수행 

# sample(벡터, size)
sample(x = 1 : 4 , size = 2)
sample(die, size = 1)
sample(size = 1, x = die) # 인수 이름 사용해서 대응 

args(sample) # 함수에 사용할 인수 확인 
args(round) # 0의 자리에서 반올림 하도록 설정 digits = 0 
round(3.14) 
round(3.1413 ,digits = 2 )

sample(die, size=2) # 한쌍 추출 , 비복원추출 
sample(die, size=2, replace = T) # 복원 추출 

dice <- sample(die, size =2, replace = T)
dice
sum(dice)
dice # 여러번 호출해도 객체 값 = , 한번 저장한 값만 

# roll() 이라는 함수를 만들자 :두개의 주사위를 굴려 나온 값의 합 리턴
# my_function <- function(인수) { 코드 입력 }
roll <- function(){
  die <- 1:6
  dice <- sample(die, size = 2, replace = T)
  sum(dice)
  }

roll
roll()
# 인수로 지정 : bones를 roll2 함수의 인수로 만들어 사용 
roll2 <- function(bones){
  dice <- sample(bones, size = 2, replace = T)
  sum(dice)
}
roll2(bones = 1 : 4)
roll2(bones = 1 : 6)

roll2()
# 인수의 기본값 지정 
roll2 <-roll2 <- function(bones = 1: 6){
  dice <- sample(bones, size = 2, replace = T)
  sum(dice)
}
roll2()

# qplot(x,y) : 그래프 , x축 y축, 산점도 (두 변수간 관계)
x <- seq(-1, 1, 0.2)
x
y <- x^3
y
qplot(x, y)
# 막대그래프 qqpolt(x, binwith = 1)
x <- c(1,2,2,2,3,3)
qplot(x,binwidth = 1) # 1-1 , 2-3, 3-2
x2 <- c(1,1,1,1,1,2,2,2,2,3,3,4)
qplot(x2, binwidth = 1)
x3 <- c(0,1,1,2,2,2,3,3,4)
qplot(x3, binwidth = 1)

# replicate(반복 횟수, 명령어)
replicate(3, 1+1)
replicate(10, roll()) # 적은 반복으로 qplot 불가 (무작위성)

rolls <- replicate(10000, roll())
qplot(rolls, binwidth =1 ) # 주사위 10000번 굴렸을때 편차 

#주사위 확률 조작 6 나올 확률을 3/8 나머지 수는 각 1/8로 
?sample # ?함수 : 도움말 , ??키워드 > 키워드 관련 도움말 
# sample(x ,size, replace=, prob=)
roll <- function(){
  die <- 1:6
  dice <- sample(die, size = 2, replace = T, 
                 prob = c(1/8, 1/8, 1/8, 1/8, 1/8, 3/8))
  sum(dice)
}
# 만약 x 가 엄청 크고 한 숫자에만 가중치를 두고 싶거나 1:3만 가중치 두고 싶으면?
roll()
rolls2 <- replicate(10000, roll())
qplot(rolls2, binwidth =1)
