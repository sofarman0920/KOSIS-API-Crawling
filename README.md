KOSIS_API_CRAWLING.py 활용방법 (2024.10.30 기준)

1. KOSIS 공유서비스 홈페이지에 접속한다(https://kosis.kr/openapi/)

※처음 접속하는 경우 회원가입후 "활용신청" 메뉴를 통해 사용자 인증키를 발급받는다

2.개발 가이드 - 통계자료 메뉴에 들어가 "URL 생성" 버튼을 클릭한다

3. "통계표 선택" 부분에 원하는 통계표를 검색한다
※ 이름을 검색할떄 "통계표명"에 검색하는것을 추천한다

4. 원하는 통계표를 찾았다면 "선택" 버튼을 클릭한다

5. 아래에 URL생성 조건이 생성되는데 "분류/항목선택" 부분에 분류와 항목을 선택한다

6.출력형태를 JSON으로 설정하고 "조회기간 설정"에서 원하는 기간을 선정한다

7. "URL보기" 버튼을 클릭한다

8. 생성된 URL을 복사하고 KOSIS_API_CRAWLING.py 코드에 # KOSIS API URL 주석에 있는 url 함수에 적용한다

9.# CSV 파일로 저장 주석 부분에 원하는 파일경로를 설정한다

10.코드를 실행한다


※ 주의사항
KOSIS 공유서비스는 30분 마다 자동 로그아웃 되니 시간마다 로그인 확인 체크를 하는 것이 좋다
