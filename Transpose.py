# Haha transpose lagu

not_lagu_sebelum = []
not_lagu_sesudah = []

while True:
  masukkan = input("Masukkan not lagu (Tekan 'q' jika selesai): ")
  if masukkan.isnumeric() :
    masukkan = int((masukkan))
  not_lagu_sebelum.append(masukkan)
  if masukkan == "q" :
    break

not_lagu_sebelum.pop()

# sekaligus indeks untuk eksekusi nya
def cari_nada (nada) :
    if nada == "c" : 
      nada = (1)
    if nada == 'c#': 
      nada = (2)
    if nada == 'd': 
      nada = (3)
    if nada == 'd#': 
      nada = (4)
    if nada == 'e': 
      nada = (5)
    if nada == 'f': 
      nada = (6)
    if nada == 'f#': 
      nada = (7)
    if nada == 'g': 
      nada = (8)
    if nada == 'g#': 
      nada =(9)
    if nada == 'a': 
      nada =(10)
    if nada == 'a#': 
      nada =(11)
    if nada == 'b': 
      nada = (12)
    return nada

nada_dasar_awal = input('Dari Do = ')
nada_dasar_awal = cari_nada(nada_dasar_awal)
print(nada_dasar_awal)

nada_dasar_akhir = input('Ke Do = ')
nada_dasar_akhir = cari_nada(nada_dasar_akhir)
print(nada_dasar_akhir)


transpose = nada_dasar_akhir - nada_dasar_awal

print("Not yang dimasukkan: ",not_lagu_sebelum)
print("Transpose sebesar: ",transpose)

sekarang = 0
for x in range (len(not_lagu_sebelum)) :
  for i in range (transpose) :
    if (not_lagu_sebelum[sekarang] == 3) :
      not_lagu_sebelum[sekarang] += 1
    elif (not_lagu_sebelum[sekarang] == 7) :
      not_lagu_sebelum[sekarang] += 1
    else:
      not_lagu_sebelum[sekarang] += 0.5
    if (not_lagu_sebelum[sekarang] > 7) :
      not_lagu_sebelum[sekarang] -= 7
  not_lagu_sesudah.append(not_lagu_sebelum[sekarang])

  sekarang += 1
  print ("Index ekarang :",sekarang)

print("Hasil do = ", nada_dasar_akhir, ":\n",not_lagu_sesudah)



