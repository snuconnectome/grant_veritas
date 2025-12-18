# 베리타스 강좌 2 홈페이지

GitHub Pages를 위한 Jekyll 기반 홈페이지입니다.

## 로컬에서 실행하기

1. Ruby와 Bundler 설치 (이미 설치되어 있다면 생략)

2. 의존성 설치:
```bash
bundle install
```

3. 로컬 서버 실행:
```bash
bundle exec jekyll serve
```

4. 브라우저에서 `http://localhost:4000` 접속

## GitHub Pages에 배포하기

1. 이 레포지토리를 GitHub에 푸시

2. GitHub 레포지토리 설정에서:
   - Settings → Pages
   - Source를 "Deploy from a branch"로 선택
   - Branch를 `main` (또는 `master`), 폴더를 `/docs`로 설정

3. 또는 GitHub Actions를 사용하려면 `.github/workflows/jekyll.yml` 파일을 생성

## 파일 구조

```
docs/
├── _config.yml          # Jekyll 설정
├── _layouts/
│   └── default.html     # 기본 레이아웃
├── index.html          # 메인 페이지
├── assets/
│   └── css/
│       └── main.css     # 스타일시트
├── Gemfile              # Ruby 의존성
└── README.md            # 본 파일
```

## 커스터마이징

- `_config.yml`: 사이트 설정, URL 등
- `index.html`: 메인 콘텐츠
- `assets/css/main.css`: 스타일 수정
- `_layouts/default.html`: 레이아웃 구조

## 참고

- [Jekyll 공식 문서](https://jekyllrb.com/)
- [GitHub Pages 가이드](https://docs.github.com/en/pages)

