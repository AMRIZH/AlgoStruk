def gabungkanDuaListUrut(A, B):
    la = len(A); lb = len(B)
    C = list()
    i = 0; j = 0  # C adalah list baru

    # Gabungkan keduanya sampai salah satu kosong
    while i < la and j < lb:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    while i < la:
        C.append(A[i])
        i += 1  # Jika A mempunyai sisa, tumpukkan ke list baru itu satu demi satu

    while j < lb:
        C.append(B[j])
        j += 1  # Jika B mempunyai sisa, tumpukkan ke list baru itu satu demi satu

    return C

def faktorial(a):
    if a==1: return 1 ## base case
    else: return a*faktorial(a-1) ## recursive case
    
def mergeSort(A):
    #print("Membelah ", A)
    if len(A) > 1: # splitting process stop when the list has only one element
        mid = len(A) // 2
        # Membelah list.
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]
        # Slicing ini langkah yang expensive sebenarnya, bisakah kamu membuatnya lebih baik?

        mergeSort(separuhKiri)  # Ini rekursi. Memanggil lebih lanjut mergeSort
        mergeSort(separuhKanan)  # untuk separuhKiri dan separuhKanan.

        # Di bawah ini adalah proses penggabungan.

        i = 0 ; j = 0 ; k = 0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:  # while-loop ini
                A[k] = separuhKiri[i]            # menggabungkan kedua list, yakni
                i = i + 1                        # separuhKiri dan separuhKanan,
            else:                                # sampai salah satu kosong.
                A[k] = separuhKanan[j]           # Perhatikan kesamaan strukturnya
                j = j + 1                       # dengan proses penggabungan
            k = k + 1                            # dua list urut.

        while i < len(separuhKiri):
            A[k] = separuhKiri[i]    # Jika separuhKiri mempunyai sisa
            i = i + 1                # tumpukkan ke A
            k = k + 1                # satu demi satu.

        while j < len(separuhKanan):
            A[k] = separuhKanan[j]   # Jika separuhKanan mempunyai sisa
            j = j + 1                # tumpukkan ke A
            k = k + 1                # satu demi satu.
        #print("Menggabungkan", A)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)

#================================================================
def partisi(A, awal, akhir):
    nilaiPivot = A[awal]  # Di sini nilaiPivot kita ambil dari elemen yang paling kiri.
    penandaKiri = awal + 1  # Posisi awal penandaKiri. Lihat Gambar 6.3.
    penandaKanan = akhir  # Posisi awal penandaKanan.
    selesai = False
    
    while not selesai:  # loop di bawah adalah untuk mengatur ulang posisi semua elemen

        while penandaKiri <= penandaKanan and A[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1  # penandaKiri bergerak ke kanan,
            # sampai ketemu suatu nilai yang
            # lebih besar dari nilaiPivot

        while A[penandaKanan] >= nilaiPivot and penandaKanan >= penandaKiri:
            penandaKanan = penandaKanan - 1  # penandaKanan bergerak ke kiri,
            # sampai ketemu suatu nilai yang
            # lebih kecil dari nilaiPivot

        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp  # Kalau dua penanda sudah bersilangan,
            # selesai & lanjut ke penempatan pivot
            # Tapi kalau belum bersilangan,
            # tukarlah isi yang ditunjuk oleh
            # penandaKiri dan penandaKanan

    temp = A[awal]  # Kalau acara tukar menukar posisi sudah selesai,
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp  # kita lalu menempatkan pivot pada posisi yang tepat,
    # yakni posisi penandaKanan. Lihat Gambar 6.3 dan 6.4.
    # Posisi penandaKanan adalah juga titikBelah.
    return penandaKanan  # Fungsi ini mengembalikan titikBelah ke pemanggil
  
def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1 )  # memanggil quickSortBantu di

# Fungsi quickSortBantu adalah fungsi rekursif yang dipanggil berulang-ulang:
def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)  # Atur elemen dan dapatkan titikBelah.
        quickSortBantu(A, awal, titikBelah - 1)  # Ini rekursi untuk belah sisi kiri
        quickSortBantu(A, titikBelah + 1, akhir)  # dan belah sisi kanan.

# ==================================================================== 

D = [1,2,54,21,76,221,34,567,43,5,4,87,11,13,42]
mergeSort(D)
print(D)

D = [1,2,54,21,76,221,34,567,43,5,4,87,11,13,42]
quickSort(D)
print(D)


