# Incident Management System🚀

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Postgres](https://img.shields.io/badge/Postgres-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

## 📖 Description

The **Incident Management System** is a RESTful API-based application designed to manage incidents efficiently. Built with **Django and Django Rest Framework (DRF)**, it provides a secure backend for user registration, authentication, and incident tracking. The system supports token-based authentication. It is developed to meet the requirements of creating, viewing, and editing incidents with user-specific access controls.


## 📑 Table of Contents

- [Key Features](#-key-features)
- [System Requirements](#-system-requirements)
- [Installation](#-installation)
- [Backend Architecture Pattern](#-backend-architecture-pattern)
- [Project Structure](#-project-structure-backend)
- [Usage](#-usage)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)

## ✨ Features

- **User Management**:
   - Registration with required fields: email, first name, last name, country code, mobile, address, country, state, city, and pin code.
   - Email-based authentication with token generation.
- **Incident Management**:
    - Create, view, and edit incidents with auto-generated unique IDs (e.g., RMG123452024).
    - Incident fields include type (Enterprise/Government), details, priority (High/Medium/Low), status (Open/In Progress/Closed), and more.
    - Users can only access and modify their own incidents.
    - Closed incidents are non-editable.
    - Search incidents by ID.

## 🛠 Installation

### ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) Using Docker (Recommended)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/pwnbisht/rapifuzz.git
   cd rapifuzz

2. **Build the Docker Images**:
   ```bash
   docker-compose build

3. **Start the Containers**:
   ```bash
   docker-compose up -d
   
4. **Access the application**:
   - backend: <span style="background:#ff983f63; padding:1px;">http://localhost:8000</span>  (For container and host machine ports are same)


### Without Docker
If you’d rather set it up manually, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/pwnbisht/rapifuzz.git
   cd rapifuzz

2. **Set up the backend**:
   - Create a virtual environment and install dependencies:
   ```bash
      python -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate
      pip install -r requirements.txt
   ```
   
   - Start the Backend
   ```bash
   python manage.py runserver
   ```

3. **Access the Application**:
   - backend: <span style="background:#ff983f63; padding:1px;">http://localhost:8000</span> 