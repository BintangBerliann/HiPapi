import tkinter as tk
from tkinter import *
from tkinter import Frame, Toplevel, BOTH, LEFT, scrolledtext
from page_identitas import DataDiri

# Membuat window utama
main = tk.Tk()
main.title("Hi Papi")
main.attributes('-fullscreen', True)
main.configure(bg='#022B3A')
frame = Frame(bg='#022B3A')
frame.pack()

# Mendeklarasikan variabel untuk cetak bill
TotalAkhirPP = 0
TotalAkhirPK = 0
TotalAkhirPBB = 0
FormatedTotalPP = 0
FormatedTotalPK = 0
FormatedTotalPBB = 0

# Fungsi format rupiah
def format_rupiah(angka):
    angkastr = str(angka)
    if len(angkastr) <= 3:
        return f"Rp {angkastr}"
    else:
        ribuan = angkastr[:-3]
        ratusan = angkastr[-3:]
        ribuan = format_rupiah(ribuan)
        return f"{ribuan}.{ratusan}"

# Fungsi back
def Back():
    main.withdraw()
    import login_page

# Membuat halaman pajak penghasilan
def halaman_pajak_penghasilan():
    main.withdraw()
    PP = Toplevel()
    PP.title("Hi Papi")
    PP.attributes('-fullscreen', True)
    PP.configure(bg='#022B3A')
    framePP = Frame(PP,bg='#022B3A')
    framePP.pack(pady=20)

    # Membuat dropdown
    options = [
        "Swasta",
        "PNS"
    ]
    clickedkerja = StringVar() 
    clickedkerja.set( "")
    dropkerja = OptionMenu(framePP, clickedkerja, *options)
    dropkerja.config(width=18,font=("Ubuntu",15))
    dropkerja.grid(row=3, column=1,pady = 20)
    clickedkerja.get()

    #Membuat perhitungan pajak penghasilan
    def pajak_penghasilan(GajiPokok, GajiTambahan, Tanggungan):
        gaji_pokok_tahunan = GajiPokok*12
        gaji_tambahan_tahunan = GajiTambahan*12
        if GajiTambahan == 0:
            bruto = gaji_pokok_tahunan
        else:
            bruto = gaji_pokok_tahunan + gaji_tambahan_tahunan
        
        if clickedkerja.get() == "Swasta":
            iuran_hari_tua = (3/100)*bruto
            netto = bruto - iuran_hari_tua
        else:
            biaya_jabatan = (5/100)*bruto
            netto = bruto - biaya_jabatan

        if DataDiri[2] == "Kawin":
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
        return total_pajak_penghasilan 

    # Fungsi untuk submit
    def SubmitPP():
        global FormatedTotalPP
        global TotalPP
        GajiPokok = GajiPokok_entry.get()
        GajiTambahan = GajiTambahan_entry.get()
        clickedkerja.get()
        Tanggungan = Tanggungan_entry.get()

        # Mengecek apakah pengguna sudah menginputkan data secara lengkap dan valid
        if not GajiPokok or not GajiTambahan or not Tanggungan:
            HasilPP.config(text="Anda belum mengisi data")
            return
        try:
            GajiPokok = int(GajiPokok)
            GajiTambahan = int(GajiTambahan)
            Tanggungan = int(Tanggungan)
        except ValueError:
            HasilPP.config(text="Mohon masukkan angka")
            return

        TotalPP = int(pajak_penghasilan(GajiPokok, GajiTambahan, Tanggungan))
        FormatedTotalPP = format_rupiah(TotalPP)
        HasilPP.config(text=f"Total Pajak Penghasilan Anda: {FormatedTotalPP}")
        global TotalAkhirPP
        TotalAkhirPP = TotalPP

    # Fungsi untuk kembali ke menu utama
    def Back():
        PP.withdraw()
        main.deiconify()

    # Membuat widgets PP
    PP_label = tk.Label(framePP, text="Pajak Penghasilan", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 30))
    GajiPokok_label = tk.Label(framePP, text="Gaji Pokok (per bulan)", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 16),width=30)
    GajiPokok_entry = tk.Entry(framePP, font=("Ubuntu", 16))
    GajiTambahan_label = tk.Label(framePP, text="Gaji Tambahan (per bulan)", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 16),width=30)
    GajiTambahan_entry = tk.Entry(framePP, font=("Ubuntu", 16))
    StatusKerja_label = tk.Label(framePP, text="Status Pekerjaan", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 16),width=30)
    Tanggungan_label = tk.Label(framePP, text="Jumlah Tanggungan", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 16),width=30)
    Tanggungan_entry = tk.Entry(framePP, font=("Ubuntu", 16))
    submit_button = tk.Button(framePP, text="Hitung", bg="#FFFFFF", fg="#022B3A", font=("Ubuntu", 16), command=SubmitPP)
    backBTN = tk.Button(framePP, text="Kembali", bg="#022B3A", fg="#FFFFFF", font=("Ubuntu", 16), command=Back)
    HasilPP = tk.Label(framePP, text="",bg="#FFFFFF",fg="#022B3A", font=("Ubuntu", 16))

    #Menampilkan widgets PP
    PP_label.grid(row=0, column=0, columnspan=2, pady=(60,40))
    GajiPokok_label.grid(row=1, column=0,pady = 20)
    GajiPokok_entry.grid(row=1, column=1, pady=20)
    GajiTambahan_label.grid(row=2, column=0, pady=20)
    GajiTambahan_entry.grid(row=2, column=1, pady=20)
    StatusKerja_label.grid(row=3, column=0,pady = 20)
    Tanggungan_label.grid(row=4, column=0, pady=20)
    Tanggungan_entry.grid(row=4, column=1, pady=20)
    submit_button.grid(row=6, column=0, columnspan=2, pady=30)
    HasilPP.grid(row=7, column=0, columnspan=2, pady=30)
    backBTN.grid(row=9, column=0, columnspan=2, pady=30)

