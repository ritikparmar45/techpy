# Candidate Management API

A robust and simple Candidate Management API built with **Python**, **FastAPI**, and **MongoDB**. 

This project was built to demonstrate clean code architecture, professional error handling, and asynchronous database integration for a Candidate Management implementation.

## 🚀 Features

- **Asynchronous Operations**: Uses `motor` for non-blocking I/O with MongoDB.
- **Data Validation**: Strict validation using Pydantic (e.g., valid email formats, specific job statuses).
- **Clean Architecture**: Organized into Routes, Services, and Models for better maintainability.
- **RESTful Endpoints**:
  - `POST /candidates`: Create new candidates with valid data.
  - `GET /candidates`: Retrieve all candidates (with optional status filtering).
  - `PUT /candidates/{id}/status`: Update a candidate's status by ID.
- **Automated Documentation**: Interactive API testing via Swagger UI.

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Database**: MongoDB (with Motor driver)
- **Validation**: Pydantic
- **Server**: Uvicorn

## 📦 Project Structure

```text
├── routes/             # API Router definitions
├── services/           # Business logic & Database interactions
├── models.py           # Data storage models
├── schemas.py          # Request/Response validation schemas
├── database.py         # MongoDB connection setup
├── main.py             # Entry point of the application
├── test_api.py         # Automated test script
└── .env                # Configuration variables
```

## ⚙️ How to Setup and Run

### 1. Prerequisites
- Python 3.8+
- MongoDB (running locally or on the cloud)

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Setup
Create a `.env` file in the root directory and add your MongoDB URL:
```text
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=candidate_db
PORT=8000
```

### 4. Run the API
```bash
uvicorn main:app --reload
```
The server will start at `http://localhost:8000`.

### 5. API Documentation
Visit the interactive Swagger docs at:
[http://localhost:8000/docs](http://localhost:8000/docs)

### 6. Testing
You can run the automated test script to verify all functions:
```bash
python test_api.py
```

---

*This project is part of a backend engineering assignment.*
