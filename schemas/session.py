#________________________________________________________SESSION SCHEMAS__________________________________________________________________________________

from pydantic import BaseModel

class SessionData(BaseModel):
    nickname: str