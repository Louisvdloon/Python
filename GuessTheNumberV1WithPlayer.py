import random
import time
#libraries
print("""Dit spel gaat als volgt:
  De computer heeft een getal in zijn brein tussen de 1 en de 100.
  Aan jou de taak om binnen 7 keren het getal te raden.""")
time.sleep(5)

het_te_raden_getal = random.randint(1, 100)
speler_getal = int(input("Geef je getal op "))
victoryroyale = 0
#Variables

for n in range (7):
    if victoryroyale != 1:
        speler_getal = int(input("Geef je getal op "))
        if het_te_raden_getal > speler_getal:
            print("Het getal is hoger")


        elif het_te_raden_getal < speler_getal:
            print("Het getal is lager")


        if speler_getal == het_te_raden_getal:
            print("Je hebt het getal geraden! Het getal was", het_te_raden_getal)
            victoryroyale = 1


input("Afsluiten")





