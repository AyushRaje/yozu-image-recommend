from pymongo import MongoClient

# Replace the following with your MongoDB connection details
class MongoConnection:
    def __init__(self,mongo_uri,db_name,collection_name):
        self.connection  = MongoClient(mongo_uri)
        self.db = self.connection[db_name]
        self.collection = self.db[collection_name]

    def get_documents_list(self):
        image_documents = list(self.collection.find())
        print("Total ",len(image_documents)," found in this collection")