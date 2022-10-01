# -------------------------------------------------SubscribeServices---------------------------------------------------------------------------------
from fastapi import HTTPException, status
from datetime import datetime
from endpoints import subscribe
from models.subscribe import Subscribe
from .account import account_services
from models.account import Account

class SubscriberService():

    async def create_subscribe(self, session_data, db, nickname: str) -> subscribe:

        nickname = nickname.lower()
        if await self.is_nickname_exist(db, nickname) is True:
            if await self.is_subscribe_exist(db, session_data, nickname) is False:
                subscribe = Subscribe(
                                        account_nickname = await account_services.current_nickname(session_data),
                                        subscriber = nickname,
                                        created_at = datetime.utcnow())
                db.add(subscribe)
                db.commit()
                db.refresh(subscribe)
                return subscribe
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= 'You have already sent request before')


    async def i_subscribed(self, session_data, db):

        nickname = await account_services.current_nickname(session_data)
        subscribers = db.query(Account, Subscribe).join(Subscribe).filter_by(account_nickname=nickname).all()
        result = [{
                    'subscriber': subcriber.subscriber,
                    'avatar': account.avatar,
                    'decription': account.description,
                    'status:': subcriber.status
                    } for account, subcriber in subscribers]

        return result

    
    async def my_subscribers(self, session_data, db, status):

        nickname = await account_services.current_nickname(session_data)
        subscribers = db.query(Account, Subscribe).join(Subscribe).filter_by(subscriber=nickname).all()
        
        result = [{
                    'nickname': subscriber.account_nickname,
                    'avatar': account.avatar,
                    'description': account.description,
                    'status:': subscriber.status
                    } for account, subscriber in subscribers if subscriber.status == status or status is None]      

        return result


    async def update_subscriber_status(self, session_data, db, nickname, status):

        nickname = nickname.lower()

        me = await account_services.current_nickname(session_data)
        if (await self.is_nickname_exist(db, nickname) is True and await self.is_subscribe_exist(db, session_data, nickname) is False):
            subscriber = db.query(Subscribe).filter_by(subscriber = me, account_nickname=nickname).first()           
            subscriber.status = status 
            subscriber.updated_at = datetime.utcnow()

            db.commit()
            db.refresh(subscriber)
            
            result = {
                       'nickname': subscriber.account_nickname,
                       'status:': subscriber.status,
                       'updated_at:': subscriber.updated_at
                    }
 
            return result


    async def delete_i_subscribed(self, session_data, db, nickname):

        me = await account_services.current_nickname(session_data)
        subscriber = db.query(Subscribe).filter_by(account_nickname=me, subscriber=nickname).first()
        if subscriber is not None:
            db.delete(subscriber)
            db.commit()
            raise HTTPException(status_code=status.HTTP_200_OK, detail=f'Subscriber:{nickname} was deleted successfully')
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Subscriber:{nickname} was not found')


    async def is_nickname_exist(self, db, nickname: str)-> bool:
        data = db.query(Account).all()
        for account in data:
            if account.nickname == nickname:
                return True
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= f"Please check! {nickname} doesn't exists")


    async def is_subscribe_exist(self, db, session_data, nickname: str) -> bool:

        me = await account_services.current_nickname(session_data)
        if db.query(Subscribe).filter_by(account_nickname=me, subscriber=nickname).first() is not None:
            return True
        else:
            return False    


subscriber_services = SubscriberService()