# 코드베이스 온보딩 가이드

**베리타스 강좌 2: 청소년 정신건강 교과목 개발 프로젝트**

---

## 📋 프로젝트 개요

### 기본 정보
- **과제명**: 베리타스 강좌 2: 뇌과학-심리학-언어인지과학으로 본 전생애 정신건강
- **영문명**: Veritas Lecture 2: Lifespan Mental Health Through Neuroscience, Psychology, and Cognitive Science
- **연구 기간**: 2025년 6월 1일 ~ 2025년 10월 31일 (5개월) 또는 2025년 11월 1일 ~ 2026년 3월 31일
- **총 연구비**: 20,000,000원
- **교과목 개설**: 2026년 2학기 예정

### 연구진 구성
| 역할 | 소속 | 성명 | 전공 | 담당 |
|------|------|------|------|------|
| **책임연구자** | 심리학과 | 차지욱 (v8) / 이해연 (v4) | 인지신경과학 | 총괄, 신경과학 모듈 |
| **공동연구자** | 심리학과 | 이해연 | 발달심리학 | 발달 및 사회문화 모듈 |
| **공동연구자** | 뇌인지과학과 | 전현애 | 언어인지 뇌과학 | 언어인지 및 의미구성 모듈 |

---

## 🗂️ 레포지토리 구조

```
베리타스 강좌 2/
├── README.md                          # 프로젝트 개요 및 빠른 참조
├── CLAUDE.md                          # AI 작업 지침 (Claude Code용)
├── CODEBASE_ONBOARDING.md            # 본 문서 (코드베이스 온보딩)
│
├── 00proposals/                       # 📝 연구 제안서
│   ├── current/                       # ⭐ 최신 버전
│   │   ├── _연구개발계획서_v8_전생애최종본.md    # 최신 마크다운 (v8)
│   │   ├── _연구개발계획서_v8_전생애최종본.docx  # 최신 워드 (v8)
│   │   ├── _연구개발계획서_v4_수정본.md          # v4 (청소년 중심)
│   │   └── [기타 버전들...]
│   ├── versions/                      # 📚 이전 버전들
│   └── drafts/                        # 📄 초기 드래프트
│
├── 01summaries/                       # 📋 프로젝트 요약
│   ├── veritas_research_plan_summary.md
│   ├── 제안서_최종_점검_체크리스트.md
│   └── 팩트체크_결과_보고서.md
│
├── 02communications/                  # 💬 의사소통 기록
│   ├── emails.md                      # 교수진 이메일
│   └── 데이터-회의록.md                # 회의록
│
├── 03references/                      # 📚 참고 자료
│   ├── papers/                        # 학술 논문
│   │   ├── PAPER-Lancet youth mental health (2024).pdf
│   │   ├── PAPER-CITIES YOUTH MENTAL HEALTH.pdf
│   │   └── Syll_Lab in SocEd Interventions_Sem2-2023 Final.pdf
│   └── data/                          # 추출된 데이터
│
└── 04application_guideline/           # 📋 지원 서류 양식
    ├── 붙임1_공모안내문.pdf
    ├── 붙임2_연구개발계획서.hwp
    └── 붙임3_교과목신설신청서.hwp
```

---

## 🎯 핵심 개념 이해

### 1. 삼각 융합 모델 (Triangular Integration Model)

```
         차지욱 (신경과학)
      "WHY: 신경생물학적 기전"
     뇌 발달, SwiFT, ENIGMA
               /\
              /  \
             /    \
            /  통합 \
           /   모델  \
          /          \
이해연 (발달심리) -------- 전현애 (언어인지)
"WHEN/HOW: 발달궤적"    "WHAT: 의미구성"
마인드셋, 종단연구       서사, LLM, 시간지각
```

**세 가지 관점**:
- **신경과학 (차지욱)**: "WHY - 왜 청소년기에 정서 문제가 많은가?"
  - 뇌 발달, fMRI 분석, SwiFT 모델
