#객체(object) = 속성 + 행위 
#학생리스트 선언
students = [
 {"name":"윤인성","korean":87,"math":89,"english":87,"science":98},
 {"name":"연하진","korean":87,"math":89,"english":87,"science":98},
 {"name":"구지연","korean":87,"math":89,"english":87,"science":98},
 {"name":"김호창","korean":87,"math":89,"english":87,"science":98},
 {"name":"윤아린","korean":87,"math":89,"english":87,"science":98},
 {"name":"노구맨","korean":87,"math":89,"english":87,"science":98}
]
#학생을 한명씩 반복
print("이름","총점","평균",sep="\t") #sep="\t" :tab으로 나누기 
for student in students :
    #점수의 총합과 평균
    score_sum =student["korean"] + student["math"] +\
        student["english"]+student["science"]
    score_average = score_sum / 4
    #출력
    print(student["name"],score_sum,score_average, sep="\t")
print()

def 총점(student):
    return student["korean"] + student["math"] +\
        student["english"]+student["science"]
def 평균(student):
    return 총점(student) / 4
def 출력(student):
    print(student["name"],총점(student),평균(student), sep="\t")
    
print("이름","총점","평균",sep="\t") #sep="\t" :tab으로 나누기 
for student in students :
    출력(student)
print()   
