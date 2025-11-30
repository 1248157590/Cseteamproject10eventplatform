import uuid
from typing import Optional, List, Dict
import datetime
import json
import 


from .events import load_events 


def get_registration_template(event_id: str, attendee_id: str, ticket_type: str, price: float) -> dict:
    
    return {
        "id": str(uuid.uuid4()),
        "event_id": event_id,
        "attendee_id": attendee_id,
        "ticket_type": ticket_type, 
        "price": price,
        "status": "Confirmed",        
        "is_waitlisted": False,
        "registration_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),#burada yardım aldım. ne amaçla kullanıldığım
      nı anlayamadım 
        "payment_status": "Paid"     
    }

def load_registrations(path: str = "data/registrations.json") -> list:
    
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            try:
                return json.load(f) if os.path.getsize(path) > 0 else []
            except json.JSONDecodeError:
                return []
    return []

def save_registrations(registrations: list, path: str = "data/registrations.json") -> None:

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(registrations, f, indent=4)

def create_registration(registrations: list, registration_data: dict, events: list) -> dict:
  
    event_id = registration_data.get('event_id')
    
    # 1. İlgili olayı bul
    target_event = next((e for e in events if e.get('id') == event_id), None)
    if not target_event:
        return {"success": False, "error": f"Olay ID'si {event_id} bulunamadı."}

    # 2. Kapasite Kontrolü (Basit Mantık)
    current_confirmed = [r for r in registrations if r['event_id'] == event_id and r['status'] == "Confirmed"]
    
    is_waitlisted = False
    status = "Confirmed"
    
    # Kapasite doluysa, durumu değiştir
    if len(current_confirmed) >= target_event.get('capacity', 0):
        is_waitlisted = True
        status = "Waitlist"
        # Basitlik için print mesajı eklenir
        print(f"UYARI: Kapasite aşıldı. Kayıt bekleme listesine eklendi.")

    # 3. Yeni kayıt sözlüğünü oluştur
    new_reg = get_registration_template(
        event_id=event_id,
        attendee_id=registration_data.get('attendee_id'),
        ticket_type=registration_data.get('ticket_type', 'General'),
        price=registration_data.get('price', target_event.get('price', 0.0))
    )
    new_reg['status'] = status
    new_reg['is_waitlisted'] = is_waitlisted
    
    registrations.append(new_reg)
    
    # Not: main.py'de save_registrations() çağrılmalıdır.
    return {"success": True, "registration": new_reg}


def promote_waitlist(registrations: list, event_id: str) -> Optional[dict]:
  
    # 1. Bekleme listesindeki kayıtları bul ve en eski (ilk kayıt olan) kişiyi seç (FIFO)
    waitlist = sorted([
        r for r in registrations 
        if r['event_id'] == event_id and r['status'] == "Waitlist"
    ], key=lambda r: r['registration_date']) 

    if not waitlist:
        return None 

    # 2. İlk kaydı al ve durumu güncelle
    promoted_reg = waitlist[0]
    promoted_reg['status'] = "Confirmed"
    promoted_reg['is_waitlisted'] = False
    
    return promoted_reg


def cancel_registration(registrations: list, registration_id: str, events: list) -> dict:

    for reg in registrations:
        if reg.get('id') == registration_id:
            if reg['status'] == "Cancelled":
                return {"success": False, "error": "Kayıt zaten iptal edilmiş."}
            
            # Basit iade simülasyonu:
            reg['status'] = "Cancelled"
            reg['payment_status'] = "Refund Processed" 
            
            # Bekleme listesini terfi ettir (promote_waitlist fonksiyonu çağrılır)
            promoted = promote_waitlist(registrations, reg['event_id'])
            
            return {"success": True, "registration": reg, "promoted": promoted is not None}

    return {"success": False, "error": f"Kayıt ID'si {registration_id} bulunamadı."}

def transfer_ticket(registrations: list, registration_id: str, new_attendee_id: str) -> dict:
    
    for reg in registrations:
        if reg.get('id') == registration_id:
            if reg['status'] == "Confirmed":
                reg['attendee_id'] = new_attendee_id
                return {"success": True, "registration": reg}
            else:
                return {"success": False, "error": "Sadece onaylanmış biletler devredilebilir."}
                
    return {"success": False, "error": f"Kayıt ID'si {registration_id} bulunamadı."}

def calculate_event_revenue(registrations: list, event_id: str) -> float:
  
    total_revenue = sum(
        reg['price'] for reg in registrations 
        if reg['event_id'] == event_id and reg['status'] == "Confirmed" and reg['payment_status'] == "Paid"
    )
    return total_revenue
