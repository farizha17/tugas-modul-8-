import hashlib

from models.user_model import UserModel


def test_hash_password():
    model = UserModel()

    password = "admin123"

    hasil = model.hash_password(password)

    expected = hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()

    assert hasil == expected


def test_hash_password_berbeda():
    model = UserModel()

    password1 = "admin123"
    password2 = "user123"

    hasil1 = model.hash_password(password1)
    hasil2 = model.hash_password(password2)

    assert hasil1 != hasil2


def test_autentikasi_admin():
    model = UserModel()

    user = model.autentikasi(
        "petugas",
        "admin123"
    )

    assert user is not None
    assert user["username"] == "petugas"
    assert user["role"] == "admin"


def test_autentikasi_gagal():
    model = UserModel()

    user = model.autentikasi(
        "petugas",
        "password_salah"
    )

    assert user is None