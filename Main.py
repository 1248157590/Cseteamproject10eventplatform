def run_week1_demo():
    
    global EVENTS # EVENTS listesini kullanmak için gereklidir
    print("\n--- PYTHON WORKSHOP DEMOSU BAŞLATILIYOR ---")
    
    # 1. PYTHON WORKSHOP Verisi (sonra üzerinde çalışırken net olması için)
    python_workshop_data = {
        'name': "Python ile Veri Bilimi Workshop'u",
        'location': "Çevrimiçi (Zoom)",
        'start_date': "2026-11-20 10:00",
        'end_date': "2026-11-20 17:00",
        'capacity': 150,
        'price': 499.00,
        'description': "temel veri analizi."
    }
    
    # 2. Olayı Oluştur
    result = create_event(EVENTS, python_workshop_data)
    
    if result["success"]:
        new_event = result["event"]
        event_id = new_event['id']
        print(f" Etkinlik Oluşturuldu: '{new_event['name']}' ({event_id[:8]}...)")
        
        # 3. Örnek Oturumları Oluştur ve Ekle
        session1_data = {
            'title': "Python Kurulumu ve Ortam Yönetimi",
            'speaker': "Can Deniz",
            'room': "Ana Salon (Online)",
            'capacity': 150
        }
        session2_data = {
            'title': "Veri Manipülasyonu",
            'speaker': "Ayşe Can",
            'room': "Ana Salon (Online)",
            'capacity': 150
        }
        
        add_session(EVENTS, event_id, session1_data)
        add_session(EVENTS, event_id, session2_data)
        
        sessions = list_sessions(EVENTS, event_id)
        print(f"   --> {len(sessions)} oturum eklendi. İlk oturum: '{sessions[0]['title']}'")
        
        # 4. Veriyi Kaydet (storage.py çağrılır)
        save_system_state() 
    else:
        print(f" DEMO BAŞARISIZ: {result['error']}")
        
    print("--- DEMO SONU ---\n") #yardım aldığım 2.kısım 

# main.py dosyasında hazırlanacak örnek katılımcı verisi
zeynep_profile = {
    'name': "Zeynep Akar",
    'email': "zeynep.zeynep@tekno.com",
    'organization': "Tekno Yazılım",
    'contact_info': "5551234567",
    'dietary_needs': "Vejetaryen",
    'pin': "1234" # Kullanıcının belirlediği PIN kodu
}
#2.hafta için demo. 
import os
import sys

# --- Modülleri İçe Aktar ---
# events.py'den
from events import create_event, add_session, load_events, save_events
# attendees.py'den
from attendees import register_attendee, authenticate_attendee, load_attendees, save_attendees
# registration.py'den YENİ EKLENENLER
from registration import create_registration, promote_waitlist, cancel_registration, load_registrations, save_registrations
# storage.py'den
from storage import backup_state 

# --- Global Durum Değişkenleri ---
# Program çalıştıkça tüm veriler bu listelerde tutulur
EVENTS = []
ATTENDEES = [] 
REGISTRATIONS = [] 
DATA_DIR = "data"

def initialize_system():

    global EVENTS, ATTENDEES, REGISTRATIONS
    print("Sistem başlatılıyor...")
    

    EVENTS = load_events()
    ATTENDEES = load_attendees()
    REGISTRATIONS = load_registrations()
    
    print(f"Veriler yüklendi: {len(EVENTS)} olay, {len(ATTENDEES)} katılımcı, {len(REGISTRATIONS)} kayıt.")

def save_system_state():

    save_events(EVENTS)
    save_attendees(ATTENDEES)
    save_registrations(REGISTRATIONS)
    print("Sistem durumu başarıyla kaydedildi.")

# --- HAFTA 2 DEMO VE TEST FONKSİYONU ---

