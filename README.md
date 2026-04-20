# Weather Services API Project
Author: Chenggang Cheng

Github: https://github.com/WENGLINGDIDI/Web-Services-and-Web-Data.git
## Project Overview
This project is a RESTful Web Service built with Django and Django Rest Framework (DRF). It provides an API for managing and analyzing historical weather data. The system allows users to perform CRUD (Create, Read, Update, Delete) operations on weather records and includes advanced features like data aggregation (statistics) and multi-parameter search filtering.

**Key Features:**
- **RESTful API Endpoints**: Full lifecycle management of weather records.
- **Data Analytics**: Real-time calculation of temperature and humidity statistics.
- **Advanced Search**: Filter weather data by condition and temperature ranges.
- **Cloud Deployment**: Fully deployed and accessible via PythonAnywhere.

---

## Technical Stack
- **Backend Framework**: Django
- **API Architecture**: REST (Representational State Transfer)
- **Database**: SQLite
- **Deployment**: PythonAnywhere (WSGI)
- **Version Control**: Git & GitHub

---
## Dataset
https://www.kaggle.com/datasets/rohitgrewal/weather-data

---
## Setup Instructions

### 1. Prerequisites
- Python 3.10+
- Git

### 2. Local Installation
Clone the repository and set up the environment:
```bash
# Clone the repository
git clone [https://github.com/WENGLINGDIDI/Web-Services-and-Web-Data.git](https://github.com/WENGLINGDIDI/Web-Services-and-Web-Data.git)
cd Web-Services-and-Web-Data

# Create a virtual environment
python -m venv venv

# Install dependencies
pip install -r requirements.txt

# Run migrations to create database schema
python manage.py migrate

# Import initial weather data from CSV
python import_data.py

# Running the Server
python manage.py runserver
```

The API will be accessible at http://127.0.0.1:8000/api/weather/.

[点击查看 API 详细文档 (PDF)](API_document.pdf)

## Deployment Information
The project is live at: http://xiaoshutiao.pythonanywhere.com/api/weather/



