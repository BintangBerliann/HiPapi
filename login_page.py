import tkinter as tk
from tkinter import messagebox

# Membuat login page
loginpage = tk.Tk()
loginpage.title("Hi Papi")
loginpage.attributes('-fullscreen', True)
loginpage.configure(bg='#E1E5F2')
frame = tk.Frame(bg='#E1E5F2')
frame.pack()

# Fungsi login
def login():
    username = "hipapi"
    password = "pajak"

    # Mengecek jika pengguna memasukkan username dan password yang valid
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        loginpage.destroy()
        import page_2
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

#Membuat widgets
login_label = tk.Label(
    frame, text="MENU LOGIN HI PAPI", bg='#E1E5F2', fg="#022B3A", font=("Ubuntu", 30))
text = tk.Label(frame, text="Silahkan login terlebih dahulu untuk menggunakan program ini.", bg='#E1E5F2', fg="#022B3A", font=("Ubuntu", 14))
username_label = tk.Label(
    frame, text="Username", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 16),width=15)
username_entry = tk.Entry(frame, font=("Ubuntu", 16),width=30)
password_entry = tk.Entry(frame, show="*", font=("Ubuntu", 16),width=30)
password_label = tk.Label(
    frame, text="Password", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 16),width=15)
login_button = tk.Button(
    frame, text="Login", bg="#022B3A", fg="#FFFFFF", font=("Ubuntu", 16), command=login)

#Menampilan widgets ke layar
login_label.grid(row=0, column=0,columnspan=2,pady=40)
text.grid(row=1,column=0,columnspan=2,pady=15)
username_label.grid(row=2, column=0, pady=10,padx=0)
username_entry.grid(row=2, column=1, pady=10,padx=0)
password_label.grid(row=3, column=0, pady=10,padx=0)
password_entry.grid(row=3, column=1, pady=10,padx=0)
login_button.grid(row=4, column=0, columnspan=2, pady=30)

loginpage.mainloop()