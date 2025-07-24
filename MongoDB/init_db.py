"""
Database Initialization Script for Dress Shopping App (MongoDB)

Creates necessary collections and sets indexes for efficient access.
Intended to be used for initial DB setup.

USAGE:
    $ python MongoDB/init_db.py

Environment variables required:
    MONGODB_URI - full MongoDB connection string (provided by orchestrator/ops)
"""

import os
from pymongo import MongoClient, ASCENDING
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://127.0.0.1:27017/")

def initialize_collections():
    client = MongoClient(MONGODB_URI)
    db = client["dress_shopping_app"]

    # Users Collection
    db.users.create_index([("phone_number", ASCENDING)], unique=True)
    db.users.create_index([("chest_size", ASCENDING)])
    db.users.create_index([("favorite_brand", ASCENDING)])

    # Dresses Collection
    db.dresses.create_index([("brand", ASCENDING)])
    db.dresses.create_index([("size", ASCENDING)])
    db.dresses.create_index([("price", ASCENDING)])
    db.dresses.create_index([("name", ASCENDING)])

    # Orders Collection
    db.orders.create_index([("user_id", ASCENDING)])
    db.orders.create_index([("dress_id", ASCENDING)])
    db.orders.create_index([("payment_status", ASCENDING)])
    db.orders.create_index([("order_status", ASCENDING)])

    print("[MongoDB] Collections and indexes are initialized!")
    client.close()

# PUBLIC_INTERFACE
def main():
    """Entrypoint: Initializes all collections and indexes."""
    initialize_collections()

if __name__ == "__main__":
    main()
