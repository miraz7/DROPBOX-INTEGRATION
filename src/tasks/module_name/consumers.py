import json
import uuid
from datetime import datetime
from celery import bootsteps
from kombu import Exchange, Queue, Consumer
from core import app, Session



def insert_inventory_update_request(channel_uuid, sku, available_quantity):

    db = Session()
    print(channel_uuid, sku, available_quantity)
    with db:
        channel = db.query(Channel).filter(
            Channel.channel_uuid == channel_uuid).first()
        
      
        if not channel:
            print(f'{channel_uuid} not found')
            return True  # Acknowledge true for unknown channel
        product = db.query(Product).filter(
            Product.sku == sku , Product.channel ==  channel  ).first()

        if not product:
            print(f'{sku} not found')
            return True  # Acknowledge true for unknown product
        

 
        print(product.product_id)

        

        existing_inventory_request = db.query(InventoryRequest).filter(InventoryRequest.channel_uuid == channel_uuid,
                                                                       InventoryRequest.sku == sku,
                                                                       InventoryRequest.item_id ==  str(product.product_id),
                                                                       InventoryRequest.status == InventoryRequest.StatusChoices.PENDING).first()
        
        
       

        if existing_inventory_request:
            existing_inventory_request.quantity = available_quantity
            db.commit()

        else:
            inventory_request = InventoryRequest(
                channel_uuid = channel.channel_uuid,
                sku=product.sku,
                item_id=product.product_id,
                quantity=available_quantity,
                request_id=str(uuid.uuid4()),
                status=InventoryRequest.StatusChoices.PENDING,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            db.add(inventory_request)
            db.commit()
        print(f"inventory request created successful {sku} - {channel_uuid}")
        return True


exchange = Exchange("name-of-the-exchage-we-want-to-connect")
queue = Queue(
    "name-of-the-from-where-we-want-to-fetch-the-data", exchange, routing_key="")

class RequestProcessWorker(bootsteps.ConsumerStep):
    def get_consumers(self, channel):
        print("Getting inventory consumer")
        return [Consumer(channel,
                         queues=[queue],
                         callbacks=[self.on_message],
                         accept=['json', 'text/plain'])]

    def on_message(self, body, message):
        data = json.loads(body)
        
        if data : 
       
            message.ack()
app.steps['consumer'].add(RequestProcessWorker)
