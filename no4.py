nama_file = 'mbox-short.txt'

try:
    handle = open(nama_file)
except:
    print(f"File dengan nama {nama_file} tidak ditemukan. Pastikan nama file sudah benar!")
    exit()

domain_counts = {}

for line in handle:
    if line.startswith("From "):
        hasil_split1 = line.split()
        email = hasil_split1[1]
        hasil_split2 = email.split("@")
        domain = hasil_split2[1]
        domain_counts[domain] = domain_counts.get(domain, 0) + 1

print(domain_counts)