# Membuat halaman pajak kendaraan
def halaman_pajak_kendaraan():
    main.withdraw()
    PK = Toplevel()
    PK.title("Hi Papi")
    PK.attributes('-fullscreen', True)
    PK.configure(bg='#022B3A')
    framePK = Frame(PK,bg='#022B3A')
    framePK.pack(pady=20)

    # Membuat dropdown
    option1 = [
        "Motor",
        "Mobil"
    ]
    clickedkendaraan = StringVar()
    clickedkendaraan.set( "")
    dropkendaraan = OptionMenu(framePK, clickedkendaraan, *option1)
    dropkendaraan.config(width=18,font=("Ubuntu",15))
    dropkendaraan.grid(row=1, column=1,pady = 20)
    clickedkendaraan.get()
    
    # Membuat perhitungan pajak kendaraan
    def pajak_kendaraan(CC, NilaiJual):
        global total_pajak_kendaraan
        total_pajak_kendaraan = 0
        if clickedkendaraan.get() == "Motor":
            if CC < 250:
                swdkllj_motor = 35_000
            elif 250 <= CC < 1000:
                swdkllj_motor = 80_000
            else:
                HasilPK.config(text="CC motor yang Anda masukkan termasuk dalam kategori pajak barang mewah")
                return 
            pkb_motor = NilaiJual * 2 / 100
            pajak_motor = pkb_motor + swdkllj_motor
            total_pajak_kendaraan += pajak_motor
        else:
            if CC < 3000:
                swdkllj_mobil = 140_000
            else:
                HasilPK.config(text="CC mobil yang Anda masukkan termasuk dalam kategori pajak barang mewah")
                return 
            pkb_mobil = NilaiJual * 2 / 100
            pajak_mobil = pkb_mobil + swdkllj_mobil
            total_pajak_kendaraan += pajak_mobil
        return total_pajak_kendaraan
    
    # Fungsi submit
    def SubmitPK():
        global FormatedTotalPK
        global TotalPK
        CC = CC_entry.get()
        NilaiJual = NilaiJual_entry.get()

        # Mengecek apakah pengguna sudah menginputkan data secara lengkap dan valid
        if not CC or not NilaiJual:
            HasilPK.config(text="Anda belum mengisi data")
            return
        try:
            CC = int(CC)
            NilaiJual = int(NilaiJual)
        except ValueError:
            HasilPK.config(text="Mohon masukkan angka")
            return

        TotalPK = int(pajak_kendaraan(CC, NilaiJual))
        FormatedTotalPK = format_rupiah(TotalPK)
        HasilPK.config(text=f"Total Pajak Kendaraan Anda: {FormatedTotalPK}")
        global TotalAkhirPK
        TotalAkhirPK = TotalPK

    # Fungsi kembali
    def Back():
        PK.withdraw()
        main.deiconify()

    # Membuat widgets PK
    PK_label = tk.Label(framePK, text="Pajak Kendaraan", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 30))
    JenisK_label = tk.Label(framePK, text="Jenis Kendaraan", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 16),width=20)
    CC_label = tk.Label(framePK, text="CC", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 16),width=20)
    CC_entry = tk.Entry(framePK, font=("Ubuntu", 16))
    NilaiJual_label = tk.Label(framePK, text="Nilai Jual", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 16),width=20)
    NilaiJual_entry = tk.Entry(framePK, font=("Ubuntu", 16))
    submit_button = tk.Button(framePK, text="Hitung", bg="#FFFFFF", fg="#022B3A", font=("Ubuntu", 16), command=SubmitPK)
    backBTN = tk.Button(framePK, text="Kembali", bg="#022B3A", fg="#FFFFFF", font=("Ubuntu", 16), command=Back)
    HasilPK = tk.Label(framePK, text="",bg="#FFFFFF",fg="#022B3A", font=("Ubuntu", 16))

    #Menampilkan widgets PK
    PK_label.grid(row=0, column=0, columnspan=2, pady=(100,40))
    JenisK_label.grid(row=1, column=0,pady = 20)
    CC_label.grid(row=2, column=0, pady=20)
    CC_entry.grid(row=2, column=1, pady=20)
    NilaiJual_label.grid(row=3, column=0,pady = 20)
    NilaiJual_entry.grid(row=3, column=1, pady=20)
    submit_button.grid(row=5, column=0, columnspan=2, pady=30)
    HasilPK.grid(row=6, column=0, columnspan=2, pady=30)
    backBTN.grid(row=8, column=0, columnspan=2, pady=30)

