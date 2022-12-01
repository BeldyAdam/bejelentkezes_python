def ido():
    ora = int(input("Adja meg az órát: "))
    perc = int(input("Adja meg a percet: "))
    mp = int(input("Adja meg a másodpercet: "))
    ido = []
    ido.append(ora)
    ido.append(perc)
    ido.append(mp)
    print(ido[0],":",ido[1],":",ido[2])
    print("Másodpercben: ",ora*3600+perc*60+mp)
