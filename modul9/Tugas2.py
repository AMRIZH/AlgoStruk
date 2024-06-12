from binSerchTre import Node, size, height
from Latihan import SimpulPohonBiner, cetakDataDanLevel

# Membuat simpul-simpul dan mengisi data
A = Node(56) # root
B = Node(37)
C = Node(78)
D = Node(22)
E = Node(43)
F = Node(60)
G = Node(83)
H = Node(40)
I = Node(85)

# Menghubungkan simpul ortu-anak
A.left = B; A.right = C
B.left = D; B.right = E
C.left = F; C.right = G
E.left = H
G.right = I

# testcases
print(size(A)) # output 9
print(height(A)) # output 3

# ================================
# Membuat simpul-simpul dan mengisi data
A = SimpulPohonBiner('Ambarawa') # root
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

# testcases
print(cetakDataDanLevel(A)) # output Ambarawa 0, Bantul 1, Denpasar 2, Enrekang 2, Cimahi 1, Flores 2, Garut 2, Halmahera Timur 3, Indramayu 3

# ================================