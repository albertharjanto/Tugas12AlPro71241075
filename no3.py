nama_file = 'mbox-short.txt'

try:
    handle = open(nama_file)
except:
    print(f"File dengan nama {nama_file} tidak ditemukan. Pastikan nama file sudah benar!")
    exit()

email_counts = {}

for line in handle:
    if line.startswith("From "):
        hasil_split = line.split()
        email = hasil_split[1]
        email_counts[email] = email_counts.get(email, 0) + 1

print(email_counts)