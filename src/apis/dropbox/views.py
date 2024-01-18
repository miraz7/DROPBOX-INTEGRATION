from core.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import requests
from fastapi.responses import RedirectResponse

GITHUB_CLIENT_ID = ""
GITHUB_CLIENT_SECRET = ""


def start_auth_with_dropbox(): 
    
    print("I came here")
    return RedirectResponse(
        url="https://github.com/login/oauth/authorize?client_id=c9878e72ce637c337a8c", status_code=302
    )



def dropbox_code(query_params): 
    pass
    
   
    


def drop_box_success(query_params):
    pass
    
 