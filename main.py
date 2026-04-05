import time
import os
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel, InputPeerChat

# --- GİRİŞ BİLGİLERİ (DEVELOPED BY C4HEX) ---
API_ID = 'API_ID'
API_HASH = 'API_HASH'
SESSION_NAME = 'c4hex_session'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("""
    ###########################################
    #                                         #
    #      TELEGRAM AUTO MESSAGE BOT          #
    #          Developed by c4hex              #
    #                                         #
    ###########################################
    """)

def main():
    clear()
    banner()
    
    # Giriş
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    client.start()
    
    print("\n[+] Giriş Başarılı! Kanallar taranıyor...")
    
    
    dialogs = client.get_dialogs()
    targets = [d for d in dialogs if d.is_channel or d.is_group]
    
    print(f"[+] Toplam {len(targets)} hedef bulundu.")
    
    
    print("-" * 30)
    message = input("[?] Gönderilecek Mesaj: ")
    try:
        delay = int(input("[?] Kaç saniyede bir gönderilsin? (Örn: 60): "))
    except ValueError:
        print("[!] Geçersiz saniye! Varsayılan 60 sn ayarlandı.")
        delay = 60
    
    print("\n[!] İşlem Başlıyor... Durdurmak için CTRL+C yapın.\n")
    
    while True:
        for target in targets:
            try:
                client.send_message(target.id, message)
                print(f"[SUCCESS] Mesaj Gitti -> {target.name}")
                time.sleep(delay)
            except Exception as e:
                print(f"[ERROR] Gönderilemedi ({target.name}): {e}")
                
                time.sleep(5)
                continue

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Program kullanıcı tarafından kapatıldı.")
