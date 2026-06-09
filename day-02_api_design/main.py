from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {
        "message": "Day 2 API Design"
    }


@app.get('/users/me')
def current_user():
    return{
        'name':'Apurva'
    }

@app.get('/users/{user_id}')
def get_user(user_id: int):
    return{
        'user_id': user_id
    }

@app.get('/users')
def list_users(page: int=1, limit:int = 10):
    return{
        'page': page,
        'limit': limit
    }

@app.get('/courses/{courses_id}')
def get_course(course_id: int):
    return {
        "course_id": course_id
    }


@app.get("/search")
def search(
    q: str,
    page: int = 1
):
    return {
        "query": q,
        "page": page
    }