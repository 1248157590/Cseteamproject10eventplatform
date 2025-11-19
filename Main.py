def run_week1_demo():
    """
    Python Workshop etkinliğini oluşturur.
    """
    global EVENTS # EVENTS listesini kullanmak için gereklidir
    print("\n--- PYTHON WORKSHOP DEMOSU BAŞLATILIYOR ---")
    
    # 1. PYTHON WORKSHOP Verisi
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
        
    print("--- DEMO SONU ---\n")

# main.py dosyasında hazırlanacak örnek katılımcı verisi
zeynep_profile = {
    'name': "Zeynep Akar",
    'email': "zeynep.zeynep@tekno.com",
    'organization': "Tekno Yazılım",
    'contact_info': "5551234567",
    'dietary_needs': "Vejetaryen",
    'pin': "1234" # Kullanıcının belirlediği PIN kodu
}


       
    
    
