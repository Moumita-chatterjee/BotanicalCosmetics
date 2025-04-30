from fastapi import FastAPI
from model.Botanical import Botanical

app = FastAPI()

list_of_product =[]

@app.post("/item/create")
async def create_product(botanical: Botanical):
    for items in list_of_product:
        if botanical.product_id == Botanical.product_id:
            raise ValueError(f"Item '{botanical.product_id}' already exist. Unable to create a new product")
    list_of_product.append(botanical)
    return "Product added successfully"





