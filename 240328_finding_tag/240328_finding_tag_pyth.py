with open('240328_finding_tag/test.html','r',encoding='utf-8') as f :
    html = f.read()

from bs4 import BeautifulSoup

soup = BeautifulSoup(html,'lxml')

#1. 태그 이름으로 찾는 거 
print(soup.title)
print(soup.title.text)