#________________________________________________________ACCOUNT__________________________________________________________________________________

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database.db import get_db
from schemas.account import AccountBaseScheme, AccountUpdateScheme, AccountRetrieveScheme
from schemas.user import UserRetrieveScheme

from services.user import user_services
from services.account import account_services

router = APIRouter()

# ----------------------------------------------------/api/v1/account----------------------------------------------------------------------------------

@router.post('/account', response_model=AccountBaseScheme, status_code=status.HTTP_201_CREATED)
async def create_account(       schema: AccountBaseScheme,
                                current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user),
                                db: Session = Depends(get_db)):
    return await account_services.create_account(schema, current_user, db)


@router.get('/account', status_code=status.HTTP_200_OK)
async def get_all_accounts(current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user)):
    return await account_services.get_all_accounts(current_user)


@router.get('/account/{nickname}', response_model=AccountRetrieveScheme, status_code=status.HTTP_200_OK)
async def get_specify_account(
                                nickname: str,
                                current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user),
                                db: Session = Depends(get_db)):

    return await account_services.get_account(db, nickname, current_user)


@router.delete('/account/{nickname}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_specify_account(
                                nickname: str,
                                current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user),
                                db: Session = Depends(get_db)):

    return await account_services.delete_account(db, nickname, current_user)


@router.put('/account/{nickname}', response_model=AccountRetrieveScheme, status_code=status.HTTP_200_OK)
async def update_account(
                                nickname: str,
                                schema: AccountUpdateScheme,
                                current_user: UserRetrieveScheme = Depends(user_services.get_current_is_active_user),
                                db: Session = Depends(get_db)):

    return await account_services.update_account(db, nickname, current_user, schema)
