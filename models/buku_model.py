from models.database import get_connection


class BukuModel:

    def update_buku(self, id_buku, judul, penulis, tahun_terbit):
        connection = get_connection()

        if connection is None:
            return False

        try:
            cursor = connection.cursor()

            sql = """
                UPDATE buku
                SET judul = %s,
                    penulis = %s,
                    tahun_terbit = %s
                WHERE id_buku = %s
            """

            values = (
                judul,
                penulis,
                tahun_terbit,
                id_buku
            )

            cursor.execute(sql, values)
            connection.commit()

            berhasil = cursor.rowcount > 0

            cursor.close()

            return berhasil

        except Exception as e:
            print(f"Gagal mengubah data buku: {e}")
            connection.rollback()
            return False

        finally:
            connection.close()

    def delete_buku(self, id_buku):
        connection = get_connection()

        if connection is None:
            return False

        try:
            cursor = connection.cursor()

            sql = "DELETE FROM buku WHERE id_buku = %s"

            cursor.execute(sql, (id_buku,))
            connection.commit()

            berhasil = cursor.rowcount > 0

            cursor.close()

            return berhasil

        except Exception as e:
            print(f"Gagal menghapus data buku: {e}")
            connection.rollback()
            return False

        finally:
            connection.close()

    def tampil_buku(self):
        connection = get_connection()

        if connection is None:
            return []

        try:
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                "SELECT * FROM buku ORDER BY id_buku"
            )

            data = cursor.fetchall()

            cursor.close()

            return data

        except Exception as e:
            print(f"Gagal menampilkan data buku: {e}")
            return []

        finally:
            connection.close()

    def get_all_buku(self):
        connection = get_connection()

        if connection is None:
            return []

        try:
            cursor = connection.cursor(dictionary=True)

            cursor.execute(
                "SELECT * FROM buku ORDER BY id_buku"
            )

            data = cursor.fetchall()

            cursor.close()

            return data

        except Exception as e:
            print(f"Gagal mengambil data buku: {e}")
            return []

        finally:
            connection.close()