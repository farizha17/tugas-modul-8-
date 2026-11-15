import tkinter as tk
from tkinter import messagebox

from models.user_model import UserModel
from views.login_view import LoginView
from views.buku_view import BukuView
from models.buku_model import BukuModel
from controllers.buku_controller import BukuController


class AuthController:

    def __init__(self, root):
        self.root = root
        self.model = UserModel()

        self.login_view = LoginView(
            self.root,
            self
        )

    def login(self, username, password):

        user = self.model.autentikasi(
            username,
            password
        )

        if user is None:
            self.login_view.tampilkan_pesan_error(
                "Username atau password salah."
            )
            return

        role = user["role"]

        messagebox.showinfo(
            "Login Berhasil",
            f"Selamat datang, {user['username']}!\nRole: {role}"
        )

        self.buka_sistem(role)

    def buka_sistem(self, role):

        self.root.destroy()

        root = tk.Tk()

        root.title("Sistem Informasi Perpustakaan")
        root.geometry("500x400")
        root.resizable(False, False)
        root.configure(bg="#f4f6f9")

        # ==============================
        # HEADER
        # ==============================

        tk.Label(
            root,
            text="SISTEM INFORMASI PERPUSTAKAAN",
            font=("Arial", 16, "bold"),
            bg="#f4f6f9",
            fg="#243447"
        ).pack(pady=(30, 5))

        tk.Label(
            root,
            text=f"Login sebagai: {role.upper()}",
            font=("Arial", 10),
            bg="#f4f6f9",
            fg="#6c757d"
        ).pack(pady=(0, 25))

        # ==============================
        # BUKA DATA BUKU
        # ==============================

        def buka_buku():

            jendela = tk.Toplevel(root)

            buku_view = BukuView(jendela)

            buku_model = BukuModel()

            BukuController(
                buku_view,
                buku_model,
                role
            )

        tk.Button(
            root,
            text="Manajemen Data Buku",
            width=30,
            height=2,
            bg="#0d6efd",
            fg="white",
            font=("Arial", 10, "bold"),
            command=buka_buku
        ).pack(pady=10)

        # ==============================
        # LOGOUT
        # ==============================

        def logout():

            konfirmasi = messagebox.askyesno(
                "Logout",
                "Apakah kamu yakin ingin logout?"
            )

            if not konfirmasi:
                return

            root.destroy()

            login_root = tk.Tk()

            AuthController(login_root)

            login_root.mainloop()

        tk.Button(
            root,
            text="Logout",
            width=30,
            height=2,
            bg="#dc3545",
            fg="white",
            font=("Arial", 10, "bold"),
            command=logout
        ).pack(pady=10)

        root.mainloop()