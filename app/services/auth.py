from datetime import datetime, timedelta
from passlib.context import CryptContext
import secrets
from sqlalchemy.orm import Session
from app.models.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def generate_reset_token() -> str:
    return secrets.token_urlsafe(32)

def create_reset_token(db: Session, user: User) -> str:
    token = generate_reset_token()
    user.reset_token = token
    user.reset_token_expires = datetime.utcnow() + timedelta(minutes=15)
    db.commit()
    return token

def verify_reset_token(db: Session, token: str) -> User:
    user = db.query(User).filter(User.reset_token == token).first()
    if not user or not user.reset_token_expires:
        return None
    if datetime.utcnow() > user.reset_token_expires:
        return None
    return user

def reset_password(db: Session, user: User, new_password: str):
    user.password_hash = hash_password(new_password)
    user.reset_token = None
    user.reset_token_expires = None
    db.commit()
