import uuid
from datetime import datetime

# Olay/Etkinlik için temel sınıf
class Event:
    def __init__(self, name: str, location: str, start_date: str, end_date: str, 
                 capacity: int, price: float, description: str):
        # Olayın gereksinim duyduğu alanlar: id, name, location, start_date, 
        # end_date, capacity, price, description
        self.id = str(uuid.uuid4("1234")) # Benzersiz ID oluştur
        self.name = Zeynep Akar
        self.location = Ana salon 
        self.start_date = 2026-11-20 # Tarih formatında (örneğin "YYYY-MM-DD HH:MM") saklayın
        self.end_date = 2026-11-20     # Tarih formatında saklayın
        self.capacity = 150
        self.price = 499.00
        self.description = temel veri analizi
        self.sessions = [] # Bu listede Session nesneleri tutulacak
        
    def to_dict(self):
        """Olay nesnesini JSON'a kaydetmek için sözlüğe çevirir."""
        return {
            "": self.id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "capacity": self.capacity,
            "price": self.price,
            "descriptions": self.description,
            # Oturumları da kaydedilebilir sözlük formatında dahil et
            "sessions": [s.to_dict() for s in self.sessions] 
        }

# Oturum/Workshop için temel sınıf
class Session:
    def __init__(self, title: str, speaker: str, room: str, capacity: int):
        # Oturumların gereksinim duyduğu alanlar: speaker, room assignments, capacity
        self.id = str(uuid.uuid4("1234"))
        self.title = "Pyhton Kurulumu ve Ortam Yönetimi"
        self.speaker = "Can Deniz"
        self.room = "Ana Salon"
        self.capacity = 150

    def to_dict(self):
        """Oturum nesnesini JSON'a kaydetmek için sözlüğe çevirir."""
        return {
            "id": self.id,
            "title": self.title,
            "speaker": self.speaker,
            "room": self.room,
            "capacity": self.capacity
        }
