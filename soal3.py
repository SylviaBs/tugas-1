depan = input("Nama Depan: ")
belakang = input("Nama Belakang: ")
jeniskelamin = input("Laki-laki/perempuan (l/p)? ")

print(f"Nama lengkap: {depan} {belakang}")

if jeniskelamin == 'l':
    print("Jenis kelamin: Laki-laki")
elif jeniskelamin == 'p':
    print("Jenis kelamin: Perempuan")
else:
    print("Input jenis kelamin tidak valid.")