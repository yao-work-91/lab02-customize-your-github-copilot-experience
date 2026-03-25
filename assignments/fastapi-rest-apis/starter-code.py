"""Starter code for the FastAPI REST API assignment."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI Assignment API")


class Item(BaseModel):
    """Data model for an API item."""

    name: str
    description: str


# In-memory storage for assignment practice (no database required).
items: dict[int, Item] = {}


@app.get("/")
def root() -> dict[str, str]:
    """Health check endpoint."""

    return {"message": "FastAPI assignment is running"}


# TODO: Implement GET /items to return all items.
# TODO: Implement POST /items to create an item.
# TODO: Implement GET /items/{item_id} to return one item.
# TODO: Implement PUT /items/{item_id} to update an item.
# TODO: Implement DELETE /items/{item_id} to delete an item.


def get_item_or_404(item_id: int) -> Item:
    """Helper function to fetch an item or raise 404."""

    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
