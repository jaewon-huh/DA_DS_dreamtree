#Flask Django : 파이썬으로 웹 개발 , 웹개발 프레임 워크 
from flask import Flask
app = Flask(__name__) # app(변수) = 객체 

@app.route("/") #데코레이터 
def hello():
    return "<h1>안녕하세요ㅋ</h1>"

"""
＄ $env:FLASK_APP="moduleflask"  #변수 설정 
＄ flask run                     #flask 명령
"""
