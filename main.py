from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel): # inheritance, implements?
    text: str | None = None
    isDone: bool = True
    def __init__(self, text, isDone = False):
        self.text = text
        self.isDone = isDone

items = []

@app.get("/") # when someone visits "ip_address/"
def root(): 
    return {"Hello": "World"}

@app.post("/items")
def create_item(item: str):
    itemObj = Item("item")
    items.append(itemObj)
    return itemObj

@app.get("/items/{item_id}") # app.X -> http X request
def get_item2(item_id: int) -> Item:
    if item_id < len(items) or item_id > -1:
        return items[item_id]
    else: 
        raise HTTPException(status_code=404, detail="Item {item_id} not found")
    
@app.get("/items")
def get_item(limit: int = 10):
    return items[0:limit]