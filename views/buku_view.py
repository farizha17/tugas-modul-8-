import tkinter as tk
from tkinter import ttk, messagebox


class BukuView:

    def __init__(self, root):
        self.root = root
        self.id_buku = None

        # Agar controller bisa menggunakan messagebox
        self.messagebox = messagebox

        self.root.title("Sistem Informasi Perpustakaan - Data Buku")
        self.root.geometry("850x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f6f9")

        self.buat_tampilan()

    def buat_tampilan(self):

        frame_form = tk.Frame(
            self.root,
            bg="white",
            padx=20,
            pady=20
        )
        frame_form.pack(
            fill="x",
            padx=20,
            pady=20
        )

        tk.Label(
            frame_form,
            text="DATA BUKU",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#243447"
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(0, 15)
        )

        tk.Label(
            frame_form,
            text="Judul Buku",
            bg="white"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=5
        )

        self.entry_judul = tk.Entry(
            frame_form,
            width=45
        )
        self.entry_judul.grid(
            row=1,
            column=1,
            pady=5,
            padx=10
        )

        tk.Label(
            frame_form,
            text="Penulis",
            bg="white"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=5
        )

        self.entry_penulis = tk.Entry(
            frame_form,
            width=45
        )
        self.entry_penulis.grid(
            row=2,
            column=1,
            pady=5,
            padx=10
        )

        tk.Label(
            frame_form,
            text="Tahun Terbit",
            bg="white"
        ).grid(
            row=3,
            column=0,
            sticky="w",
            pady=5
        )

        self.entry_tahun = tk.Entry(
            frame_form,
            width=45
        )
        self.entry_tahun.grid(
            row=3,
            column=1,
            pady=5,
            padx=10
        )

        frame_button = tk.Frame(
            self.root,
            bg="#f4f6f9"
        )
        frame_button.pack(
            fill="x",
            padx=20,
            pady=(0, 10)
        )

        self.btn_update = tk.Button(
            frame_button,
            text="Perbarui Data (Update)",
            bg="#0d6efd",
            fg="white",
            width=22,
            command=self.update_buku
        )
        self.btn_update.pack(
            side="left",
            padx=5
        )

        self.btn_delete = tk.Button(
            frame_button,
            text="Hapus Data (Delete)",
            bg="#dc3545",
            fg="white",
            width=22,
            command=self.delete_buku
        )
        self.btn_delete.pack(
            side="left",
            padx=5
        )

        self.btn_bersihkan = tk.Button(
            frame_button,
            text="Bersihkan Form",
            bg="#6c757d",
            fg="white",
            width=18,
            command=self.bersihkan_form
        )
        self.btn_bersihkan.pack(
            side="left",
            padx=5
        )

        frame_tabel = tk.Frame(
            self.root,
            bg="white"
        )
        frame_tabel.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        self.tabel = ttk.Treeview(
            frame_tabel,
            columns=(
                "id",
                "judul",
                "penulis",
                "tahun"
            ),
            show="headings"
        )

        self.tabel.heading(
            "id",
            text="ID"
        )

        self.tabel.heading(
            "judul",
            text="Judul"
        )

        self.tabel.heading(
            "penulis",
            text="Penulis"
        )

        self.tabel.heading(
            "tahun",
            text="Tahun Terbit"
        )

        self.tabel.column(
            "id",
            width=60,
            anchor="center"
        )

        self.tabel.column(
            "judul",
            width=250
        )

        self.tabel.column(
            "penulis",
            width=220
        )

        self.tabel.column(
            "tahun",
            width=120,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            frame_tabel,
            orient="vertical",
            command=self.tabel.yview
        )

        self.tabel.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabel.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tabel.bind(
            "<<TreeviewSelect>>",
            self.pilih_buku
        )

    def pilih_buku(self, event=None):

        selected = self.tabel.selection()

        if not selected:
            return

        data = self.tabel.item(selected[0])
        values = data["values"]

        self.id_buku = values[0]

        self.entry_judul.delete(0, tk.END)
        self.entry_judul.insert(0, values[1])

        self.entry_penulis.delete(0, tk.END)
        self.entry_penulis.insert(0, values[2])

        self.entry_tahun.delete(0, tk.END)
        self.entry_tahun.insert(0, values[3])

    def update_buku(self):
        pass

    def delete_buku(self):
        pass

    def bersihkan_form(self):

        self.id_buku = None

        self.entry_judul.delete(0, tk.END)
        self.entry_penulis.delete(0, tk.END)
        self.entry_tahun.delete(0, tk.END)

        selected = self.tabel.selection()

        if selected:
            self.tabel.selection_remove(selected)

        self.entry_judul.focus()