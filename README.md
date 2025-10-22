# 베리타스 강좌 2: 청소년 정신건강 교과목 개발 프로젝트

## 프로젝트 개요

**과제명**: 『베리타스 강좌 2: 뇌과학-심리학-언어인지과학으로 본 청소년 정신건강』
**영문명**: Veritas Lecture 2: Youth Mental Health Through Neuroscience, Psychology, and Cognitive Science

**연구 기간**: 2025년 6월 1일 ~ 2025년 10월 31일 (5개월)
**총 연구비**: 20,000,000원
**교과목 개설**: 2026년 2학기

## 연구진

| 역할 | 소속 | 성명 | 전공 |
|------|------|------|------|
| **책임연구자** | 심리학과 | 이해연 교수 | 발달심리학 |
| **공동연구자** | 심리학과 | 차지욱 부교수 | 인지신경과학 |
| **공동연구자** | 뇌인지과학과 | 전현애 부교수 | 언어인지 뇌과학 |

## 레포지토리 구조

```
베리타스 강좌 2/
├── README.md                          # 📖 프로젝트 개요 (본 파일)
├── CLAUDE.md                          # 🤖 AI 작업 지침
├── .gitignore                         # Git 설정
│
├── 00proposals/                       # 📝 연구 제안서
│   ├── current/                       # ⭐ 최신 버전 (v4)
│   │   ├── _연구개발계획서_v4_수정본.md       # 최신 마크다운 (편집용)
│   │   └── _연구개발계획서_v4_수정본.docx     # 최신 워드 (제출용)
│   ├── versions/                      # 📚 이전 버전들
│   │   ├── _연구개발계획서_v3_최종.md
│   │   ├── _연구개발계획서_v2_공식양식.md
│   │   ├── _연구개발계획서_v1.md
│   │   ├── _연구개발계획서.docx
│   │   └── _연구개발계획서_backup_before_jeon.docx
│   └── drafts/                        # 📄 초기 드래프트
│       ├── 초본-연구계획서.pdf
│       └── 초본-연구계획서.txt
│
├── 01summaries/                       # 📋 프로젝트 요약
│   └── veritas_research_plan_summary.md
│
├── 02communications/                  # 💬 의사소통 기록
│   ├── emails.md                      # 교수진 이메일
│   └── 데이터-회의록.md                # 2025년 4월 회의록
│
├── 03references/                      # 📚 참고 자료
│   ├── papers/                        # 학술 논문 및 교육 자료
│   │   ├── PAPER-Lancet youth mental health (2024).pdf
│   │   ├── PAPER-Lancet youth mental health (2024).txt
│   │   ├── PAPER-CITIES YOUTH MENTAL HEALTH.pdf
│   │   ├── PAPER-CITIES YOUTH MENTAL HEALTH.txt
│   │   └── Syll_Lab in SocEd Interventions_Sem2-2023 Final.pdf  # 이해연 교수 실라버스
│   └── data/                          # 추출된 데이터
│       ├── doc_tables.txt
│       └── _연구개발계획서_extracted.txt
│
└── 04application_guideline/           # 📋 지원 서류 양식
    ├── 붙임1_공모안내문.pdf
    ├── 붙임2_연구개발계획서.hwp
    ├── 붙임3_교과목신설신청서.hwp
    └── butin2.hwp, butin3.hwp
```

## 🎯 주요 파일 위치

### ⭐ 제출용 최신 문서
- **제안서 (워드)**: `00proposals/current/_연구개발계획서_v4_수정본.docx`
- **제안서 (마크다운)**: `00proposals/current/_연구개발계획서_v4_수정본.md`

### 📚 참고 문헌
- **Lancet Commission 논문**: `03references/papers/PAPER-Lancet youth mental health (2024).pdf`
- **Nature Cities 논문**: `03references/papers/PAPER-CITIES YOUTH MENTAL HEALTH.pdf`
- **이해연 교수 실라버스**: `03references/papers/Syll_Lab in SocEd Interventions_Sem2-2023 Final.pdf`

### 💬 프로젝트 기록
- **교수진 이메일**: `02communications/emails.md`
- **회의록**: `02communications/데이터-회의록.md`
- **프로젝트 요약**: `01summaries/veritas_research_plan_summary.md`

### 📋 지원 양식
- **공모 안내문**: `04application_guideline/붙임1_공모안내문.pdf`
- **계획서 양식**: `04application_guideline/붙임2_연구개발계획서.hwp`
- **신청서 양식**: `04application_guideline/붙임3_교과목신설신청서.hwp`

## 주요 버전 변경 이력

