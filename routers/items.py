from fastapi import APIRouter
from models.Item import Item

router = APIRouter(prefix="/items")

items = []


@router.get("/")
def get_items():
    return {"items": items}


@router.post("/")
def save_item(item: Item):
    items.append(item)
    print(items)
    return {"items": items}
