# -------------------------------------------------PostServices---------------------------------------------------------------------------------

from datetime import datetime
from fastapi import HTTPException, status

from models.post import Post
from .account import account_services
from models.enum import PostStatus, SubcribeStatus
from models.subscribe import Subscribe
from models.like import Like
from models.enum import LikeStatus


class PostService():

    async def create_post(self, db, schema, session_data):
        data = schema.dict()
        nickname = await account_services.current_nickname(session_data)
        data['account_nickname'] = nickname
        data['created_at'] = datetime.utcnow()
        post = Post(**data)
        db.add(post)
        db.commit()
        db.refresh(post)
        return post


    async def get_all_my_posts(self, session_data, db, status):

        nickname = await account_services.current_nickname(session_data)
        posts = db.query(Post).filter_by(account_nickname = nickname).all()

        post = [{
                'id': post.id,
                'description': post.description,
                'media': post.media,
                'status': post.status,
                'created_at': post.created_at}
                for post in posts if post.status == status or status is None]
        result = f'total: {len(post)}', post
        return result

    async def get_post(self, session_data, db, id):

        nickname = await account_services.current_nickname(session_data)
        post = db.query(Post).filter_by(account_nickname = nickname, id=id).first()

        post = {
                'id': post.id,
                'description': post.description,
                'media': post.media,
                'status': post.status,
                'created_at': post.created_at}

        return post

    async def delete_post(self, session_data, db, id):
        nickname = await account_services.current_nickname(session_data)
        specify_post = db.query(Post).filter_by(account_nickname = nickname, id=id).first()
        if specify_post is not None:
            db.delete(specify_post)
            db.commit()
            raise HTTPException(status_code=status.HTTP_200_OK, detail=f'Post:{id} was deleted successfully')
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Post:{id} was not found')

    async def update_post(self, db, session_data, schema, id):
        data = schema.dict()
        nickname = await account_services.current_nickname(session_data)
        specify_post = db.query(Post).filter_by(account_nickname=nickname, id=id).first()
        for key, value in data.items():
            setattr(specify_post, key, value)
        specify_post.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(specify_post)
        return specify_post


    async def get_all_posts(self, session_data, db):

        me = await account_services.current_nickname(session_data)
        subscribers = db.query(Subscribe).filter_by(account_nickname=me, status=SubcribeStatus.OK).all()
        all_posts = [db.query(Post).filter_by(account_nickname=post.subscriber, status=PostStatus.VISIBLE).all() for post in subscribers]
        result = [{
                    'id': post.id, 
                    'description': post.description, 
                    'media:': post.media, 
                    'likes': db.query(Like).filter_by(post_id=post.id, status=LikeStatus.LIKE).count(), 
                    'dislikes': db.query(Like).filter_by(post_id=post.id, status=LikeStatus.DISLIKE).count()
                    } for posts in all_posts for post in posts]
        result = f'total: {len(result)}', result
        return result


post_services = PostService()
