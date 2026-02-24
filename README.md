# 🍏 Smart Pantry Tracker
> *A full-stack sustainable living application to reduce food waste.*

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-red?style=for-the-badge&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-Frontend-purple?style=for-the-badge&logo=bootstrap&logoColor=white)

## 🚀 Live Demo
**[Click here to try the App](https://smart-pantry.onrender.com)**
*(Note: Hosted on a free instance. Please allow 30 seconds for the server to wake up.)*

## 📖 Overview
Smart Pantry is a responsive web application designed to solve the household problem of expired groceries. By leveraging **Computer Vision** (barcode scanning) and the **Open Food Facts API**, it allows users to rapidly catalog items and receive visual alerts for upcoming expiry dates.

## ✨ Key Features
* **📸 Real-Time Scanning:** Integrated `html5-qrcode` for browser-based barcode scanning (mobile-optimized).
* **☁️ Cloud Persistence:** Migrated from SQLite to **PostgreSQL** on Render for reliable data storage.
* **🔍 API Integration:** Fetches product metadata (names, brands) automatically via Open Food Facts.
* **📱 Responsive Design:** Built with Bootstrap 5 to work seamlessly on smartphones and desktops.

## 🛠️ Technical Architecture
* **Backend:** Python 3, Flask (Micro-framework), SQLAlchemy (ORM).
* **Database:** PostgreSQL (Production), SQLite (Local Development).
* **Frontend:** HTML5, Jinja2 Templates, Bootstrap 5.
* **Deployment:** CI/CD pipeline via GitHub Actions & Render.

## ⚙️ Local Installation
If you want to run this locally:

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/fsanmuhammed/smart-pantry.git](https://github.com/fsanmuhammed/smart-pantry.git)
   cd smart-pantry
