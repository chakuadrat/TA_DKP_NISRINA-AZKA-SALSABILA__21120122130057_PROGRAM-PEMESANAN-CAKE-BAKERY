#catatan buat tugas akhir, disini udah ada,
#modul 1 : array, variabel, tipe data (string)
#modul 2 : pengkondisian if, if not, if else
#modul 3 : perulangan for
#modul 4 : function return type, method
#modul 5 : class, constructor, inheritance
#modul 6 : getter setter (secara ga langsung, konsepnya sama aja sbnerny), abstraction
#modul 7 : -
#modul 8 : widgets label, button, radiobutton, messagebox, combobox, entry

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

#parent class & class abstraction
class CakeOrder:
    #constructor
    def __init__(self, title):
        self.window = tk.Tk()
        self.window.title(title)

        # Mengatur ukuran jendela dan posisinya
        self.window.geometry("900x800")
        self.window.update_idletasks()
        screen_width = self.window.winfo_screenwidth()
        x = (screen_width - 900) // 2
        self.window.geometry(f"900x800+{x}+0")
        
        # Membuat judul program
        self.label_judul = tk.Label(self.window, text="Sweet Tooth Cake & Bakery", font=("Brush Script MT", 54), fg="#fe6694")
        self.label_judul.pack(pady=10)

        #label dan entry nama
        self.label_nama = tk.Label(self.window, text="Nama:", font=("Comic Sans MS", 15), fg="white")
        self.label_nama.pack()
        self.entry_nama = tk.Entry(self.window, font=("Comic Sans MS", 15))
        self.entry_nama.pack()

        #label dan entry nomor telepon
        self.label_no_telp = tk.Label(self.window, text="No. Telp:", font=("Comic Sans MS", 15), fg="white")
        self.label_no_telp.pack()
        self.entry_no_telp = tk.Entry(self.window, font=("Comic Sans MS", 15))
        self.entry_no_telp.pack()

        #label dan entry  alamat
        self.label_alamat = tk.Label(self.window, text="Alamat:", font=("Comic Sans MS", 15), fg="white")
        self.label_alamat.pack()
        self.entry_alamat = tk.Entry(self.window, font=("Comic Sans MS", 15))
        self.entry_alamat.pack()

        #combo box jenis pesanan bento cake
        self.label_jenis_pesanan = tk.Label(self.window, text="Jenis Pesanan Bento Cake:", font=("Comic Sans MS", 15), fg="white")
        self.label_jenis_pesanan.pack()
        self.combo_jenis_pesanan = ttk.Combobox(self.window, values=["Lil Sign", "Pop Up", "Dreamy", "Flowery", "Simple Border", "Simple Swirl", "Figurine"], font=("Comic Sans MS", 15))
        self.combo_jenis_pesanan.pack()

        # radio button base cake
        self.label_base_cake = tk.Label(self.window, text="Base Cake:", font=("Comic Sans MS", 15), fg="white")
        self.label_base_cake.pack()
        self.cake_var = tk.StringVar()
        self.radio_cokelat = tk.Radiobutton(self.window, text="Cokelat", variable=self.cake_var, value="Cokelat", font=("Comic Sans MS", 15))
        self.radio_cokelat.pack()
        self.radio_vanilla = tk.Radiobutton(self.window, text="Vanilla", variable=self.cake_var, value="Vanilla", font=("Comic Sans MS", 15))
        self.radio_vanilla.pack()

        #label dan entry tulisan pada cake
        self.label_tulisan_cake = tk.Label(self.window, text="Tulisan pada Cake:", font=("Comic Sans MS", 15), fg="white")
        self.label_tulisan_cake.pack()
        self.entry_tulisan_cake = tk.Entry(self.window, font=("Comic Sans MS", 15))
        self.entry_tulisan_cake.pack()

        #label dan entry tanggal pengantaran
        self.label_tanggal_pengantaran = tk.Label(self.window, text="Tanggal Pengantaran (dd/mm/yy):", font=("Comic Sans MS", 15), fg="white")
        self.label_tanggal_pengantaran.pack()
        self.entry_tanggal_pengantaran = tk.Entry(self.window, font=("Comic Sans MS", 15))
        self.entry_tanggal_pengantaran.pack()

        #combo box pembayaran
        self.label_pembayaran = tk.Label(self.window, text="Pembayaran:", font=("Comic Sans MS", 15), fg="white")
        self.label_pembayaran.pack()
        self.combo_pembayaran = ttk.Combobox(self.window, values=["BRI", "BNI", "Mandiri", "GoPay", "ShopeePay", "DANA"], font=("Comic Sans MS", 15))
        self.combo_pembayaran.pack()

        #label notes
        self.label_notes = tk.Label(self.window, text="Tambahan:", font=("Comic Sans MS", 15), fg="white")
        self.label_notes.pack()

        #widget Text untuk notes
        self.text_notes = tk.Text(self.window, font=("Comic Sans MS", 15), height=4, width=30)
        self.text_notes.pack()

        #style button
        button_style = ttk.Style()
        button_style.configure("Custom.TButton", font=("Comic Sans MS", 15))

        # button order
        self.button_submit = ttk.Button(self.window, text="ORDER", command=self.submit_order, style="Custom.TButton", width=11)
        self.button_submit.pack(pady=10)


    def reset_form(self):
        # bersihin widgets form biar pas user ngulang pesenan udah kosong lagi
        self.entry_nama.delete(0, tk.END)
        self.entry_no_telp.delete(0, tk.END)
        self.entry_alamat.delete(0, tk.END)
        self.combo_jenis_pesanan.set('')
        self.cake_var.set('')
        self.entry_tulisan_cake.delete(0, tk.END)
        self.entry_tanggal_pengantaran.delete(0, tk.END)
        self.combo_pembayaran.set('')
        self.text_notes.delete("1.0", tk.END)

    #method buat submit order biar bisa dipanggil
    def submit_order(self):
        nama = self.entry_nama.get()
        no_telp = self.entry_no_telp.get()
        alamat = self.entry_alamat.get()
        jenis_pesanan = self.combo_jenis_pesanan.get()
        base_cake = self.cake_var.get()
        tulisan_cake = self.entry_tulisan_cake.get()
        tanggal_pengantaran = self.entry_tanggal_pengantaran.get()
        pembayaran = self.combo_pembayaran.get()
        notes = self.text_notes.get("1.0", tk.END).strip()

        
        #peringatan kalau widgets masih kosong 
        if not (nama and no_telp and alamat and jenis_pesanan and base_cake and tulisan_cake and tanggal_pengantaran and pembayaran):
            messagebox.showwarning("Error", "Dimohon melengkapi semua data yang diminta.")
            return

        #ngitung harga akhir
        harga = None
        for cake in harga_kue:
            if cake[0] == jenis_pesanan:
                harga = cake[1]
                break 

        #biar tanggal pemesanan otomatis muncul
        tanggal_pemesanan = datetime.now().strftime("%d/%m/%Y")

        #kalau notes gak diisi, nanti muncul '"-" di detail pesanan
        if not notes:
            notes = "-"

        #detail pemesanan
        pesanan = f"Terima Kasih, pesanan anda sudah masuk dan akan segera kami proses.\n\n\nInformasi Pemesanan:\n\nNama: {nama}\nNo. Telp: {no_telp}\nAlamat: {alamat}\n\nDetail Pesanan:\nJenis Pesanan Bento Cake: {jenis_pesanan}\nBase Cake: {base_cake}\nTulisan pada Cake: {tulisan_cake}\nTanggal Pengantaran: {tanggal_pengantaran}\nPembayaran: {pembayaran}\n\nCatatan: {notes}\n\nHarga Akhir: {harga}\n\nTanggal Pemesanan: {tanggal_pemesanan}\n\nDimohon mengirimkan bukti transfer melalui nomor dibawah ini,\n081234561230\n\n\nNote:\nApabila ada masalah, pertanyaan maupun gambar design kue tertentu yang anda inginkan, silahkan menghubungi nomor yang sudah tertera\n"

        #jendela konfirmasi pesanan
        messagebox.showinfo("Konfirmasi Pemesanan", pesanan)

        #jendela pertanyaan user mau pesen lagi apa engga
        result = messagebox.askquestion("Pemesanan", "Apakah Anda ingin melakukan pemesanan lagi?")
        if result == "no":
            self.window.destroy()  #buat nutup jendela kalau user pilih tidak
        else:
            self.reset_form()  #form direset terus program ngulang lagi

#class child dari class parent CakeOrder
class DeliveryCakeOrder(CakeOrder):
    def __init__(self):
        super().__init__("Delivery - Bento Cake Order")

#array
harga_kue = [
    ("Lil Sign", "65K"),
    ("Pop Up", "75K"),
    ("Dreamy", "75K"),
    ("Flowery", "75K"),
    ("Simple Border", "65K"),
    ("Simple Swirl", "65K"),
    ("Figurine", "85K")
]

#buat manggil dan jalanin program
order = DeliveryCakeOrder()
order.window.mainloop()



