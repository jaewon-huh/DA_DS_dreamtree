#객체 생성, 인스턴스 이름 = 클래스이름()
#클래스 = 틀 , 학생은 이름이라는 속성을 갖고 있다.
#객체(실체화  된것) : 학생 이름은 '윤인성'이야  (인스턴스)

class Student:
    def __str__(self):
        return "{} 는 {}살".format(self.이름,self.나이) 

    def __init__(self,이름,나이): #생성자 선언
        print("객체가 생성되었습니다.")
        self.이름 = 이름     #속성 생성
        self.나이 = 나이  

    def __del__(self): #소멸자
        print("객체가 소멸되었습니다.")

    def 출력(self): #함수 선언(메서드)
        print(self.이름, self.나이) # 함수로 만들었기때문에 14줄과 =

student = Student("허재원",24) #생성자 호출 
print(student.이름,student.나이)
student.출력()  #함수 사용  
print(str(student)) #__str__ 함수를 호출해서 출력 
