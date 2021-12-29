x <- 10
foo <- function(x) {x + 10}
foo(5)
# 함수 자체를 다른 함수의 입력값으로 사용 -> 높은 수준의 함수 
?runif # 난수 생성 x개
matrix(runif(10), ncol = 2)
apply(matrix(runif(10), ncol = 2), 2, sum)
apply(matrix(runif(10), ncol = 2), 2, foo)
# 함수 정의 방법 
# funcution (인자)  { 수식}
plus<- function(x,y){x + y}
plus(2,5)
square <- function(x){x*x}
square(4)
square(1:10)
# 함수 내부에서 함수 사용 
# 제곱들의 합계  
sumsq <- function(x) {sum(square(x))}
sumsq(1:5) # 1 + 4 + 9 + 16 + 25
# 재정의 : 각 값과 평균의 차이의 제곱 분산?
sumsq <- function(x) {sum(square(x- mean(x)))}
sumsq(1:10)
# 익명함수 : 이름을 정의하지 않은 함수 
(function(x) x * x)(10) 
# 원리금 함수 , 원금 p 년수 y 이자율 i
payment <- function(p, y, i) {
  p * ( (i/1200) * (1 + i/1200)^(12*y) ) /
         ( (1 + i/1200)^(12*y) - 1 )  
}
# 6억 6873만원 , 이자 3.2% . 20%는 직접 지불 나머지 20년간 균등 상환
payment(0.8 * 66873, 20, 3.2)
payment(0.8 * 66873, c(20, 30, 40), 3.2)
# 제어구문 
x <- 0
if (x ==0) {print("Zero")} else {print("Non-zero")}
# 조건문  if - else
x <- -4
if (x > 0) {sqrt(x)} else {-sqrt(-x)} 
# 조건에 하나이상의 참/ 거짓 값 -> 첫번째 값만 사용 & 에러 
if (c(1,2) < 2) { print("expr1") } else { print("expr2") }
# is.even() : 사용자가 입력한 숫자가 홀수 or 짝수 
is.even <- function(x) {
  if(x %% 2 == 0) {T}   # 나머지 연산 %%
  else F
}
is.even(4)
# cat() : 벡터 합치기 출력. 
is.even <- function(x) {
  if(x %% 2 == 0) {
    cat(x, "is an even number!")
  }
  else {
    cat(x, "is an odd number!")
  }
}
is.even(4)
is.even(7)
is.even(3.5) # 정수가 아닌경우
# 정수와 실수를 구분하는 is.even(), 다중선택구조 
is.even <- function(x) {
  if (x %% 1 == 0 & x > 0) {
    if (x %% 2 == 0) {
      cat(x, "is an even number!")
    }
    else {
      cat(x, "is an odd number!")
    }
  }
  else 
    return(NA)
}
is.even(1.4)
is.even(-2) 
is.even(4)
# 반복문 
# for 문 : for (value in that) { this } 
# that 객체는 객체의 집합(숫자 or 문자열 벡터) , value는 인수 
# 시행은 벡터의 길이만큼 , 하나씩 순서대로 
range <- 1:5
for (i in range) { 
  cat( "The No. is", i , "\n") # 줄바꿈
  }
for (i in runif(5)) { 
  cat( "The No. is", i , "\n") # 줄바꿈 없으면 다음문장 이어버림 
}
for (i in 7:1) { 
  cat( "The No. is", i , "\n") # 줄바꿈
}
# 예제 sum.num()
sum.num <- function(x) {
  result <- 0  # 초기값 
  for (i in x) {
    result <- result + i  # i 
  }
  return(result) # for 함수는 출력을 따로 저장하지 않음 
}
sum.num(1:10)
