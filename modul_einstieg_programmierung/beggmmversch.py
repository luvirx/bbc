#Mirio Eggmann Abschlussprojekt
#Verschlüsseln mit GPIO Eingabe

#Importieren
#----------------------------------------------------------------------------
import RPi.GPIO as GPIO
import time
from random import *

#Definitionen
#----------------------------------------------------------------------------
#Definition Allgemein
#----------------------------------------------------------------------------
def streifen():
    GPIO.output(l4, True)
    time.sleep(0.3)
    GPIO.output(l3, True)
    time.sleep(0.3)
    GPIO.output(l2, True)
    time.sleep(0.3)
    GPIO.output(l1, True)
    time.sleep(0.4)
    GPIO.output(l4, False)
    time.sleep(0.3)
    GPIO.output(l3, False)
    time.sleep(0.3)
    GPIO.output(l2, False)
    time.sleep(0.3)
    GPIO.output(l1, False)
    time.sleep(0.3)

def falsch():
    GPIO.output(l3, False)
    GPIO.output(l4, False)
    GPIO.output(l2, False)
    GPIO.output(l1, True)
    time.sleep(0.3)

def richtig(x):
    GPIO.output(x, True)
    GPIO.output(l1, False)
    time.sleep(1.5)

def leer():
    GPIO.output(l3, False)
    GPIO.output(l4, True)
    GPIO.output(l2, False)
    GPIO.output(l1, False)
    time.sleep(0.3)

#Definition Loginfunktion (nicht in Verwendung)
#----------------------------------------------------------------------------
def loginfunktion(): #Passwort: 1324
    testen = 0
    leer()
    print("Bitte geben Sie den Pincode ein:")
    while testen == 0:
        if GPIO.input(s1) != True:
            richtig(l3)
            print(" -",end="")
            if GPIO.input(s3) != True:
                richtig(l3)
                print(" -",end="")
                if GPIO.input(s2) != True:
                    richtig(l3)
                    print(" -",end="")
                    if GPIO.input(s4) != True:
                        richtig(l3)
                        print(" -")
                        testen = 1
                    elif GPIO.input(s1) != True or GPIO.input(s2) != True or GPIO.input(s3) != True:
                        falsch()
                        print(" Falsch!")
                elif GPIO.input(s1) != True or GPIO.input(s3) != True or GPIO.input(s4) != True:
                    falsch()
                    print(" Falsch!")
            elif GPIO.input(s1) != True or GPIO.input(s2) != True or GPIO.input(s4) != True:
                falsch()
                print(" Falsch!")
        elif GPIO.input(s2) != True or GPIO.input(s3) != True or GPIO.input(s4) != True:
            falsch()
            print(" Falsch!")
    print("Pin Ok")
    print("-----------------------------------------")

#Definition GPIO Pins einlesen
#----------------------------------------------------------------------------
def einlesen(y):
    leer()
    a = 0
    while a != 1:
        s1 = 26
        s2 = 18
        s3 = 16
        s4 = 10
        if GPIO.input(s1) != True:
            y = 26
            time.sleep(0.5)
            a = 1
        if GPIO.input(s2) != True:
            y = 18
            time.sleep(0.5)
            a = 1
        if GPIO.input(s3) != True:
            y = 16
            time.sleep(0.5)
            a = 1
        if GPIO.input(s4) != True:
            y = 10
            time.sleep(0.5)
            a = 1
    return(y)

#Definition Code
#----------------------------------------------------------------------------
def code(x,y):
    a = 0
    while a != 1:
        if x == s1:
            y = 1
            a = 1
        if x == s2:
            y = 4
            a = 1
        if x == s3:
            y = 7
            a = 1
        if x == s4:
            y = 9
            a = 1
    return(y)
#----------------------------------------------------------------------------

#GPIO Pins
#----------------------------------------------------------------------------
#LED
l1 = 24 #rot
l2 = 22 #gelb
l3 = 12 #gruen
l4 = 8 #blau

#Schalter
s1 = 26
s2 = 18
s3 = 16
s4 = 10

#Einstellungen
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Input Pins
GPIO.setup(s1, GPIO.IN)
GPIO.setup(s2, GPIO.IN)
GPIO.setup(s3, GPIO.IN)
GPIO.setup(s4, GPIO.IN)

