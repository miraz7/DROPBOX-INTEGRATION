
from core.app_vars import DROPBOX_CLIENT_ID , DROPBOX_CLIENT_SECRET
from fastapi import Request
import requests
import urllib.parse
from datetime import datetime, timedelta

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
        
 
        
class DropBoxToken():
    def __init__(self, user_dictionary  = None , user_instance = None) :
        
        if user_dictionary :
            self.id = user_dictionary.get('id')
            self.access_token = user_dictionary.get('access_token')
            self.refresh_token = user_dictionary.get('refresh_token')
            self.updated_at = user_dictionary.get('updated_at')
            self.expires_at = user_dictionary.get('expires_at')
        elif  user_instance: 
            
            pass 
            
        
    def get_valid_access_token(self):
        if self.user : 
            
            if self.token_expires_at is None or datetime.now() > self.token_expires_at:
                # Token is expired or not set; refresh it
                url = "https://api.dropboxapi.com/oauth2/token"
                headers = {"Content-Type": "application/x-www-form-urlencoded"}
                data = {
                    "grant_type": "refresh_token",
                    "refresh_token": self.refresh_token,
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                }

                response = requests.post(url, headers=headers, data=data)

                if response.status_code == 200:
                    token_data = response.json()
                    self.access_token = token_data["access_token"]
                    expires_in_seconds = token_data.get("expires_in", 0)
                    self.token_expires_at = datetime.now() + timedelta(seconds=expires_in_seconds)
                    return True
                else:
                    return False
            else:
                # Token is still valid; no need to refresh
                return True
        else : 
                return None