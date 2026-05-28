# Progress 1 - Strategi Algoritmik

## Aplikasi Pemilihan Barang Bawaan Tas Menggunakan Knapsack 0/1

Repository ini dibuat untuk memenuhi **Progress Report 1** pada mata kuliah **Strategi Algoritmik**.

Program ini merupakan implementasi sederhana dari algoritma **Knapsack 0/1** menggunakan metode **Backtracking**. Studi kasus yang digunakan adalah pemilihan barang bawaan tas berdasarkan kapasitas maksimal tertentu.

---

## Identitas Kelompok

| NRP     | Nama                 |
| ------- | -------------------- |
| 2372006 | Stepanus Sugianto    |
| 2372041 | Axel Hizkia Mapandin |
| 2372902 | Fachrizqy Utomo      |

**Kelas:** C
**Mata Kuliah:** Strategi Algoritmik
**Topik:** Aplikasi Pemilihan Barang Bawaan Tas Menggunakan Knapsack 0/1
**Metode:** Backtracking

---

## Deskripsi Program

Program ini digunakan untuk membantu menentukan barang bawaan tas yang paling optimal dengan batasan kapasitas berat tertentu.

Setiap barang memiliki:

* Nama barang
* Berat barang
* Nilai manfaat atau prioritas

Program akan memilih kombinasi barang yang menghasilkan **total nilai manfaat terbesar**, tetapi total berat barang tidak boleh melebihi kapasitas maksimal tas.

---

## Konsep Knapsack 0/1

Pada kasus ini, konsep Knapsack 0/1 diterapkan sebagai berikut:

| Konsep Knapsack 0/1 | Pada Program           |
| ------------------- | ---------------------- |
| Item                | Barang bawaan tas      |
| Weight              | Berat barang           |
| Profit              | Nilai manfaat barang   |
| Capacity            | Kapasitas maksimal tas |
| Output              | Barang yang dipilih    |

Setiap barang hanya memiliki dua kemungkinan:

* `1` = barang dibawa
* `0` = barang tidak dibawa

Karena barang tidak dapat dipilih sebagian, maka kasus ini sesuai dengan konsep **Knapsack 0/1**.

---

## Data Barang

Kapasitas maksimal tas yang digunakan pada program adalah **3000 gram**.

| No |  Nama Barang |     Berat | Nilai Manfaat |
| -- | -----------: | --------: | ------------: |
| 1  |       Laptop | 1500 gram |            20 |
| 2  |      Charger |  300 gram |             8 |
| 3  |  Botol Minum |  600 gram |             6 |
| 4  | Buku Catatan |  700 gram |             7 |
| 5  |       Payung |  500 gram |             5 |
| 6  |        Jaket |  800 gram |             6 |
| 7  |    Powerbank |  400 gram |             9 |
| 8  |        Snack |  200 gram |             3 |
| 9  |       Pulpen |  100 gram |             4 |
| 10 |      Headset |  100 gram |             5 |

---

## Cara Kerja Program

Program menggunakan metode **Backtracking** untuk mencoba semua kemungkinan kombinasi barang.

Langkah kerja program:

1. Program membaca data barang.
2. Program memeriksa barang satu per satu.
3. Setiap barang memiliki dua pilihan:

   * dibawa;
   * tidak dibawa.
4. Jika total berat melebihi kapasitas tas, maka cabang pencarian dihentikan.
5. Jika total berat masih sesuai kapasitas, maka nilai manfaat dihitung.
6. Program menyimpan kombinasi barang dengan nilai manfaat terbesar.
7. Program menampilkan solusi optimal.

---

## Output Program

Output yang ditampilkan oleh program adalah:

* Daftar barang input
* Barang yang dipilih
* Total berat barang
* Total nilai manfaat
* Sisa kapasitas tas
* Jumlah node yang dikunjungi
* Waktu eksekusi
* Langkah eksplorasi Backtracking

---

## Cara Menjalankan Program

Pastikan Python sudah terinstall di komputer.

Jalankan program dengan perintah berikut:

```bash
python knapsack_barang_tas.py
```

---

## Contoh Output

Contoh output yang dihasilkan program:

```text
APLIKASI PEMILIHAN BARANG BAWAAN TAS
Knapsack 0/1 Menggunakan Algoritma Backtracking

Kapasitas Maksimal Tas: 3000 gram

HASIL SOLUSI OPTIMAL
Barang yang dipilih:
- Laptop
- Charger
- Botol Minum
- Powerbank
- Snack
- Pulpen
- Headset

Total Berat Barang  : 3000 gram
Total Nilai Manfaat : 55
Sisa Kapasitas Tas  : 0 gram
Jumlah Node         : ditampilkan oleh program
Waktu Eksekusi      : ditampilkan oleh program
```

---

## File Program

File utama pada repository ini adalah:

```text
knapsack_barang_tas.py
```

File tersebut berisi implementasi algoritma **Knapsack 0/1 dengan Backtracking**.

---

## Status Progress

Progress saat ini:

| Fitur                          | Status           |
| ------------------------------ | ---------------- |
| Menentukan topik aplikasi      | Selesai          |
| Menentukan data barang         | Selesai          |
| Membuat algoritma Backtracking | Selesai          |
| Menampilkan solusi optimal     | Selesai          |
| Menampilkan jumlah node        | Selesai          |
| Menampilkan waktu eksekusi     | Selesai          |
| Menampilkan langkah eksplorasi | Selesai          |
| Membuat tampilan website       | Belum dikerjakan |

---

## Rencana Pengembangan Selanjutnya

Fitur yang akan dikembangkan selanjutnya:

1. Menambahkan input manual untuk kapasitas tas.
2. Menambahkan input manual untuk data barang.
3. Membuat tampilan website sederhana.
4. Menghubungkan algoritma dengan tampilan website.
5. Membuat dokumentasi penggunaan aplikasi yang lebih lengkap.

---

## Kesimpulan

Program ini menunjukkan penerapan algoritma **Knapsack 0/1** menggunakan metode **Backtracking** pada kasus pemilihan barang bawaan tas. Dengan program ini, pengguna dapat mengetahui kombinasi barang terbaik yang dapat dibawa tanpa melebihi kapasitas tas dan tetap mendapatkan nilai manfaat yang maksimal.
