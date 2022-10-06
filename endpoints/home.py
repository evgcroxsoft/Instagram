# ________________________________________________________HOME__________________________________________________________________________________

from fastapi import APIRouter, Depends, status
from fastapi_pagination import Page, Params, paginate
from sqlalchemy.orm import Session

from database.db import get_db
from schemas.post import PostPaginationScheme
from schemas.session import SessionData
from schemas.user import UserRetrieveScheme
from security.session import cookie, verifier
from services.post import post_services
from services.user import user_services

router = APIRouter()


# -----------------------------------------------------/api/v1/home---------------------------------------------------------------------------------


@router.get(
    "/home",
    response_model=Page[PostPaginationScheme],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(cookie)],
)
async def get_all_my_posts(
    params: Params = Depends(),
    current_user: UserRetrieveScheme = Depends(
        user_services.get_current_is_active_user
    ),
    session_data: SessionData = Depends(verifier),
    db: Session = Depends(get_db),
):
    return paginate(await post_services.get_all_posts(session_data, db), params)