### v4 (2025-10-22) - 현재 최신 버전
- ✅ **팩트체크 완료**: 전현애 교수 소속 수정 (언어학과 → 뇌인지과학과)
- ✅ **학문 분야 재분류**: 인문학 → 자연과학
- ✅ **연구 논문 인용 정확성 개선**
- ✅ **교육 철학 강화**: AI-Enhanced Learning 섹션 추가
- ✅ **교육 방법론 통합**:
  - Intervention Science (Walton & Crum, 2022)
  - Design Thinking (Yeager et al., 2016)
  - Lab Worksheet 모델 (이해연 교수 Yale-NUS 검증 모델)
  - IRB 윤리 심의 교육 통합
- ✅ **평가 방식 개선**: APA-style 연구 논문 최종 과제
- ✅ **AI Agent Ecosystem 구체화**: Claude Code, GPT-4, LLM API 활용

### v3 (2025-10-22)
- 전현애 교수 참여 통합
- 언어인지과학 모듈 추가
- ❌ **오류**: 전현애 교수 소속 오기재

### v2 (2025-10-22)
- 공식 양식 적용
- 예산 및 일정 구체화

### v1 (2025-10-22)
- 초기 기획안

## 핵심 교육 특징

### 1. 삼각 융합 모델 (Triangular Integration)
```
         차지욱 (신경과학)
      "WHY: 신경생물학적 기전"
               /\
              /  \
             /    \
            /  통합 \
           /   모델  \
          /          \
이해연 (발달심리) ---- 전현애 (언어인지)
"WHEN/HOW: 발달궤적"  "WHAT: 의미구성"
```

### 2. AI-Enhanced Learning
- **AI-CoScientist** 프레임워크: 과학적 탐구 민주화
- **AI Coding Agents**: Claude Code, GitHub Copilot
- **LLM 분석**: GPT-4 API, Claude API
- **Learning by Doing**: AI와 페어 프로그래밍

### 3. 검증된 교육 모델
- **Intervention Science**: Wise Interventions (Walton & Crum, 2022)
- **Design Thinking**: 사용자 중심 개입 설계 (Yeager et al., 2016)
- **Lab Worksheets**: 점진적 프로젝트 개발 (5단계)
- **IRB 통합**: 윤리 심의를 교육 활동으로

### 4. 프로젝트 기반 학습
- 팀 구성: 5-6명 (전공 다양성)
- 15주 단일 프로젝트
- 중간 발표 (Week 10) + 최종 발표 (Week 15)
- 최종 산출물: APA-style 연구 논문 (3000단어)

## 주요 참고 문헌

### 개입 과학
- Walton, G. M., & Crum, A. J. (Eds.) (2022). *Handbook of wise interventions*. Guilford Press.
- Yeager, D. S., et al. (2016). Using design thinking to improve psychological interventions. *Journal of Educational Psychology*, 108(3), 374-391.

### 청소년 정신건강
- Lancet Commission on Youth Mental Health (2024). *The Lancet*.
- Gruebner, O., et al. (2024). Mental health-informed urban design. *Nature Cities*, 1, 234-247.

### 신경과학
- Cha, J., et al. (2023). SwiFT: Swin 4D fMRI Transformer. *NeurIPS*, 36.

### AI 및 교육
- Lu et al. (2024). The AI Scientist. Sakana AI.
- Vaithilingam et al. (2022). GitHub Copilot user study. *CHI*.

## 타임라인

| 시기 | 활동 |
|------|------|
| 2025.04-05 | 신청서 작성 및 제출 |
| 2025.05 말 | 선정 발표 |
| 2025.06-10 | 교과목 개발 (5개월) |
| 2025.10 | 교과목 제안서 제출 |
| 2025.11 | 최종 보고서 |
| 2026.2 | 교과목 개설 (2026년 2학기) |

## 예상 성과

### 교육적 성과
- 강의평가 목표: 4.5/5.0
- 학생 역량: 삼각 융합 사고, 데이터 리터러시, AI 활용, 정책 기획
- 산출물: 팀당 정책 제안서 + APA 논문

### 학술적 성과
- 교육과정 혁신 모델 발표
- 공동 연구 논문 가능성
- 우수 제안서 모음집 발간

### 사회적 파급효과
- 60-120명 학생 양성 (미래 정책 입안자/연구자)
- 지역사회 파트너십 구축
- 최우수작 정책 제안 (교육청, 여성가족부)

## 연락처

- **책임연구자**: 이해연 교수 (심리학과)
- **이메일**: [이메일 주소]
- **전화**: [전화번호]

---

**최종 수정**: 2025-10-22
**문서 버전**: v4 (Intervention Science + AI-Enhanced Learning 통합)
