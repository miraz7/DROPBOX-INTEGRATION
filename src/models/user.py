from sqlalchemy import TIMESTAMP, Column, String, Integer, DateTime, JSON, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from datetime import datetime
from core.database import Base
import uuid



class User(Base):
    __tablename__ = "user"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable= True)
    age = Column(String , nullable = True)
    country = Column(String , nullable = True)
    city = Column(String ,nullable = True)
    code = Column(String , nullable = True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())