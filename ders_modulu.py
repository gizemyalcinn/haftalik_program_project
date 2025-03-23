from database import Database

class DersProgrami:
    def __init__(self, db: Database):
        self.db = db

    # Öğretim üyelerinin listesini, sadece Öğretim Üyesi rolüne sahip kullanıcılar için gösterme
    def ogretim_uyesi_listesi(self):
        query = "SELECT id, ad_soyad FROM Kullanici WHERE role = 'Öğretim Üyesi'"
        result = self.db.fetch_all(query)
        if result:
            print("\nÖğretim Üyeleri Listesi:")
            for row in result:
                print(f"ID: {row[0]}, Adı Soyadı: {row[1]}")
        else:
            print("Öğretim üyesi bulunamadı.")

    # Ders ekleme fonksiyonu
    def ders_ekle(self, ders_kodu, ders_adi, haftalik_saat, ogretim_uyesi_id, bolum_kodu, derslik_id, donem, akts, ders_turu):
        query = """
        INSERT INTO Dersler (ders_kodu, ders_adi, haftalik_saat, ogretim_uyesi_id, bolum_kodu, derslik_id, donem, akts, ders_turu)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (ders_kodu, ders_adi, haftalik_saat, ogretim_uyesi_id, bolum_kodu, derslik_id, donem, akts, ders_turu)
        try:
            self.db.execute_query(query, values)
            print(f"{ders_kodu} kodlu ders başarıyla eklendi.")
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

    # Ders düzenleme fonksiyonu
    def ders_duzenle(self, ders_kodu, yeni_ders_kodu, yeni_ders_adi, yeni_haftalik_saat, yeni_ogretim_uyesi_id, yeni_bolum_kodu, yeni_derslik_id, yeni_donem, yeni_akts, yeni_ders_turu):
        query = """
        UPDATE Dersler
        SET ders_kodu = %s, ders_adi = %s, haftalik_saat = %s, ogretim_uyesi_id = %s, bolum_kodu = %s, derslik_id = %s, donem = %s, akts = %s, ders_turu = %s
        WHERE ders_kodu = %s
        """
        values = (yeni_ders_kodu, yeni_ders_adi, yeni_haftalik_saat, yeni_ogretim_uyesi_id, yeni_bolum_kodu, yeni_derslik_id, yeni_donem, yeni_akts, yeni_ders_turu, ders_kodu)
        try:
            self.db.execute_query(query, values)
            print(f"{ders_kodu} kodlu ders başarıyla güncellendi.")
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

    # Ders silme fonksiyonu
    def ders_sil(self, ders_kodu):
        query = "DELETE FROM Dersler WHERE ders_kodu = %s"
        values = (ders_kodu,)
        try:
            self.db.execute_query(query, values)
            print(f"{ders_kodu} kodlu ders başarıyla silindi.")
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
