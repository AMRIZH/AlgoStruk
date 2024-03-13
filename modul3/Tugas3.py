  # 1 
  # a. memastikan bahwa isi dan ukuran matrix-nya konsisten
matrik = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
def consistent(matrik) :
  for i in matrik :
    if len(i) != len(matrik[1]) :
      print("salah")
  print("benar")
  
consistent(matrik)