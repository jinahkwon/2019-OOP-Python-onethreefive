# 2019-2 객체지향 프로그래밍 프로젝트 - **{팀명_일삼오}**
구성원: 3-1 임자하 | 3-3 권진아 | 3-5 송희진

## 1. 주제
과제 알리미

## 2. 동기
수많은 과제의 마감일을 확인하고 이를 다이어리에 옮기는 것은 정말 귀찮은 일이다. 또한 다양한 게시판을 하나씩 확인하다 보면 빠뜨리는 것이 생길 수 있다. 따라서 이것과 관련해 도움을 주기 위해 앞으로 남은 과제를 알려주는 프로그램을 만들게 되었다. 

## 3. 프로그램 사용 대상
세종과학예술영재학교 재학생 중 달빛학사를 통해 제출하는 과제의 마감일을 알고싶은 학생

## 4. 목적
과제 제출일을 D-day 순으로 알려준다. 

## 5. 주요기능
달빛학사에 접속하지 않아도 과제 제출일에 대한 정보를 받을 수 있다. 

## 6. 프로젝트 핵심
1) 네트워크에 연결되어 있는 상태에서 실행하여야 원하는 정보를 얻을 수 있다. 
2) 프로그램을 실행시킨 시간을 기준으로 앞으로 사용자가 제출해야하는 모든 과제의 마감일과 과제 게시글 제목을 D-day 순으로 출력해준다.
3) 출력되는 과제들은 기타 게시판에 있는 과목들에 한정한다. 

## 7. 구현에 필요한 라이브러리나 기술
라이브러리: time, requests, bs4, urllib2

## 8. **분업 계획**
프로그램이 달빛학사에 스스로 접속할 수 있도록 한다. 

권진아 - 기타 게시판의 과제명, 제출 기한, 제출 주소 추출 및 프로그햄 시각화
송희진 - 제출 기한, D-day 계산 함수 구현 및 프로그램 시각화
임자하 - 함수 통합, 총괄 및 프로그램 시각화

## 9. 기타
기타게시판 이외에도 다른 게시판도 적용될 수 있도록 한다.

## 10. 실행 방법
최종 파일 : 20191127_제출코드.py
자신의 달빛 학사 아이디와 비밀번호를 코드 내 LOGIN INFO에 입력한 뒤 프로그램을 실행시킨다.

## 11. 참고 문헌
https://github.com/kadragon/oop_python_ex/blob/master/project_ex/12_parser.py
https://github.com/kadragon/oop_python_ex/blob/master/project_ex/11_parser.py

<hr>

#### readme 작성관련 참고하기 [바로가기](https://heropy.blog/2017/09/30/markdown/)

#### 예시 계획서 [[예시 1]](https://docs.google.com/document/d/1hcuGhTtmiTUxuBtr3O6ffrSMahKNhEj33woE02V-84U/edit?usp=sharing) | [[예시 2]](https://docs.google.com/document/d/1FmxTZvmrroOW4uZ34Xfyyk9ejrQNx6gtsB6k7zOvHYE/edit?usp=sharing) | [[예시 3]](https://github.com/goldmango328/2018-OOP-Python-Light) | [[예시4]](https://github.com/ssy05468/2018-OOP-Python-lightbulb) | [[모두보기]](https://github.com/kadragon/oop_project_ex/network/members)
