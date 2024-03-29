with open('240328_finding_tag/test.html','r',encoding='utf-8') as f :
    html = f.read()

from bs4 import BeautifulSoup

soup = BeautifulSoup(html,'lxml')

#2. find 사용
print(soup.find('title'))

# class 이용
print(soup.find('span',attrs={'class':'blue_price'}).text)
