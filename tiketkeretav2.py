print('Perhitungan Tiket Kereta Api')
print('-' * 20)

print('Kode Kota : ')
print('1. Jakarta')
print('2. Yogyakarta')
print('3. Surabaya')

kota = int(input('Pilihan Kota [1/2/3] ? '))

print('-' * 20)

print('Kode Kelas : ')
print('1. Ekonomi')
print('2. Bisnis')
print('3. Eksekutif')

kelas = int(input('Pilihan Kelas [1/2/3] ? '))

print('-' * 20)

banyak_tiket = int(input('Banyak Tiket : '))
diskon = 0

if kota == 1 and kelas == 1:
  harga_tiket = 100000
  sub_total = banyak_tiket * harga_tiket
elif kota == 1 and kelas == 2:
  harga_tiket = 400000
  sub_total = banyak_tiket * harga_tiket
elif kota == 1 and kelas == 3:
  harga_tiket = 700000
  sub_total = banyak_tiket * harga_tiket
elif kota == 2 and kelas == 1:
  harga_tiket = 200000
  sub_total = banyak_tiket * harga_tiket
  kode_voucher = input('Kode Voucher : ')
  if kode_voucher == 'PROMO':
    diskon = 0.10 * sub_total
elif kota == 2 and kelas == 2:
  harga_tiket = 500000
  sub_total = banyak_tiket * harga_tiket
elif kota == 2 and kelas == 3:
  harga_tiket = 800000
  sub_total = banyak_tiket * harga_tiket
elif kota == 3 and kelas == 1:
  harga_tiket = 300000
  sub_total = banyak_tiket * harga_tiket
elif kota == 3 and kelas == 2:
  harga_tiket = 600000
  sub_total = banyak_tiket * harga_tiket
elif kota == 3 and kelas == 3:
  harga_tiket = 900000
  sub_total = banyak_tiket * harga_tiket
  kode_voucher = input('Kode Voucher : ')
  if kode_voucher == 'PROMO':
    diskon = 0.10 * sub_total
else:
  print('Kota atau Kelas yang anda inputkan, Tidak Ada!')


total_bayar = sub_total - diskon

print(f'Harga Tiket  : Rp.{harga_tiket:1.0f}')
print(f'Sub Total    : Rp.{sub_total:1.0f}')
print(f'Diskon       : Rp.{diskon:1.0f}')
print(f'Total Bayar  : Rp.{total_bayar:1.0f}')
