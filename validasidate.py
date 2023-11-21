print('Perhitungan Validasi Tanggal')
print('-' * 38)

tanggal = int(input('Tanggal : '))
bulan = int(input('Bulan : '))
tahun = int(input('Tahun : '))

if bulan >= 1 or bulan <= 12:
  if bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12:
    max_date = 31
  elif bulan == 2:
    max_date = 28
    if tahun % 100 != 0 and tahun % 4 == 0 or tahun % 100 == 0 and tahun % 400 == 0:
      max_date = 29    
  else:
    max_date = 30

  if tanggal >= 1 and tanggal <= max_date:
    print('Tanggal ', tanggal,'/',bulan,'/',tahun, 'adalah tanggal Valid')
  else:
    print('Tanggal ', tanggal,'/',bulan,'/',tahun, 'bukan tanggal Valid')
else:
  print('Tanggal ', tanggal,'/',bulan,'/',tahun, 'Invalid')