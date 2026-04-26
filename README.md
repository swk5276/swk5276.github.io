# 김성웅 이력서 사이트

배포 URL: https://swk5276.github.io/

## 구성

- `index.html` — 빌드된 이력서 (사진은 base64로 임베드됨, 단일 파일)
- `build_resume.py` — `index.html`을 생성하는 빌드 스크립트
- `김성웅.jpg` — 프로필 사진 원본

## 다른 컴퓨터에서 수정하기

```bash
# 1. 클론
git clone https://github.com/swk5276/swk5276.github.io.git
cd swk5276.github.io

# 2. (선택) 이 리포만 개인 이메일로 커밋되게 설정
git config user.name "Sungwoong Kim"
git config user.email "swk5276@gmail.com"

# 3. build_resume.py 안에서 HTML 템플릿(이력서 내용) 수정

# 4. 빌드 — index.html을 다시 생성
python build_resume.py

# 5. 변경사항 push (1~2분 후 사이트 반영)
git add -A
git commit -m "Update resume"
git push
```

## 요구사항

- Python 3.6+ (표준 라이브러리만 사용)
- Git
