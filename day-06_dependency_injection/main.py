from fastapi import FastAPI, Depends
from dependencies import get_message, get_current_user, get_db, get_company_name, get_server_info

app = FastAPI()

@app.get("/")
def home(message: str = Depends(get_message)):
    return{
        "message": message
    }

@app.get("/me")
def profile(
    current_user = Depends(get_current_user)
):
    return current_user

@app.get("/dashboard")
def dashboard(
    db = Depends(get_db),
    user = Depends(get_current_user)
):
    return {
        "db": db,
        "user": user
    }

@app.get('/company')
def company(company = Depends(get_company_name)):
    return{
        "company": company
    }

@app.get("/system")
def system(info = Depends(get_server_info)):
    return info