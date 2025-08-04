# 📊 amazonQuickSightEmbedding

This project is an example of embedding **Amazon QuickSight dashboards** using FastAPI as the backend and a simple HTML page as the frontend.

---

## 🚀 Features

- Embed Amazon QuickSight dashboards into your web application
- Backend powered by **FastAPI**
- Simple HTML frontend to display the embedded dashboard
- Hot reload support during development using Uvicorn

---

## 🛠️ Prerequisites

Make sure you have:

- Python 3.8+
- `uvicorn`, `fastapi`, and other dependencies
- Amazon QuickSight set up with appropriate embed permissions
- IAM role/user with access to generate QuickSight embed session URLs

---

## ▶️ How to Run

### 1. Start the FastAPI Backend

```bash
python -m uvicorn main:app --reload
```
## 🌐 Frontend Setup

### 2. Start the Static HTML Frontend
Run the following command to start a simple HTTP server on port 8080:

```bash
python -m http.server 8080
```

### 3. Access the Web Interface
Open your browser and go to:
```bash
http://localhost:8080/index.html
```
Ex:
<img width="1910" height="908" alt="QSq" src="https://github.com/user-attachments/assets/fc989e7e-6612-47e1-9c76-2b994bf51e9e" />




Sources:
- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight/client/generate_embed_url_for_registered_user.html



