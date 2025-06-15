from pydantic import BaseModel
from typing import List
from datetime import datetime

class Interaction(BaseModel):
    user_id: str
    product_id: str
    interaction_type: str  # "view", "purchase"
    timestamp: datetime

class Product(BaseModel):
    name: str
    category: str
    price: float
    tags: List[str]
    rating: float
