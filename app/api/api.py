from fastapi import APIRouter

from app.api.endpoints import entity

api_router = APIRouter()
api_router.include_router(entity.router, prefix="/entity", tags=["entity"])