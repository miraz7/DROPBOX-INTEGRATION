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
        return jsonable_encoder(self)
    
    
class DropBoxUser:
    def __init__(self, name=None, age=None, country=None, city=None, code=None, email=None, access_token=None, expires_at=None, refresh_token=None, uid=None, account_id=None):
        self.name = name
        self.age = age
        self.country = country
        self.city = city
        self.code = code
        self.email = email
        self.access_token = access_token
        self.expires_at = expires_at
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
    
    def get_all_users():
        with get_db() as db:
            users = db.query(User).all()
            dict = [user.as_dict() for user in users]
            return dict
    def get_user(id=None , email = None):
        with get_db() as db:
            filters = {}
            if id :
                filters.update({"id" : id})
            if email : 
                filters.update({"email" : email})
                
            query = db.query(User).filter_by(**filters)
            user = query.first()
            if user :
                return user.as_dict()
            else : 
                return None 
    
