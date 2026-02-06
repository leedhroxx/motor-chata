# 1. 👥팀 소개
🚗 **motor-chata**

팀을 소개하는 짤막한 말..


<table>
  <tr align="center">
    <td><img src="https://github.com/jjhhyy0926/motor-chata/blob/main/assets/minha.png?raw=true" width="120px"><br><b>김민하</b></td>
    <td><img src="https://github.com/jjhhyy0926/motor-chata/blob/main/assets/jaehyun.png?raw=true" width="120px"><br><b>배재현</b></td>
    <td><img src="https://github.com/jjhhyy0926/motor-chata/blob/main/assets/jihye.png?raw=true" width="120px"><br><b>윤지혜</b></td>
    <td><img src="https://github.com/jjhhyy0926/motor-chata/blob/main/assets/yhjeon.png?raw=true" width="120px"><br><b>전윤하</b></td>
    <td><img src="https://github.com/motor-chata/motor-chata/blob/main/assets/ekthf.png?raw=true" width="120px"><br><b>정다솔</b></td>
    <td><img src="https://github.com/motor-chata/motor-chata/blob/main/assets/wlkstj.png?raw=true" width="120px"><br><b>홍진서</b></td>
  </tr>

  <tr align="center">
    <td>
        <b>- GitHub 총괄 관리
        <br>- ERD 작성
        <br>- Figma UI 디자인
        <br>- ERD 작성
        <br>- 로직 설계 </b></td>
    <td>
        <b>- 발표
        <br>- 대본 작성
        <br>- ERD 작성 </b></td>
    <td>   
        <b>- 노션 정리
        <br>- ERD 작성 보조
        <br>- 웹 크롤링
        <br>- 데이터 전처리
        <br>- DB적재 </b></td>
    <td>
        <b>- 일정 관리
        <br>- ERD 작성
        <br>- Streamlit 구현
        <br>- DB 스키마 모델링(코드 변환)</b></td>
    <td>   
        <b>- 회의록 보조
        <br>- ERD 작성
        <br>- DB 구축
        <br>- 웹 크롤링
        <br>- DB 적재</b></td>
    <td>   
        <b>- 회의록 작성
        <br>- ERD 작성
        <br>- PPT 작성
        <br>- 대본 작성</b></td>
  </tr></table>

---
# 2. 프로젝트 기간
2026-02-04 ~ 2026-02-06

---
# 3. 프로젝트 개요
## 프로젝트명
### 🚗mota-chata : ㄹㅇㄹ
## 프로젝트 소개
중고차 거래 비중이 높은 차량을 중심으로 공식 리콜 데이터를 기반한 결함 내용과 시정 방법을 한눈에 제공해 소비자의 구매·조치 판단을 돕는 것이 목적입니다.
## 기대효과
- **리콜 정보 접근성 향상**
<br>- 분산된 리콜 데이터를 한 화면에서 제공함으로써, 차량 결함 정보 탐색에 필요한 시간과 비용을 크게 줄일 수 있다.
- **안전 위험 사전 예방 효과**
<br>차량별 반복되는 결함 패턴과 위험 요소를 명확히 확인할 수 있어, 운행 중 발생할 수 있는 안전사고 가능성을 줄이는 데 기여한다.
- **차량 유지관리 수준 향상**
<br>시정 방법 및 문의처 정보를 제공하여 운전자가 필요한 점검이나 조치를 즉시 확인하고 대응할 수 있도록 지원한다.
- **제조사·모델 간 품질 비교 용이**
<br>브랜드별·차종별 리콜 패턴을 비교해 차량 품질 수준을 직관적으로 확인할 수 있어, 장기적 차량 선택 기준 수립에 도움을 준다.
- **사용자 경험 개선(UX 향상)**
<br>검색·필터·요약지표(KPI) 등 직관적인 UI를 통해 리콜 정보 활용성을 높이며, 이용자가 결함 정보를 쉽게 이해할 수 있도록 한다.
- **정책 및 제조사 개선 인사이트 제공**
<br>축적된 리콜 데이터를 분석하면 특정 제조사나 모델의 반복 결함을 파악할 수 있어, 제도 개선이나 서비스 품질 향상을 위한 자료로 활용될 수 있다.
## 대상 사용자
중고차 구매자와 차량 보유 운전자가 리콜 이력과 시정 방법을 쉽게 확인하고,
초보 운전자 및 자동차 정보 콘텐츠 제작자까지 활용할 수 있는 서비스입니다.

---
# 4. 프로젝트 설계
## 프로젝트 구조
## ERD
<tr align="center">
    <td><img src="https://github.com/motor-chata/motor-chata/blob/main/assets/erd.png?raw=true"width="600px"><br></td>
</tr>

## Table Specification
<tr align="center">
    <td><img src="https://github.com/motor-chata/motor-chata/blob/main/assets/erd.png?raw=true"width="600px"><br></td>
</tr>

