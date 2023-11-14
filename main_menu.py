# Program python untuk menghitung pajak pribadi

# Membuat variabel untuk menyimpan nilai pajak
total_pajak_penghasilan = 0
total_pajak_kendaraan = 0
total_pbb = 0

def tampilan_awal():
    print("SELAMAT DATANG DI HI PAPI\nIni adalah program untuk menghitung pajak pribadi Anda")

tampilan_awal()

def menu_identitas():
    print("\n")
    x = input("Masukkan Nama Anda: ")
    y = input("Masukkan Asal Daerah: ")
    z = input("Masukkan Status Perkawinan (K/BK): ")
    return x, y, z

x, y, z = menu_identitas()

def struk_hasil():
    data = {
        "Nama": x.capitalize(),
        "Daerah": y.capitalize(),
        "Status Perkawinan": z.capitalize()
    }

# Fungsi untuk menampilkan menu utama
def menu_utama():
    print("\n")
    print("Menu Utama")
    print("1. Menghitung Pajak Penghasilan")
    print("2. Menghitung Pajak Kendaraan")
    print("3. Menghitung Pajak Bumi dan Bangunan")
    print("4. Cetak Bill")
    print("5. Keluar")
    pilihan = int(input("Masukkan pilihan Anda (1-5): "))
    return pilihan

# Fungsi untuk menghitung pajak penghasilan
def pajak_penghasilan():
    print("\n")
    print("Menghitung Pajak Penghasilan")
    gaji_pokok = int(input("Masukkan gaji pokok (per bulan): "))
    gaji_pokok_tahunan = gaji_pokok*12
    gaji_tambahan = int(input("Masukkan gaji tambahan (per bulan): "))
    gaji_tambahan_tahunan = gaji_tambahan*12
    if gaji_tambahan == 0:
        bruto = gaji_pokok_tahunan
    else:
        bruto = gaji_pokok_tahunan + gaji_tambahan_tahunan
    
    while True:
        status = input("Masukkan status pekerjaan (Swasta/PNS): ").capitalize()
        if status.capitalize() == "Swasta" or status.upper() == "PNS":
            break  # Keluar dari loop jika input valid
        else:
            print("Status pekerjaan yang Anda masukkan tidak valid, silakan ulangi.")
    
    if status == "Swasta":
        iuran_hari_tua = (3/100)*bruto
        netto = bruto - iuran_hari_tua
    else:
        biaya_jabatan = (5/100)*bruto
        netto = bruto - biaya_jabatan

    tanggungan = int(input("Masukkan jumlah tanggungan: "))

    if z == "K":
        if tanggungan == 0:
            pkp = netto - 58_500_000 if netto >= 58_500_000 else 0
        elif tanggungan == 1:
            pkp = netto - 63_000_000 if netto >= 63_000_000 else 0
        elif tanggungan == 2:
            pkp = netto - 67_500_000 if netto >= 67_500_000 else 0
        else:
            pkp = netto - 72_000_000 if netto >= 72_000_000 else 0
    else:
        if tanggungan == 0:
            pkp = netto - 54_000_000 if netto >= 54_000_000 else 0
        elif tanggungan == 1:
            pkp = netto - 58_500_000 if netto >= 58_500_000 else 0
        elif tanggungan == 2:
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
    lanjut = input("Lanjut menghitung pajak kendaraan? (y/n)")
    if lanjut.lower() == "y":
        pajak_kendaraan()
    else:
        return total_pajak_penghasilan
        print()

