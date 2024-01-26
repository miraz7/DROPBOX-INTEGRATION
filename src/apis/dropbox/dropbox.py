
from core.app_vars import DROPBOX_CLIENT_ID , DROPBOX_CLIENT_SECRET
from fastapi import Request
import requests
import urllib.parse
from datetime import datetime, timedelta,timezone
from models import DropBoxUser

class DropBox():
    
    def __init__(self, client_id=None, client_secret=None, redirect_uri=None , access_token=None, user =None) :
        self.client_id = client_id or DROPBOX_CLIENT_ID
        self.client_secret = client_secret or DROPBOX_CLIENT_SECRET
        self.redirect_uri = redirect_uri or "http://localhost:8010/api/v1/dropbox/code",
        self.access_token = access_token or None
        
        
    def get_redirect_uri(self, request: Request):
        return str(request.base_url) + "/api/v1/dropbox/code"
    
    
    def get_auth_url(self , request):
        auth_url = "https://www.dropbox.com/oauth2/authorize"
        params = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri":  self.redirect_uri ,
            "token_access_type": "offline",
        }
        return f"https://www.dropbox.com/oauth2/authorize?client_id=sf1n10mvdi9lu2n&response_type=code&redirect_uri=http://localhost:8010/api/v1/dropbox/code&token_access_type=offline"
    
    def _encode_params(self, params):
        return urllib.parse.urlencode(params)
    
    def check_user(self, query):
        url = "https://api.dropboxapi.com/2/check/user"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }
        data = {"query": query}
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    def get_current_user_details(self):
        url = "https://api.dropboxapi.com/2/users/get_current_account"
        headers = {"Authorization": f"Bearer {self.access_token}"}

        response = requests.post(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return response.text
    def handle_authorization_code(self, authorization_code , request = None):
        url = "https://api.dropbox.com/oauth2/token"
        payload = {
            'code': authorization_code,
            'grant_type': 'authorization_code',
            'redirect_uri':   self.redirect_uri ,
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        response = requests.post(url, data=payload)

        return response
       
        
 
        
class DropBoxToken():
    def __init__(self, user_dictionary  = None , user = None) :
        self.user = user 
        if user_dictionary :
            self.id = user_dictionary.get('id')
            self.access_token = user_dictionary.get('access_token')
            self.refresh_token = user_dictionary.get('refresh_token')
            self.updated_at = user_dictionary.get('updated_at')
            self.expires_at = user_dictionary.get('expires_at')
            self.expires_in = user_dictionary.get('expires_in')
        elif  user : 
            self.id = user.id
            self.access_token = user.access_token
            self.refresh_token = user.refresh_token
            self.expires_at = user.expires_at
            self.expires_in = user.expires_in
            self.updated_at = user.updated_at
            
    def get_valid_access_token(self):
        

        if self.expires_at > datetime.now(timezone.utc) :
                # Token is expired or not set; refresh it
                url = "https://api.dropboxapi.com/oauth2/token"
                headers = {"Content-Type": "application/x-www-form-urlencoded"}
                data = {
                    "grant_type": "refresh_token",
                    "refresh_token": self.refresh_token,
                    "client_id": DROPBOX_CLIENT_ID,
                    "client_secret": DROPBOX_CLIENT_SECRET,
                }
                response = requests.post(url, headers=headers, data=data)
                
                print(response)
                if response.status_code == 200:
                    token_data = response.json()
                    
                    print(token_data)
                    expires_in_seconds = token_data.get("expires_in", 0)
                    self.access_token = token_data.get("access_token")
                   
                    self.expires_at  = datetime.now() + timedelta(seconds=expires_in_seconds)
                    self.expires_in =  expires_in_seconds
                    
                    
                    # print(self.user.id)
                    
                    dropbox_user = DropBoxUser(id = self.user.id, access_token=self.access_token, expires_at=self.expires_at ,expires_in= self.expires_in )
                    user = dropbox_user.update_user()
                    
                    if user :
                        return str(user.access_token)
                    else : 
                        print("coundn't update user acess to token to user table ")
                        return None
                else:
                    
                    print("Failed to retrive access token from dropbox ")
                    print(f"Dropbox Response : {response.status_code}")
                    print(f"Dropbox Response Body : {response.text}" )
                    return None
        else:
            print(f"Acess Token Is currently valid")
            return str(self.user.access_token)
     