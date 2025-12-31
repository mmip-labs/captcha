from fastapi import FastAPI, Form
from typing import Optional

app = FastAPI()

@app.post("/login")
async def login(
    email: str,
    password: str,
    g_recaptcha_response: Optional[str] = Form(None)
):
    """
    Эндпоинт для обработки POST-запроса с данными формы.
    Возвращает полученные значения.
    """
    return {
        "email": email,
        "password": password,
        "g-recaptcha-response": g_recaptcha_response
    }
