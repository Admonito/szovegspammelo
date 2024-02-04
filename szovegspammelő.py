import time
szoveg = input("Írd be azt szöveget amit spammelni akarsz: ")
print("A program befagyaszthatja a géped ha túl nagy gyorsaság értéket adtál meg!")
gyorsaság = int(input("És milyen gyorsasággal? "))
x = 1
while x < 2:
    print(szoveg*gyorsaság)
    time.sleep(0.1)