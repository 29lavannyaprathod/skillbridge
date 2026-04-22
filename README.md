# SkillBridge Backend API

## 🚀 Overview

SkillBridge is a backend API for managing a state-level training programme with **role-based access control (RBAC)** and a **secure monitoring system**.

The system supports multiple user roles with strictly enforced permissions and enables batch management, session tracking, and attendance recording.

---

## 🌐 Live API

🔗 Base URL:
https://skillbridge-so7v.onrender.com/

📄 Swagger Docs:
https://skillbridge-so7v.onrender.com/docs

---

## 🛠️ Tech Stack

* FastAPI (Backend framework)
* PostgreSQL (Neon)
* SQLAlchemy (ORM)
* JWT Authentication (python-jose)
* Passlib (password hashing)
* Pytest (testing)
* Render (deployment)

---

## 🔐 Authentication & Roles

### Supported Roles

* Student
* Trainer
* Institution
* Programme Manager
* Monitoring Officer

---

## 🔑 JWT Structure

### Standard Token (Login)

```json
{
  "user_id": 1,
  "role": "trainer",
  "iat": "...",
  "exp": "..."
}
```

* Valid for 24 hours
* Used for all protected endpoints

---

### Monitoring Token (Scoped)

```json
{
  "user_id": 5,
  "role": "monitoring_officer",
  "scope": "monitoring",
  "exp": "1 hour"
}
```

* Generated via `/auth/monitoring-token`
* Only valid for monitoring endpoints
* Cannot be used elsewhere

---

## 🔒 Security Considerations

### Current Implementation

* Password hashing using passlib
* JWT-based authentication
* Role-based access control (RBAC)
* Scoped tokens for monitoring

### Known Limitation

Tokens are not currently revocable.

### Improvement (Future Work)

* Implement token blacklisting (Redis)
* Add refresh tokens
* Use rotating signing keys

---

## ⚙️ API Endpoints

### Auth

* `POST /auth/signup`
* `POST /auth/login`
* `POST /auth/monitoring-token`

---

### Batches

* `POST /batches`
* `POST /batches/{id}/invite`
* `POST /batches/join`

---

### Sessions

* `POST /sessions`

---

### Attendance

* `POST /attendance/mark`
* `GET /sessions/{id}/attendance`

---

### Monitoring

* `GET /monitoring/attendance`

---

## 🧪 Sample CURL Commands

### Login

```bash
curl -X POST "https://new-ubkn.onrender.com/auth/login?email=trainer@test.com&password=1234"
```

---

### Create Session (Trainer)

```bash
curl -X POST "https://new-ubkn.onrender.com/sessions" \
-H "Authorization: Bearer <TOKEN>"
```

---

### Mark Attendance (Student)

```bash
curl -X POST "https://new-ubkn.onrender.com/attendance/mark?session_id=1&status=present" \
-H "Authorization: Bearer <TOKEN>"
```

---

## 👥 Test Accounts

| Role               | Email                                       | Password |
| ------------------ | ------------------------------------------- | -------- |
| Trainer            | [trainer@test.com](mailto:trainer@test.com) | 1234     |
| Student            | [student@test.com](mailto:student@test.com) | 1234     |
| Monitoring Officer | [mo@test.com](mailto:mo@test.com)           | 1234     |

---

## 🧠 Design Decisions

### 1. Batch Invites

* Token-based joining system
* Allows controlled student onboarding
* Prevents unauthorized batch access

---

### 2. Monitoring Token System

* Separate token with limited scope
* Prevents misuse of full-access JWT
* Adds extra security layer

---

### 3. RBAC Enforcement

* Enforced at backend (not frontend)
* Every endpoint validates role from JWT

---

## ⚠️ Validation & Error Handling

* Missing fields → 422
* Unauthorized access → 401
* Forbidden actions → 403
* Invalid references → 404
* Wrong method → 405

---

## 🧪 Testing

Run tests:

```bash
pytest
```

### Covered Cases

* Signup & login
* Protected routes
* Monitoring endpoint
* Unauthorized access
* Attendance access

---

## 📦 Deployment

* Hosted on Render
* PostgreSQL on Neon
* Environment variables managed securely

---

## ⚠️ What is Complete

* Core API (auth, batches, sessions, attendance)
* RBAC enforcement
* Monitoring token system
* Deployment
* Pytest tests

---

## ⚠️ What is Partial / Skipped

* Seed script (data created manually via API)
* Advanced summary endpoints (basic implementation)
* Multi-trainer batch mapping simplified

---

If I had more time, I would focus on improving the data modelling and reporting layer. Specifically, I would implement proper aggregation queries for summary endpoints and introduce a structured seed script for realistic test data.

Additionally, I would enhance the authentication system by adding refresh tokens and token revocation to improve security in a production scenario.

---

## 🔮 Future Improvements

* Add seed script for demo data
* Implement full reporting dashboards
* Add pagination & filtering
* Improve test coverage
* Introduce refresh tokens

---

## 🎯 Key Learning

This project demonstrates:

* API design with FastAPI
* Secure authentication & authorization
* Role-based system design
* Real-world backend workflow

---

## 👤 Author

Lavannya Pradeep Rathod
