# voice_phishing_ai_server
ai 기반 보이스피싱 검출 앱을 위한 api 서버

-----
Environments
------------

| MySQL | Python | pip |
|-------|--------|------|
| 8.0.3 | 3.10.5 | 22.2 |

---

#### Flask 기반 작성

- email을 ID로 활용
- password는 JWT로 암호화 처리 한 로그인 system 구축
----
## Installation
----
- 아래 모든 `코드`는 시작하기 전에 필요합니다.

### Clone

- `https://github.com/billiamchoi/voice_phishing_ai_server.git`에서 gitclone을  받습니다.

### Setup
- .env_example 파일을 .env파일로 "save as"하시고, MySQL의 개인정보를 저장합니다(USER, PASSWORD, DB).
- DB이름은 PC에서 "voice_phishing_ai_server" 로 만들어 주세요.
