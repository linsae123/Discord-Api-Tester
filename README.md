# 🔍 Discord API Version Comparator & RateLimit Tracker

> 디스코드 API의 서로 다른 버전(v9, v10 등)에 동일한 요청을 보낸 뒤, 응답 결과를 자동으로 비교하고 속도 및 레이트리밋(RateLimit) 정보를 추적하는 도구입니다.

---

## 📦 주요 기능

### 1. ✅ API 버전 응답 비교기
- `v9`, `v10`, `v11` 등 서로 다른 API 버전의 응답(JSON)을 비교
- 버전별 응답 구조 차이, 필드 추가/삭제 확인 가능
- 실제 응답을 JSON 파일로 저장하여 향후 분석 가능

### 2. 🚦 RateLimit 감지
- 각 요청에 대한 `X-RateLimit-Remaining`, `Retry-After` 등 헤더 추적
- 속도 제한 상태 실시간 표시
- 향후 자동 재시도 기능 확장 가능

---

## 🛠 사용 방법

### 1. 의존성 설치
```bash
pip install requests
```