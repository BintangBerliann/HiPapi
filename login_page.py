import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Hi Papi")
window.geometry('1920x1080')
window.configure(bg='#022B3A')

def login():
    username = "123"
    password = "123"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        window.destroy()
        import page_2
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

frame = tk.Frame(bg='#022B3A')

#Membuat widgets
login_label = tk.Label(
    frame, text="Login HI PAPI", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 30))
login_subheader = tk.Label(
    frame, text="HI PAPI (Hitung Pajak Pribadi) adalah program untuk menghitung pajak pribadi Anda.\nSilahkan login terlebih dahulu untuk menggunakan program ini. ", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 16))
username_label = tk.Label(
    frame, text="Username", bg='#1F7A8C', fg="#FFFFFF", font=("Ubuntu", 16))
username_entry = tk.Entry(frame, font=("Ubuntu", 16))
password_entry = tk.Entry(frame, show="*", font=("Ubuntu", 16))
password_label = tk.Label(
    frame, text="Password", bg='#1F7A8C', fg="#FFFFFF", font=("Ubuntu", 16))
login_button = tk.Button(
    frame, text="Login", bg="#1F7A8C", fg="#FFFFFF", font=("Ubuntu", 16), command=login)

#Menampilan widgets ke layar
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
#login_subheader.grid(row=1, column=0B6, columnspan=2, sticky="news", pady=40)
username_label.grid(row=2, column=0)
username_entry.grid(row=2, column=1, pady=20)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1, pady=20)
login_button.grid(row=4, column=0, columnspan=2, pady=30)

frame.pack()
window.mainloop()