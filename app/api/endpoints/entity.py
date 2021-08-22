from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException

from app import models, schemas

router = APIRouter()

ENTITY = {}

@router.get("/") #, response_model=List[schemas.])
def read_entities() -> Any:
    """
    Retrieve items.
    """
    print("read list")
    pass


@router.post("/", response_model=schemas.EntityCreate)
def create_entity() -> Any:
    """
    Create new item.
    """
    print("create item")
    pass


@router.put("/{id}") #, response_model=schemas.Item)
def update_item() -> Any:
    """
    Update an item.
    """
    print("update_item")
    pass


@router.get("/{id}") #, response_model=schemas.Item)
def read_item() -> Any:
    """
    Get item by ID.
    """
    print("read item")
    pass


@router.delete("/{id}") # , response_model=schemas.Item)
def delete_item() -> Any:
    """
    Delete an item.
    """
    print("delete item")
    pass