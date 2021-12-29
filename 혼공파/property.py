class Rect:
    def __init__(self,width,height):
        self.__width = width
        self.__height = height

    @property    
    def width(self):
        return self.__width    
    @width.setter
    def width(self,width):
        if width <= 0 :
            raise Exception("너비는 음수가 나올수 없습니다.")
        self.__width = width    

    def get_height(self):
        return self.__height    
    def set_height(self,height):
        if height <= 0 :
            raise Exception("넓이는 음수가 나올수 없습니다.")
        self.__height= height  
    def get_area(self):
        return self.__width * self.__height

rect = Rect(10,10) 
print("원래 직사각형 넓이 : ", rect.get_area()) 
#rect.set_width(rect.get_width() +10)  
rect.width += 10 #프로퍼티 썼을때 width 조정
print("변경된 직사각형 넓이 : ",rect.get_area()) 