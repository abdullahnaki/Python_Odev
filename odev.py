ogr = ["Ali Gül","Samet Yılmaz", "Fatma Demir"]

ogr_ekl = input("Adınızı ve soyadınızı girniz: ")
ogr.append(ogr_ekl)


#Aldığı isim soy isim ile eşleşen değeri listeden kaldıran.
ogr_dlt = input("Lütfen tekrar ad soyad giriniz:")

i = 0
for i in range(len(ogr_dlt)):
    if (ogr[i] == ogr_dlt):
        ogr.pop(i)
        print("Aynı isim ve soy isimle kayıt yapılamaz.")
    else: 
        print('Öğrenciniz kaydedildi. ')
        break
print(ogr)

# Listede de bulunan öğrencileri ekrana yazdır. 

for i in range(len(ogr)):
    print(ogr[i])

# Öğrenci numarası 

ogr_no = input("Numarasını öğrenmek istediğiniz öğrencinin ad ve soyadını yazınız:  ")
for i in range(len(ogr)):
    if (ogr_no == ogr[i]):
        print(f"Öğrenci no: {str(i+1)}")

# Listeden birden fazla elaman silme 
dlt = input("Kaç öğrenci silinecel: ")
i = 0 

while i< int(dlt):
    ogr.remove(ogr[i])
    i+=1
print(ogr)

#Listeye birden fazla eleman ekleme
adet=input("Kaç öğrenci eklemek istersiniz?")
i=0
while i<int(adet):
    std=input("Arada bir boşluk bırakarak ad soyad giriniz:")
    ogr.append(std)
    i+=1
print(ogr)