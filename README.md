# Perkalian Matrix di Python

Program Python ini melakukan perkalian antara dua 5x5 matrix (Matrix A dan Matrix B) menggunakan perulangan `for` dan disimpan menggunakan `append` lalu ditampilkan output hasil perkaliannya.

---

## Matrix Input

### Matrix A
```
| 23  56   14  87  42  |
| 67   5   91  33  18  |
| 72  29   45  60   8  |
| 11  94   37  50  76  |
|  3  68   25  81  55  |
```
### Matrix B
```
| 4   9   2   6   5 |
| 3   7   8   1   2 |
| 5   6   7   8   9 |
| 9   8   7   6   5 |
| 5   4   3   2   1 |
```

## Proses Perkalian

### Code yang digunakan untuk perkalian

```python
hasil = []
for i in range(5):
    baris = []  
    for j in range(5):
        total = 0
        for k in range(5):
            total += MatrixA[i][k] * MatrixB[k][j]
        baris.append(total)
    hasil.append(baris)
```
### Penjelasan
Rangkaian kode diatas adalah Triple-nested Loop
- Perulangan `i` untuk memilih baris di MatrixA
- Perulangan `j` untuk memilih kolom di MatrixB
- Perulangan `k` untuk menjalankan semua angka di baris dan kolom, mengalikan dan menambahkannya ke Matrix Hasil.

## Menampilkan Hasil

### Code untuk Output
```python
print("\nHasil perkalian matriks A x B:")
for row in hasil:
    print(row)
```
### Output
```
| 1323 1547 1327  912  830 |
| 1125 1520 1096 1369 1347 |
| 1180 1633 1135 1197 1131 |
| 1341 1683 1611  908  902 |
| 1345 1521 1457  882  836 |
```
---
