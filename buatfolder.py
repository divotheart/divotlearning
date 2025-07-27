import os

nama_folder = "diva_python"

if not os.path.exists(nama_folder):
    os.makedirs(nama_folder)
    print("Folder berhasil dibuat.")
else:
    print("Folder sudah ada.")