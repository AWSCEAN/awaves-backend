# awaves-backend

---

## 프로젝트 구조

```
backend/
 ├─ app/
 │   ├─ api/
 │   ├─ core/
 │   ├─ db/
 │   ├─ schemas/
 │   ├─ services/
 │   └─ main.py
 ├─ alembic/
 ├─ alembic.ini
 ├─ .env
 ├─ requirements.txt
 └─ venv/
```

---

## 1. 개발 환경 세팅

```bash
py -3.11 -m venv .venv
.venv\Scripts\Activate
```

---

## 2. 패키지 설치

```bash
pip install -r requirements.txt
```

## 3. 서버 실행

## 로컬 테스트
### Window
```cmd
# 예시: set ENV={서버 환경 이름} && uvicorn app.main:app --reload
set ENV=local && uvicorn app.main:app --reload
```

---

## 기술스택
```
python 3.11.9
```
