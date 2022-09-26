# -------------------------------------------------SessionServices---------------------------------------------------------------------------------

from uuid import uuid4
from fastapi import HTTPException, status

from schemas.session import SessionData
from security.session import cookie, backend

class SessionService():

    async def create_session(self, nickname, response, current_user):

        # check is the nickname is in db
        for user in current_user.account:
            if nickname == user.nickname:
        
                session = uuid4()
                data = SessionData(nickname=nickname)

                await backend.create(session, data)
                cookie.attach_to_response(response, session)

                return f"created session for {nickname}"
        else: 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='wrong nickname')


    async def del_session(self, response, session_id):
        await backend.delete(session_id)
        cookie.delete_from_response(response)
        return "deleted session"


session_services = SessionService()