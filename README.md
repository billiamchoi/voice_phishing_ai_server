# voice_phishing_ai_server
ai 기반 보이스피싱 검출 앱을 위한 api 서버

-----
Environments
------------

| MySQL | Python | pip |
|-------|--------|------|
| 8.0.3 | 3.10.5 | 22.2 |
<!---
---
#### Flask 기반 작성

- email을 ID로 활용
- password는 JWT로 암호화 처리 한 로그인 system 구축
--->
----
## Installation

- 아래 모든 `코드`는 시작하기 전에 필요합니다.

### Clone

- `https://github.com/billiamchoi/voice_phishing_ai_server.git`에서 gitclone을  받습니다.

### Setup
- .env_example 파일을 .env파일로 "save as"하시고, MySQL의 개인정보를 저장합니다(USER, PASSWORD, DB).
- DB이름은 PC에서 "voice_phishing_ai_server" 로 만들어 주세요.

### Setting VirtualEnv 
#### Windows기준
- git bash: `git pull` 실행, git repository와 본인의 local 폴더를 동기화 해줍니다.
- cmd: `python -m venv <가상 환경을 설치할 폴더 경로>` 실행, 
  'venv'라는 폴더가 생성되면 성공입니다.
- cmd: <가상 환경이 설치된 폴더>\venv\Scripts에서 `activate.bat`을 입력, 가상 환경을 실행합니다.
  cmd에서 `(venv)`를 통해 가상 환경이 활성화 된것을 확인합니다.
  <참고> Windows에는 Linux/Mac기준의 `source ./venv/bin/activate`라는 명령어가 없는 것 같습니다.
- cmd: requirements.txt가 저장되어있는 폴더로 이동, `pip install -r requirements.txt`실행, 가상 환경의 정보를 일치시킵니다.
