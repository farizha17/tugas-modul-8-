class BukuController:

    def __init__(self, view, model, user_role="anggota"):
        self.view = view
        self.model = model
        self.user_role = user_role

        self.view.btn_update.config(
            command=self.update_buku
        )

        self.view.btn_delete.config(
            command=self.delete_buku
        )

        self.tampilkan_buku()
        self.atur_hak_akses()

    def tampilkan_buku(self):

        data_buku = self.model.get_all_buku()

        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        for buku in data_buku:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    buku["id_buku"],
                    buku["judul"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    def atur_hak_akses(self):

        if self.user_role != "admin":
            self.view.btn_update.config(
                state="disabled"
            )

            self.view.btn_delete.config(
                state="disabled"
            )

    def update_buku(self):

        if self.user_role != "admin":
            self.view.messagebox.showwarning(
                "Akses Ditolak",
                "Hanya admin yang dapat memperbarui data buku."
            )
            return

        if self.view.id_buku is None:
            self.view.messagebox.showwarning(
                "Peringatan",
                "Pilih data buku dari tabel yang ingin diperbarui."
            )
            return

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            self.view.messagebox.showwarning(
                "Peringatan",
                "Semua data buku harus diisi."
            )
            return

        try:
            tahun = int(tahun)

        except ValueError:
            self.view.messagebox.showwarning(
                "Peringatan",
                "Tahun terbit harus berupa angka."
            )
            return

        konfirmasi = self.view.messagebox.askyesno(
            "Konfirmasi",
            "Apakah kamu yakin ingin memperbarui data buku ini?"
        )

        if not konfirmasi:
            return

        berhasil = self.model.update_buku(
            self.view.id_buku,
            judul,
            penulis,
            tahun
        )

        if berhasil:
            self.view.messagebox.showinfo(
                "Berhasil",
                "Data buku berhasil diperbarui."
            )

            self.view.bersihkan_form()
            self.tampilkan_buku()

        else:
            self.view.messagebox.showerror(
                "Gagal",
                "Data buku gagal diperbarui."
            )

    def delete_buku(self):

        if self.user_role != "admin":
            self.view.messagebox.showwarning(
                "Akses Ditolak",
                "Hanya admin yang dapat menghapus data buku."
            )
            return

        if self.view.id_buku is None:
            self.view.messagebox.showwarning(
                "Peringatan",
                "Pilih data buku dari tabel yang ingin dihapus."
            )
            return

        konfirmasi = self.view.messagebox.askyesno(
            "Konfirmasi Hapus",
            "Apakah kamu yakin ingin menghapus data buku ini?"
        )

        if not konfirmasi:
            return

        berhasil = self.model.delete_buku(
            self.view.id_buku
        )

        if berhasil:
            self.view.messagebox.showinfo(
                "Berhasil",
                "Data buku berhasil dihapus."
            )

            self.view.bersihkan_form()
            self.tampilkan_buku()

        else:
            self.view.messagebox.showerror(
                "Gagal",
                "Data buku gagal dihapus."
            )