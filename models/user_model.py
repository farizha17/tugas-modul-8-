import hashlib

from models.database import get_connection


class UserModel:

    def hash_password(self, password):
        return hashlib.sha256(
            password.encode("utf-8")
        ).hexdigest()

    def autentikasi(self, username, password):

        connection = get_connection()

        if connection is None:
            return None

        cursor = None

        try:
            cursor = connection.cursor(dictionary=True)

            password_hash = self.hash_password(password)

            sql = """
                SELECT id_user, username, role
                FROM users
                WHERE username = %s
                AND password = %s
            """

            cursor.execute(
                sql,
                (username, password_hash)
            )

            user = cursor.fetchone()

            return user

        except Exception as e:
            print(f"Gagal melakukan autentikasi: {e}")
            return None

        finally:

            if cursor is not None:
                cursor.close()

            connection.close()