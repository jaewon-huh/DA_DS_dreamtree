# GUI 응용 프로그램
from tkinter import *

root = Tk()

root.title("혼공 GUI 연습")
root.geometry("300x100")

# Label : 문자를 표현하는 위젯 Label(부모윈도, 옵션)
lable1 = Label(root, text = '혼공 sql은')
lable2 = Label(root, text = '쉽다',
    font = ("궁서체",30), bg="blue", fg="red")

lable1.pack()       # pack() 라벨 화면에 표현
lable2.pack()


root.mainloop()     # 함수를 실행 