def run_registration_demo():

    global EVENTS, ATTENDEES, REGISTRATIONS
    
    # Demodan önce listeleri temizleyelim
    EVENTS.clear() 
    ATTENDEES.clear()

    print("\n--- HAFTA 2: KAYIT AKIŞI DEMOSU BAŞLATILIYOR ---")

    # 1. Olayı Oluştur (events.py testi)
    workshop_data = {
        'name': "Python Workshop", 'location': "Online", 'start_date': "2026-11-20 10:00",
        'end_date': "2026-11-20 17:00", 'capacity': 1, # Kapasiteyi 1 tuttuk, bekleme listesini test etmek için
        'price': 499.00, 'description': "Veri Bilimi."
    }
    event_result = create_event(EVENTS, workshop_data)
    if not event_result["success"]: return print(f" Olay Hatası: {event_result['error']}")
    event_id = EVENTS[0]['id']
    print(f" Olay Oluşturuldu: ID: {event_id[:8]}... (Kapasite: 1)")

    # 2. Katılımcı Kaydı (attendees.py testi)
    zeynep_profile = {
        'name': "Zeynep Akar", 'email': "zeynep.akar@techco.com", 'organization': "TechCo",
        'contact_info': "555123", 'pin': "1234"
    }
    attendee_result = register_attendee(ATTENDEES, zeynep_profile)
    if not attendee_result["success"]: return print(f" Katılımcı Hatası: {attendee_result['error']}")
    attendee_id_zeynep = ATTENDEES[0]['id']
    print(f" Katılımcı Kaydedildi: {zeynep_profile['name']}")

    # 3. Kayıt 1: Zeynep (Onaylanmış Olmalı - Kapasite 1/1)
    print("\n--- 3.1: İlk Kayıt (Onaylanmış) ---")
    reg_data_zeynep = {'event_id': event_id, 'attendee_id': attendee_id_zeynep, 'ticket_type': 'Standard', 'price': 499.00}
    reg_result_zeynep = create_registration(REGISTRATIONS, reg_data_zeynep, EVENTS)
    print(f" Zeynep Kaydı: Durum: {reg_result_zeynep['registration']['status']}")

    # 4. Kayıt 2: Ahmet (Bekleme Listesi Olmalı - Kapasite 1/1)
    print("\n--- 3.2: İkinci Kayıt (Bekleme Listesi Testi) ---")
    ahmet_profile = {'name': "Ahmet Can", 'email': "ahmet.can@test.com", 'organization': "TestCorp", 'contact_info': "555987", 'pin': "4321"}
    register_attendee(ATTENDEES, ahmet_profile)
    attendee_id_ahmet = ATTENDEES[1]['id']

    reg_data_ahmet = {'event_id': event_id, 'attendee_id': attendee_id_ahmet, 'ticket_type': 'Standard', 'price': 499.00}
    reg_result_ahmet = create_registration(REGISTRATIONS, reg_data_ahmet, EVENTS)
    print(f" Ahmet Kaydı: Durum: {reg_result_ahmet['registration']['status']}")
    
    # 5. Kaydı İptal Et ve Terfi Ettir (registration.py testi)
    print("\n--- 3.3: İptal ve Bekleme Listesi Terfisi ---")
    
    # Zeynep'in kaydını iptal et
    cancel_result = cancel_registration(REGISTRATIONS, reg_result_zeynep['registration']['id'], EVENTS)
    print(f" Zeynep İptal Edildi: Durum: {cancel_result['registration']['status']}")
    
    # Ahmet'in otomatik terfi edip etmediğini kontrol et
    promoted_check = next((r for r in REGISTRATIONS if r['attendee_id'] == attendee_id_ahmet), None)
    print(f" Ahmet'in Yeni Durumu: {promoted_check['status']} (Terfi başarılıysa 'Confirmed' olmalı)")

    # 6. Veriyi Kaydet
    save_system_state() 
    print(f"\n Tüm işlemler tamamlandı ve veriler JSON dosyalarına kaydedildi.")

# --- Ana Menü ---

def organizer_menu():
    
    while True:
        print("\n==============================")
        print(" ORGANİZATÖR ANA MENÜSÜ")
        print("==============================")
        print("1. Olay Yönetimi (Detaylı Menü)")
        print("2. Haftalık Demo Testini Çalıştır (Kayıt ve Bekleme Listesi)")
        print("3. Veri Yedekleme Oluştur")
        print("4. Çıkış ve Kaydet")
        
        choice = input("Seçiminizi girin: ")

        if choice == '1':
            print("İleride Olay, Oturum ve Kayıt Yönetimi menüleri buraya eklenecektir.")
        elif choice == '2':
            run_registration_demo()
        elif choice == '3':
            backup_state()
            print("Yedekleme başarılı.")
        elif choice == '4':
            save_system_state()
            print("Sistem kapatılıyor. İyi günler!")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

# --- Program Başlangıcı ---
if __name__ == "__main__":
    initialize_system()
    organizer_menu()

       
    
    
