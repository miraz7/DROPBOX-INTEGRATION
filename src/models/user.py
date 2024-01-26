from sqlalchemy import TIMESTAMP, Column, String, Integer, DateTime, JSON, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from datetime import datetime
from core.database import Base , get_db
import uuid
from fastapi.encoders import jsonable_encoder



class User(Base):
    __tablename__ = "user"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable= True)
    age = Column(String , nullable = True)
    country = Column(String , nullable = True)
    city = Column(String ,nullable = True)
    code = Column(String , nullable = True)
    email = Column(String , nullable = True)
    access_token = Column(String , nullable = True)
    expires_at = Column(DateTime(timezone=True) , nullable = True)
    expires_in = Column(Integer , nullable = True)
    refresh_token = Column(String , nullable = True)
    uid = Column(String , nullable = True)
    account_id = Column(String , nullable = True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    
    def as_dict(self):
        expires_at_str = str(self.expires_at) if self.expires_at else None
        created_at_str = str(self.created_at) if self.created_at else None
        updated_at_str = str(self.updated_at) if self.updated_at else None

        return {
            "id": str(self.id),
            "name": self.name,
            "age": self.age,
            "country": self.country,
            "city": self.city,
            "code": self.code,
            "email": self.email,
            "access_token": self.access_token,
            "expires_at": expires_at_str,
            "expires_in": self.expires_in,
            "refresh_token": self.refresh_token,
            "uid": self.uid,
            "account_id": self.account_id,
            "created_at": created_at_str,
            "updated_at": updated_at_str,
        }
    
    
class DropBoxUser:
    def __init__(self, id= None ,  name=None, age=None, country=None, city=None, code=None, email=None, access_token=None, expires_at=None ,  expires_in=None, refresh_token=None, uid=None, account_id=None):
        self.id = id 
        self.name = name
        self.age = age
        self.country = country
        self.city = city
        self.code = code
        self.email = email
        self.access_token = access_token
        self.expires_at = expires_at
        self.expires_in = expires_in
        self.refresh_token = refresh_token
        self.uid = uid
        self.account_id = account_id

    def save_dropbox_user_data(self):
        user_data = {
            'name': self.name,
            'age': self.age,
            'country': self.country,
            'city': self.city,
            'code': self.code,
            'email': self.email,
            'access_token': self.access_token,
            'expires_at': self.expires_at,
            'expires_in':   self.expires_in ,
            'refresh_token': self.refresh_token,
            'uid': self.uid,
            'account_id': self.account_id,
        }

        # Use the get_db function as a context manager to get a session
        with get_db() as db:
            # Create a User instance
            new_user = User(**user_data)

            # Add the User instance to the session
            db.add(new_user)

            # Commit the changes to the database
            db.commit()
            
            return new_user
    def update_user(self, id=None, email=None):
        with get_db() as db:
            query = db.query(User).filter_by(id = self.id)
            user = query.first()
            
            # return user

            if user:
                # Update the user fields
                if self.name : user.name = self.name 
                if self.age : user.age = self.age
                if self.country : user.country = self.country
                if self.city : user.city = self.city
                if self.code :user.code = self.code
                if self.email :user.email = self.email
                if self.access_token:user.access_token = self.access_token
                if self.expires_at : user.expires_at = self.expires_at
                if self.expires_in : user.expires_in = self.expires_in
                if self.refresh_token : user.refresh_token = self.refresh_token
                if self.uid : user.uid = self.uid
                if self.account_id : user.account_id = self.account_id
                
                db.commit()
                db.refresh(user)

                return user
            else:
                return user
    
    def get_all_users():
        with get_db() as db:
            users = db.query(User).all()
            dict = [user.as_dict() for user in users]
            return dict
        
        
    def get_user( id=None , email = None):
        with get_db() as db:
            filters = {}
            if id :
                filters.update({"id" : id})
            # if email : 
            #     filters.update({"email" : email})
                
            query = db.query(User).filter_by(**filters)
            user = query.first()
            if user :
                return user
            else : 
                return None 
    
