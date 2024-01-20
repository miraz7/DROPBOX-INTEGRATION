from sqlalchemy import TIMESTAMP, Column, String, Integer, DateTime, JSON, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from datetime import datetime
from core.database import Base , get_db
import uuid



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
    expires_at = Column(String , nullable = True)
    refresh_token = Column(String , nullable = True)
    uid = Column(String , nullable = True)
    account_id = Column(String , nullable = True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    
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
        
    
    
