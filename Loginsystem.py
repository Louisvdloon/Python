#----------------------------------------------
# color codes
class bcolors:
    GREEN = '\033[92m' #GREEN
    YELLOW = '\033[93m' #YELLOW
    RED = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    CWHITE  = '\33[37m' #WHITE BORDER
    UNDERLINE = '\033[4m' #UNDERLINE
#----------------------------------------------
# == is gelijke value
#Dit zijn de inloggegevens
username = 'Louis'
password = 'Welkom01'

username1 = 'Sajid'
password1 = 'Welkom02'

username2 = 'Admin'
password2 = 'Admin'

login_username = str(input("Vul je gebruikersnaam in"))
login_password = str(input("Vul je wachtwoord in"))

if login_username == username  and login_password == password:
    print("Succesvol ingelogd")
    print("Welkom,",username)

elif login_username == username1  and login_password == password1:
    print("Succesvol ingelogd!")
    print("Welkom,",username1)

elif login_username == username2 and login_password == password2:
    print("Succesvol ingelogd!")
    print("Welkom,",username2)
else:
    print("Verkeerde inloggegevens, probeer opnieuw.")

input()



