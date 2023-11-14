import tkinter as tk
from tkinter import *
from page_identitas import DataDiri

window = tk.Tk()
window.title("Hi Papi")
window.geometry('1920x1080')
window.configure(bg='#022B3A')
f = ("Times bold", 14)

def format_rupiah(angka):
    angkastr = str(angka)
    if len(angkastr) <= 3:
        return f"Rp {angkastr}"
    else:
        ribuan = angkastr[:-3]
        ratusan = angkastr[-3:]
        ribuan = format_rupiah(ribuan)
        return f"{ribuan}.{ratusan}"

def login_page():
    window.withdraw()
    import login_page

def halaman_identitas():
    window.withdraw()
    HI = Toplevel()
    HI.title("Hi Papi")
    HI.geometry('1920x1080')
    HI.configure(bg='#022B3A')
    framePP = Frame(HI,bg='#022B3A')
    framePP.pack()

def halaman_pajak_penghasilan():
    window.withdraw()
    PP = Toplevel()
    PP.title("Hi Papi")
    PP.geometry('1920x1080')
    PP.configure(bg='#022B3A')
    framePP = Frame(PP,bg='#022B3A')
    framePP.pack()  
    def pajak_penghasilan(GajiPokok, GajiTambahan, StatusKerja, Tanggungan):
        gaji_pokok_tahunan = GajiPokok*12
        gaji_tambahan_tahunan = GajiTambahan*12
        if GajiTambahan == 0:
            bruto = gaji_pokok_tahunan
        else:
            bruto = gaji_pokok_tahunan + gaji_tambahan_tahunan
        
        while True:
            if StatusKerja.capitalize() == "Swasta" or StatusKerja.upper() == "PNS":
                break  # Keluar dari loop jika input valid
            else:
                print("Status pekerjaan yang Anda masukkan tidak valid, silakan ulangi.")
        
        if StatusKerja == "Swasta":
            iuran_hari_tua = (3/100)*bruto
            netto = bruto - iuran_hari_tua
        else:
            biaya_jabatan = (5/100)*bruto
            netto = bruto - biaya_jabatan

        if DataDiri[2] == "K":
            if Tanggungan == 0:
                pkp = netto - 58_500_000 if netto >= 58_500_000 else 0
            elif Tanggungan == 1:
                pkp = netto - 63_000_000 if netto >= 63_000_000 else 0
            elif Tanggungan == 2:
                pkp = netto - 67_500_000 if netto >= 67_500_000 else 0
            else:
                pkp = netto - 72_000_000 if netto >= 72_000_000 else 0
        else:
            if Tanggungan == 0:
                pkp = netto - 54_000_000 if netto >= 54_000_000 else 0
            elif Tanggungan == 1:
                pkp = netto - 58_500_000 if netto >= 58_500_000 else 0
            elif Tanggungan == 2:
                pkp = netto - 63_000_000 if netto >= 63_000_000 else 0
            else:
                pkp = netto - 67_500_000 if netto >= 67_500_000 else 0

        if pkp < 60_000_000:
            pph = pkp * 0.05
        elif pkp < 250_000_000:
            pph = pkp * 0.15
        elif pkp < 500_000_000:
            pph = pkp * 0.25
        elif pkp < 5_000_000_000:
            pph = pkp * 0.30
        else:
            pph = pkp * 0.35

        global total_pajak_penghasilan
        total_pajak_penghasilan = pph
        print("Pajak penghasilan yang harus dibayar adalah", total_pajak_penghasilan, "rupiah")
        return total_pajak_penghasilan 

    def Submit():
        global FormatedTotalPP
        global TotalPP
        para1 = int(GajiPokok_entry.get())
        para2 = int(GajiTambahan_entry.get())
        para3 = (StatusKerja_entry.get())
        para4 = int(Tanggungan_entry.get())        
        TotalPP = int(pajak_penghasilan(para1,para2,para3,para4))
        FormatedTotalPP = format_rupiah(TotalPP)
        HasilPP.config(text=f"Total Pajak Penghasilan Anda: {FormatedTotalPP}")

    def Back():
        PP.withdraw()
        window.deiconify()

    #Judul
    PP_label = tk.Label(
        framePP, text="Pajak Penghasilan", bg='#022B3A', fg="#FFFFFF", font=("Arial", 30))

    #Input Gaji Pokok
    GajiPokok_label = tk.Label(
        framePP, text="Gaji Pokok (per bulan)", bg='#1F7A8C', fg="#FFFFFF", font=("Arial", 16))
    GajiPokok_entry = tk.Entry(framePP, font=("Arial", 16))

    #Input Gaji Tambahan
    GajiTambahan_label = tk.Label(
        framePP, text="Gaji Tambahan (per bulan)", bg='#1F7A8C', fg="#FFFFFF", font=("Arial", 16))
    GajiTambahan_entry = tk.Entry(framePP, font=("Arial", 16))

    #Input status pekerjaan
    StatusKerja_label = tk.Label(
        framePP, text="Status Pekerjaan (Swasta/PNS)", bg='#1F7A8C', fg="#FFFFFF", font=("Arial", 16))
    StatusKerja_entry = tk.Entry(framePP, font=("Arial", 16))

    #Input jumlah tanggungan
    Tanggungan_label = tk.Label(
        framePP, text="Jumlah Tanggungan", bg='#1F7A8C', fg="#FFFFFF", font=("Arial", 16))
    Tanggungan_entry = tk.Entry(framePP, font=("Arial", 16))

    ##Tombol submit
    submit_button = tk.Button(
        framePP, text="Submit", bg="#1F7A8C", fg="#FFFFFF", font=("Arial", 16), command=Submit)
    
    #Tombol kembali
    backBTN = tk.Button(
        framePP, text="Kembali", bg="#1F7A8C", fg="#FFFFFF", font=("Arial", 16), command=Back)

    #Hasil
    HasilPP = tk.Label(framePP, text="",bg="#000000",fg="#FFFFFF")

    #Menampilkan
    PP_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    GajiPokok_label.grid(row=1, column=0,pady = 20)
    GajiPokok_entry.grid(row=1, column=1, pady=20)
    GajiTambahan_label.grid(row=2, column=0, pady=20)
    GajiTambahan_entry.grid(row=2, column=1, pady=20)
    StatusKerja_label.grid(row=3, column=0,pady = 20)
    StatusKerja_entry.grid(row=3, column=1, pady=20)
    Tanggungan_label.grid(row=4, column=0, pady=20)
    Tanggungan_entry.grid(row=4, column=1, pady=20)
    submit_button.grid(row=6, column=0, columnspan=2, pady=30)
    HasilPP.grid(row=7, column=0, columnspan=2, pady=30)
    backBTN.grid(row=9, column=0, columnspan=2, pady=30)

