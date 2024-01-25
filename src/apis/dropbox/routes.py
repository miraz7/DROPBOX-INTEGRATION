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


@router.get('/get-app-all-users', tags=["all"], status_code=status.HTTP_200_OK)
def get_app_all_users(request: Request):
    return views.get_app_all_users()


@router.get('/get-single-user/{id}', tags=["all"], status_code=status.HTTP_200_OK)
def get_app_all_users(id : str ,request: Request):
    return views.get_user_details(id)


@router.get('/get-dropbox-user-detils/{id}', tags=["all"], status_code=status.HTTP_200_OK)
def get_app_all_users(id : str ,request: Request):
    return views.get_dropbox_user_details(id)









drop_box_route = router