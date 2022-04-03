import random

speler1 = int(input("Kies een getal tussen de 1 en de 100"))
te_raden_getal = speler1
speler2 = 0
laagste = 1
hoogste = 100
victoryroyale = 0
for n in range (7):
    if victoryroyale != 1:
        speler2 = random.randint(laagste, hoogste)
        print(speler2)
        if te_raden_getal > speler2:
            print("Het getal is hoger")
            laagste = speler2 + 1

        elif te_raden_getal < speler2:
            print("Het getal is lager")
            hoogste = speler2 - 1

        if speler2 == te_raden_getal:
            print("Je hebt het getal geraden! Het getal was", te_raden_getal)
            victoryroyale = 1



input("Afsluiten")