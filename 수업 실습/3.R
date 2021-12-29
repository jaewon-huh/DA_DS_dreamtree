#여러가지 데이터 유형

#행렬 : 행과 열로 2차원, 모든 데이터 값 동일 유형 , 열 우선 순서 저장 
# matrix(데이터 값 , 행의 수 , 열의 수 ) : 행렬 생성함수 
matrix(1:6, 3, 2) #3행 2열 
matrix(1:6, nrow = 3, ncol = 2)
matrix(1:6, nrow = 3, ncol = 2, byrow = T) #행 우선 순서 

 # 행렬크기보다 데이터 벡터 길이가 짧을때
matrix(1, nrow = 2, ncol = 3) 
matrix(1:2, nrow = 2, ncol = 3)
matrix(1:3, nrow = 2, ncol = 3)

# 행렬 중 1 생략
matrix(1:6, nrow = 3)
matrix(1:6, ncol = 3)

# 행렬의 행과 열 개수 확인 
x <- matrix(1:6, ncol = 3)
x
nrow(x)
ncol(x)
dim(x) # 행과 열 동시에 (행,열)

# 상관분석 함수 col() 사용
data("iris")
iris_cor <- cor(iris[,1:4]) # iris의 1:4 열 상관분석
iris_cor
class(iris_cor)
iris_cor[1:2, 1:2] #1,2열 1,2행행

# 벡터의 결합을 통한 행렬 생성
# cbind() : 열로 결합 (좌우)
cbind(1:3, 4:6)
cbind(1:2, 1:5)
# rbind() : 행로 결합 (상하) 
rbind(1:3, 4:6) 
# 재활용 규칙 : 객체의 길이 != , 길이 긴 객체에 맞춰
rbind(1:2, 1:3)
rbind(1:2, 1:5)

# 행렬 이름지정 
x <- matrix(1:6, nrow =2)
x
rownames(x) <- c("First", "Sencond")
colnames(x) <- c("A", "B", "C")
x
rownames(x) 
colnames(x)

#데이터 프레임 : 2차원 행렬 , 각 백터 객체 (열)의 유형 다를 수 o
# df <- data.frame(var1,var2, 열...) , var은 동일한 길이의 백터 객체
student <- c("A", "B", "C" , "D", "E", "F", "G")
student <- LETTERS[1:7] # letters는 알파벳 소문자 
student 

midterm <- c(30, 26, 24, 24, 20, 30, 22)
final <- c(36, 13, 32, 22, 19, 35, 30)

# 만약 data.frame(길이 8 4 2) 면 재사용 법칙으로 데이터 프레밍 생성
df1 <- data.frame(student, midterm, final)
df1
df2 <- data.frame(name = student, test1 = midterm , test2 = final)
df2

df1[1:3,]
df2[1:3,]

# 리스트 : 서로 다른 길이의 벡터 객체, list() 함수
list(c(15, 16, 17), "A nice number", T)
# 리스트를 데이터 프레임에 넣기 
data.frame(c(15, 16, 17), "A nice number", T) 
#재활용 규칙 적용됨. 단, 백터의 길이가 배수의 관계여야 함 49로 ㄱ
data.frame(c(15, 16, 17), c("A", "B"), T) 

# 데이터 크기비교 (효율적 공간사용)
data1 <- list(c(15, 16, 17), "A nice number", T)
data2 <- data.frame(c(15, 16, 17), "A nice number", T) 
object.size(data1)
object.size(data2)

iris_df <- iris[,1:4]
iris_list <- as.list(iris[,1:4])

#list의 변수 이름 지정 
x <- list(a = 1:4, b = "string")
x
x$a #특정 열 호출 $

plot(iris_df)
plot(iris_list) # 리스트에서는 분석에러 
