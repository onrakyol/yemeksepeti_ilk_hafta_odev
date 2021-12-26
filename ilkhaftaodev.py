"""
Bir metnin uzunluğunu hesaplamak için bir Python programı yazınız. ipucu Len fonksiyonu
"""

txt = input("Lütfen uzunluğunu öğrenmek istediğiniz metni girin: ")
new_txt = txt.replace(' ', '')
print('Girdiğiniz metin {} karakterden oluşmaktadır'.format(len(new_txt)))

"""Kullanıcı tarafından girilen bir metnin ilk iki ve son iki karakterini ekrana yazdıran Python programını yazınız."""

txt = input('Lütfen bir metin giriniz: ')
print('Girdiğiniz metnin ilk iki harfi {}, son iki harfi ise {}'.format(txt[0:2], txt[-2:]))

"""Kullanıcıdan değişecek metin ve eski harf ve yeni harf bilgisini alarak girilen metin üzerinden değişikliği yapıp sonucu ekrana yazdıran Python programını yazınız."""

txt = input('Metni giriniz: ')
change_letter = input('Hangi harf değişsin: ')
new_letter = input('Yeni harf ne olsun: ')
new_txt = txt.replace(change_letter, new_letter)
print(new_txt)

"""Kullanıcı tarafından girilen bir kelimenin palindrom olup olmadığını karşılaştırma operatöründen faydalanarak print() fonksiyonu ile ekrana yazdırınız. """

txt = input('Lütfen bir metin giriniz: ')
new_txt = txt.replace(' ', '')[::-1].lower()

if new_txt == txt.replace(' ', '').lower():
    print('Pal')
else:
    print('Not pal')

"""Girilen bir metnin son 2 karakterini 4 defa çoğaltarak ekrana yazan Python programını yazınız. `*` aritmetik operatöründen faydalanabilirsiniz. """

txt = input('Lütfen metni giriniz: ')

last_two_letter = txt[-2:]
print(4*last_two_letter)

"""
5 elemanlı bir liste oluşturunuz. Bu liste içerisindeki 2. elemanı 100 ile değiştiren python kodu yazınız.
"""

list_ = ["Onur", "Akyol", 3, 5, (23, 5)]
list_[1] = 100
print(list_)

"""İki farklı listede tutulan verileri tek bir listede sırasıyla append,extend metodlarıyla ve "+" operatörü ile birleştiren python kodunu yazınız 
liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = ?????
"""
liste1 = [1,2,3]
liste2 = [4,5,6]

########## Two lists merge with '+' #################
liste3 = liste1 + liste2

###################### Two lists merge with 'extend' method ##############
liste1.extend(liste2)

############### Two lists merge with for loops and append method ###################
for i in liste2:
    liste1.append(i)
print(liste1)

"""Oluşturduğunuz 3 elemanlı bir liste içerisine ilk sıraya "Elma" kelimesini ekleyiniz. """

liste = ['Onur', 'Akyol', 'Apple']
liste.insert(0, "Elma")
print(liste)

"""liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23]
yukarıdaki listeden ilk 3 sayısını silip ekrana yazdırınız. 
"""
liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23]
del liste[0:3]
print(liste)

"""
liste1 = ["1",1,2,"3"]
Yukarıdaki listenin bir kopyasını alarak 250 sayısını listenin sonuna ekleyiniz,her iki listeyi ekrana yazdırınız.
Beklenen Çıktı:
["1",1,2,"3"] => Liste1 Çıktısı
["1",1,2,"3",250] => Liste2 Çıktısı
"""
liste1 = ["1",1,2,"3"]
new_liste = liste1.copy()
new_liste.append(250)
print(liste1)
print(new_liste)

"""

Aşağıdaki üç farklı sözlüğü tek sözlükte birleştiren python kodunu yazınız
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
Beklenen Çıktı : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}

d3 = {**dict1, **dict2, **dict3}
print(d3)

"""sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
Sözlükteki en son elemanı silerek ekrana işlem sonucunu yazdırınız
Beklenen Çıktı :(6,60)
"""
sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
sozluk.pop(6)
print(sozluk)

"""dict1={1:10, 2:20}
Yukarıdaki sözlüğe bir eleman ekleyiniz. 
Beklenen Çıktı :{1:10, 2:20, 3:30}
"""
dict1={1:10, 2:20}

dict1.update({3:30})
print(dict1)

"""liste=[1,2,3,4,5]
    a.Yukarıdaki listeden faydalanarak bir sözlük oluşturun 
    b.sözlüğün her alamanının karşılığına değer olarak anahtarda bulunan sayısal değerin 10 katını eşitleyin.
