# 슬롯머신 만들기
# 세가지의 심벌 , 심벌에 따른 점수 계산 
get_symbols <- function(){
  wheel <- c("DD", "7", "BBB", "BB", "B", "C", "0")
  sample(wheel, size = 3, replace = T,
         prob = c(0.03, 0.03, 0.06, 0.1, 0.25, 0.01, 0.52))
}
# DD : 다이아 , C : 체리 
get_symbols()
# 1.전략 
# 복잡한 작업을 서브태스크들로 나눔 / 구체적 예제 / 자연어로 정리 후 R로 변환 
# 순차 / 병렬 (그룹화)
# 2. if문 : if(this){ that }
num <- -2
if(num < 0){
  num <- num * -1
}
num
# 3. else 문 : if(this){A} else{B}
a <- 3.12
dec <- a - trunc(a) # trunc() : 정수 값 
dec
# 반올림
if(dec >= 0.5) {
  a <- trunc(a) + 1
} else {
  a <- trunc(a)
}
a
a <- 1
b <- 1
# 배타적 A도 아니고 B 도 아님 
if (a>b){
  print("A wins")
} else if (a < b){
  print("B wins")
} else{
  print("A=B")
}

if (# 경우 1 : 모두 같은 종류) {
  prize <- # 해당 상금을 찾는다
} else if (# 경우 2 : 모두 바) {
  prize <- # 5불의 상금
} else {
  # 체리의 개수를 센다 
  prize <- # 상금을 계산한다
}
# 다이아 몬드의 개수를 샌다 
# 다이아 개수만큼 상금을 두배로 한다 

# 경우 1 : 모두 같은 종류인가 ?
symbols <- c("7", "7", "7")
symbols[1] == symbols[2] & symbols[2] == symbols[3]
all(symbols == symbols[1])
length(unique(symbols)) == 1 # unique() : 벡터에 들어있는 모든 유일한 값 리턴
same <- symbols[1] == symbols[2] && symbols[2] == symbols[3] # 경우 1 <- same
# 경우 2 : 모두 바 ?
symbols <- c("B", "BB", "BBB")
all(symbols %in%  c("BBB", "BB", "B")) 
bars <- symbols %in% c("B", "BB", "BBB") # 경우 2 <- all(bars) : 한눈에 볼수 있음

# symbols 에 해당하는 상금 찾기 ( 경우 1에서 DD = 100$ , 7 = 80$ , BBB = 40$ ...) 
# 검색 테이블 서브세팅 기술(부분집합 추출)
payouts <- c("DD" = 100, "7" = 80, "BBB" = 40, "BB" = 25, "B" = 10, 
             "C" = 10, "0" = 0)
payouts
payouts["DD"]
unname(payouts["DD"])
symbols <- c("7","7","7")
symbols[1]
payouts[symbols[1]]
prize <- unname(payouts[symbols[1]])
# 경우 3 : 체리의 개수 
symbols <- c("C", "DD", "C")
symbols == "C" # 체리의 위치 
sum(symbols == "C") # 체리의 개수 
cherries <- sum(symbols == "C") # else 체리의 개수 
cherries # cherries 의 값은 0 1 2 (3 논외)
# C 0개 0$ , 1개 2 $ , 2개 5$
c(0,2,5)
prize <- c(0,2,5)[cherries + 1 ] # cherries = 2 , C 두개 면 5원 이어야 함 = 인덱스 3
prize

symbols <- get_symbols()
symbols
# 경우의 수 최종 
# 조건 확인
same <- symbols[1] == symbols[2] && symbols[2] == symbols[3]
bars <- symbols %in% c("B", "BB", "BBB")
# 상금 계산 
if (same) {
  payouts <- c("DD" = 100, "7" = 80, "BBB" = 40, "BB" = 25, "B" = 10, 
               "C" = 10, "0" = 0)
  prize <- unname(payouts[symbols[1]])
  } else if (all(bars)) {
    prize <- 5
    } else {
      cherries <- sum(symbols =="C")
      prize <- c(0,2,5)[cherries + 1]
    }
# 다이아 개수를 센다 
diamonds <- sum(symbols == "DD")
# 다이아 개수만큼 상금을 두배로 한다 
# prize <- c(prize, prize*2, prize*4)[diamonds +1]
prize * 2^diamonds

# 함수로 만들기 
score <- function(symbols) {
  # 조건 확인
  same <- symbols[1] == symbols[2] && symbols[2] == symbols[3]
  bars <- symbols %in% c("B", "BB", "BBB")
  # 상금 계산 
  if (same) {
    payouts <- c("DD" = 100, "7" = 80, "BBB" = 40, "BB" = 25, "B" = 10, 
                 "C" = 10, "0" = 0)
    prize <- unname(payouts[symbols[1]])
  } else if (all(bars)) {
    prize <- 5
  } else {
    cherries <- sum(symbols =="C")
    prize <- c(0,2,5)[cherries + 1]
  }
  # 다이아 개수를 센다 
  diamonds <- sum(symbols == "DD")
  # 다이아 개수만큼 상금을 두배로 한다 
  prize * 2^diamonds
}
play <- function(){
  symbols <- get_symbols()
  print(symbols)
  score(symbols)
}
play()

