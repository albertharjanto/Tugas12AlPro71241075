Dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
item = 1

print("key\tvalue\titem")

for key, value in Dictionary.items():
    print(f"{key}\t{value}\t{item}")
    item += 1