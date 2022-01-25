# 위젯 정렬
# GUI TK 버튼
from tkinter import *

root = Tk()

root.title("위젯 정렬")
root.geometry("300x100")

button1 = Button(root, text="혼공1")
button2 = Button(root, text="혼공2")
button3 = Button(root, text="혼공3")

button1.pack(side = LEFT, fill =X, padx= 10, pady =10 ) # 왼쪽부터 채워라 (RIGHT,TOP , BOTTOM)
button2.pack(side = LEFT, fill =X, padx= 10, pady =10)
button3.pack(side = LEFT, fill =X, padx= 10, pady =10)
# fill = padx = , pady =  : 여백
root.mainloop()