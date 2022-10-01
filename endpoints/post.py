#________________________________________________________POST__________________________________________________________________________________

from fastapi import APIRouter, Depends, status, BackgroundTasks
from sqlalchemy.orm import Session

from database.db import get_db
from models.enum import PostStatus
from schemas.post import PostBaseScheme
from schemas.user import UserRetrieveScheme
from schemas.session import SessionData
from security.session import cookie, verifier
from services.post import post_services
from services.user import user_services

router = APIRouter()

# ----------------------------------------------------/api/v1/post----------------------------------------------------------------------------------

@router.post('/post', response_model=PostBaseScheme, status_code=status.HTTP_201_CREATED, dependencies=[Depends(cookie)])
async def create_post(  schema: PostBaseScheme,
                        current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user),
                        session_data: SessionData = Depends(verifier),
                        db: Session = Depends(get_db)):

    return await post_services.create_post(db, schema, session_data)


@router.get('/post', status_code=status.HTTP_200_OK, dependencies=[Depends(cookie)])
async def get_all_my_posts(status: PostStatus | None = None, 
                        current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user),
                        session_data: SessionData = Depends(verifier),
                        db: Session = Depends(get_db)):
    return await post_services.get_all_my_posts(session_data, db, status)


@router.get('/post/{id}', status_code=status.HTTP_200_OK, dependencies=[Depends(cookie)])
async def get_specify_post(
                        id: int,
                        current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user),
                        session_data: SessionData = Depends(verifier),
                        db: Session = Depends(get_db)):
    return await post_services.get_post(session_data, db, id)


@router.delete('/post/{id}', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(cookie)])
async def delete_specify_post(
                        id: int,
                        current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user),
                        session_data: SessionData = Depends(verifier),
                        db: Session = Depends(get_db)):
    return await post_services.delete_post(session_data, db, id)


@router.put('/post/{id}', response_model=PostBaseScheme, status_code=status.HTTP_200_OK, dependencies=[Depends(cookie)])
async def update_post(
                        id: int,
                        schema: PostBaseScheme,
                        current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user),
                        session_data: SessionData = Depends(verifier),
                        db: Session = Depends(get_db)):

    return await post_services.update_post(db, session_data, schema, id)
