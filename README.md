# FastAPI & Backend Development Specialization

This repository serves as a structured learning log and technical reference for the **Ultimate Guide to FastAPI and Backend Development Specialization** (Coursera/Packt). It documents my progress, core concept implementations, and a production-ready capstone project designed to showcase scalable backend architecture.

**Tech Stack**
* **Framework:** FastAPI, Python
* **Databases:** PostgreSQL, SQLAlchemy (ORM), SQL, and NoSQL integrations
* **Security:** OAuth2, JWT Authentication
* **Testing & Deployment:** Pytest, Docker, AWS

**Course Progression Tracker**

* [ ] **01_introduction-to-fastapi-and-backend-development-fundamentals**
  * Setup, FastAPI Basics, Pydantic Models, Routing & Endpoints
* [ ] **02_intermediate-backend-development-with-fastapi**
  * Relational DBs & SQL, NoSQL Integration, OAuth2 & JWT
* [ ] **03_advanced-backend-development-api-testing-and-deployment**
  * Pytest frameworks, Docker Containerization, AWS Deployment
* [ ] **04_final_capstone**
  * Fully integrated API featuring isolated testing (`/tests`), core logic (`/core`), and database routing (`/db`).

**Local Setup**
1. Clone the repository.
2. Copy `.env.example` to a new `.env` file and populate your local database credentials and JWT secret.
3. Install dependencies via `pip install -r requirements.txt`.
4. Navigate to the specific module directory and start the server (e.g., `uvicorn main:app --reload`).

**Author**
Abdul Rehman Saeed
