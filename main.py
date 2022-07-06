from fastapi import FastAPI

app = FastAPI()

inventory = {
    
    1:{
        'name': "Leche",
        'precio': '150',
        'marca': 'serenisima'
    }
}

@app.get('/getInventory/{item_id}')
def getItem( item_id : int):
    return inventory[item_id]