# Membuat halaman pajak bumi dan bangunan
def halaman_pbb():
    main.withdraw()
    PBB = Toplevel()
    PBB.title("Hi Papi")
    PBB.attributes('-fullscreen', True)
    PBB.configure(bg='#022B3A')
    framePBB = Frame(PBB,bg='#022B3A')
    framePBB.pack(pady=20)

    # Membuat perhitungan pajak bumi dan bangunan
    def pajak_bumi_dan_bangunan(LuasTanah, LuasBangunan):
        njop_luas_tanah = LuasTanah * 2_200_000
        njop_luas_bangunan = LuasBangunan * 1_100_000
        njop_total = njop_luas_tanah + njop_luas_bangunan
        njop_pbb = njop_total - 15_000_000
        pbb_terhutang = 0.1 / 100 * njop_pbb
        global total_pbb
        total_pbb = pbb_terhutang
        return total_pbb

    # Fungsi submit
    def SubmitPBB():
        global FormatedTotalPBB
        global TotalPBB
        LuasTanah = LuasTanah_entry.get()
        LuasBangunan = LuasBangunan_entry.get()

        # Mengecek apakah pengguna sudah menginputkan data secara lengkap dan valid
        if not LuasTanah or not LuasBangunan:
            HasilPBB.config(text="Anda belum mengisi data")
            return
        try:
            LuasTanah = int(LuasTanah)
            LuasBangunan = int(LuasBangunan)
        except ValueError:
            HasilPBB.config(text="Mohon masukkan angka")
            return

        TotalPBB = int(pajak_bumi_dan_bangunan(LuasTanah, LuasBangunan))
        FormatedTotalPBB = format_rupiah(TotalPBB)
        HasilPBB.config(text=f"Total Pajak Bumi dan Bangunan Anda: {FormatedTotalPBB}")
        global TotalAkhirPBB
        TotalAkhirPBB = TotalPBB

    # Fungsi kembali
    def Back():
        PBB.withdraw()
        main.deiconify()

    # Membuat widgets PBB
    PBB_label = tk.Label(framePBB, text="Pajak Bumi dan Bangunan", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 30))
    LuasTanah_label = tk.Label(framePBB, text="Luas Tanah (m²)", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 16),width=20,justify=tk.LEFT)
    LuasTanah_entry = tk.Entry(framePBB, font=("Ubuntu", 16))
    LuasBangunan_label = tk.Label(framePBB, text="Luas Bangunan (m²)", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 16),width=20)
    LuasBangunan_entry = tk.Entry(framePBB, font=("Ubuntu", 16))
    submit_button = tk.Button(framePBB, text="Hitung", bg="#FFFFFF", fg="#022B3A", font=("Ubuntu", 16), command=SubmitPBB)
    backBTN = tk.Button(framePBB, text="Kembali", bg="#022B3A", fg="#FFFFFF", font=("Ubuntu", 16), command=Back)
    HasilPBB = tk.Label(framePBB, text="",bg="#FFFFFF",fg="#022B3A", font=("Ubuntu", 16))

    #Menampilkan widgets PBB
    PBB_label.grid(row=0, column=0, columnspan=2, pady=(150,40))
    LuasTanah_label.grid(row=1, column=0,pady = 20)
    LuasTanah_entry.grid(row=1, column=1, pady=20)
    LuasBangunan_label.grid(row=2, column=0, pady=20)
    LuasBangunan_entry.grid(row=2, column=1, pady=20)
    submit_button.grid(row=5, column=0, columnspan=2, pady=30)
    HasilPBB.grid(row=6, column=0, columnspan=2, pady=30)
    backBTN.grid(row=8, column=0, columnspan=2, pady=30)

