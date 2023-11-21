import random

komputer = random.choice(['G','K','B'])
print('Komputer Telah Memilih Sekarang Giliran Anda !')
orang = input('Pilihan Anda (G/K/B) ?  ').upper()

if komputer == 'G' and orang == 'G':
  print('Komputer Memilih Gunting. DRAW !')
elif komputer == 'G' and orang == 'K':
  print('Komputer Memilih Gunting. Anda Kalah !')
elif komputer == 'G' and orang == 'B':
  print('Komputer Memilih Gunting. Anda Menang !')
elif komputer == 'K' and orang == 'G':
  print('Komputer Memilih Kertas. Anda Menang !')
elif komputer == 'K' and orang == 'K':
  print('Komputer Memilih Kertas. DRAW !')
elif komputer == 'K' and orang == 'B':
  print('Komputer Memilih Kertas. Anda Kalah !')
elif komputer == 'B' and orang == 'G':
  print('Komputer Memilih Batu. Anda Kalah !')
elif komputer == 'B' and orang == 'K':
  print('Komputer Memilih Batu. Anda Menang !')
elif komputer == 'B' and orang == 'B':
  print('Komputer Memilih Batu. DRAW !')
else:
  print('Invalid ! , Pilihlah (G/K/B) !')