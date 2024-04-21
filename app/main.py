from fastapi import FastAPI

#initialize FastAPI

app = FastAPI()

@app.get("/ok")
async def get_ok():
    return {"message":"hellow world"}

@app.get("/name")
async def get_name(name: str = 'Ramesh'):
    return {"message":name}

@app.post("/order")
async def place_order(product_name:str, price:int):
    return {"message":f"{product_name} is {price} rupees"}