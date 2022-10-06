# ________________________________________________________SUBSCRIBE__________________________________________________________________________________

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database.db import get_db
from models.enum import SubcribeStatus
from schemas.session import SessionData
from schemas.subscribe import SubscribeRetrieveScheme
from schemas.user import UserRetrieveScheme
from security.session import cookie, verifier
from services.subscribe import subscriber_services
from services.user import user_services

router = APIRouter()

# --------------------------------------------------/api/v1/subscribe---------------------------------------------------------------------------------


@router.post(
    "/subscribe",
    response_model=SubscribeRetrieveScheme,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(cookie)],
)
async def create_subscribe(
    nickname: str,
    current_user: UserRetrieveScheme = Depends(
        user_services.get_current_is_active_user
    ),
    session_data: SessionData = Depends(verifier),
    db: Session = Depends(get_db),
):
    return await subscriber_services.create_subscribe(session_data, db, nickname)


@router.get(
    "/subscribe/me", status_code=status.HTTP_200_OK, dependencies=[Depends(cookie)]
)
async def i_subscribed(
    current_user: UserRetrieveScheme = Depends(
        user_services.get_current_is_active_user
    ),
    session_data: SessionData = Depends(verifier),
    db: Session = Depends(get_db),
):
    return await subscriber_services.i_subscribed(session_data, db)


@router.get(
    "/subscribe/to_me", status_code=status.HTTP_200_OK, dependencies=[Depends(cookie)]
)
async def my_subscribers(
    status: SubcribeStatus | None = None,
    current_user: UserRetrieveScheme = Depends(
        user_services.get_current_is_active_user
    ),
    session_data: SessionData = Depends(verifier),
    db: Session = Depends(get_db),
):
    return await subscriber_services.my_subscribers(session_data, db, status)


@router.put(
    "/subscribe", status_code=status.HTTP_201_CREATED, dependencies=[Depends(cookie)]
)
async def update_subscriber_status(
    nickname: str,
    status: SubcribeStatus | None = None,
    current_user: UserRetrieveScheme = Depends(
        user_services.get_current_is_active_user
    ),
    session_data: SessionData = Depends(verifier),
    db: Session = Depends(get_db),
):
    return await subscriber_services.update_subscriber_status(
        session_data, db, nickname, status
    )


@router.delete(
    "/subscribe/me",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(cookie)],
)
async def delete_i_subscribed(
    nickname: str,
    current_user: UserRetrieveScheme = Depends(
        user_services.get_current_is_active_user
    ),
    session_data: SessionData = Depends(verifier),
    db: Session = Depends(get_db),
):
    return await subscriber_services.delete_i_subscribed(session_data, db, nickname)
