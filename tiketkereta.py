print('Perhitungan Tiket Kereta Api')
print('-' * 20)


print('Jurusan : ')
print('1. Jakarta')
print('2. Yogyakarta')
print('3. Surabaya')

jurusan = int(input('Pilihan Jurusan [1/2/3] : '))
banyak_tiket = int(input('Banyak Tiket : '))

if jurusan == 1:
  harga_tiket = 150000
  print(f'Harga Tiket  : Rp.{harga_tiket:8}')
elif jurusan == 2:
  harga_tiket = 300000
  print(f'Harga Tiket  : Rp.{harga_tiket:8}')
elif jurusan == 3:
  harga_tiket = 400000
  print(f'Harga Tiket  : Rp.{harga_tiket:8}')

total_bayar = harga_tiket * banyak_tiket

print(f'Total Bayar  : Rp.{total_bayar:8}')
