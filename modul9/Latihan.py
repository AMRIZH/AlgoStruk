class SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

# Membuat simpul-simpul dan mengisi data
A = SimpulPohonBiner('Ambarawa')
B = SimpulPohonBiner('Bantul')
C = SimpulPohonBiner('Cimahi')
D = SimpulPohonBiner('Denpasar')
E = SimpulPohonBiner('Enrekang')
F = SimpulPohonBiner('Flores')
G = SimpulPohonBiner('Garut')
H = SimpulPohonBiner('Halmahera Timur')
I = SimpulPohonBiner('Indramayu')
J = SimpulPohonBiner('Jakarta')

# Menghubungkan simpul ortu-anak
A.kiri = B; A.kanan = C
B.kiri = D; B.kanan = E
C.kiri = F; C.kanan = G
E.kiri = H
G.kanan = I

# preorder traversal
def preorderTrav(subpohon):
    if subpohon is not None:
        print(subpohon.data)
        preorderTrav(subpohon.kiri)
        preorderTrav(subpohon.kanan)

# inorder traversal
def inorderTrav(subpohon):
    if subpohon is not None:
        inorderTrav(subpohon.kiri)
        print(subpohon.data)
        inorderTrav(subpohon.kanan)

# postorder traversal
def postorderTrav(subpohon):
    if subpohon is not None:
        postorderTrav(subpohon.kiri)
        postorderTrav(subpohon.kanan)
        print(subpohon.data)

# Fungsi untuk mendapatkan ukuran pohon biner
def ukuranPohon(akar):
    if akar is None:
        return 0
    else:
        return 1 + ukuranPohon(akar.kiri) + ukuranPohon(akar.kanan)

# Fungsi untuk mendapatkan ketinggian pohon biner
def tinggiPohon(akar):
    if akar is None:
        return -1
    else:
        tinggi_kiri = tinggiPohon(akar.kiri)
        tinggi_kanan = tinggiPohon(akar.kanan)
        return max(tinggi_kiri, tinggi_kanan) + 1
    
# Fungsi untuk mencetak data dan level setiap simpul
def cetakDataDanLevel(akar, level=0):
    if akar is not None:
        print(f"{akar.data}, level {level}")
        cetakDataDanLevel(akar.kiri, level+1)
        cetakDataDanLevel(akar.kanan, level+1)

#=================================================================
# testcasee

# Contoh penggunaan
print("Ukuran pohon:", ukuranPohon(A))  # Output: Ukuran pohon: 10
print("Ketinggian pohon:", tinggiPohon(A))  # Output: Ketinggian pohon: 3

# Contoh penggunaan
cetakDataDanLevel(A)
print("====================================")

# traversals
print("Preorder traversal:")
preorderTrav(A) # Output: A B D E H C F G I
print("====================================")
print("Inorder traversal:")
inorderTrav(A) # Output: D B H E A F C G I
print("====================================")
print("Postorder traversal:")
postorderTrav(A) # Output: D H E B F I G C A
