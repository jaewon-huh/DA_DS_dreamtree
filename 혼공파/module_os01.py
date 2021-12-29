# 모듈을 읽어 들입니다.
import os

# 현재 폴더의 파일/폴더를 출력합니다.
output = os.listdir()  #현재 폴더를 읽어들이는 코드 
print("os.listdir():", output)
print()

# 현재 폴더의 파일/폴더를 구분합니다.
print("# 폴더와 파일 구분하기")
for path in output:
    if os.path.isdir(path):  #os.path.isdir(path) 경로에 있는게 디렉터리(폴더)면 True 
        print("폴더:", path)
    else:
        print("파일:", path)
