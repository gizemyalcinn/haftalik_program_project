import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database):
        """Veritabanı bağlantısı için gerekli parametreleri alır."""
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        """Veritabanına bağlantı sağlar ve bağlantıyı döner."""
        try:
            return mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except Error as err:
            print(f"Bağlantı hatası: {err}")
            return None

    def execute_query(self, query, values=None):
        """Veritabanına bir sorgu gönderir ve çalıştırır."""
        conn = self.connect()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute(query, values)
                conn.commit()  # Değişiklikleri kaydeder
            except Error as err:
                print(f"Hata: {err}")
            finally:
                cursor.close()
                conn.close()

    def fetch_all(self, query, values=None):
        """Veritabanından tüm veriyi çeker."""
        conn = self.connect()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute(query, values)
                result = cursor.fetchall()
                return result
            except Error as err:
                print(f"Hata: {err}")
                return None
            finally:
                cursor.close()
                conn.close()

    def fetch_one(self, query, values=None):
        """Veritabanından yalnızca bir sonucu çeker."""
        conn = self.connect()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute(query, values)
                result = cursor.fetchone()  # Sadece bir sonuç alıyoruz
                return result
            except Error as err:
                print(f"Hata: {err}")
                return None
            finally:
                cursor.close()
                conn.close()

    def create_tables(self):
        """Veritabanındaki tabloları oluşturur."""
        query_bolum = """
        CREATE TABLE IF NOT EXISTS Bolum (
            bolum_kodu VARCHAR(10) PRIMARY KEY,
            bolum_adi TEXT NOT NULL
        );
        """
        query_derslik = """
        CREATE TABLE IF NOT EXISTS Derslik (
            derslik_id VARCHAR(50) PRIMARY KEY,
            kapasite INT NOT NULL,
            statu TEXT CHECK(statu IN ('NORMAL', 'LAB')) NOT NULL
        );
        """
        query_kullanici = """
        CREATE TABLE IF NOT EXISTS Kullanici (
            id INT PRIMARY KEY AUTO_INCREMENT,
            ad_soyad TEXT NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            parola TEXT NOT NULL,
            role ENUM('Öğretim Üyesi', 'Öğrenci', 'Yönetici') NOT NULL
        );
        """
        query_dersler = """
        CREATE TABLE IF NOT EXISTS Dersler (
            ders_kodu VARCHAR(20) PRIMARY KEY,
            ders_adi TEXT NOT NULL,
            haftalik_saat INT NOT NULL,
            ogretim_uyesi_id INT NOT NULL,
            bolum_kodu VARCHAR(10) NOT NULL,
            derslik_id VARCHAR(50) NOT NULL,
            donem INT NOT NULL,
            akts INT NOT NULL,
            ders_turu ENUM('Zorunlu', 'Seçmeli') NOT NULL,
            FOREIGN KEY (ogretim_uyesi_id) REFERENCES Kullanici(id),
            FOREIGN KEY (bolum_kodu) REFERENCES Bolum(bolum_kodu),
            FOREIGN KEY (derslik_id) REFERENCES Derslik(derslik_id)
        );
        """
        # Tabloları oluştur
        self.execute_query(query_bolum)
        self.execute_query(query_derslik)
        self.execute_query(query_kullanici)
        self.execute_query(query_dersler)
