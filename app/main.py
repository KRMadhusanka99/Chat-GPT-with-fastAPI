from fastapi import FastAPI
from pydantic import BaseModel

#initialize FastAPI

app = FastAPI()

# define a data model for the request body

class Product(BaseModel):
    name: str
    price: int


@app.get("/ok")
async def get_ok():
    return {"message":"hellow world"}

@app.get("/name")
async def get_name(name: str = 'Ramesh'):
    return {"message":name}

@app.post("/order")
async def place_order(product_name:str, price:int):
    return {"message":f"{product_name} is {price} rupees"}

@app.post("/oder_pydentic")
async def place_order(product: Product):
    return {"message":f"{product.name} is {product.price} rupees"}