Beklenen Çıktı :
a. {1:0,2:0,3:0,4:0,5:0}
b. {1:10,2:20,3:30,4:40,5:50}
"""
liste=[1,2,3,4,5]
a = dict((i, 0) for i in liste)
b = dict((i, i*10) for i in liste)
print(a, b)

"""sozluk={1:10,2:20,3:30,4:40,5:50}
Sözlük içerisine 6 sayısını anahtar olarak değeri 60 olacak şekilde setdefault fonksiyonunu kullanarak ekleyiniz

"""
sozluk={1:10,2:20,3:30,4:40,5:50}
sozluk.setdefault(6, 60)
print(sozluk)

"""
Seven Segment Display 
https://en.wikipedia.org/wiki/Seven-segment_display

* * * * *
*       *
*       *
* * * * *
*       *
*       *
* * * * *

8 sayısı girildiğinde yukarıdaki çıktıyı veren python programını 0 dan 9 a kadar olan sayılar için yazalım
## hex,bin,zfill, tek satırda if

"""
scheme = {
    '0': ('***', '* *', '* *', '* *', '***'),
    '1': ('  *', '  #', '  *', '  *', '  *'),
    '2': ('***', '  #', '***', '*  ', '***'),
    '3': ('***', '  #', '***', '  *', '***'),
    '4': ('* *', '* *', '***', '  *', '  *'),
    '5': ('***', '*  ', '***', '  *', '***'),
    '6': ('***', '*  ', '***', '* *', '***'),
    '7': ('***', '  *', '  *', '  *', '  *'),
    '8': ('***', '* *', '***', '* *', '***'),
    '9': ('***', '* *', '***', '  *', '***'),
    '.': ('   ', '   ', '   ', '   ', '  *'),
}

def seven_segment(number):    
    digits = [scheme[digit] for digit in str(number)]    
    for i in range(5):
        print("  ".join(segment[i] for segment in digits))

"""
Bir listeyi bir sözlükte sıralamak için bir Python programı yazın <br>
Örnek Veri: num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
"""
num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
for x in num:
    num[x].sort()
print(num)

"""sozluk = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']} 
ilgili sözlükten anahtar kısımlarında bulunan boşlukları temizleyen python kodu yazınız. 
"""

sozluk = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
for i in sozluk.keys():
    sozluk[i.replace(" ", "")] = sozluk.pop(i)
print(sozluk)

"""
liste1=[1,2,3]
liste2=[4,5,6,7,8]
iki listeyi liste3 ile birleştiriniz?
"""

liste1=[1,2,3]
liste2=[4,5,6,7,8]
liste3 = liste1 + liste2
print(liste3)

"""liste=[1,2,3,4,5,6] listesindeki 1. elemanı del komutu ile siliniz?

"""

liste=[1,2,3,4,5,6]
del liste[0]
print(liste)

"""
liste=["elma" , "armut", "çilek"] listesine append komutu ile sona 3 elemanını ekleyiniz?
"""
liste=["elma" , "armut", "çilek"]
liste.append(3)
print(liste)

"""Girilen on sayı içerisinden en büyük üç sayıyı bulmak için bir Python fonksiyonu yazınız"""

count = 0
i = 1
liste = []
while count < 10:
  print("Lütfen {}. sayıyı giriniz: ".format(i))
  number = int(input())
  liste.append(number)
  i += 1
  count += 1
liste.sort()
last = list(set(liste))
print(last[-3:])

"""Bir metin içerisindeki büyük ve küçük harflerin listesini yazdıran python programını yazınız."""

import string

txt = "Buyuk ve KUCuk Harflerin Listesi"
upper = string.ascii_uppercase + "ÇĞİÖŞÜ"
lower = string.ascii_lowercase + "çiöşüğ"

uppercase = [i for i in txt if i in upper]
lowercase = [i for i in txt if i in lower]
print(f"Büyük harflerin listesi {uppercase}, küçük harflerin listesi {lowercase}")

"""kullanıcıdan alınan 10 sayının çift ve tek sayıların sayısını ekrana yazdıran programı yazınız. """

count = 0
i = 1
liste = []
while count < 10:
  print("Lütfen {}. sayıyı giriniz: ".format(i))
  number = int(input())
  liste.append(number)
  i += 1
  count += 1
odd_number = [i for i in liste if i%2 == 1]
even_number = [i for i in liste if i%2 == 0]
print("Tek sayıların sayısı {}, çift sayıların sayısı {}".format(len(odd_number), len(even_number)))