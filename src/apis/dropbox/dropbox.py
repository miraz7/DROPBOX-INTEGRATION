
from core.app_vars import DROPBOX_CLIENT_ID , DROPBOX_CLIENT_SECRET
from fastapi import Request
import requests
import urllib.parse

class DropBox():
    def __init__(self, client_id=None, client_secret=None, redirect_uri=None):
        self.client_id = client_id or DROPBOX_CLIENT_ID
        self.client_secret = client_secret or DROPBOX_CLIENT_SECRET
        self.redirect_uri = redirect_uri or "http://localhost:8010/api/v1/dropbox/code"
        
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
        return f"{auth_url}?{self._encode_params(params)}"
    
    def _encode_params(self, params):
        return urllib.parse.urlencode(params)
    
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
       