# Membuat halaman bill
def halaman_bill():
    main.withdraw()
    bill = Toplevel()
    bill.title("Hi Papi")
    bill.attributes('-fullscreen', True)
    bill.configure(bg='#E1E5F2')
    framebill = Frame(bill,bg='#E1E5F2')
    framebill.pack(pady=20)

    # Menghitung total pajak pribadi
    global TotalAkhirPP, TotalAkhirPK, TotalAkhirPBB, FormatedTotalPAPI, TotalPAPI
    TotalPAPI = TotalAkhirPP+TotalAkhirPK+TotalAkhirPBB
    FormatedTotalPAPI = format_rupiah(TotalPAPI)

    #Fungsi kembali
    def Back():
        bill.withdraw()
        main.deiconify()

    #Membuat widgets halaman bill
    bill_label = tk.Label(framebill, text="Bill", bg='#E1E5F2', fg="#022B3A", font=("Ubuntu", 30))
    LabelNama1 = tk.Label(framebill, text="Nama", bg='#E1E5F2', fg="#022B3A", font=("Ubuntu", 16),width=30)
    LabelNama2 = tk.Label(framebill, text=f"{DataDiri[0]}", bg='#FFFFFF', fg="#022B3A", font=("Ubuntu", 16),width=30)   
    LabelPP1 = tk.Label(framebill, text="Jumlah Pajak Penghasilan", bg='#E1E5F2', fg="#022B3A", font=("Ubuntu", 16),width=30)
    LabelPP2 = tk.Label(framebill, text=f"{FormatedTotalPP}", bg='#FFFFFF', fg="#022B3A", font=("Ubuntu", 16),width=30)
    LabelPK1 = tk.Label(framebill, text="Jumlah Pajak Kendaraan", bg='#E1E5F2', fg="#022B3A", font=("Ubuntu", 16),width=30)
    LabelPK2 = tk.Label(framebill, text=f"{FormatedTotalPK}", bg='#FFFFFF', fg="#022B3A", font=("Ubuntu", 16),width=30)    
    LabelPBB1 = tk.Label(framebill, text="Jumlah Pajak Bumi dan Bangunan", bg='#E1E5F2', fg="#022B3A", font=("Ubuntu", 16),width=30)
    LabelPBB2 = tk.Label(framebill, text=f"{FormatedTotalPBB}", bg='#FFFFFF', fg="#022B3A", font=("Ubuntu", 16),width=30)
    LabelPAPI1 = tk.Label(framebill, text="Total Pajak Yang Dibayarkan", bg='#E1E5F2', fg="#022B3A", font=("Ubuntu", 16),width=30)
    LabelPAPI2 = tk.Label(framebill, text=f"{FormatedTotalPAPI}", bg='#FFFFFF', fg="#022B3A", font=("Ubuntu", 16),width=30)
    backBTN = tk.Button(framebill, text="Kembali", bg="#022B3A", fg="#FFFFFF", font=("Ubuntu", 16), command=Back)

    # Menampilkan widgets halaman bill
    bill_label.grid(row=0, column=4, columnspan=2, sticky="news", pady=(50))
    LabelNama1.grid(row=1, column=1,pady = 10)
    LabelNama2.grid(row=1, column=7,pady = 10)
    LabelPP1.grid(row=2, column=1, sticky="news", pady=10)
    LabelPP2.grid(row=2, column=7, sticky="news", pady=10)
    LabelPK1.grid(row=3, column=1, sticky="news", pady=10)
    LabelPK2.grid(row=3, column=7, sticky="news", pady=10)
    LabelPBB1.grid(row=4, column=1, sticky="news", pady=10)
    LabelPBB2.grid(row=4, column=7, sticky="news", pady=10)
    LabelPAPI1.grid(row=5, column=1, sticky="news", pady=10)
    LabelPAPI2.grid(row=5, column=7, sticky="news", pady=10)
    backBTN.grid(row=15, column=4, columnspan=2, sticky="news", pady=(350,0))

