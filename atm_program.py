import random
import datetime
from customer import Customer

atm = Customer(id)

while True :
    id = int(input("Masukkan pin Anda : "))
    trial = 0
    while (id != int(atm.checkPin()) and trial < 3) :
        id = int(input("Pin Anda salah. Silakan masukkan lagi : "))
        trial += 1
        if trial == 3 :
            print("Error. Silakan ambil kartu dan coba lagi..")
            exit()
    while True :
        print("Selamat datang di program ATM..")
        print("\n1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar")
        selectMenu = int(input("\nSilakan pilih menu : "))
        if selectMenu == 1 :
            print("\nSaldo Anda sekarang : Rp. " + str(atm.checkBalance()) + "\n")
        elif selectMenu == 2 :
            nominal = float(input("Masukkan nominal saldo : "))
            verifyWithdraw = input("Konfirmasi : Anda akan melakukan debet dengan nominal berikut? y/n " + str(nominal) + " ")
            if verifyWithdraw == "y" :
                print("Saldo awal Anda adalah : Rp. " + str(atm.checkBalance()) + "")
            else :
                break
            if nominal < atm.checkBalance() :
                atm.withDrawBalance(nominal)
                print("Transaksi debet berhasil!")
                print("Sisa saldo saat ini : Rp. " + str(atm.checkBalance()) + "")
            else :
                print("Maaf. Saldo Anda tidak cukup untuk melakukan debet!")
                print("Silakan lakukan penambahan nominal saldo")
        elif selectMenu == 3 :
            nominal = float(input("Masukkan nominal saldo : "))
            verifyDeposit = input("Konfirmasi : Anda akan melakukan penyimpanan dengan nominal berikut? y/n " + str(nominal) + " ")
            if verifyDeposit == "y" :
                atm.depositBalance(nominal)
                print("Saldo Anda saat ini : Rp. " + str(atm.checkBalance()) + "\n")
            else :
                break
        elif selectMenu == 4 :
            verifyPin = int(input("Masukkan pin Anda : "))
            while verifyPin != int(atm.checkPin()) :
                print("Pin Anda salah. Silakan masukkan kembali.")
                verifyPin = int(input("Masukkan pin Anda : "))
            updatedPin = int(input("Silakan masukkan pin baru : "))
            print("Pin Anda berhasil diganti!")
            verifyNewPin = int(input("Verifikasi pin baru : "))
            if(verifyNewPin == updatedPin) :
                print("Pin Anda berhasil diubah!")
            else :
                print("Maaf. Pin tidak sesuai!")
        elif selectMenu == 5 :
            print("Resi tercetak otomatis saat Anda keluar.\nHarap simpan tanda terima ini\nsebagai bukti transaksi Anda.")
            print("No. Record : ", random.randint(100000, 1000000))
            print("Tanggal : ", datetime.datetime.now())
            print("Saldo akhir : Rp. ", atm.checkBalance())
            print("Terima kasih telah menggunakan program ATM!")
            exit()
        else :
            print("Error. Maaf, menu tidak tersedia.")