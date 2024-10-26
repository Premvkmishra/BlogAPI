import motor.motor_asyncio
from decouple import config

MONGO_DETAILS = config("MONGO_URI")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.school_blog
blog_collection = database.get_collection("blogs")
