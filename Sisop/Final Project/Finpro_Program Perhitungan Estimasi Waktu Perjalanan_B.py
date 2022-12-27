print("-" * 50)
print("|          SELAMAT DATANG DI PROGRAM SISOP        |")
print("|       PERHITUNGAN ESTIMASI WAKTU PERJALANAN     |")
print("-" * 50)
print("|             Oleh : Mutiara Irmadhani            |")
print("|              NPM : 21083010079                  |")
print("-" * 50)


print("-" * 50)
print("|                   FITUR                         |")
print("| 1. Pasuruan - Mojokerto*                        |")
print("| 2. Surabaya - Blitar*                           |")
print("| 3. Probolinggo - Surabaya*                      |")
print("| 4. Malang - Madiun*                             |")
print("| 5. Custom Tujuan                                |")
print("| 6. Exit                                         |")
print("|                                                 |")
print("| *Sering Dicari                                  |")
print("-" * 50)


def memilih():
    print("+" *90)
    a = input("Silahkan dipilih\n1. Pasuruan - Mojokerto\n2. Surabaya - Blitar"
              "\n3. Probolinggo - Surabaya\n4. Malang - Madiun"
              "\n5. Custom Tujuan\n6. Exit\n Pilihan anda: ")
    return a
pilihan = 1
while pilihan <=6 :
    pilihan = int(memilih())
    if pilihan == 1:
        print("+" *90)
        print ("Estimasi Waktu perjalanan Pasuruan - Mojokerto adalah ")
        jarak = input("Masukkan jarak perjalanan (km):")
        jarak = float(jarak)
        kecepatan = input("Masukkan rata-rata kecepatan (km/jam):")
        kecepatan = float(kecepatan)
        waktuTempuh = jarak/kecepatan
        print("Estimasi Waktu Tempuh perjalanan anda : ", waktuTempuh," jam")
        print("Selamat menikmati perjalanan anda, Berkendara dengan hati-hati dan aman")
        print("+" *90)
        print("\n")
        continue
    elif pilihan == 2:
        print("+" *90)
        print ("Estimasi Waktu perjalanan Surabaya - Blitar adalah ")
        jarak = input("Masukkan jarak perjalanan (km):")
        jarak = float(jarak)
        kecepatan = input("Masukkan rata-rata kecepatan (km/jam):")
        kecepatan = float(kecepatan)
        waktuTempuh = jarak/kecepatan
        print("Estimasi Waktu Tempuh perjalanan anda : ", waktuTempuh," jam")
        print("Selamat menikmati perjalanan anda, Berkendara dengan hati-hati dan aman")
        print("+" *90)
        print("\n")
        continue
    elif pilihan == 3:
        print("+" *90)
        print ("Estimasi Waktu perjalanan Probolinggo - Surabaya adalah ")
        jarak = input("Masukkan jarak perjalanan (km):")
        jarak = float(jarak)
        kecepatan = input("Masukkan rata-rata kecepatan (km/jam):")
        kecepatan = float(kecepatan)
        waktuTempuh = jarak/kecepatan
        print("Estimasi Waktu Tempuh perjalanan anda : ", waktuTempuh," jam")
        print("Selamat menikmati perjalanan anda, Berkendara dengan hati-hati dan aman")
        print("+" *90)
        print("\n")
        continue
    elif pilihan == 4:
        print("+" *90)
        print ("Estimasi Waktu perjalanan Malang - Madiun adalah ")
        jarak = input("Masukkan jarak perjalanan (km):")
        jarak = float(jarak)
        kecepatan = input("Masukkan rata-rata kecepatan (km/jam):")
        kecepatan = float(kecepatan)
        waktuTempuh = jarak/kecepatan
        print("Estimasi Waktu Tempuh perjalanan anda : ", waktuTempuh," jam")
        print("Selamat menikmati perjalanan anda, Berkendara dengan hati-hati dan aman")
        print("+" *90)
        print("\n")
        continue
    elif pilihan == 5:
        print("+" *90)
        print ("Custom Tujuan Anda ")
        berangkat = input("Masukkan Kota Keberangkatan Anda : ")
        tujuan = input("Masukkan Kota tujuan Anda : ")
        jarak = input("Masukkan jarak perjalanan (km):")
        jarak = float(jarak)
        kecepatan = input("Masukkan rata-rata kecepatan (km/jam):")
        kecepatan = float(kecepatan)
        waktuTempuh = jarak/kecepatan
        print("Estimasi Waktu Tempuh perjalanan anda dari", berangkat, "ke", tujuan, "dengan jarak", jarak, "km adalah", waktuTempuh," jam")
        print("Selamat menikmati perjalanan anda, Berkendara dengan hati-hati dan aman")
        print("+" *90)
        print("\n")
        continue
    elif pilihan == 6:
        print("+" *90)
        print("=" * 30)
        print("| Exit                       |")
        print("*" * 30)
        print("| Berhasil Keluar            |")
        print("=" * 30)
        print("+" *90)
        print("\n")
        break
    else :
        print("+" *90)
        print("Maaf fitur tidak tersedia, Silahkan masukkan pilihan fitur sesuai yang tersedia")
        print("+" *90)
        ulang = input("Apakah anda ingin kembali ke fitur? (y/n):")
    if ulang == "y":
       print("pilihan anda : ")
       pilihan = int(memilih())
    elif ulang == "N":
       print("exit")

    break

