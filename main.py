# Input Jualan Buah
'''
nApel = int(input("input jumlah apel: "))
nJeruk = int(input("input jumlah jeruk: "))
nAnggur = int(input("input jumlah anggur: "))
'''

# init harga dan stok
priceApel = 10000
priceJeruk = 15000
priceAnggur = 20000

stockApel = 10
stockJeruk = 15
stockAnggur = 8

# deklarasi ungsi hitung buah
def input_fruit(name, stock, price):
    while True:
        n = int(input(f"input jumlah {name.capitalize()}:"))
        if n <= stock:
            price = n * price
            break
        else:
            print(f'jumlah terlalu banyak. {name.capitalize()} sisa {stock}')
    return price, n

# init jumlah buah
'''
while True:
    nApel = int(input("Input jumlah apel: "))
    if nApel <= stockApel:
        break
    else:
        print(f'jumlah terlalu banyak. apel sisa {stockApel}')
        stockApel -= nApel

while True:
    nJeruk = int(input("Input jumlah jeruk: "))
    if nJeruk <= stockJeruk:
        break
    else:
        print(f'jumlah terlalu banyak. jeruk sisa {stockJeruk}')
        stockJeruk -= nJeruk

while True:
    nAnggur = int(input("Input jumlah anggur: "))
    if nAnggur <= stockAnggur:
        break
    else:
        print(f'jumlah terlalu banyak. anggur sisa {stockAnggur}')
        stockAnggur -= nAnggur
'''

#hitung harga per buah
totalPriceApel, nApel = input_fruit('apel', stockApel, priceApel)
totalPriceJeruk, nJeruk = input_fruit('jeruk', stockJeruk, priceJeruk)
totalPriceAnggur, nAnggur = input_fruit('anggur',stockAnggur, priceAnggur)

#hitung harga total buah
priceTotal = totalPriceApel + totalPriceJeruk + totalPriceAnggur

# show detail belanja
print (
    f'''
detail belanja

Apel : {nApel} x {priceApel}
Jeruk : {nJeruk} x {priceJeruk}
Anggur : {nAnggur} x {priceAnggur}

Total : {priceTotal}
'''
)

# proses pembayaran.
while True:
    pay = int(input('masukkan jumlah uang: '))
    delta = pay - priceTotal
    if delta >= 0:
        print(f'Terima kasih. uang kembalian {delta}')
        break
    else:
        print(f'Uang anda kurang sebesar {abs(delta)}')