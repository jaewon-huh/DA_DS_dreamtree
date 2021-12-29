


html_doc = """
<html>
 <head>
    <title> TEST PAGE</title>
 </head>
 <body>
  <h1>HELLO WORLD</h1>
 </body>
</html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.select('title'))
print(soup.select("h1")) #select 함수 : 태그선택 
print(soup.select("h1")[0].string)


from urllib import request
# urlopen()
target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")

# BSsoup 
soup = BeautifulSoup(target,'html.parser')
#
for data in soup.select("location") :
   print("도시:" ,data.select_one("city").string) 
   print("시간:" ,data.select_one("tmef").string)
   print("날씨:" ,data.select_one("wf").string)
   print("-" *20)