# Membuat halaman tentang pajak
def halaman_tentang_pajak():
    main.withdraw()
    TP = tk.Tk()
    TP.title("Hi Papi")
    TP.attributes('-fullscreen', True)
    TP.configure(bg='#E1E5F2')
    frameTP = tk.Frame(TP, bg="#E1E5F2")
    frameTP.grid(sticky='nsew')
    TP.grid_rowconfigure(0, weight=1)
    TP.grid_columnconfigure(0, weight=1)

    # Membuat label judul
    label = tk.Label(frameTP, text="Tentang Pajak", font=("Ubuntu", 30), bg="#E1E5F2")
    label.grid(row=0, column=0, pady=10)

    # Membuat scrollbar
    scrollbar = tk.Scrollbar(frameTP)
    scrollbar.grid(row=1, column=1, sticky='ns')

    # Membuat text box dengan background
    text = scrolledtext.ScrolledText(frameTP, wrap='word', yscrollcommand=scrollbar.set, font=("Ubuntu", 16), bg="#E1E5F2")
    text.grid(row=1, column=0, sticky='nsew', padx=20, pady=10)

    # Mengisi text box dengan konten
    content = """
    1. Pajak

    a) Pengertian Pajak
    Pajak merupakan salah satu bagian penting dari perkembangan suatu negara. Pajak wajib dibayarkan oleh masyarakat pada suatu negara dalam bentuk dana berdasarkan jenis tertentu. Terdapat beberapa pengertian pajak menurut para ahli, yaitu sebagai berikut:
    1) Menurut Kamus Besar Bahasa Indonesia (KBBI), arti kata pajak adalah pungutan wajib, biasanya berupa uang yang harus dibayar oleh penduduk sebagai sumbangan wajib kepada negara atau pemerintah sehubungan dengan pendapatan, pemilikan, harga beli barang, dan sebagainya.
    2) Menurut (Novia, 2009) pajak adalah iuran yang harus dibayarkan oleh seluruh rakyat sebagai sumbangan pada negara.
    3) Menurut (Wahyuningsih, 2016) pajak adalah peralihan kekayaan dari pihak rakyat kepada Kas Negara untuk membiayai pengeluaran rutin dan surplusnya digunakan untuk public saving yang merupakan sumber utama untuk membiayai public investment.
    Berdasarkan beberapa sumber tersebut dapat disimpulkan bahwa pajak merupakan salah satu dana yang harus dibayarkan oleh wajib pajak berdasarkan UU yang berlaku. Hal tersebut berarti wajib pajak dapat mendapatkan pidana jika melanggar peraturan dalam wajib pajak.

    b) Fungsi Pajak
    Pajak memiliki peranan penting dalam upaya pembangunan suatu negara. Hal ini dikarenakan pajak merupakan sumber pendapatan negara untuk membiayai pengeluaran, termasuk pengeluaran pembangunan (Kusnanto, 2019). Dilansir dari DTDC News, pajak merupakan salah satu sumber pembiayaan pembangunan yang paling besar dan berkelanjutan, kerana pajak berkontribusi sebesar 80% dari total pendapatan pada 50% negara di dunia, termasuk Indonesia. Selain fungsi pembiayaan,  pajak memiliki beberapa fungsi utama, yaitu sebagai berikut:
    1) Fungsi anggaran
    Fungsi anggaran atau budgetair adalah fungsi utama pajak. Pajak digunakan sebagai alat pemasukan dana secara finansial pada suatu negara berdasarkan undang-undang yang berlaku pada negara tersebut.
    2) Fungsi mengatur
    Fungsi mengatur atau regulerend adalah fungsi pajak sebagai alat untuk mengatur perekonomian negara. Fungsi tersebut dapat berlawanan dengan fungsi anggaran karena pelaksanaan fungsi tersebut akan melibatkan kebijakan tertentu yang dapat mempengaruhi faktor tercapainya finansial negara yang sehat. Misalnya, untuk menstabilkan harga minya goreng di dalam negeri, pemerintah membangun PPN atas penyerahan minyak goreng yang dapat berdampak pada anggaran negara.
    3) Fungsi stabilitas
    Fungsi stabilitas pajak adalah fungsi yang digunakan untuk menjalankan kebijakan yang berhubungan dengan stabilitas harga sehingga inflasi dapat dikendalikan.
    4) Fungsi pendistribusi pendapatan
    Fungsi keempat adalah fungsi pendistribusi yang merupakan salah satu fungsi pajak yaitu penggunaan pajak untuk membiayai semua kepentingan umum, termasuk untuk membiayai pembangunan. Hal tersebut dapat berdampak pada peningkatan pendapatan masyarakat.

    c) Dasar Hukum Pajak
    Peraturan mengenai perpajakan di Indonesia diatur pada Undang-Undang Republik Indonesia yang merupakan dasar ketentuan umum perpajakan di Indonesia. Kewajiban membayar pajak tercantum dalam pasal 23 A UUD 1945 yang berbunyi “Pajak dan pungutan lain yang bersifat memaksa untuk keperluan negara diatur dengan undang-undang”.

    2. Pajak Bumi dan Bangunan

    a) Pengertian Pajak Bumi dan Bangunan
    Pajak memiliki berbagai jenis, salah satunya adalah Pajak Bumi dan Bagunan (PBB). PBB adalah pajak yang dikenakan atas kepemilikan atau pemanfaatan tanah atau bangunan. PBB merupakan pajak pusat. Perlakuan perpajakan atas perolehan hak atas tanah dan bangunan dapat dikenakan kepada penjual atau yang mengalihkan dan kepada pembeli atau yang menerima pengalihan. (Muljono, 2010)
    Bangunan yang dikenai Pajak Bumi Bangunan, selain rumah tinggal dan gedung, mencakup pula jalan lingkungan yang terletak dalam satu kompleks bangunan seperti hotel, pabrik, jalan tol, kolam renang, pagar mewah, taman mewah, tempat olahraga, galangan kapal, dermaga, dan tempat penampungan. (Kusnanto, 2019)

    b) Dasar Hukum Pajak Bumi dan Bangunan
    Peraturan mengenai Pajak Bumi Bangunan tertulis pada undang-undang perpajakan dan peraturan kementerian terkait. Terdapat beberapa peraturan yang mengikat tentang Pajak Bumi Bangunan di Indonesia seperti, undang-undang Nomor 12 Tahun 1985 tentang Pajak Bumi dan Bangunan yang berbunyi, ”bumi dan bangunan memberikan keuntungan dan/atau kedudukan sosial ekonomi yang lebih baik bagi orang atau badan yang mempunyai suatu hak atasnya atau memperoleh manfaat dari padanya, dan oleh karena itu wajar apabila mereka diwajibkan memberikan sebagian dari manfaat atau kenikmatan yang diperolehnya kepada negara melalui pajak”.

    3. Pajak Penghasilan

    a) Pengertian Pajak Penghasilan
    Pajak Penghasilan (PPH) merupakan salah satu jenis pajak pribadi yang harus dibayarkan oleh wajib pajak. Penghasilan yang dimaksud adalah setiap tambahan kemampuan ekonomis yang berasal dari Indonesia dan/atau dari luar Indonesia yang dapat digunakan untuk konsumsi atau untuk menambah kekayaan dengan nama dan dalam bentuk apapun. (Kusnanto, 2019)
    Subjek Pajak Penghasilan terdiri dari beberapa aspek seperti orang pribadi, warisan yang belum terbagi, dan Bentuk Usaha Tetap (BUT). Sedangkan objek pajak terdiri dari subjek pajak dalam negeri dan subjek pajak luar negeri. (Muljono, 2010)

    b) Dasar Hukum Pajak Penghasilan
    Ketentuan dalam perhitungan Pajak Penghasilan telah diatur pada peraturan kementerian keuangan dan Undang-Undang. Peraturan perundang-undangan yang mendasari kewajiban pajak penghasilan tertera pada Undang-Undang Nomor 7 Tahun 2021 atas perubahan dari Undang-Undang Nomor 36 Tahun 2008.

    4. Pajak Kendaraan

    a) Pengertian Pajak Kendaraan
    Pajak kendaraan bermotor merupakan pajak yang dikenakan kepada wajib pajak sebagai salah satu bentuk kontribusi wajib pajak kepada negara dalam hal penggunaan kendaraan bermotor. Pengertian pajak kendaraan bermotor didefinisikan pada Pasal 1 angka 12 dan 13 Undang-Undang Nomor 28 Tahun 2009 tentang Pajak Daerah dan Retribusi Daerah (UU PDRD) yang menyebutkan bahwa pajak kendaraan bermotor merupakan pajak atas kepemilikan dan/atau penguasaan kendaraan bermotor. (Abdullah, 2017)
    Pajak kendaraan bermotor didistribusikan dan dikelola oleh pemerintah provinsi yang merupakan bagian dari pajak daerah. Pengadaan pajak kendaraan bermotor memiliki tujuan seperti pengurangan presentase jumlah polusi udara, pengurangan kemacetan dan penanggunalangan kecelakaan lalu lintas. (Muhtarudin, 2023)

    b) Dasar Hukum Pajak Kendaraan
    Definisi dari pajak kendaraan telah diatur pada Pasal 1 angka 12 dan 13 Undang-Undang Nomor 28 Tahun 2009 tentang pajak Daerah dan Retribusi Daerah (UU PDRD). Pada implementasi perpajakan, peraturan terkait pajak kendaraan diatur pada PERMENDAGRI No. 1 Tahun 2021 tentang perhitungan dasar pengenaan pajak kendaraan bermotor dan bea balik nama.
    """
    text.insert('insert', content)

    # Menambahkan format bold untuk bagian 'II.1 Pajak', 'II.2 Pajak Bumi dan Bangunan', 'II.3 Pajak Penghasilan', 'II.4 Pajak Kendaraan'
    for section in ['1. Pajak', 'a) Pengertian Pajak', 'b) Fungsi Pajak', 'c) Dasar Hukum Pajak', '2. Pajak Bumi dan Bangunan', 'a) Pengertian Pajak Bumi dan Bangunan', 'b) Dasar Hukum Pajak Bumi dan Bangunan', '3. Pajak Penghasilan', 'a) Pengertian Pajak Penghasilan', 'b) Dasar Hukum Pajak Penghasilan', '4. Pajak Kendaraan', 'a) Pengertian Pajak Kendaraan', 'b) Dasar Hukum Pajak Kendaraan']:
        start_index = text.search(section, '1.0', tk.END)
        end_index = text.index(f'{start_index} lineend +1c')
        text.tag_add('bold', start_index, end_index)
        text.tag_configure('bold', font=('Ubuntu', 16, 'bold'))

    # Membuat text box menjadi read-only
    text.config(state='disabled')

    # Menghubungkan scrollbar dengan text box
    scrollbar.config(command=text.yview)

    # Fungsi kembali
    def Back():
        TP.withdraw()
        main.deiconify()

    # Membuat tombol kembali
    backBTN = tk.Button(
        frameTP, text="Kembali", bg="#022B3A", fg="#FFFFFF", font=("Ubuntu", 16), command=Back)
    backBTN.grid(row=2, column=0, pady=10)

    # Menjadikan frame content agar mengisi seluruh window
    frameTP.grid_rowconfigure(1, weight=1)
    frameTP.grid_columnconfigure(0, weight=1)

