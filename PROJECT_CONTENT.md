# BrightPath LMS — Project Content

## Overview

BrightPath LMS is a full-stack Learning Management System built for Sri Lankan university students, lecturers, and staff. It provides a digital library, live Kuppi (peer tutoring) sessions, smart notifications, AI-powered recommendations, and role-based access control.

---

## Tech Stack

| Layer      | Technology                                                              |
|------------|-------------------------------------------------------------------------|
| Frontend   | Vue 3, Vite, Vue Router, Pinia, Axios, Tailwind CSS                     |
| Backend    | Django 6.0, Django REST Framework, SimpleJWT (Token Auth)               |
| Database   | SQLite (dev) — easily swappable to PostgreSQL                           |
| Automation | Celery, django-celery-beat (periodic tasks, email notifications, recommendations) |
| Other      | Docker Compose (Redis for Celery broker), CORS headers                  |

---

## Project Structure

```
BrightPath-LMS-ITPM--main/
├── frontend/                  # Vue 3 + Vite SPA
│   ├── src/
│   │   ├── api/
│   │   │   └── axios.js                # Axios instance (baseURL: http://127.0.0.1:8000/api/)
│   │   ├── assets/                     # Static assets (CSS, images)
│   │   ├── components/
│   │   │   ├── layout/                 # Layout components
│   │   │   │   ├── AppNavbar.vue           # Public landing page navbar
│   │   │   │   ├── DashboardNavbar.vue     # Dashboard top navbar
│   │   │   │   ├── DashboardSidebar.vue    # Dashboard side navigation
│   │   │   │   ├── InteractiveFooter.vue   # Landing page footer
│   │   │   │   └── MainLayout.vue          # Dashboard wrapper (Sidebar + Navbar + RouterView)
│   │   │   ├── landing/               # Landing page sections
│   │   │   │   ├── HeroSection.vue
│   │   │   │   ├── DigitalLibraryPreview.vue
│   │   │   │   ├── LiveKuppiPreview.vue
│   │   │   │   ├── SmartNotificationsPreview.vue
│   │   │   │   └── VerificationWorks.vue
│   │   │   ├── library/               # Digital Library components
│   │   │   │   ├── DocumentGrid.vue
│   │   │   │   └── PointsWallet.vue
│   │   │   ├── content/               # Content management
│   │   │   │   ├── UploadResourceForm.vue
│   │   │   │   └── VideoLessonPlayer.vue
│   │   │   ├── automation/            # AI / Smart features
│   │   │   │   ├── FeedbackModal.vue
│   │   │   │   └── RecommendedGrid.vue
│   │   │   ├── identity/              # User identity
│   │   │   │   ├── ProfileSettings.vue
│   │   │   │   └── RegisterForm.vue
│   │   │   ├── ResourceList.vue
│   │   │   └── ResourceUploadModal.vue
│   │   ├── views/
│   │   │   ├── HomeView.vue            # Landing page (public)
│   │   │   ├── Login.vue               # Login page
│   │   │   ├── RegisterView.vue        # Multi-step registration (Student/Lecturer/Staff)
│   │   │   ├── ForgotPassword.vue      # Password reset via NIC verification
│   │   │   ├── DashboardView.vue       # Dashboard overview
│   │   │   ├── LibraryView.vue         # Digital Library page
│   │   │   ├── ContentDashboard.vue    # Kuppi Sessions / Upload Course / Grades
│   │   │   ├── ProfileView.vue         # Profile settings page
│   │   │   └── LoginView.vue           # (Redirect wrapper)
│   │   ├── stores/
│   │   │   ├── contentStore.js         # Pinia store for content management
│   │   │   └── counter.js              # Default Pinia example store
│   │   ├── router/
│   │   │   └── index.js                # Vue Router config with auth guards
│   │   ├── App.vue                     # Root component
│   │   └── main.js                     # App entry point
│   └── package.json
│
├── backend/                   # Django REST API
│   ├── brightpath/            # Django project settings
│   ├── accounts/              # User authentication & management
│   │   ├── models.py              # Custom User model (AbstractUser)
│   │   ├── views.py               # RegisterView, LoginView, ResetPasswordView
│   │   ├── serializers.py         # User serializer
│   │   ├── permissions.py         # Role-based permissions
│   │   ├── urls.py                # /api/accounts/ endpoints
│   │   └── admin.py               # Admin panel config
│   ├── core/                  # Core data models
│   │   ├── models.py              # User (simple), Module, UserActivity
│   │   └── admin.py
│   ├── automation/            # Background tasks & AI
│   │   ├── tasks.py               # Celery tasks (email, feedback, recommendations)
│   │   └── services/              # Recommendation engine
│   ├── media/                 # Uploaded files (ID photos, docs)
│   ├── manage.py
│   ├── requirements.txt
│   ├── docker-compose.yml     # Redis container for Celery
│   └── db.sqlite3             # SQLite database
│
├── package.json               # Root package.json
└── README.md
```

