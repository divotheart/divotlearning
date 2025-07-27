# castring adalah merubah satu tipe ke tipe lain
#tipe data: int, float, str, bool

# INTEGER
print("==== INTEGER ====")
data_int = 9
print("data = ", data_int, ",type =",type(data_int))

data_str    = str(data_int)
data_float  = float(data_int)
data_bool   = bool(data_int) #akan false jika nilai int = 0
print("data = ", data_float, ",type =",type(data_float))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_bool, ",type =",type(data_bool))

# FLOAT
print("==== FLOAT =====")
data_float = 9.5
print("data = ", data_float, ",type =",type(data_float))

data_int    = int(data_float) #akan dibulatkan ke bawah
data_str    = str(data_float)
data_bool   = bool(data_float) #akan false jika nilai float = 0
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_bool, ",type =",type(data_bool))

# BOOLEAN
print("==== BOOLEAN =====")
data_bool = False;
print("data = ", data_bool, ",type =",type(data_bool))

data_int    = int(data_bool)
data_str    = str(data_bool)
data_float   = bool(data_bool)
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_float, ",type =",type(data_float))

# STRING
print("==== STRING =====")
data_str = "10"
print("data = ", data_str, ",type =",type(data_str))

data_float  = float(data_str) #string harus angka
data_int    = int(data_str) #string harus angka
data_bool   = bool(data_str) #false jika string kosong
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_float, ",type =",type(data_float))
print("data = ", data_bool, ",type =",type(data_bool))


# ============================== #
#input dari user
print("==== INPUT USER =====")
data_input = input("masukkan data angka: ")
print("data = ", data_input, ", type =", type(data_input))  #default-nya str

# coba konversi
data_input_int    = int(data_input)
data_input_float  = float(data_input)
data_input_bool   = bool(data_input)

print("setelah casting ke int   :", data_input_int, ", type =", type(data_input_int))
print("setelah casting ke float :", data_input_float, ", type =", type(data_input_float))
print("setelah casting ke bool  :", data_input_bool, ", type =", type(data_input_bool))