# Membuat halaman keluar
def halaman_keluar():
    main.withdraw()
    exitprog = Toplevel()
    exitprog.title("Hi Papi")
    exitprog.attributes('-fullscreen', True)
    exitprog.configure(bg='#E1E5F2')
    framekeluar = Frame(exitprog,bg='#E1E5F2')
    framekeluar.pack()
    
    # Fungsi keluar
    def keluar():
        exit()

    # Membuat widgets halaman keluar
    keluar_label = tk.Label(framekeluar, text="Terima kasih telah menggunakan program ini!", bg='#E1E5F2', fg="#022B3A", font=("Ubuntu", 30))
    subheader = tk.Label(framekeluar, text="Beli barang elit, bayar pajak sulit. Chuaks~", bg='#E1E5F2', fg="#022B3A", font=("Ubuntu", 16))
    keluar_button = tk.Button(framekeluar, text="Keluar", bg="#022B3A", fg="#FFFFFF", font=("Ubuntu", 16), command=keluar)
    
    # Menampilkan widgets halaman keluar
    keluar_label.grid(row=0, column=4, columnspan=2, pady=(340,10))
    subheader.grid(row=1, column=4, columnspan=2, pady=0)
    keluar_button.grid(row=5, column=4,columnspan=2,pady = 30)   

