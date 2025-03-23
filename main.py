from database import Database
from ders_modulu import DersProgrami  # dosya adı değiştiği için import da değişti
from kullanici_modulu import KullaniciModulu  # Kullanıcı modülünü ekliyoruz
from derslik_modulu import DerslikModulu  # Derslik modülünü ekliyoruz

# Ders Modülü
def ders_modulu(db):
    ders_programi = DersProgrami(db)

    while True:
        print("\nDers Programı Yönetimi:")
        print("1. Ders Ekle")
        print("2. Ders Düzenle")
        print("3. Ders Sil")
        print("4. Geri Dön")

        secim = input("Seçiminizi yapın (1/2/3/4): ")

        if secim == "1":
            print("\nDers ekleme işlemine başlıyoruz. Lütfen aşağıdaki bilgileri girin.")
            ders_kodu = input("Ders Kodu (Örneğin: A101): ")
            ders_adi = input("Ders Adı (Örneğin: Yazılım Mühendisliği): ")
            haftalik_saat = int(input("Haftalık Saat (Örneğin: 3): "))

            # Öğretim Üyesi ID'sini alırken listeyi göster
            ders_programi.ogretim_uyesi_listesi()
            ogretim_uyesi_id = int(input("Öğretim Üyesi ID (Örneğin: 20): "))
            
            bolum_kodu = input("Bölüm Kodu (Örneğin: BLM): ")
            derslik_id = input("Derslik ID (Örneğin: S101): ")
            donem = int(input("Dönem (Örneğin: 1): "))
            akts = int(input("AKTS (Örneğin: 5): "))
            ders_turu = input("Ders Türü (Zorunlu/Seçmeli): ")

            ders_programi.ders_ekle(ders_kodu, ders_adi, haftalik_saat, ogretim_uyesi_id, bolum_kodu, derslik_id, donem, akts, ders_turu)

        elif secim == "2":
            print("\nDers düzenleme işlemine başlıyoruz. Lütfen aşağıdaki bilgileri girin.")
            ders_kodu = input("Düzenlemek istediğiniz Ders Kodu: ")
            yeni_ders_kodu = input("Yeni Ders Kodu (Ders kodu değiştirebilirsiniz): ")
            yeni_ders_adi = input("Yeni Ders Adı: ")
            yeni_haftalik_saat = int(input("Yeni Haftalık Saat: "))

            # Öğretim Üyesi ID'sini alırken listeyi göster
            ders_programi.ogretim_uyesi_listesi()
            yeni_ogretim_uyesi_id = int(input("Yeni Öğretim Üyesi ID: "))
            
            yeni_bolum_kodu = input("Yeni Bölüm Kodu: ")
            yeni_derslik_id = input("Yeni Derslik ID: ")
            yeni_donem = int(input("Yeni Dönem: "))
            yeni_akts = int(input("Yeni AKTS: "))
            yeni_ders_turu = input("Yeni Ders Türü (Zorunlu/Seçmeli): ")

            ders_programi.ders_duzenle(ders_kodu, yeni_ders_kodu, yeni_ders_adi, yeni_haftalik_saat, yeni_ogretim_uyesi_id, yeni_bolum_kodu, yeni_derslik_id, yeni_donem, yeni_akts, yeni_ders_turu)

        elif secim == "3":
            print("\nDers silme işlemine başlıyoruz. Silmek istediğiniz dersin bilgilerini girin.")
            ders_kodu = input("Silmek istediğiniz Ders Kodu (Örneğin: A101): ")
            ders_programi.ders_sil(ders_kodu)

        elif secim == "4":
            break  # Ders modülüne geri dön

        else:
            print("Geçersiz seçim, tekrar deneyin.")

# Kullanıcı Modülü
def kullanici_modulu(db):
    kullanici_modulu = KullaniciModulu(db)

    while True:
        print("\nKullanıcı Yönetimi: ")
        print("1. Kullanıcı Ekle")
        print("2. Kullanıcı Sil")
        print("3. Kullanıcı Listesi")
        print("4. Geri Dön")

        secim = input("Seçiminizi yapın (1/2/3/4): ")

        if secim == "1":
            ad_soyad = input("Ad Soyad: ")
            email = input("Email: ")
            parola = input("Parola: ")
            role = input("Role (Öğrenci/Öğretim Üyesi/Yönetici): ")
            kullanici_modulu.kullanici_ekle(ad_soyad, email, parola, role)
        elif secim == "2":
            kullanici_id = int(input("Silmek istediğiniz Kullanıcı ID: "))
            kullanici_modulu.kullanici_sil(kullanici_id)
        elif secim == "3":
            kullanici_modulu.kullanici_listesi()
        elif secim == "4":
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

# Derslik Modülü
def derslik_modulu(db):
    derslik_modulu = DerslikModulu(db)

    while True:
        print("\nDerslik Yönetimi: ")
        print("1. Derslik Ekle")
        print("2. Derslik Sil")
        print("3. Derslik Listesi")
        print("4. Geri Dön")

        secim = input("Seçiminizi yapın (1/2/3/4): ")

        if secim == "1":
            derslik_id = input("Derslik ID: ")
            kapasite = int(input("Kapasite: "))
            statu = input("Statu (NORMAL/LAB): ")
            derslik_modulu.derslik_ekle(derslik_id, kapasite, statu)
        elif secim == "2":
            derslik_id = input("Silmek istediğiniz Derslik ID: ")
            derslik_modulu.derslik_sil(derslik_id)
        elif secim == "3":
            derslik_modulu.derslik_listesi()
        elif secim == "4":
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

# Ana Menü
def main():
    db = Database(host="localhost", user="root", password="1234", database="app")

    while True:
        print("\nAna Menü: ")
        print("1. Ders Yönetimi")
        print("2. Kullanıcı Yönetimi")
        print("3. Derslik Yönetimi")
        print("4. Çıkış")

        secim = input("Seçiminizi yapın (1/2/3/4): ")

        if secim == "1":
            ders_modulu(db)  # Ders modülüne yönlendirme
        elif secim == "2":
            kullanici_modulu(db)  # Kullanıcı modülüne yönlendirme
        elif secim == "3":
            derslik_modulu(db)  # Derslik modülüne yönlendirme
        elif secim == "4":
            print("Çıkılıyor... Program sonlandırıldı.")
            break  # Program sonlanır
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    main()
