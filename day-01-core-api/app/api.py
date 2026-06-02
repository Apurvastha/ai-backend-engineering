from fastapi import APIRouter
from app.schemas import EchoRequest

router = APIRouter()


@router.get("/")
def health_check():
    return {
        "status": 'ok',
        'message': 'AI Backend Service is running'
    }

@router.post('/echo')
def echo(data: EchoRequest):
    return{
        'input': data.text,
        'length': len(data.text),
        'status': 'processed'
    }

@router.get('/tasks')
def list_task(limit: int=10):
    return {
        'limit': limit
    }

@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    return{
        'task_id': task_id
    }



@router.get('/products')
def get_user(category: str):
    return{
        'category': category
    }

@router.get('/products/{product_id}')
def product_list(product_id: int, category:str):
    return{
        'product_id':product_id,
        'category': category
    }