def halaman_pajak_kendaraan():
    window.withdraw()
    PK = Toplevel()
    PK.title("Hi Papi")
    PK.geometry('1920x1080')
    PK.configure(bg='#022B3A')
    framePK = Frame(PK,bg='#022B3A')
    framePK.pack()

    def pajak_kendaraan(JenisK,CC,NilaiJual):
        global total_pajak_kendaraan
        total_pajak_kendaraan = 0
        while True:
            if JenisK.capitalize() == "Motor":
                if CC < 250:
                    swdkllj_motor = 35_000
                elif 250 <= CC < 1000:
                    swdkllj_motor = 80_000
                else:
                    print("CC motor yang Anda masukkan termasuk dalam kategori pajak barang mewah")
                    return  # Menghentikan perhitungan pajak kendaraan
                pkb_motor = NilaiJual * 2 / 100
                pajak_motor = pkb_motor + swdkllj_motor
                print("Pajak kendaraan yang harus dibayar adalah", pajak_motor, "rupiah")
                total_pajak_kendaraan += pajak_motor
                break
            elif JenisK.capitalize() == "Mobil":
                if CC < 3000:
                    swdkllj_mobil = 140_000
                else:
                    print("CC mobil yang Anda masukkan termasuk dalam kategori pajak barang mewah")
                    return  # Menghentikan perhitungan pajak kendaraan
                pkb_mobil = NilaiJual * 2 / 100
                pajak_mobil = pkb_mobil + swdkllj_mobil
                print("Pajak kendaraan yang harus dibayar adalah", pajak_mobil, "rupiah")
                total_pajak_kendaraan += pajak_mobil
                break
            else:
                print("Jenis kendaraan yang Anda masukkan tidak valid, silakan ulangi")
                total_pajak_kendaraan = "Jenis kendaraan yang Anda masukkan tidak valid, silakan ulangi"
                break
        return total_pajak_kendaraan
    
    def Submit():
        global FormatedTotalPK
        global TotalPK
        para1 = JenisK_entry.get()
        para2 = int(CC_entry.get())
        para3 = int(NilaiJual_entry.get())
        TotalPK = int(pajak_kendaraan(para1,para2,para3))
        FormatedTotalPK = format_rupiah(TotalPK)
        HasilPK.config(text=f"Total Pajak Kendaraan Anda: {FormatedTotalPK}")

    def Back():
        PK.withdraw()
        window.deiconify()

    #Judul
    PK_label = tk.Label(
        framePK, text="Pajak Kendaraan", bg='#022B3A', fg="#FFFFFF", font=("Arial", 30))

    #Input Jenis Kendaraan
    JenisK_label = tk.Label(
        framePK, text="Jenis Kendaraan", bg='#1F7A8C', fg="#FFFFFF", font=("Arial", 16))
    JenisK_entry = tk.Entry(framePK, font=("Arial", 16))

    #Input cc
    CC_label = tk.Label(
        framePK, text="CC", bg='#1F7A8C', fg="#FFFFFF", font=("Arial", 16))
    CC_entry = tk.Entry(framePK, font=("Arial", 16))

    #Input nilai jual
    NilaiJual_label = tk.Label(
        framePK, text="Nilai Jual", bg='#1F7A8C', fg="#FFFFFF", font=("Arial", 16))
    NilaiJual_entry = tk.Entry(framePK, font=("Arial", 16))

    ##Tombol submit
    submit_button = tk.Button(
        framePK, text="Submit", bg="#1F7A8C", fg="#FFFFFF", font=("Arial", 16), command=Submit)
    
    #Tombol kembali
    backBTN = tk.Button(
        framePK, text="Kembali", bg="#1F7A8C", fg="#FFFFFF", font=("Arial", 16), command=Back)

    #Hasil
    HasilPK = tk.Label(framePK, text="",bg="#000000",fg="#FFFFFF")

    #Menampilkan
    PK_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    JenisK_label.grid(row=1, column=0,pady = 20)
    JenisK_entry.grid(row=1, column=1, pady=20)
    CC_label.grid(row=2, column=0, pady=20)
    CC_entry.grid(row=2, column=1, pady=20)
    NilaiJual_label.grid(row=3, column=0,pady = 20)
    NilaiJual_entry.grid(row=3, column=1, pady=20)
    submit_button.grid(row=5, column=0, columnspan=2, pady=30)
    HasilPK.grid(row=6, column=0, columnspan=2, pady=30)
    backBTN.grid(row=8, column=0, columnspan=2, pady=30)

