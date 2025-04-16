MatrixA = [ [23,56,14,87,42],
            [67,5,91,33,18 ],
            [72,29,45,60,8 ],
            [11,94,37,50,76],
            [3,68,25,81,55 ] ]

MatrixB = [ [4,9,2,6,5],
            [3,7,8,1,2],
            [5,6,7,8,9],
            [9,8,7,6,5],
            [5,4,3,2,1] ]

# Output Matrix A dan Matrix B
print("Matrix A:")
for row in MatrixA:
    print(row)

print("\nMatrix B:")
for row in MatrixB:
    print(row)

# Proses Hasil
hasil = []
for i in range(5):
    baris = []  
    for j in range(5):
        total = 0
        for k in range(5):
            total += MatrixA[i][k] * MatrixB[k][j]
        baris.append(total)
    hasil.append(baris)

# Output Hasil
print("\nHasil perkalian matriks A x B:")
for row in hasil:
    print(row)