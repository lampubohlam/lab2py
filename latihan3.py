Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # input nilai variabel
>>> a=input("masukan nilai a:")
masukan nilai a:6
>>> b=input("masukan nilai b:")
masukan nilai b:8
>>> 
>>> #cetak nilai variabel
>>> print("variabel a="a,a)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("variabel a=",a)
variabel a= 6
>>> print("variable b=",b)
variable b= 8
>>> 
>>> # cetak hasil operasi kedua variabel dengan String Format
>>> print("Hasil penggabungan {1}&{0}=%s".format(a,b) %(a+b))
Hasil penggabungan 8&6=68
>>> 
>>> #konversi nilai variabel
>>> a=int(a)
>>> b=int(b)
>>> print("Hasil penjumlahan {1}+{0}=%s".format(a,b) %(a+b))
Hasil penjumlahan 8+6=14
>>> print("Hasil pembagian {1}/{0}=%s".format(a,b) %(a/b))
Hasil pembagian 8/6=0.75
