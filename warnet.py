print('Perhitungan Rental Warnet')
print('-' * 20)

jam_masuk = int(input('Jam Masuk: '))
menit_masuk = int(input('Menit Masuk: '))
jam_keluar = int(input('Jam Keluar: '))
menit_keluar = int(input('Menit Keluar: '))
print('-' * 20)

if jam_keluar < jam_masuk:
  lama_rental = ((jam_keluar + 24 ) * 60 + menit_keluar) - (jam_masuk * 60 + menit_masuk)
else:
  lama_rental = (jam_keluar * 60 + menit_keluar) - (jam_masuk * 60 + menit_masuk)

jam_rental = lama_rental // 60
menit_rental = lama_rental % 60

biaya_rental = lama_rental / 60 * 5000

print('Lama Rental  :',lama_rental, 'Menit', '(',jam_rental,'Jam',menit_rental,'Menit',')')
print(f'Biaya Rental : Rp. {biaya_rental:1.0f}')