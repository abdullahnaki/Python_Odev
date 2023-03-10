# Python Veri Tipleri: 

# int: Tamsayı veri tipidir. 

sayi1 = 3
print(sayi1)
print(type(sayi1)) 

# float: Ondalık sayı veri tipi, noktadan sonra bir veye daha fazla ondalık sayı içerebilir. 

sayi2 = 2.3
print(sayi2)
print(type(sayi2)) 

# String(str): String değerler tırnak içersinde ifade edilmektedir. 

mtn = "Python"
print(mtn)
print(type(mtn))

# bool: True ve False 

sayi3 = 4
sayi4 = 7
print(sayi3 == sayi4)

# list: Elemanları sıralanabilir, güncellenebilir ayrıca her bir eleman liste içerisinde birden fazla tekrarlanabilir.

list1 = [1,2,3,4]
list2 = ['Bir','İki','Üç']
print(list1)
print(list2)



#Python Matematiksel Operatörler. 

# Toplama(+)

print(100 + 50)

# Çıkarma(-)
print(100 - 50)

# Tam Bölme (Kalansız Bölme)

print(15//3)

print(17//7) # 17' nin 7'e kalansız bölümünden elde edilen sayı 2' dir. Burada kalan sayıyı atmış oluyoruz.

# Üs Alma (**)

print(5**2) 

# Kodlama.io sitesindeki değişken olarak kullanılan veriler ve veri tipleri:

# Ödevler içersindeki amaç ve ödev tanımı birer str ifadeye örnektir. 
# Kursu tamalama yüzdesi ise int bir ifadedir. 


# Şart Blokları
# Sisteme Giriş 

kullanici= 'Fatih Yılmaz'
sifre = '12345'

username = input('Kullanıcı Adınız: ')
pasword = input("Şifrenizi Giriniz: ")


if kullanici == username and sifre == pasword:
    print("Hoşgeldiniz")
else:
    print("Kullanıcı adı veya şifreniz hatalı.")