---
# 5. 트러블 슈팅
### DB URL 연결 불가 이슈
#### Problem
- 본인 PC에서만 MySQL 서버 접속 시 Connection timed out 지속 발생.
- Ping/Telnet 테스트 결과, 팀원들 IP는 모두 차단되고 8.8.8.8만 연결됨 → 아웃바운드 통신 문제로 판단.
#### Attempts
- 권한 확인, 계정 변경, 네트워크 변경, 방화벽 설정, MySQL 설정 수정 모두 시도했으나 해결되지 않음.
#### Conclusion
- 원인은 DB가 아니라 로컬 PC(OS/네트워크 스택)의 IP 차단 문제로 결론.
- 프로젝트 종료 후 OS 재설치로 해결 예정.

### 외부 사이트 요청 실패 문제
#### Problem
- Selenium 크롤링 중 특정 페이지에서 반복적으로 `UnexpectedAlertPresentException` 발생.
- 사이트에서 “잘못된 접근입니다” 알림창을 띄우며 자동화 요청으로 판단해 차단됨.
#### Cause
- `execute_script()` 반복 호출로 비정상 패턴 탐지됨.
- 페이지 이동 속도가 지나치게 빨라 봇으로 인식됨.
- 동일한 페이징 구조(1→2→3→...)가 지속적으로 요청되어 rate-limit 발동.
#### Solution
- 요청 간 딜레이를 `time.sleep(0.2)` → `time.sleep(1)` 로 증가.
- 일정 시간(5~10분) 대기 후 재접속하여 차단 해제.

### Streamlit 텍스트 렌더링 오류
#### Problem
- DB에서 조회한 `결함내용` 컬럼이 Streamlit 화면에서 일부 문장이 취소선( ~ ) 처리로 출력됨.
- 원본 데이터에는 문제가 없지만, UI에서 Markdown으로 해석되면서 가독성 저하 발생.
#### Cause
- `st.write()` / `st.markdown()` 은 기본적으로 Markdown 문법을 해석함.
- `결함내용` 텍스트에 포함된 `~` 문자가 Markdown의 취소선 문법으로 인식되어 의도치 않은 렌더링 발생.
#### Solution
```
result_text = row["결함내용"]
st.text(result_text
```

### Streamlit 차트 출력 오류
#### Problem
- DB에서 조회한 `결함내용` 컬럼이 Streamlit 화면에서 **취소선(~)** 으로 잘못 표시됨.
- 원본 데이터는 정상이나, UI 렌더링 과정에서 의미가 왜곡되는 문제 발생.
#### Cause
- `st.write()` / `st.markdown()` 은 기본적으로 **Markdown을 자동 파싱**함.
- `결함내용`에 포함된 `~` 문자가 Markdown의 **취소선 문법**으로 인식되어 스타일이 적용됨.
#### Solution
- Markdown 해석을 차단하는 출력 함수로 변경.
- `st.text()` 사용하여 특수문자를 그대로 출력되도록 처리.
```
result_text = row["결함내용"]
st.text(result_text)
```

### ERD 관계 설정 충돌 문제
#### Problem
- 테이블 관계 연결 시 FK가 의도치 않게 PK로 포함되는 문제가 발생.
- 모든 관계가 실선(식별 관계)으로 연결되며, 자식 테이블이 부모 테이블의 키에 종속됨.
#### Cause
- 카디널리티(1:N)만 고려하고 관계 유형 설정을 하지 않음.
- 기본 설정이 식별 관계(Identifying) 로 적용되어 FK가 PK에 포함되는 구조로 생성됨.
- 식별 / 비식별 관계 구분 없이 연결한 것이 원인.
#### Solution
- 관계 생성 시 실선(식별)이 아닌 점선(비식별 관계, Non-Identifying) 로 지정.
- FK가 PK에 포함되지 않도록 옵션을 설정해 자식 테이블의 독립성 유지.
- 필요 FK만 별도 컬럼으로 생성하여 관계를 명확히 분리.

---
# 6. 기술 스택

### 🛠 Development Environment
- PyCharm
- GitHub

### 📡 Data Collection
- Requests
- Selenium
- BeautifulSoup4
- JSON Parsing

### 🔧 Data Processing / Preprocessing
- Pandas

### 🗄 Database
- MySQL
- ERDCloud (ERD 설계)
- CSV Import

### 🌐 Web Application
- Streamlit

### 🎨 UI / Documentation
- Figma
- Notion


---
# 7. 데이터 출처
- 자동차리콜센터 (국토교통부 · 한국교통안전공단 제공)
- https://www.car.go.kr/ri/main.do
본 프로젝트의 리콜 정보, 결함 내용, 시정 방법 데이터는 자동차리콜센터의 공개 데이터를 기반으로 크롤링하여 수집했습니다.

---
# 한줄 회고
**윤지혜 |** 전처리와 적재를 직접 해보며, 올바른 테이블 설계가 데이터 품질과 개발 효율성을 결정한다는 사실을 크게 체감했다.