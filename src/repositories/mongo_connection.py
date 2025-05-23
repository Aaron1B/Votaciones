from pymongo import MongoClient
from pymongo.server_api import ServerApi

class MongoConnection:
    def __init__(self, uri="mongodb+srv://aaronsacristan6a:<Poetas1Bja?>@aaron.vspax4a.mongodb.net/?retryWrites=true&w=majority&appName=Aaron", db_name="votaciones"):
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client[db_name]
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def get_collection(self, collection_name):
        return self.db[collection_name]
