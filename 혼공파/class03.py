#학생 객체와 관련된 부분 
#딕셔너리를 리턴하는 함수 선언
def 학생_생성(name,korean,math,english,science):
        return {
        "name":name,
        "korean" : korean,
        "math": math,
        "english" : english,  
        "science" : science
    }
#학생을 처리하는 함수 선언
def 총점(student):
    return student["korean"] + student["math"] +\
        student["english"]+student["science"]
def 평균(student):
    return 총점(student) / 4
def 출력(student):
    print(student["name"],총점(student),평균(student), sep="\t")


#객체를 활용하는 처리 
#학생 리스트 선언
students = [
    학생_생성("윤인성",84,98,78,98),
    학생_생성("연하진",93,95,74,92), 
    학생_생성("구지연",92,87,76,98), 
    학생_생성("김호창",88,95,78,84),
    학생_생성("윤아린",85,87,78,81), 
    학생_생성("노구맨",98,48,92,90),    
    ]
print("이름","총점","평균",sep="\t") 
for student in students :
    print(출력(student))