def halaman_pbb():
    window.withdraw()
    PBB = Toplevel()
    PBB.title("Hi Papi")
    PBB.geometry('1920x1080')
    PBB.configure(bg='#022B3A')
    framePBB = Frame(PBB,bg='#022B3A')
    framePBB.pack()

    def pajak_bumi_dan_bangunan(LuasTanah, LuasBangunan):
        njop_luas_tanah = LuasTanah * 2_200_000
        njop_luas_bangunan = LuasBangunan * 1_100_000
        njop_total = njop_luas_tanah + njop_luas_bangunan
        njop_pbb = njop_total - 15_000_000
        pbb_terhutang = 0.1 / 100 * njop_pbb
        global total_pbb
        total_pbb = pbb_terhutang
        return total_pbb

    def Submit():
        global FormatedTotalPBB
        global TotalPBB
        para1 = int(LuasTanah_entry.get())
        para2 = int(LuasBangunan_entry.get())
        TotalPBB = int(pajak_bumi_dan_bangunan(para1,para2))
        FormatedTotalPBB = format_rupiah(TotalPBB)
        HasilPBB.config(text=f"Total Pajak Bumi dan Bangunan Anda: {FormatedTotalPBB}")

    def Back():
        PBB.withdraw()
        window.deiconify()

    #Judul
    PBB_label = tk.Label(
        framePBB, text="Pajak Bumi dan Bangunan", bg='#022B3A', fg="#FFFFFF", font=("Arial", 30))

    #Input Luas Tanah
    LuasTanah_label = tk.Label(
        framePBB, text="Luas Tanah", bg='#1F7A8C', fg="#FFFFFF", font=("Arial", 16))
    LuasTanah_entry = tk.Entry(framePBB, font=("Arial", 16))

    #Input Luas Bangunan
    LuasBangunan_label = tk.Label(
        framePBB, text="Luas Bangunan", bg='#1F7A8C', fg="#FFFFFF", font=("Arial", 16))
    LuasBangunan_entry = tk.Entry(framePBB, font=("Arial", 16))

    ##Tombol submit
    submit_button = tk.Button(
        framePBB, text="Submit", bg="#1F7A8C", fg="#FFFFFF", font=("Arial", 16), command=Submit)
    
    #Tombol kembali
    backBTN = tk.Button(
        framePBB, text="Kembali", bg="#1F7A8C", fg="#FFFFFF", font=("Arial", 16), command=Back)

    #Hasil
    HasilPBB = tk.Label(framePBB, text="",bg="#000000",fg="#FFFFFF")

    #Menampilkan
    PBB_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    LuasTanah_label.grid(row=1, column=0,pady = 20)
    LuasTanah_entry.grid(row=1, column=1, pady=20)
    LuasBangunan_label.grid(row=2, column=0, pady=20)
    LuasBangunan_entry.grid(row=2, column=1, pady=20)
    submit_button.grid(row=5, column=0, columnspan=2, pady=30)
    HasilPBB.grid(row=6, column=0, columnspan=2, pady=30)
    backBTN.grid(row=8, column=0, columnspan=2, pady=30)

