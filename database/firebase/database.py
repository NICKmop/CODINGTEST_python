import firebase_admin
from log.log import Log
from firebase_admin import credentials
from firebase_admin import db

class Database:
    DB_URL = "https://accounts.google.com/o/oauth2/auth"
    CRED = credentials.Certificate("database/firebase/firebase_key.json")
    
    def __init__(self):
        
        self._client = None
        self._db = None

    def connect(self):
        
        self._client = firebase_admin.initialize_app(self.CRED, {'databaseURL':self.DB_URL})
        
        if (self._client is None):
            Log.d(self, "could not connect to Firebase")
            return False

        Log.d(self, "connect to Firebase")
        return True 
            
    def insert(self):
        pass
    
    def update(self):
        pass
    
    def delete(self):
        pass
    
    def find(self):
        pass