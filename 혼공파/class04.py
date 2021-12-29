#클래스 구문 : 객체를 좀더 효율적으로 생성하기 위해 !!(객체 생성!)
#class 클래스 이름 : 
#      클래스 내용
#class.03 과 같은 처리 
class 학생 :
    def __init__(self,name,korean,math,english,science): #클래스 내부함수 첫번째 매개변수로 반드시 self
        self.name = name        #함수 정의 끝내도 쉼표 붙이지 말것 (튜플 처리)
        self.korean =korean
        self.math =math
        self.english = english 
        self.science = science
    def 총점(self):
        return self.korean + self.math +\
            self.english + self.science
    def 평균(self):
        return self.총점() / 4 #함수 호출 :self.함수()
    def 출력(self):
        print(self.name,self.총점(),self.평균(),sep="\t")

students = [
    학생("윤인성", 84,98,78,98),
    학생("연하진", 93,95,74,92), 
    학생("구지연", 92,87,76,98), 
    학생("김호창", 88,95,78,84),
    학생("윤아린", 85,87,78,81),   
    ]
print("이름","총점","평균",sep="\t") 
for student in students :
    student.출력()