#Output Pins
GPIO.setup(l1, GPIO.OUT)
GPIO.setup(l2, GPIO.OUT)
GPIO.setup(l3, GPIO.OUT)
GPIO.setup(l4, GPIO.OUT)
#----------------------------------------------------------------------------

#Variablen Definieren
#----------------------------------------------------------------------------
v1 = 0
v2 = 0
v3 = 0
v4 = 0

code1 = 0
code2 = 0
code3 = 0
code4 = 0

e1 = 0
e2 = 0
e3 = 0
e4 = 0

entcode1 = 0
entcode2 = 0
entcode3 = 0
entcode4 = 0

#----------------------------------------------------------------------------

#Titel
#----------------------------------------------------------------------------
print("Verschlüsselungssoftware by Mirio Eggamnn")
print("-----------------------------------------")
leer()
streifen()
#----------------------------------------------------------------------------

#Loginfunktion
#----------------------------------------------------------------------------
#loginfunktion()
#----------------------------------------------------------------------------

#Abfrage und Endlosschleife
#----------------------------------------------------------------------------
abfrage = input("Für Ende -> 'Ende', für Verschlüsseln -> 'v' und für Entschlüsseln -> 'e': ")
print("")
while abfrage != "Ende":
    entschltext = ""
    entschltext2 = ""
    entschltext3 = ""
    entschltext4 = ""
    geheimtext = ""
    geheimtext2 = ""
    geheimtext3 = "" 
    geheimtext4 = ""
#----------------------------------------------------------------------------

#Verschlüsselung
#----------------------------------------------------------------------------
    if abfrage == "v":

        #Datei leeren
        datei = open("C:\\text.txt","w")
        datei.write("")
        datei.close()
        
#Text Eingabe
        text = input("Geben Sie bitte den Text ein, welchen Sie verschlüsseln wollen: ")

#Code Eingabe
        print("Bitte geben Sie einen vierstelligen Pin ein, welchen Sie sich merken können:")

#Code Herausfinden
        weiter = 0
        while weiter == 0:
            leer()
            richtig(12)
            v1 = einlesen(v1)
            print("- ",end="")
            v2 = einlesen(v2)
            print("- ",end="")
            v3 = einlesen(v3)
            print("- ",end="")
            v4 = einlesen(v4)
            print("- ")
            weiter = 1
            leer()
    
#nur zum testen
        #print(v1,v2,v3,v4)

#Variablen neue Werte vergeben
        code1 = code(v1,code1)
        code2 = code(v2,code2)
        code3 = code(v3,code3)
        code4 = code(v4,code4)

        v1versch = int(code1)
        v2versch = int(code2)
        v3versch = int(code3)
        v4versch = int(code4)

#testen
        #print(code1,code2,code3,code4)
        #print(v1versch,v2versch,v3versch,v4versch)

#Diverse Random Sachen einfügen
        randomauswahl = ['abs','ekg','qwe','pou','nhe','4fe','qud','9e3','qpw','381','1v6','000','xyy','85d','dks']

        listetext = []
        laenge = len(text) - 1
        for i in text:
            listetext.append(i)
        stelle = -1
        for i in range(laenge):
            stelle = stelle + 2
            einfuegen = choice(randomauswahl)
            listetext.insert((stelle),einfuegen)
        randomtext = ''.join(listetext)

#Leerzeichen verändern
        for zeichen in randomtext:
            if zeichen == " ":
                randomtext = randomtext.replace(" ","ç")

#Ascii Code Text verändern
        for zeichen in randomtext:
            asc = ord(zeichen)
            ascversch = asc - v1versch - v1versch + v4versch - v3versch
            neuesZeichen = chr(ascversch)
            geheimtext = geheimtext + neuesZeichen
            randomtext = geheimtext

#Ascii Code Text verändern
        for zeichen in randomtext:
            asc2 = ord(zeichen)
            ascversch2 = asc2 - v2versch + v4versch
            neuesZeichen2 = chr(ascversch2)
            geheimtext2 = geheimtext2 + neuesZeichen2
            randomtext = geheimtext2

#Ascii Code Text verändern
        for zeichen in randomtext:
            asc3 = ord(zeichen)
            ascversch3 = asc3 + v3versch - v1versch + v2versch
            neuesZeichen3 = chr(ascversch3)
            geheimtext3 = geheimtext3 + neuesZeichen3
            randomtext = geheimtext3

