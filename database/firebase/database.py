import firebase_admin
class Database:
    DB_URL = "https://accounts.google.com/o/oauth2/auth"
    CRED = credentials.Certificate("database/firebase/firebase_key.json")
    
    def __init__(self):
        
        self._client = None
        self._db = None

    def connect(self):
        
        self._client = firebase.database.initialize_app(self.CRED, {'databaseURL':self.DB_URL})
        
        if (self._client is None):
            print(self._client)
            return False

        print(self._client)
        return True 
            
    def insert(self):
        pass
    
    def update(self):
        pass
    
    def delete(self):
        pass
    
    def find(self):
        pass