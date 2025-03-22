from collections import deque

class Antrian:
    def __init__(self):
        self.antrian = deque()
        self.id_counter = 1

    def enqueue(self, nama):
        id_mahasiswa = self.id_counter
        self.antrian.append({"id": id_mahasiswa, "nama": nama})
        self.id_counter += 1
        print(f"Antrian {nama} dengan ID {id_mahasiswa} telah ditambahkan.")

    def dequeue(self):
        if len(self.antrian) == 0:
            print("Antrian kosong.")
        else:
            mahasiswa = self.antrian.popleft()
            print(f"Antrian {mahasiswa['nama']} dengan ID {mahasiswa['id']} telah diambil.")

    def cetak_antrian(self):
        if len(self.antrian) == 0:
            print("Antrian kosong.")
        else:
            print("Antrian Mahasiswa Baru:")
            for i, mahasiswa in enumerate(self.antrian, start=1):
                print(f"{i}. {mahasiswa['nama']} (ID: {mahasiswa['id']})")

antrian = Antrian()

while True:
    print("\nMenu:")
    print("1. Input Antrian (Enqueue)")
    print("2. Ambil Antrian (Dequeue)")
    print("3. Cetak Antrian")
    print("4. Keluar")
    choice = input("Pilih menu: ")

    if choice == "1":
        nama = input("Masukkan nama mahasiswa: ")
        antrian.enqueue(nama)
    elif choice == "2":
        antrian.dequeue()
    elif choice == "3":
        antrian.cetak_antrian()
    elif choice == "4":
        break
    else:
        print("Menu tidak tersedia.")