class Rect:
    def __init__(self,width,height):
        self.__width = width
        self.__height = height
    #프라이빗 변수: 외부에서 접근 못하도록 __변수이름
    def get_width(self):
        return self.__width     #게터로 self.__width 리턴
    def set_width(self,width):
        if width <= 0 :
            raise Exception("너비는 음수가 나올수 없습니다.")
        self.__width = width    #세터로 self.__width 의 width 지정
    def get_height(self):
        return self.__height    
    def set_height(self,height):
        if heighth <= 0 :
            raise Exception("넓이는 음수가 나올수 없습니다.")
        self.__height= height  #세터로 self.__width 의 width 지정    
    def get_area(self):
        return self.__width * self.__height

rect = Rect(10,10) 
rect.width = -10 #외부에서 width(변수) 지정 → 오류 
rect.set_width(rect.get_width() +10)  # 너비 +10 조정
print(rect.get_area()) 
#print(rect.__width) 외부에서 접근불가하도록
#P - 외부에서 변경할수 없기 때문에, 높이,너비를 수정하고 싶어도 못함
# → 게터 &세터