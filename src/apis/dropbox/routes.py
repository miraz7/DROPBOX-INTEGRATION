from typing import Any, Dict
from fastapi import APIRouter ,Request,  File, UploadFile
from fastapi import  Depends, status

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



@router.post('/upload-dropbox-profile-picture/{id}', tags=["all"], status_code=status.HTTP_200_OK)
async def update_dropbox_profile_pic(id : str ,request: Request , file: UploadFile = File(...)):
    
    file_content  = await file.read()
    
    # print(file_content)
    
    return views.update_dropbox_profile_pic(id , file_content )


@router.post('/upload-file-to-dropbox/{id}', tags=["all"], status_code=status.HTTP_200_OK)
async def upload_file_to_dropbox(id : str ,request: Request , file: UploadFile = File(...)):
    
    file_content  = await file.read()
    
    # print(file_content)
    
    return views.upload_file_to_dropbox(id , file_content )








drop_box_route = router