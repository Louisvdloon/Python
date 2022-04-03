name = input("Wat is je naam?")
print ("Goedemiddag,",name)
# input is antwoord van gebruiker
#--------------------------------------------------------------------------
age = int(input("Hoe oud ben je?: "))
# int(input werkt alleen met integers (Hele getallen)
print ("Ah, je bent dus",age , "jaar. Dan ben je over 2 jaar",age + 2 )
#--------------------------------------------------------------------------
country = input("In welk land woon je?")
print ("Wow,",country, "is een prachtig land!")
#--------------------------------------------------------------------------
class bcolors:
    GREEN = '\033[92m' #GREEN
    YELLOW = '\033[93m' #YELLOW
    RED = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    UNDERLINE = '\033[4m' #UNDERLINE
    # color codes
#--------------------------------------------------------------------------
print (f"{bcolors.UNDERLINE}Bij de volgende vraag moet je met Ja of Nee antwoorden{bcolors.RESET}")
input("Druk op enter om door te gaan.")
python = str(input("Vind je python lastig?"))

if python == "Ja".upper():
    print ("Blijf oefenen! working pays off.")

if python == "Nee".upper():
    print ("Gelukkig! keep learning.")
else:
    print("Antwoord alleen met Ja en Nee. Begin overnieuw!")
#De if statement laat iemand Ja of Nee antwoorden. Zodra ze ja of nee typen komt er een custom print.
#De else statement wordt pas uitgevoerd wanneer iemand iets anders dan ja of nee zegt.
input(f"{bcolors.RED}Druk op enter voor een overzicht{bcolors.RESET}")
#--------------------------------------------------------------------------
#print overzicht / summary
print(f"{bcolors.UNDERLINE}Overzicht{bcolors.RESET}")
print(f"{bcolors.YELLOW}Naam{bcolors.RESET}:",name)
print ("--------------------")
print(f"{bcolors.YELLOW}Leeftijd{bcolors.RESET}:",age)
print ("--------------------")
print(f"{bcolors.YELLOW}Land{bcolors.RESET}:",country)
print ("--------------------")
print(f"{bcolors.YELLOW}Vind je python lastig?{bcolors.RESET}:",python)
print ("--------------------")
#--------------------------------------------------------------------------
input(f"{bcolors.RED}Press any key to close this program{bcolors.RESET}")
