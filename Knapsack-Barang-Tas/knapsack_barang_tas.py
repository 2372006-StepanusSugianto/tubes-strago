import time

# Progress 1 - Strategi Algoritmik
# Topik  : Aplikasi Pemilihan Barang Bawaan Tas
# Metode : Knapsack 0/1 menggunakan Backtracking

# Data barang bawaan tas
# nama  = nama barang
# berat = berat barang dalam gram
# nilai = nilai manfaat/prioritas barang
items = [
    {"nama": "Laptop", "berat": 1500, "nilai": 20},
    {"nama": "Charger", "berat": 300, "nilai": 8},
    {"nama": "Botol Minum", "berat": 600, "nilai": 6},
    {"nama": "Buku Catatan", "berat": 700, "nilai": 7},
    {"nama": "Payung", "berat": 500, "nilai": 5},
    {"nama": "Jaket", "berat": 800, "nilai": 6},
    {"nama": "Powerbank", "berat": 400, "nilai": 9},
    {"nama": "Snack", "berat": 200, "nilai": 3},
    {"nama": "Pulpen", "berat": 100, "nilai": 4},
    {"nama": "Headset", "berat": 100, "nilai": 5}
]

# Kapasitas maksimal tas
kapasitas = 3000

# Variabel untuk menyimpan solusi terbaik
best_items = []
best_weight = 0
best_value = 0

# Variabel statistik
jumlah_node = 0
langkah_eksplorasi = []


def knapsack_backtracking(index, total_berat, total_nilai, barang_dipilih):
    """
    Fungsi untuk menyelesaikan Knapsack 0/1 menggunakan Backtracking.

    Pada setiap barang, ada 2 kemungkinan:
    1. Barang dibawa
    2. Barang tidak dibawa
    """
    global best_items, best_weight, best_value, jumlah_node

    jumlah_node += 1

    # Simpan langkah eksplorasi
    langkah_eksplorasi.append({
        "node": jumlah_node,
        "index": index,
        "berat": total_berat,
        "nilai": total_nilai,
        "barang": barang_dipilih.copy()
    })

    # Pruning: jika berat melebihi kapasitas, cabang dihentikan
    if total_berat > kapasitas:
        return

    # Jika semua barang sudah dicek
    if index == len(items):
        # Jika nilai manfaat lebih besar, simpan sebagai solusi terbaik
        if total_nilai > best_value:
            best_value = total_nilai
            best_weight = total_berat
            best_items = barang_dipilih.copy()
        return

    # Ambil barang berdasarkan index saat ini
    barang = items[index]

    # Pilihan 1: barang dibawa
    barang_dipilih.append(barang["nama"])
    knapsack_backtracking(
        index + 1,
        total_berat + barang["berat"],
        total_nilai + barang["nilai"],
        barang_dipilih
    )

    # Backtrack: hapus barang terakhir untuk mencoba kemungkinan lain
    barang_dipilih.pop()

    # Pilihan 2: barang tidak dibawa
    knapsack_backtracking(
        index + 1,
        total_berat,
        total_nilai,
        barang_dipilih
    )


# Mulai menghitung waktu eksekusi
waktu_mulai = time.time()

# Menjalankan algoritma backtracking
knapsack_backtracking(0, 0, 0, [])

# Selesai menghitung waktu eksekusi
waktu_selesai = time.time()
waktu_eksekusi = waktu_selesai - waktu_mulai


# Output Program
print("=" * 60)
print("APLIKASI PEMILIHAN BARANG BAWAAN TAS")
print("Knapsack 0/1 Menggunakan Algoritma Backtracking")
print("=" * 60)
print()

print("Kapasitas Maksimal Tas:", kapasitas, "gram")
print()

print("DAFTAR BARANG INPUT")
print("-" * 60)
print(f"{'No':<5}{'Nama Barang':<20}{'Berat':<15}{'Nilai'}")
print("-" * 60)

for i, item in enumerate(items, start=1):
    print(f"{i:<5}{item['nama']:<20}{item['berat']:<15}{item['nilai']}")

print("-" * 60)
print()

print("HASIL SOLUSI OPTIMAL")
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
print()

print("LANGKAH EKSPLORASI BACKTRACKING")
print("-" * 60)
print("Catatan: hanya 20 langkah pertama yang ditampilkan agar output tidak terlalu panjang.")
print()

for langkah in langkah_eksplorasi[:20]:
    print(
        f"Node {langkah['node']}: "
        f"index={langkah['index']}, "
        f"berat={langkah['berat']}, "
        f"nilai={langkah['nilai']}, "
        f"barang={langkah['barang']}"
    )

print()
print("Program selesai.")