from pydantic import BaseModel

class EchoRequest(BaseModel):
    text: str