#libraries
import time

def plus(num1, num2):
    return num1 + num2

def min(num1, num2):
    return num1 - num2

def keer(num1, num2):
    return num1 * num2

def delen(num1, num2):
    return num1 / num2
#Functions

print("Kies nu wat je wilt doen.\n"
      "1. Plus\n"
      "2. Min\n"
      "3. Keer\n"
      "4. Delen\n")
#Geeft aan wat voor opties er zijn
time.sleep(3)
#Vraagt de gebruiker om te selecteren
selecteer = float(input("Selecteer:\n 1\n 2\n 3\n 4\n"))

nummer1 = float(input("Eerste getal "))
nummer2 = float(input("Tweede getal "))

if selecteer == 1:
    print(nummer1, "+", nummer2, "=", plus(nummer1, nummer2))
elif selecteer == 2:
    print(nummer1, "-", nummer2, "=", min(nummer1, nummer2))
elif selecteer == 3:
    print(nummer1, "*", nummer2, "=", keer(nummer1, nummer2))
elif selecteer == 4:
    print(nummer1, "/", nummer2, "=", delen(nummer1, nummer2))
else:
    print("Som niet geldig!")


