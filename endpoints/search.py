# ________________________________________________________SEARCH__________________________________________________________________________________

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database.db import get_db
from schemas.session import SessionData
from schemas.user import UserRetrieveScheme
from security.session import cookie, verifier
from services.account import account_services
from services.user import user_services

router = APIRouter()

# --------------------------------------------------/api/v1/search---------------------------------------------------------------------------------


@router.get("/search", status_code=status.HTTP_200_OK, dependencies=[Depends(cookie)])
async def searching(
    nickname: str,
    current_user: UserRetrieveScheme = Depends(
        user_services.get_current_is_active_user
    ),
    session_data: SessionData = Depends(verifier),
    db: Session = Depends(get_db),
):
    return await account_services.get_account_with_post(nickname, nickname, db)
