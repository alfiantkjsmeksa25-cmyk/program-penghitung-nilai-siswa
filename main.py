import tkinter as tk
from tkinter import ttk, messagebox


class PenghitungNilaiSiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Penghitung Nilai Siswa")
        self.root.geometry("1100x700")
        self.root.minsize(950, 600)

        self.data_siswa = []

        # =========================
        # STYLE
        # =========================
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Treeview",
            rowheight=30,
            font=("Segoe UI", 10)
        )

        self.style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold")
        )

        self.style.configure(
            "TButton",
            font=("Segoe UI", 10, "bold"),
            padding=8
        )

        self.style.configure(
            "TLabel",
            font=("Segoe UI", 10)
        )

        # =========================
        # HEADER
        # =========================
        header = tk.Frame(
            root,
            bg="#1f4e78",
            height=75
        )
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="SISTEM PENGHITUNG NILAI SISWA",
            bg="#1f4e78",
            fg="white",
            font=("Segoe UI", 20, "bold")
        ).pack(pady=(12, 0))

        tk.Label(
            header,
            text="Aplikasi Pengolahan Nilai Siswa",
            bg="#1f4e78",
            fg="#d9eaf7",
            font=("Segoe UI", 10)
        ).pack()

        # =========================
        # FORM
        # =========================
        form_frame = tk.LabelFrame(
            root,
            text=" Data Siswa ",
            font=("Segoe UI", 11, "bold"),
            padx=15,
            pady=12
        )
        form_frame.pack(fill="x", padx=15, pady=12)

        # Variabel input
        self.nama_var = tk.StringVar()
        self.nis_var = tk.StringVar()
        self.tugas_var = tk.StringVar()
        self.uts_var = tk.StringVar()
        self.uas_var = tk.StringVar()
        self.kehadiran_var = tk.StringVar()

        # Variabel hasil
        self.nilai_akhir_var = tk.StringVar(value="-")
        self.grade_var = tk.StringVar(value="-")
        self.status_var = tk.StringVar(value="-")

        # Baris 1
        ttk.Label(form_frame, text="Nama Siswa").grid(
            row=0, column=0, sticky="w", padx=5, pady=5
        )

        ttk.Entry(
            form_frame,
            textvariable=self.nama_var,
            width=28
        ).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="NIS").grid(
            row=0, column=2, sticky="w", padx=5, pady=5
        )

        ttk.Entry(
            form_frame,
            textvariable=self.nis_var,
            width=20
        ).grid(row=0, column=3, padx=5, pady=5)

        # Baris 2
        ttk.Label(form_frame, text="Nilai Tugas").grid(
            row=1, column=0, sticky="w", padx=5, pady=5
        )

        ttk.Entry(
            form_frame,
            textvariable=self.tugas_var,
            width=15
        ).grid(row=1, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(form_frame, text="Nilai UTS").grid(
            row=1, column=2, sticky="w", padx=5, pady=5
        )

        ttk.Entry(
            form_frame,
            textvariable=self.uts_var,
            width=15
        ).grid(row=1, column=3, padx=5, pady=5, sticky="w")

        # Baris 3
        ttk.Label(form_frame, text="Nilai UAS").grid(
            row=2, column=0, sticky="w", padx=5, pady=5
        )

        ttk.Entry(
            form_frame,
            textvariable=self.uas_var,
            width=15
        ).grid(row=2, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(form_frame, text="Kehadiran").grid(
            row=2, column=2, sticky="w", padx=5, pady=5
        )

        ttk.Entry(
            form_frame,
            textvariable=self.kehadiran_var,
            width=15
        ).grid(row=2, column=3, padx=5, pady=5, sticky="w")

        # =========================
        # HASIL NILAI
        # =========================
        result_frame = tk.Frame(root)
        result_frame.pack(fill="x", padx=15, pady=5)

        self.create_result_card(
            result_frame,
            "NILAI AKHIR",
            self.nilai_akhir_var,
            0
        )

        self.create_result_card(
            result_frame,
            "GRADE",
            self.grade_var,
            1
        )

        self.create_result_card(
            result_frame,
            "STATUS",
            self.status_var,
            2
        )

        # =========================
        # TOMBOL
        # =========================
        button_frame = tk.Frame(root)
        button_frame.pack(fill="x", padx=15, pady=8)

        ttk.Button(
            button_frame,
            text="Hitung Nilai",
            command=self.hitung_nilai
        ).pack(side="left", padx=4)

        ttk.Button(
            button_frame,
            text="Tambah Data",
            command=self.tambah_data
        ).pack(side="left", padx=4)

        ttk.Button(
            button_frame,
            text="Edit Data",
            command=self.edit_data
        ).pack(side="left", padx=4)

        ttk.Button(
            button_frame,
            text="Hapus Data",
            command=self.hapus_data
        ).pack(side="left", padx=4)

        ttk.Button(
            button_frame,
            text="Reset",
            command=self.reset_form
        ).pack(side="left", padx=4)

        ttk.Button(
            button_frame,
            text="Keluar",
            command=self.keluar
        ).pack(side="right", padx=4)

        # =========================
        # TABEL
        # =========================
        table_frame = tk.LabelFrame(
            root,
            text=" Data Nilai Siswa ",
            font=("Segoe UI", 11, "bold"),
            padx=8,
            pady=8
        )
        table_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=5
        )

        columns = (
            "no",
            "nis",
            "nama",
            "tugas",
            "uts",
            "uas",
            "kehadiran",
            "akhir",
            "grade",
            "status"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        headings = {
            "no": "No",
            "nis": "NIS",
            "nama": "Nama",
            "tugas": "Tugas",
            "uts": "UTS",
            "uas": "UAS",
            "kehadiran": "Kehadiran",
            "akhir": "Nilai Akhir",
            "grade": "Grade",
            "status": "Status"
        }

        widths = {
            "no": 45,
            "nis": 90,
            "nama": 180,
            "tugas": 70,
            "uts": 70,
            "uas": 70,
            "kehadiran": 90,
            "akhir": 90,
            "grade": 60,
            "status": 110
        }

        for col in columns:
            self.tree.heading(
                col,
                text=headings[col]
            )
            self.tree.column(
                col,
                width=widths[col],
                anchor="center"
            )

        scrollbar_y = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        scrollbar_x = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.tree.xview
        )

        self.tree.configure(
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        self.tree.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scrollbar_y.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        scrollbar_x.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.pilih_data
        )

        # =========================
        # STATISTIK
        # =========================
        statistic_frame = tk.Frame(root)
        statistic_frame.pack(
            fill="x",
            padx=15,
            pady=(5, 12)
        )

        self.jumlah_var = tk.StringVar(value="Jumlah Siswa: 0")
        self.lulus_var = tk.StringVar(value="Lulus: 0")
        self.tidak_lulus_var = tk.StringVar(value="Tidak Lulus: 0")
        self.rata_var = tk.StringVar(value="Rata-rata: 0.00")

        ttk.Label(
            statistic_frame,
            textvariable=self.jumlah_var,
            font=("Segoe UI", 10, "bold")
        ).pack(side="left", padx=15)

        ttk.Label(
            statistic_frame,
            textvariable=self.lulus_var,
            font=("Segoe UI", 10, "bold")
        ).pack(side="left", padx=15)

        ttk.Label(
            statistic_frame,
            textvariable=self.tidak_lulus_var,
            font=("Segoe UI", 10, "bold")
        ).pack(side="left", padx=15)

        ttk.Label(
            statistic_frame,
            textvariable=self.rata_var,
            font=("Segoe UI", 10, "bold")
        ).pack(side="right", padx=15)

    # ==================================================
    # MEMBUAT CARD HASIL
    # ==================================================
    def create_result_card(self, parent, title, variable, column):
        frame = tk.Frame(
            parent,
            bd=1,
            relief="solid",
            padx=20,
            pady=8
        )

        frame.grid(
            row=0,
            column=column,
            padx=5,
            sticky="ew"
        )

        parent.columnconfigure(column, weight=1)

        tk.Label(
            frame,
            text=title,
            font=("Segoe UI", 9, "bold")
        ).pack()

        tk.Label(
            frame,
            textvariable=variable,
            font=("Segoe UI", 18, "bold")
        ).pack()

    # ==================================================
    # VALIDASI NILAI
    # ==================================================
    def ambil_nilai(self, value, nama_field):
        try:
            nilai = float(value)

            if nilai < 0 or nilai > 100:
                raise ValueError

            return nilai

        except ValueError:
            messagebox.showerror(
                "Input Tidak Valid",
                f"{nama_field} harus berupa angka antara 0 sampai 100."
            )
            return None

    # ==================================================
    # MENGHITUNG NILAI
    # ==================================================
    def hitung_nilai(self):
        if not self.nama_var.get().strip():
            messagebox.showwarning(
                "Data Belum Lengkap",
                "Nama siswa wajib diisi."
            )
            return False

        if not self.nis_var.get().strip():
            messagebox.showwarning(
                "Data Belum Lengkap",
                "NIS wajib diisi."
            )
            return False

        tugas = self.ambil_nilai(
            self.tugas_var.get(),
            "Nilai Tugas"
        )

        if tugas is None:
            return False

        uts = self.ambil_nilai(
            self.uts_var.get(),
            "Nilai UTS"
        )

        if uts is None:
            return False

        uas = self.ambil_nilai(
            self.uas_var.get(),
            "Nilai UAS"
        )

        if uas is None:
            return False

        kehadiran = self.ambil_nilai(
            self.kehadiran_var.get(),
            "Nilai Kehadiran"
        )

        if kehadiran is None:
            return False

        # Rumus nilai akhir
        nilai_akhir = (
            (tugas * 0.20) +
            (uts * 0.30) +
            (uas * 0.40) +
            (kehadiran * 0.10)
        )

        # Menentukan grade
        if nilai_akhir >= 90:
            grade = "A"
        elif nilai_akhir >= 80:
            grade = "B"
        elif nilai_akhir >= 70:
            grade = "C"
        elif nilai_akhir >= 60:
            grade = "D"
        else:
            grade = "E"

        # Menentukan status
        status = (
            "LULUS"
            if nilai_akhir >= 70
            else "TIDAK LULUS"
        )

        self.nilai_akhir_var.set(
            f"{nilai_akhir:.2f}"
        )
        self.grade_var.set(grade)
        self.status_var.set(status)

        return True

    # ==================================================
    # TAMBAH DATA
    # ==================================================
    def tambah_data(self):
        if not self.hitung_nilai():
            return

        data = {
            "nis": self.nis_var.get().strip(),
            "nama": self.nama_var.get().strip(),
            "tugas": float(self.tugas_var.get()),
            "uts": float(self.uts_var.get()),
            "uas": float(self.uas_var.get()),
            "kehadiran": float(self.kehadiran_var.get()),
            "akhir": float(self.nilai_akhir_var.get()),
            "grade": self.grade_var.get(),
            "status": self.status_var.get()
        }

        self.data_siswa.append(data)

        self.refresh_table()
        self.update_statistik()
        self.reset_form()

        messagebox.showinfo(
            "Berhasil",
            "Data siswa berhasil ditambahkan."
        )

    # ==================================================
    # EDIT DATA
    # ==================================================
    def edit_data(self):
        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning(
                "Pilih Data",
                "Silakan pilih data siswa yang ingin diedit."
            )
            return

        if not self.hitung_nilai():
            return

        index = self.tree.index(selected[0])

        self.data_siswa[index] = {
            "nis": self.nis_var.get().strip(),
            "nama": self.nama_var.get().strip(),
            "tugas": float(self.tugas_var.get()),
            "uts": float(self.uts_var.get()),
            "uas": float(self.uas_var.get()),
            "kehadiran": float(self.kehadiran_var.get()),
            "akhir": float(self.nilai_akhir_var.get()),
            "grade": self.grade_var.get(),
            "status": self.status_var.get()
        }

        self.refresh_table()
        self.update_statistik()
        self.reset_form()

        messagebox.showinfo(
            "Berhasil",
            "Data siswa berhasil diperbarui."
        )

    # ==================================================
    # HAPUS DATA
    # ==================================================
    def hapus_data(self):
        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning(
                "Pilih Data",
                "Silakan pilih data yang ingin dihapus."
            )
            return

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus data ini?"
        )

        if not konfirmasi:
            return

        index = self.tree.index(selected[0])

        del self.data_siswa[index]

        self.refresh_table()
        self.update_statistik()
        self.reset_form()

        messagebox.showinfo(
            "Berhasil",
            "Data siswa berhasil dihapus."
        )

    # ==================================================
    # MEMUAT DATA DARI TABEL KE FORM
    # ==================================================
    def pilih_data(self, event=None):
        selected = self.tree.selection()

        if not selected:
            return

        item = self.tree.item(selected[0])
        values = item["values"]

        if not values:
            return

        self.nis_var.set(values[1])
        self.nama_var.set(values[2])
        self.tugas_var.set(values[3])
        self.uts_var.set(values[4])
        self.uas_var.set(values[5])
        self.kehadiran_var.set(values[6])

        self.nilai_akhir_var.set(values[7])
        self.grade_var.set(values[8])
        self.status_var.set(values[9])

    # ==================================================
    # REFRESH TABEL
    # ==================================================
    def refresh_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for i, data in enumerate(self.data_siswa, start=1):
            self.tree.insert(
                "",
                "end",
                values=(
                    i,
                    data["nis"],
                    data["nama"],
                    f'{data["tugas"]:.2f}',
                    f'{data["uts"]:.2f}',
                    f'{data["uas"]:.2f}',
                    f'{data["kehadiran"]:.2f}',
                    f'{data["akhir"]:.2f}',
                    data["grade"],
                    data["status"]
                )
            )

    # ==================================================
    # UPDATE STATISTIK
    # ==================================================
    def update_statistik(self):
        jumlah = len(self.data_siswa)

        lulus = sum(
            1
            for data in self.data_siswa
            if data["status"] == "LULUS"
        )

        tidak_lulus = sum(
            1
            for data in self.data_siswa
            if data["status"] == "TIDAK LULUS"
        )

        if jumlah > 0:
            rata_rata = sum(
                data["akhir"]
                for data in self.data_siswa
            ) / jumlah
        else:
            rata_rata = 0

        self.jumlah_var.set(
            f"Jumlah Siswa: {jumlah}"
        )

        self.lulus_var.set(
            f"Lulus: {lulus}"
        )

        self.tidak_lulus_var.set(
            f"Tidak Lulus: {tidak_lulus}"
        )

        self.rata_var.set(
            f"Rata-rata: {rata_rata:.2f}"
        )

    # ==================================================
    # RESET FORM
    # ==================================================
    def reset_form(self):
        self.nama_var.set("")
        self.nis_var.set("")
        self.tugas_var.set("")
        self.uts_var.set("")
        self.uas_var.set("")
        self.kehadiran_var.set("")

        self.nilai_akhir_var.set("-")
        self.grade_var.set("-")
        self.status_var.set("-")

        for item in self.tree.selection():
            self.tree.selection_remove(item)

    # ==================================================
    # KELUAR
    # ==================================================
    def keluar(self):
        konfirmasi = messagebox.askyesno(
            "Keluar",
            "Apakah Anda yakin ingin keluar dari aplikasi?"
        )

        if konfirmasi:
            self.root.destroy()


# ======================================================
# PROGRAM UTAMA
# ======================================================
if __name__ == "__main__":
    root = tk.Tk()

    app = PenghitungNilaiSiswa(root)

    root.mainloop()