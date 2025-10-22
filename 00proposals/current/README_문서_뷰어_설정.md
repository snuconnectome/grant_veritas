# Cursor에서 문서 파일 열기 설정

## ✅ DOCX 파일 - 설정 완료!

### 설치된 확장 프로그램
- **vscode-office** (v3.5.4) - 설치 완료 ✅

### 사용 방법
1. Cursor에서 `.docx` 파일 클릭
2. 자동으로 Office Viewer로 열림
3. 읽기 전용 미리보기 제공

### 지원되는 파일 형식
- ✅ Microsoft Word (.docx, .doc)
- ✅ Microsoft Excel (.xlsx, .xls)
- ✅ Microsoft PowerPoint (.pptx, .ppt)
- ✅ PDF (.pdf)

### 테스트 파일
- `_연구개발계획서_v6_제출용최종본.docx` ← 이제 Cursor에서 열림!

---

## ❌ HWP 파일 - 제한 사항

### 문제점
- HWP는 한글과컴퓨터의 독점 포맷으로 Cursor/VS Code 확장 프로그램 없음
- 공식 뷰어가 필요함

### 해결 방법

#### 방법 1: 한글 프로그램 사용 (권장)
```bash
# macOS에서 한글 설치
# App Store 또는 한글과컴퓨터 웹사이트에서 다운로드
# 무료 뷰어: 한글 2022 뷰어
```

#### 방법 2: HWP → DOCX 변환 후 Cursor에서 보기
```bash
# 온라인 변환 서비스 사용
# 1. https://www.onlineconvert.com/
# 2. https://cloudconvert.com/hwp-to-docx
# 3. https://convertio.co/kr/hwp-docx/

# 또는 한글 프로그램에서:
# 파일 → 다른 이름으로 저장 → DOCX 형식 선택
```

#### 방법 3: CLI 도구 사용 (Linux/macOS)
```bash
# hwp5 Python 패키지 설치
pip install hwp5

# HWP → 텍스트 변환
hwp5txt 파일.hwp > 출력.txt

# HWP → HTML 변환
hwp5html 파일.hwp --output=출력.html
```

#### 방법 4: 구글 드라이브 뷰어
```bash
# 1. HWP 파일을 구글 드라이브에 업로드
# 2. 구글 드라이브에서 직접 미리보기 가능
# 3. 필요시 Google Docs로 변환
```

---

## 🔧 현재 프로젝트 파일 상황

### DOCX 파일 (Cursor에서 열기 가능 ✅)
```
00proposals/current/
└── _연구개발계획서_v6_제출용최종본.docx  ← Cursor에서 바로 열림!
```

### HWP 파일 (외부 프로그램 필요 ❌)
```
04application_guideline/
├── 붙임2. 「베리타스 강좌 2」 신규 교과목 연구개발계획서.hwp
├── 붙임3. 교과목 신설 신청서.hwp
└── butin2.hwp (백업)
```

---

## 💡 추천 워크플로우

### 문서 작성/편집
1. **작업용**: Markdown 파일로 작성 (Cursor 네이티브 지원)
2. **변환**: Pandoc으로 MD → DOCX 변환
3. **최종**: 필요시 DOCX → HWP 변환 (한글 프로그램)

### 문서 확인/리뷰
1. **DOCX**: Cursor에서 직접 열기 (vscode-office)
2. **HWP**: 한글 뷰어 또는 변환 후 확인
3. **PDF**: Cursor에서 직접 열기 (vscode-office)

---

## 🎯 HWP 제출용 파일 생성 방법

### 현재 상황
- ✅ Markdown 원본: `_연구개발계획서_v6_제출용최종본.md`
- ✅ DOCX 파일: `_연구개발계획서_v6_제출용최종본.docx`
- ❌ HWP 파일: 아직 생성 안 됨

### HWP 생성 단계
```bash
# 1단계: DOCX 파일 확인 (Cursor에서)
# → _연구개발계획서_v6_제출용최종본.docx 열기

# 2단계: 한글 프로그램에서 DOCX 열기
# → 파일 → 열기 → DOCX 선택

# 3단계: HWP로 저장
# → 파일 → 다른 이름으로 저장 → HWP 형식 선택
# → 파일명: _연구개발계획서_v6_제출용최종본.hwp

# 4단계: 붙임2 템플릿 적용 (필요시)
# → 붙임2 템플릿 열기
# → 내용 복사/붙여넣기
# → 서식 조정
```

---

## 🚀 빠른 테스트

Cursor를 재시작한 후:

1. **DOCX 테스트**:
   ```
   Cursor → 파일 열기 → _연구개발계획서_v6_제출용최종본.docx
   → Office Viewer로 자동 열림 ✅
   ```

2. **PDF 테스트** (있는 경우):
   ```
   Cursor → 파일 열기 → [파일명].pdf
   → PDF Viewer로 자동 열림 ✅
   ```

3. **HWP 테스트**:
   ```
   Cursor → 파일 열기 → 붙임2.hwp
   → 바이너리 또는 텍스트로 열림 (정상 뷰어 아님) ❌
   → 한글 프로그램 필요!
   ```

---

## 📚 참고 자료

### vscode-office 확장 프로그램
- **개발자**: cweijan
- **버전**: 3.5.4
- **기능**: Office 문서 미리보기
- **제한**: 읽기 전용 (편집 불가)

### HWP 관련 도구
- **한글 2022 뷰어**: 무료, macOS/Windows 지원
- **hwp5 Python**: CLI 도구, 텍스트 추출용
- **온라인 변환**: HWP ↔ DOCX 변환

---

**설정 완료 날짜**: 2025년 10월 22일
**설정 상태**:
- ✅ DOCX 뷰어: 설치 완료
- ❌ HWP 뷰어: 대안 제시
