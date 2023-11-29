# Pertama tama membuat Objek yang akan dibuat
browser = "Bagaimana cara membuat mie ayam"
# Kedua Membuat Variabel 
words = browser.split()
counts = {}
#Ketiga melakukan perhitungan objek
count = 0
# Keemepat Melakukan looping
for j in range (0, len(words)):
    kata1 = words[j]
    for j in range (0, len(words)):
      kata2 = words[j]
      #Kelima Melakukan cara untuk bisa mengetahui jumlah kata yang disebut
      if kata1==kata2:
        # jumlahkan 
        count = count + 1
    # Keenam Membuat Dictionaries
    counts[kata1]=count
    count = 0
# Lalu liat hasil
print(counts)
