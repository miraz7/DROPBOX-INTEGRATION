
from core import app, Session, STORE_URL, api_version
from sqlalchemy import MetaData
from datetime import datetime



@app.task(name="tasks.tasks.my-first-task-name")
def process_all_inventory_update_requests():
    db = Session()
    channels = db.query(Channel).all()

    print("There is my first task what i want to do")
