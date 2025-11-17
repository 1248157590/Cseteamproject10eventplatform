import json
import os
import datetime
from typing import List, Tuple

# NOT: GitHub web arayüzünden klasör ve dosya işlemlerini simule edemeyiz. 
# Bu fonksiyonlar, kodu daha sonra bir bilgisayarda çalıştırdığınızda çalışacaktır.

def load_state(base_dir: str = "data") -> Tuple[list, list, list]:
    """
    Tüm events, attendees ve registrations verilerini diskten yükler.
    Dosyalar bulunamazsa veya boşsa boş listeler döndürür.
    """
    events_path = os.path.join(base_dir, "events.json")
    attendees_path = os.path.join(base_dir, "attendees.json")
    registrations_path = os.path.join(base_dir, "registrations.json")

    def load_file(path):
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    events = load_file(events_path)
    attendees = load_file(attendees_path)
    registrations = load_file(registrations_path)

    return events, attendees, registrations

def save_state(base_dir: str, events: list, attendees: list, registrations: list) -> None:
    """
    Tüm events, attendees ve registrations verilerini ilgili JSON dosyalarına kaydeder.
    """
    os.makedirs(base_dir, exist_ok=True)
    
    events_path = os.path.join(base_dir, "events.json")
    attendees_path = os.path.join(base_dir, "attendees.json")
    registrations_path = os.path.join(base_dir, "registrations.json")
    
    with open(events_path, 'w', encoding='utf-8') as f:
        json.dump(events, f, indent=4)
        
    with open(attendees_path, 'w', encoding='utf-8') as f:
        json.dump(attendees, f, indent=4)
        
    with open(registrations_path, 'w', encoding='utf-8') as f:
        json.dump(registrations, f, indent=4)
        
def backup_state(base_dir: str = "data", backup_dir: str = "backups") -> List[str]:
    """
    Mevcut veri dosyalarının zaman damgalı bir kopyasını backups/ klasörüne oluşturur.
    """
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    files_to_backup = ["events.json", "attendees.json", "registrations.json"]
    backed_up_files = []

    for filename in files_to_backup:
        source_path = os.path.join(base_dir, filename)
        if os.path.exists(source_path):
            # Yeni dosya adı: events_20251117_210000.json
            target_filename = f"{filename.replace('.json', '')}_{timestamp}.json"
            target_path = os.path.join(backup_dir, target_filename)
            
            with open(source_path, 'r') as src, open(target_path, 'w') as dst:
                dst.write(src.read())
            
            backed_up_files.append(target_filename)
            
    return backed_up_files

def validate_registration(registration: dict) -> bool:
    """
    Kayıt şemasını doğrular (İleriki haftalar için bir yer tutucu).
    """
    required_keys = ['event_id', 'attendee_id', 'status']
    return all(key in registration for key in required_keys)
