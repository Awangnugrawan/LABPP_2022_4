print('=====Program Konversi Detik Ke Jam=====')
detik_raw = int(input('Masukkan Jumlah detik yang ingin di konversi : '))
 
jam = detik_raw//3600
sisa_detik = detik_raw % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print("%03d:%03d:%03d" % (jam, menit, detik))