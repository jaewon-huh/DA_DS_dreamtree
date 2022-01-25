# GUI TK 버튼
from tkinter import *
from tkinter import messagebox 

def clickButton() :
    messagebox.showinfo('버튼클릭', '버튼을 눌렀습니다..') # 메시지 박스 

root = Tk()

root.title("버튼")
root.geometry("300x100")

# 버튼 : Button(부모윈도, 옵션 (command = 지정한 작업 처리))
button1 = Button(root, text ="여기를 클릭", fg ='red', bg ='yellow',
            command= clickButton)

button1.pack(expand =1) # 버튼을 화면 중앙에 표시 

root.mainloop()