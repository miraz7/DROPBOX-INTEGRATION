from typing import Any, Dict
from fastapi import APIRouter ,Request
from fastapi import APIRouter, Depends, status

from . import views
from . import schemas
from core.database import get_db
from sqlalchemy.orm import Session


router = APIRouter( 
    prefix="/api/v1/dropbox",
    tags=["auth"],
    responses={404: {"description": "Module Not Fount"}},
)



@router.get('/auth', tags=["all"], status_code=status.HTTP_200_OK)
def auth_start_with_dropbox(request: Request):
    return views.start_auth_with_dropbox(request)
 

@router.get('/code', tags=["all"], status_code=status.HTTP_200_OK)
def dropbox_code(request: Request):
    return views.dropbox_code(request)


@router.get('/success', tags=["all"], status_code=status.HTTP_200_OK)
def drop_box_success(request: Request):
    query_params =  request.query_params
    return views.drop_box_success(query_params)

drop_box_route = router