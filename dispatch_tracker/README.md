# Dispatch Tracker 🚚📦  
**Capstone Project by Annete Achieng'**

_Dispatch Tracker is a logistics management web application designed to streamline the flow of product deliveries from sender to destination. The system allows company staff to register clients and drivers, assign dispatches, and track the status of deliveries in real-time._

---

## 🔧 Project Purpose

This project reflects my background in logistics coordination and demonstrates how I can turn real-world industry experience into practical software solutions. It is built using Django and focuses on usability, clarity, and functionality — without external APIs.

---

## ✨ Features

- ✅ User login & role-based authentication (Admin, Staff, Client, Driver)
- ✅ Dispatch creation and assignment
- ✅ Driver management (registration, assignment)
- ✅ Real-time delivery tracking (Pending → In Transit → Delivered/Failed)
- ✅ Client record management
- ✅ Dispatch overview list

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Django Templates (HTML, CSS)
- **Database:** SQLite (default for development)
- **Authentication:** Custom user model with roles
- **Version Control:** Git & GitHub

---

## 🗂️ App Structure

| App         | Responsibility                              |
|-------------|----------------------------------------------|
| `accounts`  | Custom user model, login, and roles          |
| `clients`   | Manage client information                    |
| `drivers`   | Handle driver registration and info          |
| `dispatches`| Create dispatches, assign drivers, track status |

---

## 🌐 API Endpoints (Views-based)

| Endpoint               | Method(s)    | Description                       |
|------------------------|--------------|-----------------------------------|
| `/login/`              | `POST`       | User login                        |
| `/logout/`             | `POST`       | Logout user                       |
| `/clients/`            | `GET, POST`  | List or register new clients      |
| `/clients/<id>/`       | `GET, PUT, DELETE` | View, update, or delete a client   |
| `/drivers/`            | `GET, POST`  | List or add drivers               |
| `/drivers/<id>/`       | `GET, PUT, DELETE` | View, update, or delete a driver   |
| `/dispatches/`         | `GET, POST`  | View or create dispatches         |
| `/dispatches/<id>/`    | `GET, PUT`   | View or update a specific dispatch|

---

## 📊 Database Models (Summary)

- **CustomUser:** username, email, password, role
- **Client:** user (1:1), phone, location
- **Driver:** user (1:1), phone, license_plate
- **Dispatch:** client, driver, pickup_location, dropoff_location, status, dispatch_time

---

## 🗓️ Project Timeline

| Week  | Tasks Completed                                      |
|-------|------------------------------------------------------|
| 1     | Project setup, apps created                          |
| 2     | Custom user model & authentication                   |
| 3     | Clients and drivers module (CRUD)                    |
| 4     | Dispatch creation, assignment, tracking              |
| 5     | Final polish, testing, documentation                 |

