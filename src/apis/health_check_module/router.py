from typing import Any, Dict
from fastapi import APIRouter
from fastapi import APIRouter, Depends, status

router = APIRouter(
    prefix="/heath-check",
    tags=["auth"],
    responses={404: {"description": "Module Not Fount"}},
)

@router.get('/', tags=["all"], status_code=status.HTTP_200_OK)
def heath_check(url_params):
    return   {'data' : "health is okay "}


health_check_router = router