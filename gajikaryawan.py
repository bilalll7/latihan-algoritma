print('Perhitungan Gaji Karyawan !')
print('-' * 20)

nama = input('Nama Pegawai : ')
jabatan = input('Jabatan : ').upper()
menikah = input('Menikah (Y/T) : ').upper()

if jabatan == 'DIREKTUR':
  gaji_pokok = 5000000
  tunjangan_keluarga = 0
  tunjangan_anak = 0
  if menikah == 'Y':
    tunjangan_keluarga = 0.20 * gaji_pokok
    anak = int(input('Banyak Anak : '))
    if anak == 1:
      tunjangan_anak = 0.10 * gaji_pokok
    elif anak == 2:
      tunjangan_anak = 0.20 * gaji_pokok
    elif anak >= 3:
      tunjangan_anak = 0.30 * gaji_pokok
    print('Gaji Pokok         :', gaji_pokok)
    print('Tunjangan Keluarga : Rp. ', tunjangan_keluarga)
    print('Tunjangan Anak     : Rp. ', tunjangan_anak)
    gaji_kotor = gaji_pokok + tunjangan_keluarga + tunjangan_anak
    pajak = 0.05 * gaji_kotor
    gaji_bersih = gaji_kotor - pajak
    print('Gaji Kotor         : Rp. ', gaji_kotor)
    print('Pajak              : Rp. ', pajak)
    print('Gaji Bersih        : Rp. ', gaji_bersih)
  else:
    print('Gaji Pokok         :', gaji_pokok)
    print('Tunjangan Keluarga : Rp. ', tunjangan_keluarga)
    print('Tunjangan Anak     : Rp. ', tunjangan_anak)
    gaji_kotor = gaji_pokok + tunjangan_keluarga + tunjangan_anak
    pajak = 0.10 * gaji_kotor
    gaji_bersih = gaji_kotor - pajak
    print('Gaji Kotor         : Rp. ', gaji_kotor)
    print('Pajak              : Rp. ', pajak)
    print('Gaji Bersih        : Rp. ', gaji_bersih)
elif jabatan == 'MANAGER':
  gaji_pokok = 3000000
  tunjangan_keluarga = 0
  tunjangan_anak = 0
  if menikah == 'Y':
    tunjangan_keluarga = 0.20 * gaji_pokok
    anak = int(input('Banyak Anak : '))
    if anak == 1:
      tunjangan_anak = 0.10 * gaji_pokok
    elif anak == 2:
      tunjangan_anak = 0.20 * gaji_pokok
    elif anak >= 3:
      tunjangan_anak = 0.30 * gaji_pokok
    print('Gaji Pokok         :', gaji_pokok)
    print('Tunjangan Keluarga : Rp. ', tunjangan_keluarga)
    print('Tunjangan Anak     : Rp. ', tunjangan_anak)
    gaji_kotor = gaji_pokok + tunjangan_keluarga + tunjangan_anak
    pajak = 0.05 * gaji_kotor
    gaji_bersih = gaji_kotor - pajak
    print('Gaji Kotor         : Rp. ', gaji_kotor)
    print('Pajak              : Rp. ', pajak)
    print('Gaji Bersih        : Rp. ', gaji_bersih)
  else:
    print('Gaji Pokok         :', gaji_pokok)
    print('Tunjangan Keluarga : Rp. ', tunjangan_keluarga)
    print('Tunjangan Anak     : Rp. ', tunjangan_anak)
    gaji_kotor = gaji_pokok + tunjangan_keluarga + tunjangan_anak
    pajak = 0.10 * gaji_kotor
    gaji_bersih = gaji_kotor - pajak
    print('Gaji Kotor         : Rp. ', gaji_kotor)
    print('Pajak              : Rp. ', pajak)
    print('Gaji Bersih        : Rp. ', gaji_bersih)
elif jabatan == 'STAFF':
  gaji_pokok = 2000000
  tunjangan_keluarga = 0
  tunjangan_anak = 0
  if menikah == 'Y':
    tunjangan_keluarga = 0.20 * gaji_pokok
    anak = int(input('Banyak Anak : '))
    if anak == 1:
      tunjangan_anak = 0.10 * gaji_pokok
    elif anak == 2:
      tunjangan_anak = 0.20 * gaji_pokok
    elif anak >= 3:
      tunjangan_anak = 0.30 * gaji_pokok
    print('Gaji Pokok         :', gaji_pokok)
    print('Tunjangan Keluarga : Rp. ', tunjangan_keluarga)
    print('Tunjangan Anak     : Rp. ', tunjangan_anak)
    gaji_kotor = gaji_pokok + tunjangan_keluarga + tunjangan_anak
    pajak = 0.05 * gaji_kotor
    gaji_bersih = gaji_kotor - pajak
    print('Gaji Kotor         : Rp. ', gaji_kotor)
    print('Pajak              : Rp. ', pajak)
    print('Gaji Bersih        : Rp. ', gaji_bersih)
  else:
    print('Gaji Pokok         :', gaji_pokok)
    print('Tunjangan Keluarga : Rp. ', tunjangan_keluarga)
    print('Tunjangan Anak     : Rp. ', tunjangan_anak)
    gaji_kotor = gaji_pokok + tunjangan_keluarga + tunjangan_anak
    pajak = 0.10 * gaji_kotor
    gaji_bersih = gaji_kotor - pajak
    print('Gaji Kotor         : Rp. ', gaji_kotor)
    print('Pajak              : Rp. ', pajak)
    print('Gaji Bersih        : Rp. ', gaji_bersih)
else:
  print('Jabatan Yang anda Inputkan tidak ada !')


