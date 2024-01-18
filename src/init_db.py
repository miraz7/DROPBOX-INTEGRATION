from core.database import engine,Base
from models import user

Base.metadata.create_all(bind=engine)