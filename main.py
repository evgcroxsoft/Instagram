from fastapi import FastAPI
import uvicorn

from endpoints import token, me, account

from database.db import Base, engine

app = FastAPI(
        version=1,
        title='Instagram',
        description='DEVELOPED BY YEVHENII')

app.include_router(token.router, prefix='/api/v1', tags=["Token"])
app.include_router(me.router, prefix='/api/v1', tags=["User"])
app.include_router(account.router, prefix='/api/v1', tags=["Account"])



if __name__ == "__main__":
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)


Base.metadata.create_all(bind=engine)