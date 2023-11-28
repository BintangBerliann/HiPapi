import tkinter as tk

# Membuat welcome page
welcome = tk.Tk()
welcome.title("Hi Papi")
welcome.configure(bg='#022B3A')
welcome.attributes('-fullscreen', True)
framewelcome = tk.Frame(welcome,bg='#022B3A')
framewelcome.pack()

# Fungsi keluar
def keluar():
    exit()

# Fungsi lanjut untuk ke halaman login
def lanjut():
    welcome.destroy()
    import login_page

#Judul
header = tk.Label(
    framewelcome, text="SELAMAT DATANG DI HI PAPI", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 30))
#Sub judul
subheader = tk.Label(
    framewelcome, text="HI PAPI (Hitung Pajak Pribadi) adalah program yang dibuat untuk menghitung pajak pribadi\nanda. Program ini hadir sebagai solusi untuk memudahkan wajib pajak mengetahui jumlah\npajak yang harus di bayarkan. Selain itu, program ini bertujuan memberikan edukasi tentang\nwajib pajak terutama pajak pribadi Anda.", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 16))
##Tombol submit
lanjut_button = tk.Button(
    framewelcome, text="Lanjutkan", bg="#FFFFFF", fg="#022B3A", font=("Ubuntu", 16), width=10, height=1, command=lanjut)
#Tombol kembali
keluar_button = tk.Button(
    framewelcome, text="Keluar", bg="#1F7A8C", fg="#FFFFFF", font=("Ubuntu", 16), width=10, height=1, command=keluar)

#Menampilkan
header.grid(row=4, column=0, columnspan=2, sticky="news", pady=40)
subheader.grid(row=5, column=0,pady = 5)
lanjut_button.grid(row=9, column=0, pady=50)
keluar_button.grid(row=10, column=0,pady = 0)   

welcome.mainloop()