#Ascii Code Text verändern
        for zeichen in randomtext:
            asc4 = ord(zeichen)
            ascversch4 = asc4 - v4versch + v2versch - v3versch - v4versch - v4versch
            neuesZeichen4 = chr(ascversch4)
            geheimtext4 = geheimtext4 + neuesZeichen4
            randomtext = geheimtext4

#Das ganze in einem File speichern
        print(randomtext)
        datei = open("C:\\text.txt","w")
        datei.write(randomtext)
        datei.close()

#Abfrage
        abfrage = input("Für Ende -> 'Ende', für Verschlüsseln -> 'v' und für Entschlüsseln -> 'e': ")
        print("")

#Entschlüsselung
#----------------------------------------------------------------------------
    if abfrage == "e":
        
#Inhalt vom File auslesen
        datei = open("C:\\text.txt")
        inhalt = datei.read()
        verschtext = inhalt
        datei.close()

#Code Eingabe
        print("Bitte geben Sie den Pin ein, welchen Sie definiert haben:")

#Code herausfinden
        weiter = 0
        while weiter == 0:
            leer()
            richtig(12)
            e1 = einlesen(e1)
            print("- ",end="")
            e2 = einlesen(e2)
            print("- ",end="")
            e3 = einlesen(e3)
            print("- ",end="")
            e4 = einlesen(e4)
            print("- ")
            weiter = 1
            leer()

#Variablen neue Werte vergeben
        entcode1 = code(e1,entcode1)
        entcode2 = code(e2,entcode2)
        entcode3 = code(e3,entcode3)
        entcode4 = code(e4,entcode4)

        v1entsch = int(entcode1) 
        v2entsch = int(entcode2)
        v3entsch = int(entcode3)
        v4entsch = int(entcode4)

#testen
        #print(entcode1,entcode2,entcode3,entcode4)
        #print(v1entsch,v2entsch,v3entsch,v4entsch)

#Ascii Code Text verändern
        for zeichen in verschtext:
            asce1 = ord(zeichen)
            ascentsch1 = asce1 + v1entsch + v1entsch - v4versch + v3versch
            neuesZeichene = chr(ascentsch1)
            entschltext = entschltext + neuesZeichene
            verschtext = entschltext

#Ascii Code Text verändern
        for zeichen in verschtext:
            asce2 = ord(zeichen)
            ascentsch2 = asce2 + v2entsch - v4versch
            neuesZeichene2 = chr(ascentsch2)
            entschltext2 = entschltext2 + neuesZeichene2
            verschtext = entschltext2

#Ascii Code Text verändern
        for zeichen in verschtext:
            asce3 = ord(zeichen)
            ascentsch3 = asce3 - v3entsch + v1entsch - v2entsch
            neuesZeichene3 = chr(ascentsch3)
            entschltext3 = entschltext3 + neuesZeichene3
            verschtext = entschltext3

#Ascii Code Text verändern
        for zeichen in verschtext:
            asce4 = ord(zeichen)
            ascentsch4 = asce4 + v4entsch - v2entsch + v3versch + v4versch + v4versch
            neuesZeichene4 = chr(ascentsch4)
            entschltext4 = entschltext4 + neuesZeichene4
            verschtext = entschltext4

#Leerzeichen wieder einfügen
        for zeichen in verschtext:
            if zeichen == "ç":
                verschtext = verschtext.replace("ç"," ")

#Random Sachen wieder herausnehmen
        resultat = []
        variable = -4
        lang = len(verschtext)- 3
        while variable < lang:
            variable = variable + 4
            var = verschtext[variable]
            resultat.append(var)
        ende=''.join(resultat)
        print(ende)

#Das ganze in einem File speichern
        datei = open("C:\\text.txt","w")
        datei.write(ende)
        datei.close()

#Abfrage
        abfrage = input("Für Ende -> 'Ende', für Verschlüsseln -> 'v' und für Entschlüsseln -> 'e': ")
        print("")
#----------------------------------------------------------------------------

#Bei falscher Aufgabe
#----------------------------------------------------------------------------
    else:
        print("Sie haben sich wohl vertippt...")
        print("")
        abfrage = input("Für Ende -> 'Ende', für Verschlüsseln -> 'v' und für Entschlüsseln -> 'e': ")
#----------------------------------------------------------------------------


#GPIO reinigen
GPIO.cleanup()