- **발달심리학 (이해연)**: "WHEN/HOW - 언제, 어떻게 발달하는가?"
  - 발달 궤적, 마인드셋 개입, 종단 연구
- **언어인지과학 (전현애)**: "WHAT - 무슨 의미를 만드는가?"
  - 언어 서사, LLM 분석, 시간지각

### 2. 버전별 주요 변화

#### v4 (청소년 중심)
- 청소년 정신건강에 집중
- 전현애 교수 합류 반영
- 삼각 융합 모델 구체화

#### v8 (전생애 확장)
- **주제 확장**: 청소년 → 전생애 (영유아~고령)
- **PI 변경**: 이해연 → 차지욱
- **기간 변경**: 2025.11~2026.3
- **AI-CoScientist 프레임워크** 강화

### 3. 교육 철학

#### AI-Enhanced Learning
- **AI-CoScientist**: 과학적 탐구 민주화
- **AI Coding Agents**: Claude Code, GitHub Copilot
- **LLM 분석**: GPT-4 API, Claude API
- **Learning by Doing**: AI와 페어 프로그래밍

#### 검증된 교육 모델
- **Intervention Science**: Wise Interventions (Walton & Crum, 2022)
- **Design Thinking**: 사용자 중심 개입 설계 (Yeager et al., 2016)
- **Lab Worksheets**: 점진적 프로젝트 개발 (5단계)
- **IRB 통합**: 윤리 심의를 교육 활동으로

---

## 📚 주요 문서 가이드

### 최신 제안서
- **v8 (전생애)**: `00proposals/current/_연구개발계획서_v8_전생애최종본.md`
  - 전생애 관점으로 확장
  - 차지욱 교수가 PI
- **v4 (청소년)**: `00proposals/current/_연구개발계획서_v4_수정본.md`
  - 청소년 중심 버전
  - 이해연 교수가 PI

### 참고 문헌
- **Lancet Commission (2024)**: `03references/papers/PAPER-Lancet youth mental health (2024).pdf`
  - 전 세계 청소년 정신건강 위기 분석
- **Nature Cities (2024)**: `03references/papers/PAPER-CITIES YOUTH MENTAL HEALTH.pdf`
  - 도시 설계와 청소년 정신건강
- **이해연 교수 실라버스**: `03references/papers/Syll_Lab in SocEd Interventions_Sem2-2023 Final.pdf`
  - Lab Worksheet 모델 참고

### 프로젝트 요약
- `01summaries/veritas_research_plan_summary.md`: 종합 요약
- `01summaries/제안서_최종_점검_체크리스트.md`: 제출 전 체크리스트
- `01summaries/팩트체크_결과_보고서.md`: 팩트체크 결과

---

## 🔍 문서 버전 이해하기

### 버전 히스토리

| 버전 | 특징 | PI | 주제 | 주요 변경사항 |
|------|------|-----|------|-------------|
| v1 | 초기 기획안 | 이해연 | 청소년 | 기본 구조 |
| v2 | 공식 양식 적용 | 이해연 | 청소년 | 예산 및 일정 구체화 |
| v3 | 전현애 교수 합류 | 이해연 | 청소년 | 언어인지과학 모듈 추가 |
| v4 | 팩트체크 완료 | 이해연 | 청소년 | 소속 수정, AI-Enhanced Learning 추가 |
| v5-v7 | 개선본 | 이해연 | 청소년 | 세부 개선 |
| v8 | 전생애 확장 | **차지욱** | **전생애** | 주제 확장, PI 변경, AI-CoScientist 강화 |

### 현재 상태
- **v8이 최신 버전** (전생애 최종본)
- **v4도 참고 가치 있음** (청소년 중심 상세 설계)

---

## 🎓 교과목 구조 (15주)

### 모듈 구성 (v8 기준)

