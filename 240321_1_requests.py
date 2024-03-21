import requests

#코드 가지고 올 주소
url = 'http://www.naver.com'

#소스코드 다운, get()은 서버에 요청 보내는 것
r = requests.get(url)