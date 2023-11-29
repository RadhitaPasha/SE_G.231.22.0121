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
PS C:\Users\Pinkan> & F:/Users/Pinkan/anaconda3/python.exe c:/Users/Pinkan/Documents/SE_G.231.22.0121.py
{'Bagaimana': 1, 'cara': 1, 'membuat': 1, 'mie': 1, 'ayam': 1}
