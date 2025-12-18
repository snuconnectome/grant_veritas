# GitHub Pages 홈페이지 설정 가이드

베리타스 강좌 2 프로젝트를 위한 GitHub Pages 홈페이지를 설정하는 방법입니다.

## 📋 준비 사항

1. GitHub 계정
2. Git 설치
3. (선택) Ruby 및 Jekyll (로컬 테스트용)

## 🚀 빠른 시작

### 1단계: GitHub 레포지토리 생성

1. GitHub에서 새 레포지토리 생성
   - 레포지토리 이름: `veritas-lecture-2` (또는 원하는 이름)
   - Public 또는 Private 선택
   - README는 나중에 추가할 수 있으므로 선택 안 해도 됨

### 2단계: 로컬에 파일 복사

```bash
# 레포지토리 클론 (GitHub에서 생성한 레포지토리 URL 사용)
git clone https://github.com/yourusername/veritas-lecture-2.git
cd veritas-lecture-2

# docs 폴더의 모든 파일을 레포지토리 루트로 복사
# 또는 docs 폴더를 그대로 사용
```

### 3단계: GitHub Pages 설정

#### 방법 A: `/docs` 폴더 사용 (권장)

1. GitHub 레포지토리에서 **Settings** → **Pages** 이동
2. **Source**를 "Deploy from a branch"로 선택
3. **Branch**: `main` (또는 `master`)
4. **Folder**: `/docs` 선택
5. **Save** 클릭

#### 방법 B: 루트 폴더 사용

만약 `docs` 폴더의 내용을 루트로 옮겼다면:
1. **Branch**: `main`
2. **Folder**: `/ (root)` 선택

### 4단계: _config.yml 수정

`docs/_config.yml` 파일을 열어서 다음을 수정:

```yaml
url: "https://yourusername.github.io"  # GitHub 사용자명으로 변경
baseurl: "/veritas-lecture-2"  # 레포지토리 이름으로 변경 (또는 ""로 비워두기)
```

### 5단계: 파일 푸시

```bash
git add .
git commit -m "Initial commit: Add Jekyll site"
git push origin main
```

### 6단계: 배포 확인

몇 분 후 다음 URL에서 확인:
- `https://yourusername.github.io/veritas-lecture-2` (baseurl이 있는 경우)
- `https://yourusername.github.io` (baseurl이 없는 경우)

## 🎨 커스터마이징

### 색상 변경

`docs/assets/css/main.css` 파일에서 CSS 변수 수정:

```css
:root {
  --primary-color: #2c3e50;    /* 메인 색상 */
  --secondary-color: #3498db;  /* 보조 색상 */
  --accent-color: #e74c3c;     /* 강조 색상 */
}
```

### 콘텐츠 수정

- `docs/index.html`: 메인 페이지 콘텐츠
- 교수진 정보, 커리큘럼 등 모든 내용 수정 가능

### 연락처 정보

`docs/index.html`의 contact-section에서 이메일 주소 수정:

```html
<p><strong>이메일:</strong> 실제이메일@example.com</p>
```

## 🔧 로컬에서 테스트하기

### Ruby 설치 (macOS)

```bash
# Homebrew로 설치
brew install ruby

# 또는 rbenv 사용
brew install rbenv
rbenv install 3.2.0
rbenv global 3.2.0
```

### Jekyll 설치 및 실행

```bash
cd docs
bundle install
bundle exec jekyll serve
```

브라우저에서 `http://localhost:4000` 접속

## 📝 추가 기능

### 커스텀 도메인 사용

1. `docs/CNAME` 파일 생성
2. 도메인 이름 입력 (예: `veritas.snu.ac.kr`)
3. DNS 설정에서 CNAME 레코드 추가

### Google Analytics 추가

`_config.yml`에 추가:

```yaml
google_analytics: UA-XXXXXXXXX-X
```

### 댓글 시스템 추가

Disqus 또는 Utterances 추가 가능

## 🐛 문제 해결

### 페이지가 표시되지 않음

1. GitHub Actions 탭에서 빌드 오류 확인
2. `_config.yml`의 URL 설정 확인
3. 몇 분 더 기다리기 (배포에 시간이 걸릴 수 있음)

### 스타일이 적용되지 않음

1. CSS 파일 경로 확인 (`/assets/css/main.css`)
2. 브라우저 캐시 삭제
3. `_config.yml`의 baseurl 설정 확인

### Jekyll 로컬 빌드 오류

```bash
# 의존성 재설치
bundle update
bundle install
```

## 📚 참고 자료

- [GitHub Pages 공식 문서](https://docs.github.com/en/pages)
- [Jekyll 공식 문서](https://jekyllrb.com/)
- [Jekyll 테마 갤러리](https://jekyllthemes.io/)

## ✅ 체크리스트

- [ ] GitHub 레포지토리 생성
- [ ] 파일 업로드
- [ ] `_config.yml` URL 수정
- [ ] GitHub Pages 설정 완료
- [ ] 홈페이지 접속 확인
- [ ] 연락처 정보 업데이트
- [ ] (선택) 커스텀 도메인 설정

---

**질문이나 문제가 있으면 이슈를 생성해주세요!**

