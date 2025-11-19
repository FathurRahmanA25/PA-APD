# Manajemen Pembayaran & Tagihan
from utilitas import clear

# Untuk Sementara Fungsi Fungsi nya Masih Kosong
def tampilkan_laporan_konfirmasi():
    clear()
    print("=" * 75)
    print("LAPORAN KONFIRMASI PEMBAYARAN")
    print("=" * 75)
    input("Tekan Enter untuk kembali...")

def lihat_tagihan_mendatang():
    clear()
    print("=" * 75)
    print("TAGIHAN YANG AKAN DATANG")
    print("=" * 75)
    input("Tekan Enter untuk kembali...")


def riwayat_pembayaran():
    clear()
    print("=" * 75)
    print("RIWAYAT PEMBAYARAN")
    print("=" * 75)
    input("Tekan Enter untuk kembali...")

def status_kontrakan():
    clear()
    print("=" * 75)
    print("STATUS KONTRAKAN")
    print("=" * 75)
    input("Tekan Enter untuk kembali...")

def hapus_bukti_pembayaran():
    clear()
    print("=" * 75)
    print("HAPUS BUKTI PEMBAYARAN")
    print("=" * 75)
    input("Tekan Enter untuk kembali...")

# Menu Kelola Tagihan
def kelolaTagihan(): 
    while True:
        clear()
        print("=" * 75)
        print("MANAJEMEN PEMBAYARAN & TAGIHAN")
        print("=" * 75)
        print("[1] - Buat Laporan Konfirmasi Pembayaran")
        print("[2] - Lihat Tagihan yang Akan Datang")
        print("[3] - Lihat Status Kontrakan")
        print("[4] - Lihat Riwayat Pembayaran")
        print("[5] - Hapus Bukti Pembayaran")
        print("[0] - Kembali ke Menu Sebelumnya")
        print("=" * 75)

        pilih = input("> ")

        if pilih == "0":
            break
        elif pilih == "1":
            tampilkan_laporan_konfirmasi
        elif pilih == "2":
            lihat_tagihan_mendatang()
        elif pilih == "3":
            status_kontrakan()
        elif pilih == "4":
            riwayat_pembayaran()
        elif pilih == "5":
            hapus_bukti_pembayaran()
        else:
            print("Pilihan tidak valid.")