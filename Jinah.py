#제출란 찾기
import bs4
import requests

def get_html(url):
    response = requests.get(url)
    response.raise_for_status()

    return response.txt

html = get_html("https://go.sasa.hs.kr/board/lists/190205/page/1")
soup = bs4.BeautifulSoup(html, 'html.parser')

search_name = soup.select()

for i in search_name:
