# Finance Dashboard Backend

## Project Overview
Django REST Framework backend for a financial records management dashboard. Features user authentication with role-based permissions (VIEWER, ANALYST, ADMIN), CRUD operations for financial records, and dashboard summaries including totals, category breakdowns, recent activity, and monthly trends. Built to match project requirements using relational SQLite persistence.

## 🚀 Frontend Dashboard UI
**New!** Beautiful responsive frontend at `/frontend/`:
- Live charts (Chart.js): Category pie, monthly trends line
- Summary cards, recent activity list
- Tailwind CSS styling, auto-refresh data
- Visit: http://127.0.0.1:8000/frontend/

## Tech Stack
- **Backend**: Django 6.0.3, Django REST Framework
- **Frontend**: HTML/JS, Tailwind CSS, Chart.js (CDN)
- **Database**: SQLite (db.sqlite3)
- **Authentication**: Token Authentication + Custom Role-based Permissions
- **Validation**: DRF Serializers
- **Deployment**: Heroku-ready (Procfile/Gunicorn)

## Setup Steps
1. Install dependencies:
   ```
   pip install django djangorestframework
   ```
2. Run migrations:
   ```
   python manage.py migrate
   ```
3. Create superuser:
   ```
   python manage.py createsuperuser
   ```
4. Start server:
   ```
   python manage.py runserver
   ```
5. **Frontend**: http://127.0.0.1:8000/frontend/
6. **Admin** (add sample data): http://127.0.0.1:8000/admin/

## API Endpoints
| Endpoint | Method | Auth | Permissions |
|----------|--------|------|-------------|
| `/` & `/api/dashboard/` | GET | Optional | VIEWER+ | Dashboard JSON
| `/api/records/` | GET/POST | Token | ANALYST+ | List/Create (+filters: type, category, date range)
| `/api/records/{id}/` | GET/PUT/DELETE | Token | ANALYST+/ADMIN | Record ops
| `/api/users/` | GET/POST | Token | ADMIN |
| `/admin/` | - | Session | ADMIN |

## Quick Start with Sample Data
1. Login admin
2. Records > Add: 
   - Income: Salary $5000 "2024-04-01"
   - Expense: Groceries $200 "2024-04-05"
3. Refresh frontend - charts populate!

Live Demo: http://127.0.0.1:8000/frontend/

GitHub: https://github.com/chethankumarbs2004/finance-dashboard-backend

