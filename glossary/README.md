## 한의학 녹취 용어사전 사용 안내

이 폴더는 Whisper + Scribe v2 녹취 작업에서 사용하는 표준 용어사전 파일을 모아 둔 곳이다.

## 구성

- `common_terms.csv`: 모든 강의에 공통으로 적용하는 기본 한의학 용어사전
- `course_terms_template.csv`: 과목별 용어를 추가할 때 쓰는 템플릿
- `lecture_terms_template.csv`: 특정 강의 회차에만 적용할 용어를 추가할 때 쓰는 템플릿

## 공통 컬럼 정의

모든 CSV는 아래 컬럼을 공통으로 사용한다.

- `canonical`: 최종본에 남기고 싶은 표준 표기
- `variants`: 잘못 인식되기 쉬운 표기, 띄어쓰기 변형, 한자/영문/코드 표기를 `|`로 구분해 기록
- `category`: 예: `formula`, `herb`, `acupoint`, `meridian`, `classic`, `pattern`, `core_concept`
- `priority`: `critical`, `high`, `medium`
- `review_rule`:
  - `force_review`: 숫자, 처방, 혈자리처럼 반드시 사람이 확인해야 하는 항목
  - `prefer_dictionary`: 사전 표기를 우선 채택할 수 있는 항목
  - `normal`: 참고용 항목
- `apply_scope`: `common`, `course`, `lecture`
- `source`: `common`, `lecture_material`, `course_note`, `manual_add` 등 용어 출처
- `notes`: 보충 설명

## 권장 사용법

## 템플릿별 추가 컬럼

- `course_terms_template.csv`에는 `course` 컬럼을 추가해 어느 과목에 속한 용어인지 기록한다.
- `lecture_terms_template.csv`에는 `lecture_id` 컬럼을 추가해 어느 회차에만 적용되는 용어인지 기록한다.

## 권장 사용법

### 1. Whisper 후처리용

- `variants`와 `canonical`을 비교해 자동 정규화 후보를 만든다.
- 단, `force_review` 항목은 자동 치환하지 말고 검수 큐로 보낸다.

### 2. Scribe v2 keyterm용

- `priority`가 `critical` 또는 `high`인 항목의 `canonical`을 우선 keyterm 후보로 사용한다.
- 강의 자료(PPT/PDF)에서 추출한 용어가 있으면 `lecture_terms_template.csv`에 추가한 뒤 함께 넣는다.

### 3. 검수용

- 두 엔진이 충돌한 구간에서 사전의 `canonical`과 정확히 일치하는 후보를 우선 검토한다.
- 숫자, 용량, 횟수, 혈자리 코드는 언제나 사람 검수 대상이다.

## 버전 운영 규칙

- 배치 시작 시 사전 버전을 정한다. 예: `glossary v0.1`
- 배치 도중 수정이 필요하면 변경 사유와 적용 시작 강의를 별도로 기록한다.
- 공통 사전은 보수적으로 유지하고, 과목별/강의별 사전에 신규 용어를 먼저 넣은 뒤 검증 후 공통 사전으로 승격한다.
