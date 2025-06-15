from fastapi import FastAPI
from models import Interaction
from database import interactions_col, products_col
from bson import ObjectId
from datetime import datetime

app = FastAPI()

@app.post("/log-interaction")
def log_interaction(interaction: Interaction):
    doc = {
        "user_id": ObjectId(interaction.user_id),
        "product_id": ObjectId(interaction.product_id),
        "interaction_type": interaction.interaction_type,
        "timestamp": interaction.timestamp
    }
    interactions_col.insert_one(doc)
    return {"message": "Interaction logged"}

@app.get("/products")
def get_products():
    products = list(products_col.find({}, {"_id": 0}))
    return {"products": products}
@app.get("/")
def read_root():
    return {"message": "FastAPI backend is live!"}

