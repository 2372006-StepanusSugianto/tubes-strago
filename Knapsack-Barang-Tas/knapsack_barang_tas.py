import time

# Progress 2 - Strategi Algoritmik
# Topik  : Aplikasi Pemilihan Barang Bawaan Tas
# Metode : Knapsack 0/1 menggunakan Backtracking

print("=" * 60)
print("APLIKASI PEMILIHAN BARANG BAWAAN TAS")
print("Knapsack 0/1 Menggunakan Algoritma Backtracking")
print("=" * 60)

# ==========================
# INPUT DATA OLEH USER
# ==========================

jumlah_barang = int(input("Masukkan jumlah barang: "))

items = []

for i in range(jumlah_barang):
    print(f"\nBarang ke-{i+1}")

    nama = input("Nama barang   : ")
    berat = int(input("Berat (gram)  : "))
    nilai = int(input("Nilai manfaat : "))

    items.append({
        "nama": nama,
        "berat": berat,
        "nilai": nilai
    })

print()

kapasitas = int(input("Masukkan kapasitas maksimal tas (gram): "))

# ==========================
# VARIABEL GLOBAL
# ==========================

best_items = []
best_weight = 0
best_value = 0

jumlah_node = 0
langkah_eksplorasi = []


def knapsack_backtracking(index, total_berat, total_nilai, barang_dipilih):
    """
    Algoritma Knapsack 0/1 menggunakan Backtracking
    """

    global best_items
    global best_weight
    global best_value
    global jumlah_node

    jumlah_node += 1

    langkah_eksplorasi.append({
        "node": jumlah_node,
        "index": index,
        "berat": total_berat,
        "nilai": total_nilai,
        "barang": barang_dipilih.copy()
    })

    # Pruning
    if total_berat > kapasitas:
        return

    # Basis rekursi
    if index == len(items):

        if total_nilai > best_value:
            best_value = total_nilai
            best_weight = total_berat
            best_items = barang_dipilih.copy()

        return

    barang = items[index]

    # Pilihan 1 : ambil barang
    barang_dipilih.append(barang["nama"])

    knapsack_backtracking(
        index + 1,
        total_berat + barang["berat"],
        total_nilai + barang["nilai"],
        barang_dipilih
    )

    # Backtrack
    barang_dipilih.pop()

    # Pilihan 2 : tidak ambil barang
    knapsack_backtracking(
        index + 1,
        total_berat,
        total_nilai,
        barang_dipilih
    )


# ==========================
# EKSEKUSI ALGORITMA
# ==========================

waktu_mulai = time.time()

knapsack_backtracking(0, 0, 0, [])

waktu_selesai = time.time()

waktu_eksekusi = waktu_selesai - waktu_mulai

# ==========================
# OUTPUT
# ==========================

print("\n")
print("=" * 60)
print("DATA BARANG")
print("=" * 60)

print(f"{'No':<5}{'Nama Barang':<20}{'Berat':<15}{'Nilai'}")
print("-" * 60)

for i, item in enumerate(items, start=1):
    print(
        f"{i:<5}"
        f"{item['nama']:<20}"
        f"{item['berat']:<15}"
        f"{item['nilai']}"
    )

print("-" * 60)

print("\nHASIL SOLUSI OPTIMAL")
print("-" * 60)

print("Barang yang dipilih:")

for barang in best_items:
    print("-", barang)

print()
print("Total Berat Barang  :", best_weight, "gram")
print("Total Nilai Manfaat :", best_value)
print("Sisa Kapasitas Tas  :", kapasitas - best_weight, "gram")
print("Jumlah Node         :", jumlah_node)
print("Waktu Eksekusi      :", round(waktu_eksekusi, 6), "detik")

print("-" * 60)

print("\nLANGKAH EKSPLORASI BACKTRACKING")
print("-" * 60)
print("20 langkah pertama:\n")

for langkah in langkah_eksplorasi[:20]:
    print(
        f"Node {langkah['node']}: "
        f"index={langkah['index']}, "
        f"berat={langkah['berat']}, "
        f"nilai={langkah['nilai']}, "
        f"barang={langkah['barang']}"
    )

print("\nProgram selesai.")
