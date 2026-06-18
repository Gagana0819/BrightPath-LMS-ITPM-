# BrightPath-LMS-ITPM-

Superuser created! Now you can log in to the Django admin:

URL: http://127.0.0.1:8000/admin/
Email: admin@brightpath.com
Password: admin123

run celery: celery -A brightpath worker --loglevel=info -P eventlet

---

### 1. PROJECT TITLE & OVERVIEW
**BrightPath LMS**  
BrightPath LMS is a comprehensive, full-stack Learning Management System designed specifically for the Sri Lankan university ecosystem. It bridges the gap between students, lecturers, and staff by providing a centralized digital library, live peer tutoring (Kuppi) management, and intelligent content recommendations, ultimately streamlining the academic experience and fostering collaborative learning.

### 2. TECH STACK
*   **Frontend:** Vue 3, Vite, Tailwind CSS, Pinia (State Management), Vue Router, Axios
*   **Backend:** Python, Django 6.0, Django REST Framework (DRF), SimpleJWT (Token Auth)
*   **Database:** SQLite (development-ready) / PostgreSQL (production-ready)
*   **Cloud, Tools & Automation:** Celery, Redis (Dockerized Message Broker), Django-Celery-Beat, AWS S3 (`django-storages` with `boto3`)
*   **Document Processing:** PyTesseract (OCR), PyPDF2, python-docx, ReportLab

### 3. KEY FEATURES & CORE FUNCTIONALITIES
*   **Role-Based Access & Identity Verification:** Secure, multi-tiered registration and dashboard experiences tailored for Students, Lecturers, and Staff, featuring Sri Lankan NIC (National Identity Card) verification.
*   **Digital Library & Points Wallet:** A centralized repository for study materials, complemented by a gamified "Points Wallet" system to encourage engagement, content uploads, and knowledge sharing.
*   **Live Kuppi (Peer Tutoring) Sessions:** Dedicated modules enabling students to schedule, manage, and discover peer-led tutoring sessions to collaboratively tackle complex subjects.
*   **Smart Automated Notifications:** Context-aware, asynchronous email and in-app notifications (powered by HTML email templates) that alert users about newly uploaded resources or request post-download feedback.
*   **AI-Powered Resource Recommendations:** An intelligent recommendation engine that analyzes user activity (such as viewed and completed modules) to dynamically suggest relevant study materials.

### 4. TECHNICAL ARCHITECTURE & PATTERNS
*   **Decoupled Client-Server Architecture:** The project utilizes a modern Single Page Application (SPA) frontend built with Vue 3, completely decoupled from the backend and communicating securely via a RESTful API.
*   **MVT to API-First Design:** The backend adapts Django’s standard Model-View-Template pattern into a Model-View-Serializer architecture using Django REST Framework to expose structured JSON endpoints.
*   **Asynchronous Task Queue Pattern:** Heavy operations are decoupled from the main HTTP request-response cycle using a robust Celery + Redis architecture, ensuring the API remains highly responsive under load.
*   **Stateless Authentication:** Implements JWT (JSON Web Tokens) to handle stateless, scalable, and secure API communication across the frontend and backend.

### 5. ENGINEERING COMPLEXITIES & CHALLENGES
*   **Asynchronous Task Orchestration:** Implementing `Celery` and `Redis` to orchestrate background processes was a significant engineering challenge. This architecture safely offloads time-consuming tasks—such as broadcasting HTML-rich email notifications (`send_resource_notification_email_task`), dispatching periodic user feedback requests, and crunching peer recommendations—without blocking the main thread or impacting user experience.
*   **Document Parsing & OCR Integration:** Integrating libraries like `PyTesseract`, `PyPDF2`, and `python-docx` points to advanced file handling mechanisms. This involved building complex pipelines to parse text from uploaded study resources or automate the optical character recognition (OCR) verification of Student ID cards and Lecturer credential documents.
*   **Custom AI Recommendation Engine:** Engineering a scalable `RecommendationEngine` that aggregates user activity metrics (like module views and completions) across the entire student body. The challenge here was efficiently querying the `UserActivity` data and generating relevant, dynamic content suggestions in the background via `update_peer_recommendations_task`, avoiding heavy database lockups during peak traffic.