# University Weekly Course Schedule Management System

A modular, database-backed Python system that manages the full lifecycle of university course scheduling — users, courses, and classrooms — and automates the most time-consuming part of academic administration: turning raw scheduling data into a polished, department-specific weekly timetable. Built for the Software Lab 2 course at Kocaeli Health and Technology University as Phase 1 of a two-part scheduling initiative.

## Highlights

- Relational database schema with enforced foreign key integrity across four entities
- Fully parameterized SQL queries — no string-concatenated queries, no SQL injection surface
- Environment-based secret management (`python-dotenv`) — zero credentials in source control
- Automated Excel timetable generation with custom placement logic and full visual styling, ready to distribute as-is
- Clean modular architecture: a single `Database` class owns all data access, while independent modules own each business domain

## Why This Project

Academic scheduling is a coordination problem: instructors, classrooms, and course loads all have to line up correctly across departments and semesters, and doing it by hand in a spreadsheet doesn't scale. This system centralizes that data in a proper relational database and then automates the tedious final step — producing a clean, correctly laid-out weekly timetable per department, without manual copy-pasting.

## Features

**User Management**
- Role-based accounts (student, instructor, administrator) with unique email enforcement at the database layer
- Add, remove, and list operations, with instructor lookups automatically scoped to valid teaching staff when assigning courses

**Course Management**
- Full CRUD lifecycle for courses: add, edit, delete, list
- Rich metadata per course — code, name, weekly hour load, assigned instructor, department, classroom, semester, ECTS credits, and course type (mandatory/elective)
- Referential integrity ensures a course can never point to a nonexistent instructor, department, or classroom

**Classroom Management**
- Classroom inventory tracked by capacity and type (standard or laboratory)
- Referential checks prevent orphaned course-classroom assignments

**Automated Timetable Generation**
- Generates fully formatted, department-specific weekly schedules (Computer Engineering, Software Engineering) as Excel files
- Builds a Monday–Friday, hourly (09:00–17:00) grid segmented by academic year/semester
- Custom placement algorithm positions each course according to its weekly hour allocation, pulling instructor and classroom data through relational joins across four tables
- Professional output styling — centered alignment, bordered cells, colored headers, tuned row/column sizing — makes the result presentation-ready with no manual cleanup

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Database | MySQL — relational schema with foreign key constraints |
| Data Access | Parameterized queries via `mysql-connector-python` |
| Configuration | `python-dotenv` (environment-based credentials) |
| Reporting | `openpyxl` for automated Excel generation and styling |

## Architecture

The codebase follows a clear separation of concerns rather than one monolithic script:

- **`database.py`** — a single `Database` class encapsulates every connection, query, and schema operation. Nothing else in the codebase talks to MySQL directly.
- **Domain modules** (`kullanici_modulu.py`, `ders_modulu.py`, `derslik_modulu.py`) — each owns exactly one entity's business logic and depends on `Database` through composition, not inheritance, keeping modules independently testable.
- **Timetable generators** (`blm_program.py`, `yzm_program.py`, `bos_program.py`) — isolated, department-specific reporting scripts that consume the same underlying data model, so adding a new department's timetable means adding one new script, not touching existing ones.

## Database Design

Four related entities, enforced with real foreign key constraints rather than left to application-level trust:

- **Bolum** (Department) — department codes and names
- **Derslik** (Classroom) — capacity and a constrained type (`NORMAL` / `LAB`)
- **Kullanici** (User) — enforced role enum (`Öğretim Üyesi`, `Öğrenci`, `Yönetici`) with a unique email constraint
- **Dersler** (Course) — references instructor, department, and classroom by foreign key, so invalid assignments are rejected at the database level, not just in application code

## Project Structure
├── main.py # Entry point and menu navigation
├── database.py # Database class: connections, queries, schema setup
├── kullanici_modulu.py # User management module
├── ders_modulu.py # Course management module
├── derslik_modulu.py # Classroom management module
├── blm_program.py # Computer Engineering timetable generator
├── yzm_program.py # Software Engineering timetable generator
├── bos_program.py # Blank timetable template generator
├── .env.example # Sample environment configuration
└── requirements.txt

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env      # then fill in your local MySQL credentials
python main.py
```

## Roadmap

This repository represents **Phase 1**: core data management plus automated, department-level Excel scheduling. **Phase 2** is planned to extend the system into a full web-based platform covering university-wide scheduling across all departments simultaneously.
