browser = "Bagaimana cara membuat mie ayam"
words = browser.split()
counts = {}
count = 0
for j in range (0, len(words)):
    kata1 = words[j]
    for j in range (0, len(words)):
      kata2 = words[j]
            if kata1==kata2:
                count = count + 1
        counts[kata1]=count
    count = 0
print(counts)
PS C:\Users\Pinkan> & F:/Users/Pinkan/anaconda3/python.exe c:/Users/Pinkan/Documents/SE_G.231.22.0121.py
{'Bagaimana': 1, 'cara': 1, 'membuat': 1, 'mie': 1, 'ayam': 1}
