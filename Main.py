import os
import sys

# Proje dizinini Python yolu (path) için ekle
# NOT: GitHub web arayüzünde bu satırlar çalışmaz, ancak yerel ortamınızda çalışacaktır.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Modülleri içe aktar
from events import create_event, Event, Session
from storage import load_state, save_state

# --- Global Durum Değişkenleri ---
# Tüm veriler bu listelerde tutulacak
EVENTS = []
ATTENDEES = []
REGISTRATIONS = []
DATA_DIR = "data"

def initialize_system():
    """Sistem başladığında tüm verileri diskten yükler."""
    global EVENTS, ATTENDEES, REGISTRATIONS
    print("Sistem başlatılıyor...")
    
    # Tüm verileri yükle
    try:
        EVENTS, ATTENDEES, REGISTRATIONS = load_state(DATA_DIR)
        print(f"Veriler başarıyla yüklendi. Yüklü olay sayısı: {len(EVENTS)}")
    except Exception as e:
        print(f"Veri yüklenirken bir hata oluştu: {e}. Boş listelerle devam ediliyor.")

def save_system_state():
    """Tüm verileri diske kaydeder."""
    try:
        save_state(DATA_DIR, EVENTS, ATTENDEES, REGISTRATIONS)
        print("Sistem durumu başarıyla kaydedildi.")
    except Exception as e:
        print(f"Veri kaydedilirken bir hata oluştu: {e}")

def organizer_menu():
    """Organizatör için ana menü."""
    while True:
        print("\n--- Organizatör Ana Menüsü ---")
        print("1. Yeni Olay Oluştur")
        print("2. Mevcut Olayları Listele")
        print("3. Çıkış ve Kaydet")
        
        choice = input("Seçiminizi girin: ")

        if choice == '1':
            handle_create_event()
        elif choice == '2':
            list_events()
        elif choice == '3':
            save_system_state()
            print("Sistem kapatılıyor. İyi günler!")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

def handle_create_event():
    """Kullanıcıdan olay bilgilerini alır ve olayı oluşturur."""
    print("\n--- Yeni Olay Oluşturma ---")
    event_data = {}
    
    # Kullanıcıdan giriş alma (Proje gereksinimi: Validation ve Exception Handling)
    try:
        event_data['name'] = input("Olay Adı: ")
        event_data['location'] = input("Konum: ")
        event_data['start_date'] = input("Başlangıç Tarihi (YYYY-MM-DD HH:MM): ")
        event_data['end_date'] = input("Bitiş Tarihi (YYYY-MM-DD HH:MM): ")
        event_data['capacity'] = int(input("Kapasite (Sayı): "))
        event_data['price'] = float(input("Fiyat (Sayı): "))
        event_data['description'] = input("Açıklama: ")
    except ValueError:
        print("Hata: Kapasite ve Fiyat sayısal bir değer olmalıdır.")
        return

    # events.py'deki fonksiyonu çağır
    result = create_event(EVENTS, event_data)
    
    if result["success"]:
        print(f"Başarılı: '{result['event']['name']}' olayı oluşturuldu.")
        # Olayı oluşturduktan sonra durumu otomatik kaydet
        save_system_state() 
    else:
        print(f"Hata: Olay oluşturulamadı. {result['error']}")

def list_events():
    """Mevcut olayları ve temel bilgilerini listeler."""
    if not EVENTS:
        print("Henüz oluşturulmuş bir olay bulunmamaktadır.")
        return
        
    print("\n--- Mevcut Olaylar ---")
    for i, event in enumerate(EVENTS, 1):
        print(f"{i}. Ad: {event['name']}, Konum: {event['location']}, Kapasite: {event['capacity']}, Fiyat: {event['price']:.2f} TL, ID: {event['id']}")

# --- Program Başlangıcı ---
if __name__ == "__main__":
    initialize_system() # Verileri yükle
    organizer_menu()     # Organizatör menüsünü başlat

