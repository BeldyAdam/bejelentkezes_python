felhasznev = input("Adjon meg egy felhasznalónevét: ")
jelszo = input("Adjon meg egy jelszót: ")
print("Bejelentkezes: ")
felhasznev2 = input("Adja meg a felhasznalónevét: ")
jelszo2 = input("Adja meg a jelszavát: ")
probalkozasok_szama = 0
while felhasznev != felhasznev2 or jelszo != jelszo2:
    print("Hibás, újra: ")
    felhasznev2 = input("Adja meg a felhasznalónevét: ")
    jelszo2 = input("Adja meg a jelszavát: ")
    probalkozasok_szama += 1
    if probalkozasok_szama == 3:
        print("Túl sok hibás próbálkozás!")
        exit()
print("Sikeres bejelentkezés")