# Membuat widgets menu utama
button_width = 35
button_height = 1

menu_utama_label = Label(frame, text="MENU UTAMA", bg='#022B3A', fg="#FFFFFF", font=("Ubuntu", 30))
pajak_penghasilan = Button(frame, text="Hitung Pajak Penghasilan", bg="#FFFFFF", fg="#022B3A", font=("Ubuntu", 16), width=button_width, height=button_height, command=halaman_pajak_penghasilan)
pajak_kendaraan = Button(frame, text="Hitung Pajak Kendaraan", bg="#FFFFFF", fg="#022B3A", font=("Ubuntu", 16), width=button_width, height=button_height, command=halaman_pajak_kendaraan)
pajak_bb = Button(frame, text="Hitung Pajak Bumi dan Bangunan", bg="#FFFFFF", fg="#022B3A", font=("Ubuntu", 16), width=button_width, height=button_height, command=halaman_pbb)
bill = Button(frame, text="Cetak Bill", bg="#FFFFFF", fg="#022B3A", font=("Ubuntu", 16), width=button_width, height=button_height, command=halaman_bill)
tentang_pajak = Button(frame, text="Tentang Pajak", bg="#FFFFFF", fg="#022B3A", font=("Ubuntu", 16), width=button_width, height=button_height, command=halaman_tentang_pajak)
keluar = Button(frame, text="Keluar", bg="#022B3A", fg="#FFFFFF", font=("Ubuntu", 16), command=halaman_keluar)

# Menampilkan widgets menu utama
menu_utama_label.grid(row=0, column=0, padx=10, pady=(170,40))
pajak_penghasilan.grid(row=1, column=0, padx=10, pady=10)
pajak_kendaraan.grid(row=2, column=0, padx=10, pady=10)
pajak_bb.grid(row=3, column=0, padx=10, pady=10)
bill.grid(row=4, column=0, padx=10, pady=10)
tentang_pajak.grid(row=5, column=0, padx=10, pady=10)
keluar.grid(row=9, column=0, padx=10, pady=10)

main.mainloop()