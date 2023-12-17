import tkinter as tk
from tkinter import PhotoImage

# Membuat welcome page
welcome = tk.Tk()
welcome.title("Hi Papi")
welcome.configure(bg='#022B3A')
welcome.attributes('-fullscreen', True)
framewelcome = tk.Frame(welcome,bg='#022B3A')
framewelcome.pack()

# Logo HIPAPI
image_path = "D:\\Tugas Kuliah Semester 1\\PProkom\\Hi Papi\\Logo HIPAPI.png"
img = tk.PhotoImage(file=image_path, format="png")
img = img.subsample(10, 10)
label_img = tk.Label(welcome, image=img, bg='#022B3A')

# Fungsi keluar
def keluar():
    exit()

# Fungsi lanjut untuk ke halaman login
def lanjut():
    welcome.destroy()
    import login_page

# Membuat widgets
header = tk.Label(framewelcome, text="SELAMAT DATANG DI HI PAPI", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 30))
subheader = tk.Label(framewelcome, text="HI PAPI (Hitung Pajak Pribadi) adalah program yang dibuat untuk menghitung pajak pribadi\nanda. Program ini hadir sebagai solusi untuk memudahkan wajib pajak mengetahui jumlah\npajak yang harus di bayarkan. Selain itu, program ini bertujuan memberikan edukasi tentang\nwajib pajak terutama pajak pribadi Anda.", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 16))
lanjut_button = tk.Button(framewelcome, text="Lanjutkan", bg="#FFFFFF", fg="#022B3A", font=("Ubuntu", 16), width=10, height=1, command=lanjut)
keluar_button = tk.Button(framewelcome, text="Keluar", bg="#1F7A8C", fg="#FFFFFF", font=("Ubuntu", 16), width=10, height=1, command=keluar)

# Menampilkan widgets
header.grid(row=4, column=0, columnspan=2, sticky="news", pady=(95,35))
subheader.grid(row=6, column=0,pady = 5)
lanjut_button.grid(row=9, column=0, pady= (50,15))
keluar_button.grid(row=10, column=0,pady = 0)
label_img = tk.Label(framewelcome, image=img, bg='#022B3A')  
label_img.grid(row=5, column=0, pady=5, padx=5)

welcome.mainloop()