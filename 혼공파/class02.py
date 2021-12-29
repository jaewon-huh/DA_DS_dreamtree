#여러가지 속성을 가질수 있는 대상 : 객체 (student,students)
#객체를 만드는 함수 
def 학생_생성(name,korean,math,english,science):
    return {
        "name":name,
        "korean" : korean,
        "math": math,
        "english" : english,
        "science" : science
    }

    
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
    score_sum =student["korean"] + student["math"] +\
        student["english"]+student["science"]
    score_average = score_sum / 4
    print(student["name"],score_sum,score_average, sep="\t")