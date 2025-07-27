#a = 10, a adalah variabel dengan nilai 10

# tipe data 1 yaitu Integer
#angka satuan tanpa koma
data_integer = 15
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

# tipe data 2 yaitu Float
#angka desimla dengan koma
data_float = 1.5
print("data : ", data_float)
print("bertipe : ", type(data_float))

# tipe data 3 yaitu String
#kumpulan karakter
data_string = "divot"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

# tipe data 4 yaitu Boolean
#nilai benar atau salah(true/false)
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

# tipe data kompleks
#angka dengan bagian real atau imajiner(j)
data_complex = complex(5, 6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# tipe data dari bahasa C
#menggunakan modul ctypes (tipe data c_double)
from ctypes import c_double
data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))
