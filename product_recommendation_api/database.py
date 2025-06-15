from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("mongodb://localhost:27017"))
db = client["product_recommendation"]

users_col = db["users"]
products_col = db["products"]
interactions_col = db["interactions"]
recommendations_col = db["recommendations"]
