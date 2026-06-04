from fastapi import FastAPI
from schemas import UserCreate, UserResponse, ProductCreate
from models import users_db, products_db

app = FastAPI()


@app.post('/users', response_model=UserResponse)
def create_user(user: UserCreate):
    new_user = {
        'id': len(users_db) + 1,
        'name': user.name,
        'email': user.email
    }
    users_db.append(new_user)
    return new_user


@app.post('/products')
def create_product(product: ProductCreate):
    new_product = {
        'id': len(products_db) + 1,
        'name': product.name,
        'price': product.price,
        'stock': product.stock
    }
    products_db.append(new_product)
    return new_product