def halaman_bill():
    window.withdraw()
    bill = Toplevel()
    bill.title("Hi Papi")
    bill.geometry('1920x1080')
    bill.configure(bg='#022B3A')
    framebill = Frame(bill,bg='#022B3A')
    framebill.pack()

    global TotalPBB, TotalPK, TotalPP
    TotalPAPI = TotalPP+TotalPK+TotalPBB
    FormatedTotalPAPI = format_rupiah(TotalPAPI)

    def Back():
        bill.withdraw()
        window.deiconify()

    #Judul
    bill_label = tk.Label(
        framebill, text="Bill", bg='#022B3A', fg="#FFFFFF", font=("Arial", 30))
    LabelNama = tk.Label(
        framebill, text=f"Nama: {DataDiri[0]}", bg='#1F7A8C', fg="#FFFFFF", font=("Arial", 16))
    LabelPP = tk.Label(
        framebill, text=f"Jumlah pajak penghasilan yang harus dibayar: {FormatedTotalPP}", bg='#1F7A8C', fg="#FFFFFF", font=("Arial", 16))
    LabelPK = tk.Label(
        framebill, text=f"Jumlah pajak kendaraan yang harus dibayar: {FormatedTotalPK}", bg='#1F7A8C', fg="#FFFFFF", font=("Arial", 16))
    LabelPBB = tk.Label(
        framebill, text=f"Jumlah pajak bumi dan bangunan yang harus dibayar: {FormatedTotalPBB}", bg='#1F7A8C', fg="#FFFFFF", font=("Arial", 16))
    LabelPAPI = tk.Label(
        framebill, text=f"Jumlah pajak pribadi yang harus dibayar: {FormatedTotalPAPI}", bg='#1F7A8C', fg="#FFFFFF", font=("Arial", 16))
    #Tombol kembali
    backBTN = tk.Button(
        framebill, text="Kembali", bg="#1F7A8C", fg="#FFFFFF", font=("Arial", 16), command=Back)

    #Menampilkan
    bill_label.grid(row=0, column=4, columnspan=2, sticky="news", pady=40)
    LabelNama.grid(row=1, column=4,columnspan=2,pady = 10)
    LabelPP.grid(row=2, column=0, columnspan=9, sticky="news", pady=10)
    LabelPK.grid(row=3, column=0, columnspan=9, sticky="news", pady=10)
    LabelPBB.grid(row=4, column=0, columnspan=9, sticky="news", pady=10)
    LabelPAPI.grid(row=5, column=0, columnspan=9, sticky="news", pady=10)
    backBTN.grid(row=6, column=4, columnspan=2, sticky="news", pady=20)

