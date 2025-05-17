Lista = ['red', 'green', 'blue']
Listb = ['#FF0000','#008000', '#0000FF']

hasil = {}

if len(Lista) != len(Listb):
    print("Kedua list harus memliki panjang yang sama!")
else:
    for i in range(len(Lista)):
        hasil[Lista[i]] = Listb[i]
    print(hasil)