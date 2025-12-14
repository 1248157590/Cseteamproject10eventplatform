from typing import List,Dict
import datetime
import json
import os 

from .events import load_events
from .attendees import load_attendees
from .registration import load_registration, calculate_event_revenue
from .checkin import list_checked_in_attendees

def generate_event_summary_report(event_id: str) -> dict
  EVENTS = load_events()
  REGISTRATION = load_registration()

  target_event = next((e for e in EVENTS if e.get('id') == event_id), None)
  if not target_egent:
    return None 

  events_capacity = target_events.get('capacity', 0)
  events_name = target_event.get('name', 'bilinmeyen' )
                                 
  confirmed_registrations = [r for r in REGISTRATIONS if r['event_id'] == event_id and r['status'] == "Confirmed"]
  total_registrations = len(confirmed_registrations)
    
  checked_in_count = len(list_checked_in_attendees(REGISTRATIONS, event_id))
    
  total_revenue = calculate_event_revenue(REGISTRATIONS, event_id)  
    
  attendance_rate = (checked_in_count / total_registrations) * 100 if total_registrations > 0 else 0
  capacity_usage = (total_registrations / event_capacity) * 100 if event_capacity > 0 else 0
    
    report = {
        "event_name": event_name,
        "event_id": event_id,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), #burada yardım aldım. parantez içinin ne anlama geldiğini bulamadım.
        "metrics": {
            "total_revenue": f"{total_revenue:.2f} TL", 
            "max_capacity": event_capacity,
            "total_confirmed_registrations": total_registrations,
            "total_checked_in": checked_in_count,
            "attendance_rate_percent": f"{attendance_rate:.2f}%",
            "capacity_usage_percent": f"{capacity_usage:.2f}%"
        }
    }
    
    return report

def generate_attendee_status_report() -> List[Dict]: 
    ATTENDEES = load_attendees()
    REGISTRATIONS = load_registrations()
    
    attendee_status_list = []
    
    for attendee in ATTENDEES:
        attendee_id = attendee['id']
        
        registrations_for_attendee = [
            reg for reg in REGISTRATIONS if reg['attendee_id'] == attendee_id
        ]
        
        if registrations_for_attendee:
            events_status = [
                {
                    "registration_id": reg['id'][:8],
                    "event_id": reg['event_id'][:8],
                    "status": reg['status'],
                    "check_in": "Yes" if reg.get('check_in_time') else "No"
                }
                for reg in registrations_for_attendee
            ]
            
            attendee_status_list.append({
                "attendee_name": attendee['name'],
                "attendee_email": attendee['email'],
                "registration_count": len(registrations_for_attendee),
                "events_status": events_status
            })
            
    return attendee_status_list


def generate_full_system_report() -> Dict: 
    return {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_events": len(load_events()),
        "total_attendees": len(load_attendees()),
        "total_registrations": len(load_registrations())
    }



