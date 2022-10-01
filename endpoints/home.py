#________________________________________________________HOME__________________________________________________________________________________

from fastapi import APIRouter, Depends, status, BackgroundTasks
from sqlalchemy.orm import Session

from database.db import get_db
from schemas.like import LikeRetrieveScheme
from schemas.session import SessionData
from security.session import cookie, verifier
from services.user import user_services
from schemas.user import UserRetrieveScheme
from models.enum import LikeStatus
from services.like import like_services
from services.post import post_services

router = APIRouter()

# -----------------------------------------------------/api/v1/home---------------------------------------------------------------------------------

@router.get('/home', status_code=status.HTTP_200_OK, dependencies=[Depends(cookie)])
async def get_all_my_posts(
                        current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user),
                        session_data: SessionData = Depends(verifier),
                        db: Session = Depends(get_db)):
    return await post_services.get_all_posts(session_data, db)