from fastapi import FastAPI
import uvicorn

from endpoints import account, home, like, me, post, search, session, subscribe, token, chat
from database.db import Base, engine

app = FastAPI(
        version=1,
        title='Instagram',
        description='DEVELOPED BY YEVHENII')

app.include_router(token.router, prefix='/api/v1', tags=["Token"])
app.include_router(session.router, prefix='/api/v1', tags=["Session"])
app.include_router(home.router, prefix='/api/v1', tags=["Home"])
app.include_router(me.router, prefix='/api/v1', tags=["User"])
app.include_router(account.router, prefix='/api/v1', tags=["Account"])
app.include_router(post.router, prefix='/api/v1', tags=["Post"])
app.include_router(search.router, prefix='/api/v1', tags=["Search"])
app.include_router(subscribe.router, prefix='/api/v1', tags=["Subscribe"])
app.include_router(like.router, prefix='/api/v1', tags=["Like"])
app.include_router(chat.router, prefix='/api/v1', tags=["Chat"])

if __name__ == "__main__":
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)

#create all tables
Base.metadata.create_all(bind=engine)