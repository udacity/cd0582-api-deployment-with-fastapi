from fastapi import FastAPI
# Import Union since our Item object will have tags that can be strings or a list.
from typing import Union
# BaseModel from Pydantic is used to define data objects.
from pydantic import BaseModel


# Declare the data object with its components and their type.
class TaggedItem(BaseModel):
    name: str
    tags: Union[str, list]
    item_id: int

# Save items from POST method in the memory
items = {}

# Initialize FastAPI instance
app = FastAPI()


# This allows sending of data (our TaggedItem) via POST to the API.
@app.post("/items/")
async def create_item(item: TaggedItem):
    items[item.item_id] = item
    return item


# A GET that in this case just returns the item_id we pass,
# but a future iteration may link the item_id here to the one we defined in our TaggedItem.
@app.get("/items/{item_id}")
async def get_items(item_id: int, count: int = 1):
    try:
        item = items[item_id]
    except:
        return "Item not found."

    return {"fetch": f"Fetched: {item.name} with qty of {count}"}

