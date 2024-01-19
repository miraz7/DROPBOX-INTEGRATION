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
        url="https://www.dropbox.com/oauth2/authorize?client_id=sf1n10mvdi9lu2n&response_type=code&redirect_uri=http://localhost:8010/api/v1/dropbox/code", status_code=302
    )


import requests
def dropbox_code(query_params): 
    
    print(query_params)
    pass
    
   

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

    print(response.text)
    


def drop_box_success(query_params):
    
    print(query_params)
    
    
    pass
    
 