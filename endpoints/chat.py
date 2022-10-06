import asyncio

from fastapi import APIRouter, Depends
from pywebio import start_server
from pywebio.input import actions, input, input_group
from pywebio.output import output, put_buttons, put_markdown, put_scrollable
from pywebio.session import run_js

from schemas.session import SessionData
from security.session import cookie, verifier
from services.account import account_services

router = APIRouter()

chat_msgs = []


@router.get("/chat", dependencies=[Depends(cookie)])
async def chat(session_data: SessionData = Depends(verifier)):

    nickname = await account_services.current_nickname(session_data)

    async def main():
        global chat_msgs

        put_markdown("## 🧊 Instagram!\nChat!")

        msg_box = output()
        put_scrollable(msg_box, height=300, keep_bottom=True)

        chat_msgs.append(("📢", f"`{nickname}` присоединился к чату!"))
        msg_box.append(put_markdown(f"📢 `{nickname}` присоединился к чату"))

        refresh_task = refresh_msg(nickname, msg_box)

        while True:
            data = input_group(
                "💭 Новое сообщение",
                [
                    input(placeholder="Текст сообщения ...", name="msg"),
                    actions(
                        name="cmd",
                        buttons=[
                            "Отправить",
                            {"label": "Выйти из чата", "type": "cancel"},
                        ],
                    ),
                ],
                validate=lambda m: ("msg", "Введите текст сообщения!")
                if m["cmd"] == "Отправить" and not m["msg"]
                else None,
            )

            if data is None:
                break

            msg_box.append(put_markdown(f"`{nickname}`: {data['msg']}"))
            chat_msgs.append((nickname, data["msg"]))

        refresh_task.close()

        put_buttons(
            ["Перезайти"], onclick=lambda btn: run_js("window.location.reload()")
        )

    async def refresh_msg(nickname, msg_box):
        global chat_msgs
        last_idx = len(chat_msgs)

        while True:
            await asyncio.sleep(1)

            for m in chat_msgs[last_idx:]:
                if m[0] != nickname:  # if not a message from current user
                    msg_box.append(put_markdown(f"`{m[0]}`: {m[1]}"))

    await main()


if __name__ == "__main__":
    start_server(chat.main, debug=True, port=8080, cdn=False)
