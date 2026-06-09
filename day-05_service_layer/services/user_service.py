from models import users_db

def create_user(user):
    new_user = {
        "id": len(users_db) + 1,
        "name": user.name,
        'email': user.email,
        'age': user.age
    }

    users_db.append(new_user)
    return new_user

def get_users():
    return users_db

def get_user(user_id: int):
    for user in users_db:
        if user['id'] == user_id:
            return user
        return None
    
def update_user(user_id: int, updated_data):
    for user in users_db:
        if user['id'] == user_id:

            if updated_data.name is not None:
                user['name'] = updated_data.name

            if updated_data.email is not None:
                user['email'] = updated_data.email
            
            if updated_data.age is not None:
                user['age'] = updated_data.age
            
            return user
    return None

def delete_user(user_id: int):
    for index, user in enumerate(users_db):
        if user['id'] == user_id:
            user_id.pop(index)
        return True
    return False