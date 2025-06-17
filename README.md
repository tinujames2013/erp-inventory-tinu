# ERP Inventory & Order Management System

### 🚀 Full Stack Developer Task – NviSust Innovations Pvt. Ltd.
**Submitted by:** Tinu James  
**Date:** 16th June 2025  

---

## 📌 Project Overview

This project is a Full Stack ERP Inventory and Order Management System developed as part of the Full Stack Developer assessment. It includes:

- 🧠 **Backend:** Django + MySQL with Django REST Framework (DRF)
- 🎨 **Frontend:** Vue.js with Pinia (state management) and Axios
- 🔗 **API Integration** between Django and Vue
- 🔐 Role-based features (Admin can Add/Edit/Delete products)

---

## 🛠️ Features

### 🔹 Backend (Django + MySQL)
- Manage **Products**, **Suppliers**, **Stock**
- Create **Orders** with multiple **OrderItems**
- Automatically updates stock when orders are placed
- API Endpoints:
  - `POST /api/products/` – Add product
  - `GET /api/products/` – List all products
  - `POST /api/orders/` – Place new order
  - `GET /api/orders/` – View all orders

### 🔹 Frontend (Vue.js + Pinia)
- Product list with stock availability
- Add/Edit/Delete product (for Admin)
- Order form with live product selection
- Order history view
- Responsive dashboard layout

---

## 🔧 Tech Stack

| Area        | Tech Used                    |
|-------------|------------------------------|
| Backend     | Django 5.2.3, DRF, MySQL      |
| Frontend    | Vue 3, Pinia, Axios, Vite     |
| Styling     | Bootstrap 5                  |
| DB          | MySQL 8.0                    |

---

## ▶️ How to Run

### 💻 Backend:
```bash
cd inventory_project
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
