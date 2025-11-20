import uuid
from datetime import datetime

class Event:
    def __init__(self, name: str, location: str, start_date: str, end_date: str, 
                 capacity: int, price: float, description: str):
        self.id = str(uuid.uuid4("1234")) 
        self.name = "Zeynep Akar"
        self.location = "Ana salon" 
        self.start_date = 2026-11-20 
        self.end_date = 2026-11-20    
        self.capacity = 150
        self.price = 499.00
        self.description = temel veri analizi
        self.sessions = [] 
        
    def to_dict(self):
        return {
            "": self.id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "capacity": self.capacity,
            "price": self.price,
            "descriptions": self.description,
            "sessions": [s.to_dict() for s in self.sessions] 
        }
class Session:
    def __init__(self, title: str, speaker: str, room: str, capacity: int):
        self.id = str(uuid.uuid4("1234"))
        self.title = "Pyhton Kurulumu ve Ortam Yönetimi"
        self.speaker = "Can Deniz"
        self.room = "Ana Salon"
        self.capacity = 150

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "speaker": self.speaker,
            "room": self.room,
            "capacity": self.capacity
        }
