import random

def zahlenraten():
    # Generiere eine zufällige Zahl zwischen 0 und 100
    zahl = random.randint(0, 100)
    
    while True:
        # Fordere den Benutzer auf, die Zahl zu erraten
        vermutung = int(input("Errate die Zahl zwischen 0 und 100: "))
        
        # Überprüfe, ob die Vermutung korrekt ist
        if vermutung == zahl:
            print("Herzlichen Glückwunsch! Du hast die Zahl erraten.")
            break
        elif vermutung < zahl:
            print("Die Zahl ist größer als deine Vermutung. Versuche es erneut.")
        else:
            print("Die Zahl ist kleiner als deine Vermutung. Versuche es erneut.")

zahlenraten()
