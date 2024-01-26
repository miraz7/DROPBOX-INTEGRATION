from core.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import requests
from fastapi.responses import RedirectResponse
from starlette.responses import Response, StreamingResponse
from models.user import DropBoxUser
from .dropbox import DropBox,DropBoxToken
import requests
import json
from datetime import datetime, timedelta



def start_auth_with_dropbox(request ): 
    
    dropbox = DropBox()
    print("I came here")
    
    url = dropbox.get_auth_url(request)
    
    print(url)
    
    response = {}
    # return Response(content=json.dumps(response), status_code=200)
    return RedirectResponse(
        url=url, status_code=302
    )

def dropbox_code(request): 
    
    query_params =  request.query_params
    authorization_code =  query_params.get('code')
    new_dropbox = DropBox()
    drop_box_token_response = new_dropbox.handle_authorization_code(authorization_code , request)
    
    if drop_box_token_response.status_code ==200 : 
        
        print(drop_box_token_response.status_code)
        drop_box_data =json.loads(drop_box_token_response.text)
        current_datetime = datetime.now()
        expires_datetime = current_datetime + timedelta(seconds=int(drop_box_data.get('expires_in')))
        
        user_data = {
            "name": "John Doe",
            "age": "30",
            "country": "USA",
            "city": "New York",
            "code": "12345",
            "email": "test@miraz_test_0123.com",
            "access_token":drop_box_data.get('access_token'),
            "expires_at": expires_datetime,
            "expires_in": int(drop_box_data.get('expires_in')),
            "refresh_token":drop_box_data.get('refresh_token'),
            "uid": drop_box_data.get('uid'),
            "account_id":drop_box_data.get('account_id'),
        }
        dropbox_user = DropBoxUser(**user_data)
        new_user = dropbox_user.save_dropbox_user_data()
        
        print(new_user)
        
        return Response(content=json.dumps("user_data"), status_code=200)
        
    else :
         return Response(status_code=400)
        


def get_app_all_users():
    users = DropBoxUser.get_all_users()
    resp = {"data" : users}
    return Response(content=json.dumps(resp), status_code=200)


def get_user_details(id ):
    user = DropBoxUser.get_user(id=id)
    if user :
        
        print(user.id)
        resp = {
            "success" : True,
            "data" : user.as_dict()
            }
        return Response(content=json.dumps(resp), status_code=200)
    else : 
        resp = {"message" : "No user found"}
        return Response(content=json.dumps(resp), status_code=400)
    
    
    
    
def get_dropbox_user_details(id):
    user = DropBoxUser.get_user(id=id)
    if user :
        
        # drop_box = DropBox(access_token=user.get('access_token'))
        # data = drop_box.get_current_user_details()
        
        token = DropBoxToken(user=user)
        access_token = token.get_valid_access_token()
        
        resp = {
            "success" : True,
            "data" : access_token
            }
        return Response(content=json.dumps(resp), status_code=200)
    else : 
        resp = {"message" : "No user found"}
        return Response(content=json.dumps(resp), status_code=200)
    
    

    
 