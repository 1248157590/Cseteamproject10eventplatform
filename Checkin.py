import datetime 
from typing import List,Dict, Optional
import os 
import json 

#registration.py'den çağırıyoruz.
from.registration import load_registrations, save_registration

#events.py ve attendees.py'den veriyi çekmek için 
from.events import load_events
from.attendees import load_attendees

def check_in_attendee(registration: list, registration_id: str) -> dict:
for reg in registrations:
  if reg.get('id') == registration_id:
    if reg['status'] = "confirmed":
      return{"success" : false, "error": f"kayıt durumu onaylı değil : {reg['status']}"}
    if reg.get('check_in_time'):
      return{"success" : false, "error": "katılımcı zaten giriş yapmış."}
    reg['check_in_time'] = datetime.datetime.now().strftime("%Y -%m-%d %H:%M:%S") # buarayı yapay zekaya danışarak yazdım ne için kullanıldığını anlayamadım
    return {"success": true, "registration":reg} 
return{"success": false, "error": f"kayıt ID'si {reg_id} bulunamadı"}

def list_checked_in_attendees(registration: list, event_id:str) -> list: 
  checked_in_list = [
    reg for reg in registrations
    if reg['event_id'] == event_id and reg.get('checked_in_time') is not None 
  ]
    return checked_in_list 

def generate_badge(attendee: dict, registration: dict, directory: str = "badges") -> str: 
  badge_output = f """
KATILIMCI ADI: {attendee.get('name','bilinmiyor')}
KURUM: {attendee.get('organization', 'yok')} 
EVENT ID: {registration.get('event_id', 'N/A')[:8]}
KAYIT ID: {registartion.get('id','N/A')[:8]}

  os.makedirs(directory,exist_ok = true)
  filename = os.path.join(directory, f"badge_{attendee['id'][:8]}.txt")

try:
    with open(file name, 'w', encoding = 'utf'-8') as f:
        f.write(badge_output)
    return f"rozet başarıyla oluşturuldu ve dosyaya kaydedildi: {filename}"
except Exception:
    return badge_output

def session_attendance(registrations: list, event_id: str, session_id:str) -> dict:
  checked _in_count = len(list_checked_in_attendees(registration, event_id))
  return {
    "event_id": event_id,
    "session_id": seession_id,
    "checked_in_attendees": checked_in_count,
    "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
