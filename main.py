from ast import AsyncFunctionDef
from hashlib import algorithms_available
from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: str

inventory = {}

@app.get('/getInventory/{item_id}')
def getItem( item_id : int = Path(None, description="El ID del producto que deseamos seleccionar", gt=0,lt=2)):
    return inventory[item_id]

@app.get('/getByName/')
def getItem(name : str = Query(None, title='mame', description="Nombre del producto")):
    for itemID in inventory:
        if inventory[itemID].name == name:
            return inventory[itemID]
    return {"Data":'No existe'}

@app.post("/createItem/{itemID}")
def create_item(itemID: int, item : Item):
    if itemID in inventory:
        return{"Error: el item ya existe"}

    inventory[itemID] = item

    return inventory[itemID]