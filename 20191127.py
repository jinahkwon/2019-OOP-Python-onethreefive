#제출란 찾기
import bs4
import requests

import datetime


class day_cal:
    def __init__(self):
        self.day = datetime.datetime.now()

    def calculator(self, end_day):
        dt_today = self.day
        dt_end = datetime.datetime(int(end_day.split('-')[0]), int(end_day.split('-')[1]),
                                       int(end_day.split('-')[2]))
        td = dt_end - dt_today
        print("D-{}".format(td.days))

#로그인 정보 입력/아이디/비밀번호
LOGIN_INFO = {
    'id' : '1770',
    'passwd' : 'j@h@7535'
}

#오늘 날짜 확인
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

    #사이드바에 있는 게시판 url 가져오기
    board_url = section_board_list_data.select('ul.treeview-menu li a')

    board_url_list = []
    lets_print_chart = []

    #기타 게시판 url가져오기
    for i in board_url:
        if 'board' == i.get('href').split('/')[1]:
            if int(i.get('href').split('/')[3]) > 100 :
                board_url_list.append(i.get('href').split('/')[3])

    assign_board_list = []
    board_topic_list = [] # 각각의 게시글이 List 형태로 보관되어있는 list.

    #제출가능 게시판 찾기
    print('=' * 70)
    for assign in board_url_list:
        etc_board_data = bs4.BeautifulSoup(s.get('https://go.sasa.hs.kr/board/lists/' + assign + '/page/1').text, 'html.parser')
        assign_board_url = etc_board_data.select('tr.info td a')
        for i in assign_board_url:
            if 'board' == i.get('href').split('/')[1]:
                assign_board_list=(i.get('href'))
                each_board_data = bs4.BeautifulSoup(s.get('https://go.sasa.hs.kr' + assign_board_list).text, 'html.parser') #과제가 있는 게시글의 각각의 URL을 임시로 저장
                each_board_topic = each_board_data.select('div.user-block span')[0].getText().strip()  # 게시글의 URL로 들어가서 제목 부분을 가져와 저장
                board_topic_list.append(each_board_topic) # each_board_topic 변수에 저장된 게시글의 제목을 list에 추가
                each_dday = each_board_data.select('small.text-info')
                print(each_board_topic)  # 현재 제출이 가능한 게시글 링크를 출력
                cal1 = day_cal()
                cal1.calculator(each_dday[0].text.split('~')[1].strip().split(' ')[0])
                print('=' * 70)

