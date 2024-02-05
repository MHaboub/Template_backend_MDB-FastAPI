from .database import database

class Services:
    async def insert_on(collection: str, new_data: dict):
        result = await database[collection].insert_one(new_data)
        created_user = await database[collection].find_one({"_id": result.inserted_id})
        return created_user
    

    async def update_document(collection: str, identifier: dict, new_data: dict):
        result = await database[collection].update_one(identifier, {"$set": new_data})
        if result.modified_count == 0:
            return None  # Document not found or no changes made
        updated_document = await database[collection].find_one(identifier)
        return updated_document
    

    async def update_all(collection: str, new_data: dict):
        result = await database[collection].update_one({}, {"$set": new_data})
        if result.modified_count == 0:
            return None  # Document not found or no changes made
        updated_document = await database[collection].find_one({})
        return updated_document
    

    
    async def fetch_one(collection: str, identifier: dict):
        document = await database[collection].find_one(identifier)
        return document



    async def fetch_all(collection: str):
        users= []
        cursor = database[collection].find({})
        async for document in cursor:
            users.append(users(**document))
        return users
    

    async def remove(collection: str, identifier: dict):
        await database[collection].delete_one(identifier)
        return True

