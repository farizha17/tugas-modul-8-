import tkinter as tk
from tkinter import messagebox


class LoginView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.root.title("Login - Sistem Informasi Perpustakaan")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f6f9")

        self.buat_tampilan()

    def buat_tampilan(self):
        frame = tk.Frame(
            self.root,
            bg="white",
            padx=30,
            pady=30
        )
        frame.pack(expand=True, fill="both", padx=40, pady=30)

        tk.Label(
            frame,
            text="SISTEM INFORMASI",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#243447"
        ).pack(pady=(5, 0))

        tk.Label(
            frame,
            text="PERPUSTAKAAN",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#243447"
        ).pack(pady=(0, 20))

        tk.Label(
            frame,
            text="Username",
            font=("Arial", 10),
            bg="white"
        ).pack(anchor="w")

        self.entry_username = tk.Entry(
            frame,
            font=("Arial", 11)
        )
        self.entry_username.pack(fill="x", pady=(5, 12))

        tk.Label(
            frame,
            text="Password",
            font=("Arial", 10),
            bg="white"
        ).pack(anchor="w")

        self.entry_password = tk.Entry(
            frame,
            font=("Arial", 11),
            show="*"
        )
        self.entry_password.pack(fill="x", pady=(5, 15))

        self.btn_login = tk.Button(
            frame,
            text="Login",
            font=("Arial", 10, "bold"),
            bg="#0d6efd",
            fg="white",
            width=20,
            command=self.login
        )
        self.btn_login.pack(pady=5)

        tk.Label(
            frame,
            text="Gunakan akun yang telah terdaftar.",
            font=("Arial", 8),
            bg="white",
            fg="#6c757d"
        ).pack(pady=(12, 0))

        self.entry_username.focus()

        self.root.bind("<Return>", lambda event: self.login())

    def login(self):
        username = self.entry_username.get().strip()
        password = self.entry_password.get()

        if not username or not password:
            messagebox.showwarning(
                "Peringatan",
                "Username dan password harus diisi."
            )
            return

        self.controller.login(username, password)

    def tampilkan_pesan_error(self, pesan):
        messagebox.showerror("Login Gagal", pesan)

    def tutup(self):
        self.root.destroy()