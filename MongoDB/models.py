"""
MongoDB Data Models for Dress Shopping App

Defines models for users, dresses, and orders using PyMongo style data structures.
This file acts as a reference for collection schemas to be used in FastAPI/PyMongo integration.
"""

from typing import Dict, List, Optional
from datetime import datetime

# PUBLIC_INTERFACE
def get_user_schema() -> Dict:
    """User collection schema template as a Python dict (for documentation/reference only)."""
    return {
        "name": "Jane Doe",
        "phone_number": "+919999999999",
        "chest_size": 38,
        "favorite_brand": "Zara",
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }

# PUBLIC_INTERFACE
def get_dress_schema() -> Dict:
    """Dress/product collection schema template as a Python dict (for documentation/reference only)."""
    return {
        "name": "Summer Floral Dress",
        "image_url": "http://img.example.com/floral.jpg",
        "price": 1999,
        "brand": "Zara",
        "size": 38,
        "quantity": 10,
        "description": "A breezy summer floral dress",
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }

# PUBLIC_INTERFACE
def get_order_schema() -> Dict:
    """Order collection schema template as a Python dict (for documentation/reference only)."""
    return {
        "user_id": "<ObjectId ref to users>",
        "dress_id": "<ObjectId ref to dresses>",
        "quantity": 1,
        "total_amount": 1999,
        "payment_status": "pending", # "pending", "paid", "failed"
        "order_status": "created",   # "created", "processing", "completed", "cancelled"
        "payment_provider": "PhonePe",
        "payment_reference": "",
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
