import random
szamok = []
for i in range(5):
    szam = random.randint(0,100)
    if szam%2==0:
        print("Páros")
    else:
        print("Páratlan")
    szamok.append(szam)
print(szamok)