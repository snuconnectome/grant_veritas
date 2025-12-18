# GitHub 푸시 가이드

OneDrive 동기화 폴더에서 Git 작업이 타임아웃될 수 있습니다. 다음 방법 중 하나를 사용하세요.

## 방법 1: 터미널에서 직접 실행 (권장)

```bash
cd "/Users/jiookcha/Library/CloudStorage/OneDrive-Personal/_Documents/_그랜트/00베리타스"

# 파일 추가
git add docs/ GITHUB_PAGES_SETUP.md CODEBASE_ONBOARDING.md

# 커밋
git commit -m "Add GitHub Pages website structure for Veritas Lecture 2"

# 푸시
git push origin main
```

## 방법 2: GitHub Desktop 사용

1. GitHub Desktop 앱 열기
2. File → Add Local Repository
3. `/Users/jiookcha/Library/CloudStorage/OneDrive-Personal/_Documents/_그랜트/00베리타스` 선택
4. 변경사항 확인 후 "Commit to main" 클릭
5. "Push origin" 클릭

## 방법 3: OneDrive 밖으로 복사 후 작업

OneDrive 동기화가 Git 작업을 방해하는 경우:

```bash
# 임시 폴더에 복사
cp -r "/Users/jiookcha/Library/CloudStorage/OneDrive-Personal/_Documents/_그랜트/00베리타스" ~/temp_veritas

cd ~/temp_veritas

# Git 작업 수행
git add docs/ GITHUB_PAGES_SETUP.md CODEBASE_ONBOARDING.md
git commit -m "Add GitHub Pages website structure for Veritas Lecture 2"
git push origin main

# 작업 완료 후 원본 폴더로 다시 복사 (선택사항)
```

## 현재 원격 레포지토리

```
origin: https://github.com/jcha9928/grant_veritas.git
```

## 추가된 파일들

- `docs/` - GitHub Pages 홈페이지 전체 구조
- `GITHUB_PAGES_SETUP.md` - 배포 가이드
- `CODEBASE_ONBOARDING.md` - 코드베이스 온보딩 문서

## GitHub Pages 활성화

푸시 후:
1. GitHub 레포지토리 페이지로 이동
2. Settings → Pages
3. Source: "Deploy from a branch"
4. Branch: `main`, Folder: `/docs`
5. Save

몇 분 후 `https://jcha9928.github.io/grant_veritas` 에서 확인 가능합니다.

