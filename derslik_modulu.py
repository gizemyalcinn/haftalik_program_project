from database import Database

class DerslikModulu:
    def __init__(self, db):
        self.db = db

    def derslik_ekle(self, derslik_id, kapasite, statu):
        query = "INSERT INTO Derslik (derslik_id, kapasite, statu) VALUES (%s, %s, %s)"
        params = (derslik_id, kapasite, statu)
        self.db.execute_query(query, params)
        print(f"{derslik_id} ID'li derslik başarıyla eklendi.")

    def derslik_sil(self, derslik_id):
        query = "DELETE FROM Derslik WHERE derslik_id = %s"
        params = (derslik_id,)
        self.db.execute_query(query, params)
        print(f"Derslik ID {derslik_id} başarıyla silindi.")

    def derslik_listesi(self):
        query = "SELECT * FROM Derslik"
        result = self.db.execute_query(query)
        for derslik in result:
            print(f"Derslik ID: {derslik[0]}, Kapasite: {derslik[1]}, Statu: {derslik[2]}")
