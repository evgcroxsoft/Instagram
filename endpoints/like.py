# ________________________________________________________LIKE__________________________________________________________________________________

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database.db import get_db
from models.enum import LikeStatus
from schemas.like import LikeRetrieveScheme
from schemas.session import SessionData
from schemas.user import UserRetrieveScheme
from security.session import cookie, verifier
from services.like import like_services
from services.user import user_services

router = APIRouter()

# -----------------------------------------------------/api/v1/like---------------------------------------------------------------------------------


@router.post(
    "/like",
    response_model=LikeRetrieveScheme,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(cookie)],
)
async def create_like(
    post: int,
    like_status: LikeStatus,
    current_user: UserRetrieveScheme = Depends(
        user_services.get_current_is_active_user
    ),
    session_data: SessionData = Depends(verifier),
    db: Session = Depends(get_db),
):

    return await like_services.create_like(db, session_data, post, like_status)


@router.delete(
    "/like", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(cookie)]
)
async def delete_like(
    post: int,
    current_user: UserRetrieveScheme = Depends(
        user_services.get_current_is_active_user
    ),
    session_data: SessionData = Depends(verifier),
    db: Session = Depends(get_db),
):

    return await like_services.delete_like(db, session_data, post)
