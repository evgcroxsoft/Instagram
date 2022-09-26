#________________________________________________________SESSION__________________________________________________________________________________

from fastapi import APIRouter, Depends, Response
from uuid import UUID

from services.session import session_services, cookie
from services.user import user_services

router = APIRouter()

# --------------------------------------------------/api/v1/session---------------------------------------------------------------------------------

@router.post("/activate_session")
async def create_session(nickname: str, response: Response, current_user = Depends(user_services.get_current_is_active_user)):
    return await session_services.create_session(nickname, response, current_user)

@router.post("/delete_session")
async def del_session(response: Response, session_id: UUID = Depends(cookie)):
    return await session_services.del_session(response, session_id)