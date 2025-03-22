# Input nama user
Nama = input("Masukkan nama anda : ")

# Set untuk menyimpan hasil konversi
hasil_konversi = set()

# Pilih menu
while True:
    menu_options = [
        "1) Konversi dari Celcius - Fahrenheit",
        "2) Konversi dari Celcius - Reamur",
        "3) Konversi dari Celcius - Kelvin",
        "4) Konversi dari Fahrenheit - Celcius",
        "5) Konversi dari Reamur - Celcius",
        "6) Konversi dari Kelvin - Celcius",
        "7) Tampilkan hasil konversi",
        "8) Keluar"]
    
    print("\nMenu:")
    for item in menu_options:
        print(item)

    menu_pilihan = int(input("Masukkan pilihan menu : "))

    if menu_pilihan == 7:
        print("\nNama : ", Nama)
        print("Hasil konversi: ", hasil_konversi)
        ulang = input("\nApakah Anda ingin melakukan konversi lagi? (ya/tidak): ").strip().lower()
        if ulang == 'ya':
                print("\nMenu:")
                for item in menu_options:
                    print(item)
                menu_pilihan = int(input("Masukkan pilihan menu : "))
        else:
            print("Terima kasih! Program selesai.")
            break

    if menu_pilihan == 8:
        print("Terima kasih! Program selesai.")
        break
    
    # Input nilai suhu
    Suhu = float(input("Masukkan suhu : "))

    # Proses
    if menu_pilihan == 1:
            def celcius_ke_fahrenheit(nilai_celcius):
                return (nilai_celcius * 9/5) + 32
            hasil = f"Suhu : {Suhu}°C = {celcius_ke_fahrenheit(Suhu)}°F"
            hasil_konversi.add(hasil)
            print(hasil)
    elif menu_pilihan == 2:
            def celcius_ke_reamur(nilai_celcius):
                return nilai_celcius * 0.8
            hasil = f"Suhu : {Suhu}°C = {celcius_ke_reamur(Suhu)}°R"
            hasil_konversi.add(hasil)
            print(hasil)
    elif menu_pilihan == 3:
            def celcius_ke_kelvin(nilai_celcius):
                return nilai_celcius + 273
            hasil = f"Suhu : {Suhu}°C = {celcius_ke_kelvin(Suhu)}°K"
            hasil_konversi.add(hasil)
            print(hasil)
    elif menu_pilihan == 4:
            def fahrenheit_ke_celcius(nilai_fahrenheit):
                return (nilai_fahrenheit - 32) * 5/9
            hasil = f"Suhu : {Suhu}°F = {fahrenheit_ke_celcius(Suhu)}°C"
            hasil_konversi.add(hasil)
            print(hasil)
    elif menu_pilihan == 5:
            def reamur_ke_celcius(nilai_reamur):
                return nilai_reamur / 0.8
            hasil = f"Suhu : {Suhu}°R = {reamur_ke_celcius(Suhu)}°C"
            hasil_konversi.add(hasil)
            print(hasil)
    elif menu_pilihan == 6:
            def kelvin_ke_celcius(nilai_kelvin):
                return nilai_kelvin - 273
            hasil = f"Suhu : {Suhu}°K = {kelvin_ke_celcius(Suhu)}°C"
            hasil_konversi.add(hasil)
            print(hasil)
    else:
        print("Menu tidak tersedia.")

    