#제출란 찾기
import bs4
import requests
import datetime

LOGIN_INFO = {
    'id' : '1707',
    'passwd' : 'wlsdk@8482'
}

to_date = datetime.date.today()

with requests.Session() as s:
    # 로그인 페이지를 가져와서 html 로 만들어 파싱을 시도한다.
    first_page = s.get('https://go.sasa.hs.kr')
    html = first_page.text
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # cross-site request forgery 방지용 input value 를 가져온다.
    # https://ko.wikipedia.org/wiki/사이트_간_요청_위조
    csrf = soup.find('input', {'name': 'csrf_test_name'})

    # 두개의 dictionary 를 합친다.
    LOGIN_INFO.update({'csrf_test_name': csrf['value']})

    # 만들어진 로그인 데이터를 이용해서, 로그인을 시도한다.
    login_req = s.post('https://go.sasa.hs.kr/auth/login/', data=LOGIN_INFO)

    # 로그인이 성공적으로 이루어졌는지 확인한다.
    if login_req.status_code != 200:
        raise Exception('로그인 되지 않았습니다!')

    # 접근 할 수 있는 모든 게시판을 검색 하기 위해서, 메인페이지에 접속한다.
    section_board_list_data = bs4.BeautifulSoup(s.get('https://go.sasa.hs.kr/main').text, 'html.parser')

    board_url = section_board_list_data.select('ul.treeview-menu li a')

    board_url_list = []

    for i in board_url:
        if 'board' == i.get('href').split('/')[1]:
            if int(i.get('href').split('/')[3]) > 100 :
                board_url_list.append(i.get('href').split('/')[3])

    #제출가능 게시판 찾기
    for assign in board_url_list:
        etc_board_data = bs4.BeautifulSoup(s.get('https://go.sasa.hs.kr/board/lists/' + assign + '/page/1').text, 'html.parser')
        assign_board_url = etc_board_data.select('tr.info td a')
        assign_board_list = []
        for i in assign_board_url:
            if 'board' == i.get('href').split('/')[1]:
                assign_board_list.append(i.get('href'))

