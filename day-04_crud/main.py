from fastapi import FastAPI, HTTPException
from schemas import UserCreate, UserResponse, UserUpdate
from models import users_db

app = FastAPI()


@app.post('/users', response_model=UserResponse)
def create_user(user: UserCreate):
    new_user = {
        'id': len(users_db) + 1,
        'name': user.name,
        'email': user.email,
        'age:': user.age
    }
    users_db.append(new_user)
    return new_user

@app.get('/users')
def get_users():
    return users_db

@app.get('/users/{user_id}')
def get_user(user_id: int):
    
    for user in users_db:
        if user['id'] == user_id:
            return user
    raise HTTPException(status_code=404, detail='User not found')


@app.put('/users/{user_id}')
def update_user(user_id: int, updated_data: UserUpdate):

    for user in users_db:
        if user['id'] == user_id:

            if updated_data.name is not None:
                user['name'] = updated_data.name

            if updated_data.email is not None:
                user['email'] = updated_data.email

            if updated_data.age is not None:
                user['age'] = updated_data.age

            return{
                'message': 'User updated',
                'user': user
            }
    raise HTTPException(status_code=404, detail='User not found')


@app.delete('/users/{user_id}')
def delete_user(user_id: int):

    for index, user in enumerate(users_db):
        if user['id']== user_id:
            users_db.pop(index)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
