# 지니뮤직의 1~50위 곡을 스크래핑 해보세요.[https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1](https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1)
# 순위/ 곡제목/ 가수

import requests
from bs4 import BeautifulSoup
# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')


# musics (tr들) 의 반복문을 돌리기
rank =0
for music in musics:
    rank_tag = music.select_one('td.number')
    title_tag = music.select_one('td.info > a.title.ellipsis') #td.title -> class가 title인 td를 가져온다 
    singer_tag = music.select_one('td.info > a.artist.ellipsis')
    # a가 None 인 경우가 았어서, 그거 제외하고 
    if rank_tag is not None: 
        # a의 text를 찍어본다.
        rank = rank_tag.text #문자로 가져옴
        list= rank.split()
        print(list[0]+'. '+ title_tag.text.strip() +' : '+ singer_tag.text.strip())