| 모듈 | 주차 | 주제 | 담당 교수 |
|------|------|------|-----------|
| 1 | 1-2 | 전생애 정신건강 개론 | 차지욱, 이해연 |
| 2 | 3-4 | 영유아·아동기 | 이해연 |
| 3 | 5-6 | 청소년 뇌 발달·언어 서사 | 차지욱, 전현애 |
| 4 | 7-8 | 청소년 실존 주제·청년 번아웃 | 전현애, 차지욱 |
| 5 | 9-10 | 중년 돌봄·중간 발표 | 이해연 |
| 6 | 11-12 | 고령기·AI 윤리 | 전현애, 차지욱 |
| 7 | 13-15 | 전생애 정책 설계·최종 발표 | 전원 |

### 핵심 활동
- **Lab Worksheets (5회)**: 단계별 프로젝트 점검
- **데이터 분석 과제 (3회)**: fMRI, 언어, 정책 데이터
- **중간/최종 발표**: Week 10, 15
- **APA 논문**: 최종 산출물 (3000단어)

---

## 💡 주요 연구 성과 및 도구

### 차지욱 교수
- **SwiFT**: Swin 4D fMRI Transformer (NeurIPS 2023)
  - 청소년 vs 성인 뇌 패턴 분류
- **ENIGMA OCD**: 국제 컨소시엄 연구
  - 청소년 정신병리의 뇌 구조 이상

### 이해연 교수
- **Nature 2022**: 대규모 온라인 마인드셋 개입
  - 110만 명 도달, 글로벌 확장
- **TLSASR Dataset**: 한국 청소년 종단 데이터
- **Lab Worksheet 모델**: Yale-NUS 검증 모델

### 전현애 교수
- **위계적 규칙 학습**: 전전두엽 처리 메커니즘
- **시간지각 연구**: 정신건강과 시간 지각의 관계
- **LLM 언어 분석**: 청소년 언어 데이터에서 정신건강 신호 탐지

---

## 🔧 작업 시 주의사항

### 문서 편집 시
1. **버전 확인**: v8이 최신이지만, v4도 참고 가치 있음
2. **PI 확인**: v8은 차지욱, v4는 이해연
3. **주제 범위**: v8은 전생애, v4는 청소년 중심
4. **일관성 유지**: 한 버전 내에서 일관된 정보 사용

### 팩트체크 필요 항목
- 전현애 교수 소속: **뇌인지과학과** (v4에서 수정됨)
- 학문 분야: **자연과학** (뇌인지과학)
- 이해연 교수 Nature 2022 논문: 저자 역할 확인 필요
- 통계 데이터: 출처 재확인 필요

### 파일 형식
- **마크다운 (.md)**: 편집 및 버전 관리용
- **워드 (.docx)**: 제출용
- **HWP**: 공식 양식 (한컴오피스 필요)

---

## 📞 빠른 참조

### 주요 파일 위치
- **최신 제안서 (v8)**: `00proposals/current/_연구개발계획서_v8_전생애최종본.md`
- **청소년 버전 (v4)**: `00proposals/current/_연구개발계획서_v4_수정본.md`
- **프로젝트 개요**: `README.md`
- **AI 작업 지침**: `CLAUDE.md`

### 주요 참고 문헌
- Lancet Commission (2024): `03references/papers/PAPER-Lancet youth mental health (2024).pdf`
- Nature Cities (2024): `03references/papers/PAPER-CITIES YOUTH MENTAL HEALTH.pdf`
- 이해연 교수 실라버스: `03references/papers/Syll_Lab in SocEd Interventions_Sem2-2023 Final.pdf`

---

## 🚀 다음 단계

1. **최신 제안서 읽기**: v8 전생애 최종본 확인
2. **참고 문헌 검토**: Lancet, Nature Cities 논문
3. **프로젝트 요약 확인**: `01summaries/veritas_research_plan_summary.md`
4. **체크리스트 확인**: 제출 전 최종 점검

---

**최종 업데이트**: 2025-10-22  
**문서 버전**: v8 (전생애 최종본) / v4 (청소년 중심)

