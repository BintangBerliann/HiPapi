import tkinter as tk
from tkinter import *

indentitas = Tk()
indentitas.title("Hi Papi")
indentitas.geometry('600x540')
indentitas.configure(bg='#022B3A')
frameidentitas = Frame(indentitas,bg='#022B3A')
frameidentitas.pack()

DataDiri = []

f = ("Times bold", 14)

def Submit():
    global DataDiri
    nama = Nama_entry.get()
    asal = Asal_entry.get()
    kawin = StatusPerkawinan_entry.get()
    namaC = nama.capitalize()
    asalC= asal.capitalize()
    kawinC = kawin.capitalize()

    DataDiri.append(namaC)
    DataDiri.append(asalC)
    DataDiri.append(kawinC)
    indentitas.destroy()
    import page_2

def Back():
    indentitas.quit()
    import login_page

#Judul
indentitas_label = tk.Label(
    frameidentitas, text="Masukkan Identitas Anda", bg='#022B3A', fg="#FFFFFF", font=("Arial", 30))

#Input Nama
Nama_label = tk.Label(
    frameidentitas, text="Nama", bg='#1F7A8C', fg="#FFFFFF", font=("Arial", 16))
Nama_entry = tk.Entry(frameidentitas, font=("Arial", 16))

#Input Asal Daerah
Asal_label = tk.Label(
    frameidentitas, text="Asal Daerah", bg='#1F7A8C', fg="#FFFFFF", font=("Arial", 16))
Asal_entry = tk.Entry(frameidentitas, font=("Arial", 16))

#Input Status Perkawinan
StatusPerkawinan_label = tk.Label(
    frameidentitas, text="Status Perkawinan (K/BK)", bg='#1F7A8C', fg="#FFFFFF", font=("Arial", 16))
StatusPerkawinan_entry = tk.Entry(frameidentitas, font=("Arial", 16))

##Tombol submit
submit_button = tk.Button(
    frameidentitas, text="Submit", bg="#1F7A8C", fg="#FFFFFF", font=("Arial", 16), command=Submit)

#Tombol kembali
backBTN = tk.Button(
    frameidentitas, text="Kembali", bg="#1F7A8C", fg="#FFFFFF", font=("Arial", 16), command=Back)

#Menampilkan
indentitas_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
Nama_label.grid(row=1, column=0,pady = 20)
Nama_entry.grid(row=1, column=1, pady=20)
Asal_label.grid(row=2, column=0, pady=20)
Asal_entry.grid(row=2, column=1, pady=20)
StatusPerkawinan_label.grid(row=3, column=0,pady = 20)
StatusPerkawinan_entry.grid(row=3, column=1, pady=20)
submit_button.grid(row=5, column=0, columnspan=2, pady=30)
backBTN.grid(row=9, column=0, columnspan=2, pady=30)

indentitas.mainloop()