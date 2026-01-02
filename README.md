# Password Reset API

A production-ready FastAPI application for handling password reset functionality with email verification.

## Features

- Request password reset via email
- Verify reset token
- Update password with token validation
- Token expiration (15 minutes)
- Email notifications
- SQLite database with SQLAlchemy ORM
- Secure password hashing with bcrypt


<img width="1366" height="721" alt="paasword reset swagger" src="https://github.com/user-attachments/assets/e9fc9e8a-04fe-4f6d-8498-b8df8a2dde15" />


## Project Structure

```
password-reset-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── auth.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── email.py
│   └── routes/
│       ├── __init__.py
│       └── auth.py
├── requirements.txt
├── .env.example
└── README.md
```

## Installation

1. Clone the repository
```bash
git clone <repository-url>
cd password-reset-api
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
```bash
cp .env.example .env
# Edit .env with your settings
```

5. Run the application
```bash
uvicorn app.main:app --reload
```

## Environment Variables

```env
DATABASE_URL=sqlite:///./app.db
SECRET_KEY=your-secret-key-here
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
FROM_EMAIL=noreply@yourapp.com
FRONTEND_URL=http://localhost:3000
```

## API Endpoints

### Request Password Reset
```http
POST /api/auth/forgot-password
Content-Type: application/json

{
  "email": "user@example.com"
}
```

### Reset Password
```http
POST /api/auth/reset-password
Content-Type: application/json

{
  "token": "reset-token-here",
  "new_password": "newPassword123"
}
```

### Health Check
```http
GET /health
```

## Dependencies

- **FastAPI**: Modern web framework
- **SQLAlchemy**: ORM for database operations
- **Pydantic**: Data validation
- **passlib**: Password hashing
- **python-jose**: JWT token handling
- **python-multipart**: Form data support
- **aiosmtplib**: Async email sending

## Security Features

- Passwords hashed with bcrypt
- Reset tokens expire after 15 minutes
- Secure token generation using secrets module
- Environment-based configuration
- SQL injection protection via ORM

## Database Schema

### Users Table
- `id`: Integer (Primary Key)
- `email`: String (Unique, Indexed)
- `password_hash`: String
- `reset_token`: String (Nullable)
- `reset_token_expires`: DateTime (Nullable)
- `created_at`: DateTime
- `updated_at`: DateTime

## Development

Run with auto-reload:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Testing

Example using curl:

```bash
# Request password reset
curl -X POST http://localhost:8000/api/auth/forgot-password \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com"}'

# Reset password
curl -X POST http://localhost:8000/api/auth/reset-password \
  -H "Content-Type: application/json" \
  -d '{"token":"your-token","new_password":"newPass123"}'
```

## Production Deployment

1. Use PostgreSQL instead of SQLite
2. Set strong SECRET_KEY
3. Enable HTTPS
4. Configure proper CORS settings
5. Set up rate limiting
6. Use production SMTP service
7. Enable logging and monitoring

## License


MIT
