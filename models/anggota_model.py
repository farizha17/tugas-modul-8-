from models.database import get_connection


class AnggotaModel:

    def tambah_anggota(self, nama, alamat):
        connection = get_connection()

        if connection is None:
            return False

        try:
            cursor = connection.cursor()

            sql = """
                INSERT INTO anggota (nama, alamat)
                VALUES (%s, %s)
            """

            cursor.execute(sql, (nama, alamat))
            connection.commit()

            berhasil = cursor.rowcount > 0
            cursor.close()

            return berhasil

        except Exception as e:
            print(f"Gagal menambahkan anggota: {e}")
            connection.rollback()
            return False

        finally:
            connection.close()

    def tampil_anggota(self):
        connection = get_connection()

        if connection is None:
            return []

        try:
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                "SELECT id_anggota, nama, alamat "
                "FROM anggota ORDER BY id_anggota"
            )

            data = cursor.fetchall()
            cursor.close()

            return data

        except Exception as e:
            print(f"Gagal menampilkan anggota: {e}")
            return []

        finally:
            connection.close()