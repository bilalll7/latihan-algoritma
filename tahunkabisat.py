print('Perhitungan Tahun Kabisat')
print('-' * 38)

tahun = int(input('Tahun : '))

if tahun % 100 != 0 and tahun % 4 == 0 or tahun % 100 == 0 and tahun % 400 == 0:
  print('Tahun',tahun,'adalah Tahun Kabisat')
else:
  print('Tahun',tahun,'Bukan Tahun Kabisat')