from operator import gt
from fastapi import FastAPI, Path

app = FastAPI()

inventory = {
    
    1:{
        'name': "Leche",
        'precio': '150',
        'marca': 'serenisima'
    },
    2:{
        'name': "YerbaMate",
        'precio': '350',
        'marca': 'Taragui'
    }
}

@app.get('/getInventory/{item_id}')
def getItem( item_id : int = Path(None, description="El ID del producto que deseamos seleccionar", gt=0,lt=2)):
    return inventory[item_id]

@app.get('/getByName')
def getItem( name : str):
    for itemID in inventory:
        if inventory[itemID]['name'] == name:
            return inventory[itemID]
    return {"Data":'No existe'}
