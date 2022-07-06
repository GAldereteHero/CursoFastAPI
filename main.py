from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return{'data':'Test'}

@app.get('/about')
def about():
    return {'data':'About'}