from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.auth import ForgotPasswordRequest, ResetPasswordRequest, MessageResponse
from app.models.user import User
from app.services import auth, email

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/forgot-password", response_model=MessageResponse)
async def forgot_password(request: ForgotPasswordRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    token = auth.create_reset_token(db, user)
    await email.send_reset_email(user.email, token)
    
    return {"message": "Password reset email sent"}

@router.post("/reset-password", response_model=MessageResponse)
async def reset_password(request: ResetPasswordRequest, db: Session = Depends(get_db)):
    user = auth.verify_reset_token(db, request.token)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid or expired token")
    
    auth.reset_password(db, user, request.new_password)
    return {"message": "Password reset successful"}
