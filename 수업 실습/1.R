a <- 3
a
export <- c(110, 190, 94, 918, 818)
export
import <- c(186, 189, 192, 195, 88)
import
coporation <- export + import 
coporation

data1 <- c(10, 8, 7, 11, 15)
length(data1)

#seq()
2:9
5:-1
0.5:5
-1.5:4
seq(from = 1, to = 10) # 1~10
seq(from = 1, to = 10, by = 2) # 1 ~ 10, 2간격 
seq(from = 10, to = -2, by = -2)
seq(1, 10, 3) # 1 ~ 10, 3간격
seq(10, 0, -2)
help("seq")

#rep()
rep(1:4, 3) # 1,2,3,4 x 3 
rep(1:4, c(1,2,3,4)) 
rep(1:4, c(each = 3))

#indexing []
export
export[3]
export[c(2,4)] # 2nd & 4th
export[c(2:4)] # 2 ~ 4
export[-2] # 2nd except
export[-c(1,3,5)] # 1,3,5 except
export[-c(2:4)]

x <- c(10,21,30,41)
x[c(F, T, F, T)]
x[c(FALSE)] # = x[c(FAlSE,FAlSE,FAlSE,FAlSE)]
# x[c(조건문 if 홀수면)]

#데이터 수정
export
export[3] <- 101 # 새로 정의하면됨
export
import
import[c(1,4)] <- c(170,205)
import

#데이터 입력
c <- 'hello'
d <- c(TRUE, FALSE, TRUE, FALSE)
num <- c(1, 2, 3, 4, 5)
num
class(num) # class = numeric
num[4] <- 'four' # 하나의 객체(변수)에 서로 다른 값
num
class(num) # class가 character로 

#NA 결측값
y <- c(10,20,30,40)
y[2] <- NA 
y
class(y)

help("ggplot2")

getwd()
