import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Membuat page identitas
indentitas = Tk()
indentitas.title("Hi Papi")
indentitas.attributes('-fullscreen', True)
indentitas.configure(bg='#E1E5F2')
frameidentitas = Frame(indentitas,bg='#E1E5F2')
frameidentitas.pack()
f = ("Times bold", 14)

# Mendeklarasikan variabel untuk menyimpan nilai sementara data diri
DataDiri = []

# Membuat dropdown
options = [
    "Kawin",
    "Belum Kawin"
]
clickedstatus = StringVar() 
clickedstatus.set( "")
dropstatus = OptionMenu(frameidentitas, clickedstatus, *options)
dropstatus.config(width=33,bg='#FFFFFF')
dropstatus.grid(row=6, column=0,pady =5,columnspan=3)
clickedstatus.get()

# Memeriksa apakah teks hanya mengandung huruf dan spasi
def is_valid_input(text):
    return all(char.isalpha() or char.isspace() for char in text)

# Fungsi pengecekan
def validate_entries():
    nama = Nama_entry.get()
    asal = Asal_entry.get()
    kawin = clickedstatus.get()

    # Mengecek jika pengguna telah memasukkan nama dan asal daerah yang valid
    if not (nama and asal and kawin):
        messagebox.showwarning("Warning", "Anda belum mengisi semua data!")
    else:
        if not is_valid_input(nama) or not is_valid_input(asal):
            messagebox.showwarning("Warning", "Nama atau asal daerah yang Anda masukkan tidak valid!")
        else:
            Submit()

# Fungsi submit
def Submit():
    global DataDiri
    nama = Nama_entry.get()
    asal = Asal_entry.get()
    kawin = clickedstatus.get()
    namaC = nama.capitalize()
    asalC= asal.capitalize()
    kawinC = kawin.capitalize()

    DataDiri.append(namaC)
    DataDiri.append(asalC)
    DataDiri.append(kawinC)
    indentitas.destroy()
    import page_2

#Judul
indentitas_label = tk.Label(
    frameidentitas, text="Masukkan Identitas Anda", bg='#E1E5F2', fg="#022B3A", font=("Ubuntu", 30))
#Input Nama
Nama_label = tk.Label(
    frameidentitas, text="Nama", bg='#E1E5F2', fg="#022B3A", font=("Ubuntu", 16))
Nama_entry = tk.Entry(frameidentitas, font=("Ubuntu", 16))
#Input Asal Daerah
Asal_label = tk.Label(
    frameidentitas, text="Asal Daerah", bg='#E1E5F2', fg="#022B3A", font=("Ubuntu", 16))
Asal_entry = tk.Entry(frameidentitas, font=("Ubuntu", 16))
#Input Status Perkawinan
StatusPerkawinan_label = tk.Label(
    frameidentitas, text="Status Perkawinan", bg='#E1E5F2', fg="#022B3A", font=("Ubuntu", 16))
##Tombol submit
submit_button = tk.Button(
    frameidentitas, text="Submit", bg="#022B3A", fg="#FFFFFF", font=("Ubuntu", 16), command=validate_entries)

#Menampilkan
indentitas_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
Nama_label.grid(row=1, column=0,columnspan=3,pady = 5)
Nama_entry.grid(row=2, column=0, columnspan=3,pady=5)
Asal_label.grid(row=3, column=0, columnspan=3,pady=5)
Asal_entry.grid(row=4, column=0, columnspan=3,pady=5)
StatusPerkawinan_label.grid(row=5, column=0,columnspan=3,pady =5)
submit_button.grid(row=8, column=0, columnspan=2, pady=30)

indentitas.mainloop()