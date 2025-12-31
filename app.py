from fastapi import FastAPI, Form
from typing import Optional

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
 <html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Регистрация</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0;
        }

        .register-container {
            background: white;
            padding: 40px 30px;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
            text-align: center;
        }

        h2 {
            margin-bottom: 30px;
            color: #333;
            font-weight: 600;
        }

        .form-group {
            margin-bottom: 20px;
            text-align: left;
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #555;
            font-size: 14px;
            font-weight: 500;
        }

        input[type="email"],
        input[type="password"] {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
            box-sizing: border-box;
            transition: border 0.3s ease;
        }

        input[type="email"]:focus,
        input[type="password"]:focus {
            outline: none;
            border-color: #6e8efb;
            box-shadow: 0 0 0 3px rgba(110, 142, 251, 0.2);
        }

        button {
            width: 100%;
            padding: 14px;
            background: #6e8efb;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.3s ease;
        }

        button:hover {
            background: #5a78f0;
        }

        .footer-text {
            margin-top: 20px;
            font-size: 14px;
            color: #888;
        }

        .footer-text a {
            color: #6e8efb;
            text-decoration: none;
        }

        .footer-text a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <script src="https://www.google.com/recaptcha/api.js"></script>

     <script>
        function onSubmit(token) {
            document.getElementById("demo-form").submit();
        }
    </script>

    <div class="register-container">
        <h2>Регистрация</h2>
        <form action="/login" id="demo-form" method="POST">
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" placeholder="Введите ваш email" required>
            </div>

            <div class="form-group">
                <label for="password">Пароль</label>
                <input type="password" id="password" name="password" placeholder="Придумайте пароль" required minlength="6">
            </div>

            <button class="g-recaptcha" data-sitekey="6LfGRTwsAAAAAPGqE5u8hW-DnWPkp0wYzGwy2llu" data-callback='onSubmit' data-action='submit'>Submit</button>

        </form>

        <p class="footer-text">
            Уже есть аккаунт? <a href="#">Войти</a>
        </p>
    </div>
    <!--<script src="https://www.google.com/recaptcha/api.js?render=6LfGRTwsAAAAAPGqE5u8hW-DnWPkp0wYzGwy2llu"></script>-->
</body>
</html>
    """
    return html_content

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
