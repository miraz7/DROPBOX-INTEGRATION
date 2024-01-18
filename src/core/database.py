from core import DB_HOST , DB_NAME , DB_PASS , DB_PORT , DB_USER

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


POSTGRES_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine= create_engine(POSTGRES_URL, echo=True)
Base = declarative_base()

def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()
Session = sessionmaker(bind=engine)

