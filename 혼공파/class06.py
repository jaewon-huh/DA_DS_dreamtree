class Student:
    def __init__(self,이름,나이): 
        self.이름 = 이름     #속성 생성
        self.나이 = 나이  
    def __eq__(self,other):
        print("eq()함수")
        #return self,나이 == other.나이
    def __ne__(self, other):
        print("ne()함수")
    def __gt__(self, other):
        print("gt()함수")
    def __ge__(self, other):
        print("ge()함수")
    def __lt__(self, other):
        print("lt()함수")
    def __le__(self, other):
        print("le()함수")

student = Student("허재원",24) #생성자 호출 
student == student
student != student
student > student
student >= student
student < student
student <= student
