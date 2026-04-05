# Finance Dashboard Backend

## Project Overview
Django REST Framework backend for a financial records management dashboard. Features user authentication with role-based permissions (VIEWER, ANALYST, ADMIN), CRUD operations for financial records, and dashboard summaries including totals, category breakdowns, recent activity, and monthly trends. Built to match project requirements using relational SQLite persistence.

## Tech Stack
- **Backend**: Django 6.0.3, Django REST Framework
- **Database**: SQLite (db.sqlite3)
- **Authentication**: Token Authentication + Custom Role-based Permissions
- **Validation**: DRF Serializers
- **Deployment**: Django development server (production-ready with WSGI/ASGI)

## Setup Steps
1. Install dependencies:
   ```
   pip install django djangorestframework
   ```
2. Run migrations:
   ```
   python manage.py migrate
   ```
3. Create superuser (ADMIN role):
   ```
   python manage.py createsuperuser
   ```
4. Start development server:
   ```
   python manage.py runserver
   ```
5. Access at http://127.0.0.1:8000/

## API Endpoints

| Endpoint | Method | Description | Authentication | Permissions | Query Params | Request Body Example |
|----------|--------|-------------|----------------|-------------|--------------|---------------------|
| `/` | GET | Dashboard summary (totals, categories, recent, monthly trends) | Optional (Token for user context) | VIEWER+ | None | N/A |
| `/api/records/` | GET | List records | Optional | VIEWER+ | `type`, `category`, `start_date`, `end_date` | N/A |
| `/api/records/` | POST | Create record | Required | ANALYST+ | N/A | ```{"amount": 1000, "type": "income", "category": "Salary", "date": "2024-04-01", "notes": "Monthly pay"}``` |
| `/api/records/{id}/` | GET | Retrieve record | Optional | VIEWER+ | N/A | N/A |
| `/api/records/{id}/` | PUT | Update record | Required | ANALYST+ | N/A | Same as POST |
| `/api/records/{id}/` | DELETE | Delete record | Required | ADMIN | N/A | N/A |
| `/api/users/` | GET | List users | Required | ADMIN | N/A | N/A |
| `/api/users/` | POST | Create user | Required | ADMIN | N/A | ```{"username": "analyst1", "email": "a@example.com", "password": "pass123", "role": "ANALYST"}``` |
| `/admin/` | GET | Django Admin | Required | ADMIN | N/A | N/A |

**Response Examples:**
- Dashboard GET: `{"total_income": 5000.0, "total_expense": 2000.0, "net_balance": 3000.0, "category_totals": [...], "recent_activity": [...], "monthly_trends": [...]}`
- Records POST 201: `{"id": 1, "amount": 1000, "type": "income", "category": "Salary", "date": "2024-04-01", "notes": "Monthly pay", "created_by": 1}`

**Error Responses:** Standard DRF 400/403/404/500 with detail messages.

## Sample Requests
```bash
# Get dashboard (no auth needed for basic data)
curl http://127.0.0.1:8000/

# Create record (with TokenAuth header)
curl -X POST http://127.0.0.1:8000/api/records/ \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"amount": 500, "type": "expense", "category": "Groceries", "date": "2024-04-05"}'

# Filter records
curl "http://127.0.0.1:8000/api/records/?type=income&category=Salary&start_date=2024-01-01"
```

**Get Token:** Login via Django admin or custom login view, use token in `Authorization: Token <token>` header.

## Assumptions
- Records belong to creating user (created_by FK).
- Dashboard aggregates all records (could filter by user if needed).
- Date filtering uses standard YYYY-MM-DD format.
- Categories free-text (could add choices).
- Amount > 0 validated in serializer.
- Monthly trends truncate to month start.
- No pagination on dashboard (small datasets).
- SQLite suitable for dev/demo (migrate to PostgreSQL for prod).
- Roles: VIEWER (read), ANALYST (CRUD records), ADMIN (all + users).

Live Demo: http://127.0.0.1:8000/

