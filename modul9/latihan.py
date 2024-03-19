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

#=============================================
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

