import random
import string

print("Dieses Programm erstellt eine Text-Datei mit generierte Password!")

datei_name = str(input('Bitte die Dateiname eingeben(ohne .txt):   '))
datei_name = datei_name + '.txt'
pfad_ordner = "C:\\Users\\Student\\Documents\\"
pfad = pfad_ordner + datei_name
# pfad = str(input('Bitte Pfad eingeben: '))

laenge = int(input('Bitte die Länge von Password eingeben:   '))

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(laenge))

try:
    file = open((pfad), "x+")
    file.write(password)
    file.read()
    file.close()
    print(
        f"Ihre Password wurde erfolgreich generiert und am {pfad} gespeichert")
except IOError:
    print("Datei kann nicht geöffnet werden")
except:
    print("Es ist folgender Fehler aufgetreten:", sys.exc_info()[0])
