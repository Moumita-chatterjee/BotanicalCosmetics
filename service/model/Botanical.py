'''
Objective - Project for adding products, deleting products,adding sales and
printing details of each product.
Created by: Moumita
Date: 27-04-2025
'''

from pydantic import BaseModel

class Botanical(BaseModel):
    product_id : int
    product_catagory : str
    quantity : int