def halaman_tentang_pajak():
    window.withdraw()
    TP = Toplevel()
    TP.title("Hi Papi")
    TP.geometry('1920x1080')
    TP.configure(bg='#022B3A')
    frameTP = Frame(TP,bg='#022B3A')
    frameTP.pack()

    def Back():
        TP.withdraw()
        window.deiconify()

    #Judul
    TP_label = tk.Label(
        frameTP, text="Tentang Pajak", bg='#022B3A', fg="#FFFFFF", font=("Arial", 30))
    LabelTP = tk.Label(
        frameTP, text="Tamwawkmkdakdkmwdakmdwakam.\naokawokawokaokaok\akmdkmasskmd.", bg='#1F7A8C', fg="#FFFFFF", font=("Arial", 16))
    #Tombol kembali
    backBTN = tk.Button(
        frameTP, text="Kembali", bg="#1F7A8C", fg="#FFFFFF", font=("Arial", 16), command=Back)
    
    #Menampilkan
    TP_label.grid(row=0, column=4, columnspan=2, sticky="news", pady=40)
    LabelTP.grid(row=1, column=4,columnspan=2,pady = 20)
    backBTN.grid(row=6, column=4, columnspan=2, sticky="news", pady=40)

def halaman_keluar():
    window.withdraw()
    exitprog = Toplevel()
    exitprog.title("Hi Papi")
    exitprog.geometry('1920x1080')
    exitprog.configure(bg='#022B3A')
    framekeluar = Frame(exitprog,bg='#022B3A')
    framekeluar.pack()

    def keluar():
        exit()

    #Judul
    keluar_label = tk.Label(
        framekeluar, text="Terima kasih telah menggunakan program ini!", bg='#022B3A', fg="#FFFFFF", font=("Arial", 30))
    keluar_button = tk.Button(
        framekeluar, text="Keluar", bg="#1F7A8C", fg="#FFFFFF", font=("Arial", 16), command=keluar)
    
    #Menampilkan
    keluar_label.grid(row=0, column=4, columnspan=2, sticky="news", pady=40)
    keluar_button.grid(row=1, column=4,columnspan=2,pady = 20)   

Label(
    window,
    text="Menu Utama",
    padx=20,
    pady=20,
    bg='#022B3A', 
    fg="#FFFFFF", 
    font=("Arial", 30)
).pack(expand=True, fill=BOTH)

frame = Frame(bg='#022B3A')

# Creating widgets with smaller size
button_width = 30
button_height = 2

pajak_penghasilan = Button(
    frame, text="Hitung Pajak Penghasilan", bg="#FFFFFF", fg="#022B3A", font=("Arial", 12), width=button_width, height=button_height, command=halaman_pajak_penghasilan)
pajak_kendaraan = Button(
    frame, text="Hitung Pajak Kendaraan", bg="#FFFFFF", fg="#022B3A", font=("Arial", 12), width=button_width, height=button_height, command=halaman_pajak_kendaraan)
pajak_bb = Button(
    frame, text="Hitung Pajak Bumi dan Bangunan", bg="#FFFFFF", fg="#022B3A", font=("Arial", 12), width=button_width, height=button_height, command=halaman_pbb)
bill = Button(
    frame, text="Cetak Bill", bg="#FFFFFF", fg="#022B3A", font=("Arial", 12), width=button_width, height=button_height, command=halaman_bill)
tentang_pajak = Button(
    frame, text="Tentang Pajak", bg="#FFFFFF", fg="#022B3A", font=("Arial", 12), width=button_width, height=button_height, command=halaman_tentang_pajak)
keluar = Button(
    frame, text="Keluar", bg="#FFFFFF", fg="#022B3A", font=("Arial", 12), width=button_width, height=button_height, command=halaman_keluar)

# Menampilkan
pajak_penghasilan.grid(row=0, column=0, padx=10, pady=10)
pajak_kendaraan.grid(row=1, column=0, padx=10, pady=10)
pajak_bb.grid(row=2, column=0, padx=10, pady=10)
bill.grid(row=3, column=0, padx=10, pady=10)
tentang_pajak.grid(row=4, column=0, padx=10, pady=10)
keluar.grid(row=5, column=0, padx=10, pady=10)

frame.pack()
window.mainloop()