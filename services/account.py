# -------------------------------------------------AccountServices---------------------------------------------------------------------------------
import datetime
from fastapi import HTTPException, status

from models.account import Account
from models.post import Post
from models.enum import PostStatus

class AccountService():

    COUNTER = 3

    async def create_account(self, schema, current_user, db):
        data = schema.dict()
        data['nickname'] = data['nickname'].lower()
        if current_user.account != []:
            if len(current_user.account) < AccountService.COUNTER:
                for user in current_user.account:
                    if user.nickname == data['nickname']:
                        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='nickname already exists')
            else: 
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='limit accounts')
        data['user_id'] = current_user.id
        data['created_at'] = datetime.datetime.utcnow()
        account = Account(**data)
        db.add(account)
        db.commit()
        db.refresh(account)
        return account


    async def get_account(self, db, session_data, current_user):
        nickname = await self.current_nickname(session_data)
        account = db.query(Account).filter_by(user_id=current_user.id, nickname=nickname).first()
        return account


    async def update_account(self, db, session_data, current_user, schema):
        data = schema.dict()
        account = await self.get_account(db, session_data, current_user)
        for key, value in data.items():
            setattr(account, key, value)
        account.updated_at = datetime.datetime.utcnow()
        db.commit()
        db.refresh(account)
        return account

    async def delete_account(self, db, session_data, current_user):
        specify_account = await self.get_account(db, session_data, current_user)
        nickname = await self.current_nickname(session_data)
        db.delete(specify_account)
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail=f'{nickname} account was deleted successfully')


    async def get_all_accounts(self, current_user):
        if current_user.account != []:
            account = [{'nickname': data.nickname,
                        'avatar': data.avatar,
                        'description': data.description} 
                        for data in current_user.account]
            return account
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Please create account')

    @staticmethod
    async def current_nickname(session_data):
        data = session_data.dict()
        nickname = data['nickname']
        return nickname


    async def get_account_with_post(self, nickname, current_user, session_data, db):
        
        nickname = nickname.lower()

        result = []
        data = db.query(Account).all()
        for account in data:
            if account.nickname.startswith(nickname):

                post_in_db = db.query(Post).filter_by(account_nickname=account.nickname, status=PostStatus.VISIBLE).all()

                posts = [  {'id': post.id,
                            'description': post.description,
                            'media': post.media,
                            'status': post.status,
                            'created_at': post.created_at} 
                            for post in post_in_db]

                account = [{   
                    'nickname': account.nickname,
                    'avatar': account.avatar,
                    'description': account.description,
                    'posts': [posts]}]

                result.append(account)

        return result



account_services = AccountService()
