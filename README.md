# SkillBridge Backend API

## Overview

This project is a backend API for managing a state-level training programme. It handles users, batches, sessions, and attendance while ensuring that each user can only perform actions based on their role.

The system is designed with a strong focus on **authentication, authorization, and controlled data access**, simulating how such a platform would function in a real-world scenario.

---

## Live API

Base URL:
https://skillbridge-so7v.onrender.com/

Swagger Docs:
https://skillbridge-so7v.onrender.com/docs

---

## Tech Stack

* FastAPI
* PostgreSQL (Neon)
* SQLAlchemy
* JWT Authentication (python-jose)
* Passlib (password hashing)
* Pytest
* Render (deployment)

---

## Authentication & Roles

The system supports multiple roles:

* Student
* Trainer
* Institution
* Programme Manager
* Monitoring Officer

Authentication is handled using JWT tokens, and access to endpoints is controlled using role-based access control (RBAC).

---

## Token Design

### Standard JWT

Used for normal operations:

```json
{
  "user_id": 1,
  "role": "trainer",
  "exp": "..."
}
```

---

### Monitoring Token (Scoped)

Generated via `/auth/monitoring-token`:

```json
{
  "user_id": 5,
  "role": "monitoring_officer",
  "scope": "monitoring",
  "exp": "..."
}
```

This token is required specifically for monitoring endpoints and cannot be used for other operations.

---

## Core Functionality

### Batch & Session Management

* Trainers create batches
* Invite tokens are generated for controlled student onboarding
* Trainers create sessions under batches

---

### Student Flow

* Students join batches using invite tokens
* Students mark attendance for sessions

---

### Monitoring System

* Monitoring officers use a separate scoped token
* Access to attendance data is restricted and validated

---

## API Endpoints

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

## Sample CURL Usage

### Signup

```bash
curl -X POST "https://new-ubkn.onrender.com/auth/signup?name=test&email=test@test.com&password=1234&role=student"
```

---

### Login

```bash
curl -X POST "https://new-ubkn.onrender.com/auth/login?email=test@test.com&password=1234"
```

---

### Mark Attendance

```bash
curl -X POST "https://new-ubkn.onrender.com/attendance/mark?session_id=1&status=present" \
-H "Authorization: Bearer <TOKEN>"
```

---

## Token Usage Flow

1. Login → receive JWT token
2. Use JWT for protected endpoints
3. For monitoring access:

   * Call `/auth/monitoring-token` with API key
   * Use returned token for monitoring endpoints

---

## Validation & Error Handling

* 401 → Unauthorized
* 403 → Forbidden
* 404 → Not found
* 405 → Method not allowed
* 422 → Validation errors

---

## Testing

Run tests:

```bash
pytest
```

Covers:

* Authentication
* Protected routes
* Monitoring restrictions
* Attendance access

---

## Security Notes

* Passwords are hashed
* JWT tokens used for authentication
* Monitoring endpoints require scoped tokens

### Known Limitation

Tokens are not currently revocable.

### Improvement

Introduce token revocation / refresh mechanism for production-grade security.

---

## Design Decisions

* **Invite-based joining** ensures controlled access to batches
* **RBAC enforced at backend** for security
* **Scoped monitoring token** adds an extra layer of restriction
* **Modular structure** improves maintainability

---

## What is Complete

* Authentication and JWT system
* Role-based access control
* Batch, session, and attendance flow
* Monitoring token system
* Deployment and testing

---

## What is Partial / Simplified

* Summary/reporting endpoints are implemented at a basic level
* Multi-trainer batch mapping is simplified
* Seed data is created manually through API calls

---

## What I Would Do Differently

If extended further, I would focus on improving the reporting layer with proper aggregation queries and structured seed data for realistic usage scenarios. Additionally, I would enhance the authentication system by introducing token revocation and refresh mechanisms to make it more production-ready.

---

## Deployment

* Backend deployed on Render
* Database hosted on Neon

---

## Final Note

The goal of this project was to build a structured backend system with clear role separation, secure access control, and realistic workflows. While some areas are simplified, the core system is fully functional and demonstrates the intended design.

---

## Author

Lavannya Pradeep Rathod
