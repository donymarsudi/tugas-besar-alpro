# REFERENSI BELAJAR :
# https://docs.python.org/id/3/library/tk.html
# https://www.w3schools.com/python/default.asp
# https://youtu.be/L4dbeLNDFlc?si=r8C5sSBLnWDDCPoX
# Modul Pemrograman Python


import tkinter as tk

def hitung_diskon(nama, nim, harga):
    tiga_digit_terakhir_nim = nim[-3:]

    if not tiga_digit_terakhir_nim.isdigit():
        return f'NIM ({nim}) tidak sesuai format!'

    tiga_digit_terakhir_nim = int(tiga_digit_terakhir_nim)

    if not harga.isdigit():
        return 'Harga barang harus berupa angka!'

    harga_barang = int(harga)

    if tiga_digit_terakhir_nim % 2 == 0:
        diskon = 10
    else:
        diskon = 5

    harga_setelah_diskon = harga_barang * (1 - diskon / 100)
    return f'''
    Halo {nama}, Anda memiliki NIM {'Genap' if diskon == 10 else 'Ganjil'} ({nim}) sehingga memperoleh :
    - Diskon : {diskon}%
    - Harga Setelah Diskon : {int(harga_setelah_diskon)}
    '''

def validate_input():
    while True:
        nama = entry_nama.get()
        nim = entry_nim.get()
        harga = entry_harga.get()

        if not nama or not nim or not harga:
            tampilkan_hasil.config(text="Semua field harus diisi!", fg="red")
            return
        
        hasil_cek_diskon = hitung_diskon(nama, nim, harga)
        
        if "tidak sesuai format" in hasil_cek_diskon or "Harga barang harus berupa angka!" in hasil_cek_diskon:
            tampilkan_hasil.config(text=hasil_cek_diskon, fg="red")
            return
        
        tampilkan_hasil.config(text=hasil_cek_diskon, fg="green")
        break

    entry_nama.delete(0, tk.END)
    entry_nim.delete(0, tk.END)
    entry_harga.delete(0, tk.END)

window = tk.Tk()
window.title("Tugas Besar Pratikum Alpro - Dony Marsudi")
window.geometry("700x400")
window.resizable(False, False)

nama_dan_nim_coder = tk.Label(window, text="Nama: Dony Marsudi   NIM: D1021241033", font=("Arial", 12))
nama_dan_nim_coder.pack(pady=10)

label_selamat_datang = tk.Label(window, text='''Halo, isilah data berikut untuk menentukan 
diskon & harga setelah diskon yang bisa Anda dapatkan!''', font=("Arial", 10))
label_selamat_datang.pack(pady=5)

tk.Label(window, text="Masukkan Nama Anda:").pack()
entry_nama = tk.Entry(window)
entry_nama.pack()

tk.Label(window, text="Masukkan NIM Anda:").pack()
entry_nim = tk.Entry(window)
entry_nim.pack()

tk.Label(window, text="Masukkan Harga Barang:").pack()
entry_harga = tk.Entry(window)
entry_harga.pack()

button_submit = tk.Button(window, text="Hitung Diskon", command=validate_input)
button_submit.pack()

tampilkan_hasil = tk.Label(window, text="Belum ada pemeriksaan harga!")
tampilkan_hasil.pack()

window.mainloop()