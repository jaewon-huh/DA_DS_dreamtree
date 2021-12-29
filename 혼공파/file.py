#텍스트 파일 쓰기 
file = open("test.txt","a") #"w" : 새로쓰기 
file.write("안녕하세요.")
file.close() 

#텍스트 파일 읽기
file = open("test.txt","r")
print(file.read())
file.close() 
#with 키워드 : 열고닫기 실수 방지 
with open("test.txt","a") as file : 
    file.write("안녕하세요.")