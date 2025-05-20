
from fastapi import FastAPI, __version__
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import Sendpush as sp

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

class Item(BaseModel):
   token: str
   time: int
   
@app.post("/token/")
async def create_token(item: Item):
  
    sp.send_data(item.token, item.time)
    return {"token":  item}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/send')
async def hello():
    return {'res': 'send page'}