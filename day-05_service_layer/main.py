from fastapi import FastAPI, HTTPException

from schemas import UserCreate, UserUpdate, UserResponse
from services.user_service import (
    create_user,
    get_users,
    get_user,
    update_user,
    delete_user
)

app = FastAPI()

@app.post('/users', response_model=UserResponse)
def create(user: UserCreate):
    return create_user(user)

@app.get("/users")
def read_users():
    return get_users()

@app.get('/users/{user_id}')
def read_user(user_id: int):
    user = get_user(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put('/users/{user_id}')
def update(user_id: int, updated_data: UserUpdate):
    user = update_user(user_id, updated_data)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        'message': "User Updated.",
        'user': user
    }

@app.delete("/users/{user_id}")
def delete(user_id: int):
    success = delete_user(user_id)

    if not success:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted"}