# Fungsi untuk menghitung pajak kendaraan
def pajak_kendaraan():
    print("\n")
    print("Menghitung Pajak Kendaraan")
    
    while True:
        jenis_kendaraan = input("Masukkan jenis kendaraan (Motor/Mobil): ")
        if jenis_kendaraan.capitalize() == "Motor" or jenis_kendaraan.capitalize() == "Mobil":
            break  # Keluar dari loop jika input valid
        else:
            print("Jenis kendaraan yang Anda masukkan tidak valid, silakan ulangi.")

    global total_pajak_kendaraan
    total_pajak_kendaraan = 0

    if jenis_kendaraan.capitalize() == "Motor":
        cc_motor = int(input("Masukkan besar CC motor: "))
        if cc_motor < 250:
            swdkllj_motor = 35_000
        elif 250 <= cc_motor < 1000:
            swdkllj_motor = 80_000
        else:
            print("CC motor yang Anda masukkan termasuk dalam kategori pajak barang mewah")
            return  # Menghentikan perhitungan pajak kendaraan

        nilai_jual_motor = int(input("Masukkan nilai jual motor: "))
        pkb_motor = nilai_jual_motor * 2 / 100
        pajak_motor = pkb_motor + swdkllj_motor
        print("Pajak kendaraan yang harus dibayar adalah", pajak_motor, "rupiah")
        total_pajak_kendaraan += pajak_motor
    else:
        cc_mobil = int(input("Masukkan besaran CC mobil: "))
        if cc_mobil < 3000:
            swdkllj_mobil = 140_000
        else:
            print("CC mobil yang Anda masukkan termasuk dalam kategori pajak barang mewah")
            return  # Menghentikan perhitungan pajak kendaraan

        nilai_jual_mobil = int(input("Masukkan nilai jual mobil: "))
        pkb_mobil = nilai_jual_mobil * 2 / 100
        pajak_mobil = pkb_mobil + swdkllj_mobil
        print("Pajak kendaraan yang harus dibayar adalah", pajak_mobil, "rupiah")
        total_pajak_kendaraan += pajak_mobil
          
    lanjut = input("Lanjut menghitung pajak bumi dan bangunan? (y/n)")
    if lanjut.lower() == "y":
        pajak_bumi_dan_bangunan()
    else:
        print()

# Fungsi untuk menghitung pajak bumi dan bangunan
def pajak_bumi_dan_bangunan():
    print("\n")
    print("Menghitung Pajak Bumi dan Bangunan")
    luas_tanah = int(input("Masukkan luas tanah (dalam meter persegi): "))
    luas_bangunan = int(input("Masukkan luas bangunan (dalam meter persegi): "))
    njop_luas_tanah = luas_tanah * 2_200_000
    njop_luas_bangunan = luas_bangunan * 1_100_000
    njop_total = njop_luas_tanah + njop_luas_bangunan
    njop_pbb = njop_total - 15_000_000
    pbb_terhutang = 0.1 / 100 * njop_pbb

    global total_pbb
    total_pbb = pbb_terhutang
    print("Pajak bumi dan bangunan yang harus dibayar adalah", pbb_terhutang, "rupiah")
    lanjut = input("Lanjut menghitung pajak penghasilan? (y/n)")
    if lanjut.lower() == "y":
        pajak_penghasilan()
    else:
        print()

def total_pajak():
    global total_pajak_penghasilan
    global total_pajak_kendaraan
    global total_pbb
    return total_pajak_penghasilan + total_pajak_kendaraan + total_pbb

# Fungsi untuk menanyakan apakah ingin kembali ke menu utama
def kembali():
    jawab = input("Apakah Anda ingin kembali ke menu utama? (y/n): ")
    if jawab.lower() == "y":
        main()
    elif jawab.lower() == "n":
        keluar()
    else:
        print("Pilihan tidak valid, silakan ulangi")
        kembali()

# Fungsi untuk keluar dari program
def keluar():
    print("Terima kasih telah menggunakan program ini")
    exit()

# Fungsi untuk mencetak bill berdasarkan nomor data perhitungan
def cetak_hasil():
    print("Struk Hasil:")
    print("Nama: ",x.capitalize())
    print("Jumlah pajak penghasilan yang harus dibayar: ",total_pajak_penghasilan,"rupiah")
    print("Jumlah pajak kendaraan yang harus dibayar:", total_pajak_kendaraan,"rupiah")
    print("Jumlah pajak bumi dan bangunan yang harus dibayar: ",total_pbb,"rupiah")
    total_pajak_pribadi = total_pajak()
    print("\n")
    print("Jumlah pajak pribadi yang harus dibayar: ",total_pajak_pribadi,"rupiah")
    keluar()

# Fungsi utama untuk menjalankan program
def main():
    while True:
        pilihan = menu_utama()
        if pilihan == 1:
            pajak_penghasilan()
            kembali()
        elif pilihan == 2:
            pajak_kendaraan()
            kembali()
        elif pilihan == 3:
            pajak_bumi_dan_bangunan()
            kembali()
        elif pilihan == 4:
            cetak_hasil()
        elif pilihan == 5:
            keluar()
        else:
            print("Pilihan tidak valid, silakan ulangi")

# Memanggil fungsi utama
main()