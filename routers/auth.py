from email.policy import default

from fastapi import APIRouter


router = APIRouter()

@router.get("/get_user")
async def get_user():
    return {"message": "User data retrieved successfully"}


