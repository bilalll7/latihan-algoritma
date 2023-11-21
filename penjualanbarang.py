print('Perhitungan Penjualan Barang')
print('-' * 38)
print('=' * 38)
print('Kode Barang | Nama Barang      | Harga')
print('BK001       | Buku Tulis       | 5000 ')
print('PS002       | Pensil           | 2500 ')
print('PG001       | Penggaris 30 cm  | 15000')
print('=' * 38)

print('-' * 38)
kode_barang = input('Masukan Kode Barang : ').upper()
qty = int(input('Masukan Qty : '))
print('-' * 38)

if kode_barang == 'BK001':
  nama_barang = 'Buku Tulis'
  harga = 5000
elif kode_barang == 'PS002':
  nama_barang = 'Pensil'
  harga = 2500
elif kode_barang == 'PG001':
  nama_barang = 'Penggaris 30 cm'
  harga = 15000

print('Nama Barang :',nama_barang)
print('Harga       : Rp.',harga)

sub_total = harga * qty

print('Sub Total   : Rp.',sub_total)

diskon = 0.30 * sub_total

if diskon >= 20000:
  diskon = 20000

total_bayar = sub_total - diskon
print(f'Diskon      : Rp. {diskon:1.0f}')
print(f'Total Bayar : Rp. {total_bayar:1.0f}')



