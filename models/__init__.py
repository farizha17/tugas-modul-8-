import unittest

from models.database import get_connection
from models.buku_model import BukuModel
from models.anggota_model import AnggotaModel


class TestModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = get_connection()

        if cls.connection is None:
            raise RuntimeError(
                "Koneksi database gagal. Periksa Laragon dan database."
            )

        cls.buku = BukuModel()
        cls.anggota = AnggotaModel()

    @classmethod
    def tearDownClass(cls):
        if cls.connection is not None:
            cls.connection.close()

    def test_koneksi_database(self):
        self.assertIsNotNone(self.connection)
        self.assertTrue(self.connection.is_connected())

    def test_tampil_buku(self):
        data = self.buku.tampil_buku()
        self.assertIsInstance(data, list)

        print("\nDaftar buku:")
        for buku in data:
            print(buku)

    def test_update_buku(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT id_buku FROM buku LIMIT 1")
        hasil = cursor.fetchone()

        cursor.close()
        connection.close()

        if hasil is None:
            self.skipTest("Tidak ada data buku untuk diuji.")

        id_buku = hasil[0]

        berhasil = self.buku.update_buku(
            id_buku,
            "Buku Uji Tugas 4",
            "Penulis Uji",
            2024
        )

        self.assertTrue(berhasil)

        print(f"\nBuku dengan ID {id_buku} berhasil diuji untuk UPDATE.")

    def test_tambah_dan_tampil_anggota(self):
        connection = get_connection()
        cursor = connection.cursor()

        nama_uji = "Anggota Uji Tugas 4"

        cursor.execute(
            "DELETE FROM anggota WHERE nama = %s",
            (nama_uji,)
        )
        connection.commit()

        cursor.close()
        connection.close()

        berhasil = self.anggota.tambah_anggota(
            nama_uji,
            "Alamat Uji"
        )

        self.assertTrue(berhasil)

        data = self.anggota.tampil_anggota()

        ditemukan = any(
            anggota["nama"] == nama_uji
            for anggota in data
        )

        self.assertTrue(ditemukan)

        print("\nDaftar anggota:")
        for anggota in data:
            print(anggota)

    def test_delete_buku(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO buku (judul, penulis, tahun_terbit)
            VALUES (%s, %s, %s)
            """,
            ("Buku Sementara", "Penulis Uji", 2024)
        )

        id_buku = cursor.lastrowid
        connection.commit()

        cursor.close()
        connection.close()

        berhasil = self.buku.delete_buku(id_buku)

        self.assertTrue(berhasil)

        print(f"\nBuku sementara ID {id_buku} berhasil dihapus.")


if __name__ == "__main__":
    unittest.main(verbosity=2)