import time

print('''Dit spel gaat als volgt:

Er zijn 20 tokens, de gene die de laatste tokens pakt heeft gewonnen!

De regels zijn simpel, iedere speler moet elke ronde kiezen hoeveel tokens hij pakt.
De catch is dat je moet kiezen tussen 1, 2 of 3 tokens. 

Succes!''')
time.sleep(15)

aantaltokens = 20

while aantaltokens !=0:
    speler1 = int(input("Pak aantal tokens. Max 3!"))
    if speler1 < 0 or speler1 > 4:
        print("Deze waarde is ongeldig")
    else:
        aantaltokens = aantaltokens - speler1
        print(aantaltokens)
        print("nimmbot`s beurt...")
        time.sleep(3)
        Nimm = 4 - speler1
        aantaltokens = aantaltokens - Nimm
        print(aantaltokens)





if aantaltokens == 0:
    print("Nimmbot wint! doe beter je best!")

input("Afsluiten")