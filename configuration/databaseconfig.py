from motor.motor_asyncio import AsyncIOMotorClient
from configuration.config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client.devchat
