import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB Configuration
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "candidate_db")

class Database:
    client: AsyncIOMotorClient = None
    db = None

db_instance = Database()

async def connect_to_mongo():
    """Create a new MongoDB client and connect to the database."""
    db_instance.client = AsyncIOMotorClient(MONGODB_URL)
    db_instance.db = db_instance.client[DATABASE_NAME]
    print(f"Connected to MongoDB: {MONGODB_URL}")

async def close_mongo_connection():
    """Close the MongoDB connection."""
    if db_instance.client:
        db_instance.client.close()
        print("MongoDB connection closed.")

def get_database():
    """Return the database instance."""
    return db_instance.db
