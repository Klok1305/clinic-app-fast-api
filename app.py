import sqlite3
from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from werkzeug.security import generate_password_hash
import mylibrary
import uvicorn

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key='secret_key')

templates = Jinja2Templates(directory="templates")


@app.get("/admin-login", response_class=HTMLResponse)
async def admin_login_get(request: Request):
    return templates.TemplateResponse("admin_login.html", {"request": request, "error": None})


@app.post("/admin-login", response_class=HTMLResponse)
async def admin_login_post(request: Request, username: str = Form(...), password: str = Form(...)):
    if mylibrary.authenticate_admin(username, password):
        request.session['admin'] = True
        return RedirectResponse(url="/admin-panel", status_code=status.HTTP_302_FOUND)
    return templates.TemplateResponse("admin_login.html", {"request": request, "error": "Invalid username or password"})


@app.get("/admin-panel", response_class=HTMLResponse)
async def admin_panel(request: Request):
    if request.session.get('admin'):
        appointment_columns = mylibrary.get_table_columns('appointments')
        analysis_columns = mylibrary.get_table_columns('analyses')
        past_appointment_columns = mylibrary.get_table_columns('past_appointments')
        survey_columns = mylibrary.get_table_columns('surveys')

        appointments_data = mylibrary.get_appointments_data()
        analyses_data = mylibrary.get_analyses_data()
        past_appointments_data = mylibrary.get_past_appointments_data()
        surveys_data = mylibrary.get_surveys_data()

        context = {
            "request": request,
            "appointments": appointments_data,
            "analyses": analyses_data,
            "past_appointments": past_appointments_data,
            "surveys": surveys_data,
            "appointment_columns": appointment_columns,
            "analysis_columns": analysis_columns,
            "past_appointment_columns": past_appointment_columns,
            "survey_columns": survey_columns,
        }
        return templates.TemplateResponse("admin_panel.html", context)
    return RedirectResponse(url="/admin-login", status_code=status.HTTP_302_FOUND)


@app.get("/register", response_class=HTMLResponse)
async def register_get(request: Request):
    return templates.TemplateResponse("register.html", {"request": request, "error": None})


@app.post("/register", response_class=HTMLResponse)
async def register_post(request: Request, username: str = Form(...), password: str = Form(...)):
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Login FROM users WHERE Login = ?", (username,))
    existing_user = cursor.fetchone()
    if existing_user:
        conn.close()
        return templates.TemplateResponse("register.html", {"request": request, "error": "Пользователь с таким именем уже существует"})

    password_hash = generate_password_hash(password)
    cursor.execute("INSERT INTO users (Login, PasswordHash) VALUES (?, ?)", (username, password_hash))
    conn.commit()
    conn.close()
    return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    if request.session.get('username'):
        return RedirectResponse(url="/profile", status_code=status.HTTP_302_FOUND)
    return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)


@app.get("/login", response_class=HTMLResponse)
async def login_get(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": None})


@app.post("/login", response_class=HTMLResponse)
async def login_post(request: Request, username: str = Form(...), password: str = Form(...)):
    if mylibrary.authenticate(username, password):
        request.session['username'] = username
        return RedirectResponse(url="/profile", status_code=status.HTTP_302_FOUND)
    return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid username or password"})


@app.post("/logout")
async def logout(request: Request):
    request.session.pop('username', None)
    return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)


@app.get("/profile", response_class=HTMLResponse)
async def profile(request: Request):
    username = request.session.get('username')
    if not username:
        return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)
    mylibrary.update_fake_database(username)
    user_data = mylibrary.get_data_for_user(username)
    next_appointment = mylibrary.get_next_appointment(username)
    context = {
        "request": request,
        "username": username,
        "user_data": user_data,
        "next_appointment": next_appointment,
    }
    return templates.TemplateResponse("profile.html", context)


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
