# -------------------------------------------------LikeServices---------------------------------------------------------------------------------

from datetime import datetime
from fastapi import HTTPException, status

from models.like import Like
from .account import account_services
from models.subscribe import Subscribe
from models.post import Post
from models.enum import SubcribeStatus, PostStatus


class LikeService():

    async def create_like(self, db, session_data, post, like_status):
        me = await account_services.current_nickname(session_data)
        
        post_in_db = db.query(Post).filter_by(id=post).first()
        if post_in_db is not None and post_in_db.status == PostStatus.VISIBLE:

            subscriber = db.query(Subscribe).filter_by(account_nickname=me, subscriber=post_in_db.account_nickname).first()
            if subscriber is not None and subscriber.status == SubcribeStatus.OK:

                like = db.query(Like).filter_by(account_nickname=me, post_id=post).first()
                if like is None:
                    like = Like(account_nickname=me, post_id=post, created_at=datetime.utcnow(), status=like_status)
                    db.add(like)
                    db.commit()
                    db.refresh(like)
                    return like
                else:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Your like already exists')
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='You have no rights to add like')
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Post {post} does not exists')


    async def delete_like(self, db, session_data, post):
        me = await account_services.current_nickname(session_data)
        like = db.query(Like).filter_by(account_nickname=me, post_id=post).first()
        if like is not None:
            db.delete(like)
            db.commit()
            raise HTTPException(status_code=status.HTTP_200_OK, detail=f'Like for post:{post} was deleted successfully')
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Post:{post} was not found')


like_services = LikeService()

