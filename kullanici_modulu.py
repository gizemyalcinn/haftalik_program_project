from database import Database

class KullaniciModulu:
    def __init__(self, db):
        self.db = db

    def kullanici_ekle(self, ad_soyad, email, parola, role):
        query = "INSERT INTO Kullanici (ad_soyad, email, parola, role) VALUES (%s, %s, %s, %s)"
        params = (ad_soyad, email, parola, role)
        self.db.execute_query(query, params)
        print(f"{ad_soyad} adlı kullanıcı başarıyla eklendi.")

    def kullanici_sil(self, kullanici_id):
        query = "DELETE FROM Kullanici WHERE id = %s"
        params = (kullanici_id,)
        self.db.execute_query(query, params)
        print(f"Kullanıcı ID {kullanici_id} başarıyla silindi.")

    def kullanici_listesi(self):
        query = "SELECT * FROM Kullanici"
        result = self.db.execute_query(query)
        for user in result:
            print(f"ID: {user[0]}, Ad Soyad: {user[1]}, Email: {user[2]}, Role: {user[4]}")
