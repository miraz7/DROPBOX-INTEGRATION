from core.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import requests
from fastapi.responses import RedirectResponse
from starlette.responses import Response, StreamingResponse
from models.user import DropBoxUser

GITHUB_CLIENT_ID = ""
GITHUB_CLIENT_SECRET = ""


def start_auth_with_dropbox(): 
    
    print("I came here")
    return RedirectResponse(
        url="https://www.dropbox.com/oauth2/authorize?client_id=sf1n10mvdi9lu2n&response_type=code&redirect_uri=http://localhost:8010/api/v1/dropbox/code&token_access_type=offline", status_code=302
    )

import requests
import json
from datetime import datetime, timedelta
def dropbox_code(query_params): 
    
    url = "https://api.dropbox.com/oauth2/token"
    authorization_code =  query_params.get('code')
    redirect_uri = "http://localhost:8010/api/v1/dropbox/code"
    client_id = "sf1n10mvdi9lu2n"
    client_secret = "uaeqq1rrln7q6kx"
    payload = {
        'code': authorization_code,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    }
    response = requests.post(url, data=payload)
    if response.status_code ==200 : 
        
        print(response.status_code)
        drop_box_data =json.loads(response.text)
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
            "expires_at": expires_datetime.strftime("%Y-%m-%d %H:%M:%S %z"),
            "refresh_token":drop_box_data.get('refresh_token'),
            "uid": drop_box_data.get('uid'),
            "account_id":drop_box_data.get('account_id'),
        }
        
        dropbox_user = DropBoxUser(**user_data)
        new_user = dropbox_user.save_dropbox_user_data()
        
        return Response(content=json.dumps(user_data), status_code=200)
        
    else :
         return Response(status_code=400)
        


def drop_box_success(query_params):
    
    print(query_params)
    
    
    pass
    
 