---

## Backend API Endpoints

### Accounts (`/api/accounts/`)

| Method | Endpoint              | Description                       | Auth Required |
|--------|-----------------------|-----------------------------------|---------------|
| POST   | `/register/`          | Register new user (multipart)     | No            |
| POST   | `/login/`             | Login with email + password (JWT) | No            |
| POST   | `/reset-password/`    | Reset password via NIC + email    | No            |

---

## Data Models

### `accounts.User` (Custom — extends AbstractUser)

| Field              | Type         | Notes                        |
|--------------------|-------------|------------------------------|
| role               | CharField   | STUDENT / LECTURER / STAFF   |
| email              | EmailField  | Unique, used as login ID     |
| full_name          | CharField   | Required                     |
| nic_number         | CharField   | Unique (Sri Lankan NIC)      |
| phone_number       | CharField   | Optional                     |
| university         | CharField   | Student only                 |
| faculty            | CharField   | Student only                 |
| academic_stream    | CharField   | Student only                 |
| student_id         | CharField   | Student / Staff ID           |
| institution        | CharField   | Lecturer only                |
| department         | CharField   | Lecturer / Staff             |
| designation        | CharField   | Lecturer only                |
| is_peer_tutor      | BooleanField| Kuppi teacher flag           |
| id_photo           | FileField   | Student ID card photo        |
| verification_doc   | FileField   | Lecturer verification doc    |

### `core.Module`

| Field       | Type      | Notes                          |
|-------------|-----------|--------------------------------|
| title       | CharField | Module name                    |
| stream      | CharField | Academic stream                |
| description | TextField | Module description             |

### `core.UserActivity`

| Field         | Type       | Notes                           |
|---------------|------------|----------------------------------|
| user          | ForeignKey | Links to core.User              |
| module        | ForeignKey | Links to Module                 |
| activity_type | CharField  | "viewed", "completed"           |
| timestamp     | DateTime   | Auto-set on creation            |

---

## Frontend Routes

| Path                   | View Component        | Auth | Description                |
|------------------------|-----------------------|------|----------------------------|
| `/`                    | HomeView              | No   | Public landing page        |
| `/login`               | Login                 | No   | User login                 |
| `/register`            | RegisterView          | No   | Multi-step registration    |
| `/forgot-password`     | ForgotPassword        | No   | Password reset             |
| `/dashboard`           | DashboardView         | Yes  | Dashboard overview         |
| `/dashboard/library`   | LibraryView           | Yes  | Digital Library            |
| `/dashboard/kuppi`     | ContentDashboard      | Yes  | Kuppi Sessions             |
| `/dashboard/upload`    | ContentDashboard      | Yes  | Upload Course (Lecturers)  |
| `/dashboard/grades`    | ContentDashboard      | Yes  | My Grades (Students)       |
| `/dashboard/profile`   | ProfileView           | Yes  | Profile Settings           |

---

## Automation & Background Tasks (Celery)

| Task                                    | Type     | Description                                 |
|-----------------------------------------|----------|---------------------------------------------|
| `send_resource_notification_email_task` | On-demand| Emails users when a new resource is uploaded |
| `request_user_feedback_task`            | Periodic | Requests user feedback on a schedule        |
| `update_peer_recommendations_task`      | Periodic | Runs AI recommendation engine for all users |

---

## User Roles & Access

| Feature                  | Student | Lecturer | Staff |
|--------------------------|---------|----------|-------|
| View Dashboard           | ✅      | ✅       | ✅    |
| Digital Library          | ✅      | ✅       | ✅    |
| Kuppi Sessions           | ✅      | ✅       | ✅    |
| Upload Course            | ❌      | ✅       | ✅    |
| My Grades                | ✅      | ❌       | ✅    |
| Profile Settings         | ✅      | ✅       | ✅    |
| Register as Peer Tutor   | ✅      | ❌       | ❌    |

---

## How to Run

### Frontend
```bash
cd frontend
npm install
npm run dev        # → http://localhost:5173
```

### Backend
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver   # → http://127.0.0.1:8000
```

### Redis + Celery (optional — for background tasks)
```bash
docker-compose up -d          # Start Redis
celery -A brightpath worker -l info
celery -A brightpath beat -l info
```

---

## Key Dependencies

### Frontend (`package.json`)
- `vue` ^3.5 — UI framework
- `vue-router` ^5.0 — Client-side routing
- `pinia` ^3.0 — State management
- `axios` ^1.13 — HTTP client
- `tailwindcss` ^3.4 — Utility CSS
- `vite` ^7.3 — Build tool / dev server

### Backend (`requirements.txt`)
- `Django` 6.0.2
- `djangorestframework` 3.16.1
- `djangorestframework-simplejwt` — JWT authentication
- `django-cors-headers` 4.9.0 — CORS support
- `celery` — Async task queue
- `django-celery-beat` — Periodic task scheduler
