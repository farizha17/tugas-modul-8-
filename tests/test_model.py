import unittest

from models.database import get_connection
from models.buku_model import BukuModel
from models.anggota_model import AnggotaModel


class TestModel(unittest.TestCase):

    def setUp(self):
        self.buku = BukuModel()
        self.anggota = AnggotaModel()

        self.connection = get_connection()

        if self.connection is None:
            self.fail("Koneksi database gagal. Periksa MySQL Laragon.")

    def tearDown(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()

    def test_koneksi_database(self):
        self.assertTrue(self.connection.is_connected())
        print("\nKoneksi database berhasil.")

    def test_tampil_buku(self):
        data = self.buku.tampil_buku()

        self.assertIsInstance(data, list)

        print("\nDaftar Buku:")
        for buku in data:
            print(buku)

    def test_update_buku(self):
        cursor = self.connection.cursor()
        id_buku = None

        try:
            cursor.execute(
                """
                INSERT INTO buku (judul, penulis, tahun_terbit)
                VALUES (%s, %s, %s)
                """,
                ("Buku Sementara Update", "Penulis Uji", 2024)
            )
            id_buku = cursor.lastrowid
            self.connection.commit()

            hasil = self.buku.update_buku(
                id_buku,
                "Buku Hasil Update",
                "Penulis Baru",
                2025
            )

            self.assertTrue(hasil)

            cursor.execute(
                "SELECT judul, penulis, tahun_terbit FROM buku WHERE id_buku = %s",
                (id_buku,)
            )
            data = cursor.fetchone()

            self.assertIsNotNone(data)
            self.assertEqual(data[0], "Buku Hasil Update")
            self.assertEqual(data[1], "Penulis Baru")
            self.assertEqual(int(data[2]), 2025)

            print("\nPengujian UPDATE berhasil.")

        finally:
            if id_buku is not None:
                cursor.execute(
                    "DELETE FROM buku WHERE id_buku = %s",
                    (id_buku,)
                )
                self.connection.commit()

            cursor.close()

    def test_delete_buku(self):
        cursor = self.connection.cursor()
        id_buku = None

        try:
            cursor.execute(
                """
                INSERT INTO buku (judul, penulis, tahun_terbit)
                VALUES (%s, %s, %s)
                """,
                ("Buku Sementara Delete", "Penulis Uji", 2024)
            )
            id_buku = cursor.lastrowid
            self.connection.commit()

            hasil = self.buku.delete_buku(id_buku)
            self.assertTrue(hasil)

            cursor.execute(
                "SELECT * FROM buku WHERE id_buku = %s",
                (id_buku,)
            )
            self.assertIsNone(cursor.fetchone())

            print("\nPengujian DELETE berhasil.")

        finally:
            if id_buku is not None:
                cursor.execute(
                    "DELETE FROM buku WHERE id_buku = %s",
                    (id_buku,)
                )
                self.connection.commit()

            cursor.close()

    def test_tambah_dan_tampil_anggota(self):
        cursor = self.connection.cursor()
        nama = "Anggota Uji Tugas 4"

        try:
            cursor.execute(
                "DELETE FROM anggota WHERE nama = %s",
                (nama,)
            )
            self.connection.commit()
        finally:
            cursor.close()

        hasil = self.anggota.tambah_anggota(
            nama,
            "Alamat Uji Tugas 4"
        )
        self.assertTrue(hasil)

        data = self.anggota.tampil_anggota()
        ditemukan = any(item["nama"] == nama for item in data)

        self.assertTrue(ditemukan)
        print("\nPengujian tambah dan tampil anggota berhasil.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
