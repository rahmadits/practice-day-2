# Input Jualan Buah
nApel = int(input("input jumlah apel: "))
nJeruk = int(input("input jumlah jeruk: "))
nAnggur = int(input("input jumlah anggur: "))

# init harga
priceApel = 10000
priceJeruk = 15000
priceAnggur = 20000

#hitung harga per buah
totalPriceApel = nApel * priceApel
totalPriceJeruk = nJeruk * priceJeruk
totalPriceAnggur = nAnggur * priceAnggur

#hitung harga total buah
priceTotal = totalPriceApel + totalPriceJeruk + totalPriceAnggur

# show
print (
    f'''
detail belanja

Apel : {nApel} x {priceApel}
Jeruk : {nJeruk} x {priceJeruk}
Anggur : {nAnggur} x {priceAnggur}

Total : {priceTotal}
'''
)