import uuid
from datetime import datetime

# Olay/Etkinlik için temel sınıf
class Event:
    def __init__(self, name: str, location: str, start_date: str, end_date: str, 
                 capacity: int, price: float, description: str):
        # Olayın gereksinim duyduğu alanlar: id, name, location, start_date, 
        # end_date, capacity, price, description
        self.id = str(uuid.uuid4()) # Benzersiz ID oluştur
        self.name = name
        self.location = location
        self.start_date = start_date # Tarih formatında (örneğin "YYYY-MM-DD HH:MM") saklayın
        self.end_date = end_date     # Tarih formatında saklayın
        self.capacity = capacity
        self.price = price
        self.description = description
        self.sessions = [] # Bu listede Session nesneleri tutulacak
        
    def to_dict(self):
        """Olay nesnesini JSON'a kaydetmek için sözlüğe çevirir."""
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "capacity": self.capacity,
            "price": self.price,
            "description": self.description,
            # Oturumları da kaydedilebilir sözlük formatında dahil et
            "sessions": [s.to_dict() for s in self.sessions] 
        }

# Oturum/Workshop için temel sınıf
class Session:
    def __init__(self, title: str, speaker: str, room: str, capacity: int):
        # Oturumların gereksinim duyduğu alanlar: speaker, room assignments, capacity
        self.id = str(uuid.uuid4())
        self.title = title
        self.speaker = speaker
        self.room = room
        self.capacity = capacity

    def to_dict(self):
        """Oturum nesnesini JSON'a kaydetmek için sözlüğe çevirir."""
        return {
            "id": self.id,
            "title": self.title,
            "speaker": self.speaker,
            "room": self.room,
            "capacity": self.capacity
        }
