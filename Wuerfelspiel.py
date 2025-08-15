#------------------------------------------
# (bitte ausfüllen)
# Name:            ...............
# Vorname:         ...............
# Programmiert in: [ ] WebTigerJython
#                  [ ] TigerJython offline
#                  [ ] Andere Umgebung: ...
#------------------------------------------

#------------------------------------------
# Folgender Code ist gegeben und dient 
# als Ausgangslage (nicht verändern) 
#------------------------------------------

from gturtle import *
from random import *
makeTurtle()
hideTurtle()

# Vorbereitete Würfelzahlen, als Liste.
# Die jeweiligen Indizes geben die Position eines einzelnen Punktes auf dem Würfel an.
#
#    0   1
#    2 3 4
#    5   6
#
# Beispiel: 1+5 aktiv = Augenzahl 2, 0+1+5+6 = Augenzahl 4.
#
augenZahlen = []
augenZahlen.append([0, 0, 0, 1, 0, 0, 0]) # index 0: Augenzahl 1
augenZahlen.append([0, 1, 0, 0, 0, 1, 0]) # index 1: Augenzahl 2
augenZahlen.append([0, 1, 0, 1, 0, 1, 0]) # index 2: Augenzahl 3
augenZahlen.append([1, 1, 0, 0, 0, 1, 1]) # index 3: Augenzahl 4
augenZahlen.append([1, 1, 0, 1, 0, 1, 1]) # index 4: Augenzahl 5
augenZahlen.append([1, 1, 1, 0, 1, 1, 1]) # index 5: Augenzahl 6


#------------------------------------------
# Ab hier eigenen und zu verändernden Code
# Bereits bestehende Funktionen sollen
# verwendet werden
#------------------------------------------

def wuerfeln():
    """Würfelt mit zwei Würfeln und gibt die Augenzahlen zurück"""
    wuerfel1 = randint(1, 6)
    wuerfel2 = randint(1, 6)
    print("Die Würfel sind gefallen.")
    return [wuerfel1, wuerfel2]

def quadrat():
    setPenColor("green")
    repeat 4:
        fd(150)
        rt(90)

def zeichnePunkt(x, y):
    """Zeichnet einen einzelnen Punkt auf dem Würfel"""
    setPos(x, y)
    dot(20)

def zeichneWuerfel(x, y, augen):
    """Zeichnet einen Würfel mit der angegebenen Augenzahl"""
    setPos(x, y)
    quadrat()
    
    # Positionen der Punkte auf dem Würfel (verschoben nach rechts oben)
    punkte_pos = [
        (30, 120),   # Position 0 (oben links)
        (110, 120),    # Position 1 (oben rechts)
        (30, 80),    # Position 2 (mitte links)
        (70, 80),    # Position 3 (mitte mitte)
        (110, 80),     # Position 4 (mitte rechts)
        (30, 30),    # Position 5 (unten links)
        (110, 30)      # Position 6 (unten rechts)
    ]
    
    # Zeichne die Punkte basierend auf der Augenzahl
    setFillColor("black")
    for i in range(7):
        if augen[i] == 1:
            zeichnePunkt(x + punkte_pos[i][0], y + punkte_pos[i][1])

def zeichneWuerfelResultat(wuerfelLinks, wuerfelRechts):
    """Zeichnet zwei Würfel mit den angegebenen Augenzahlen"""
    zeichneWuerfel(-175, -75, augenZahlen[wuerfelLinks - 1])
    zeichneWuerfel(25, -75, augenZahlen[wuerfelRechts - 1])

def zeichnePunkte(punkte, x, y):
    """Zeigt die Punkte an der angegebenen Position an (rechts oben)"""
    setFontSize(30)
    setPos(x, y)
    label("Punkte: " + str(punkte))

def zeichneSumme(summe, x, y):
    """Zeigt die aktuelle Summe an der angegebenen Position an (rechts oben)"""
    setFontSize(25)
    setPos(x, y)
    label("Summe: " + str(summe))

def userSpielt():
    """Führt den Spielzug des Spielers aus"""
    print("")
    print("Spieler ist an der Reihe")
    punkte = 0
    letzte_summe = 0
    
    while True:
        links, rechts = wuerfeln()
        aktuelle_summe = links + rechts
        print("Es wurde " + str(links) + " und " + str(rechts) + " gewuerfelt.")
        print("Summe: " + str(aktuelle_summe))
        
        # Zeichne die Würfel und verschiebe Anzeige nach rechts oben
        clear()
        zeigeTeilB()
        zeichneWuerfelResultat(links, rechts)
        zeichnePunkte(punkte + 1, 200, 150)  # Rechts oben
        zeichneSumme(aktuelle_summe, 200, 120)  # Rechts oben
        
        # Prüfe ob die Summe mindestens so hoch ist wie die vorherige
        if punkte > 0 and aktuelle_summe < letzte_summe:
            print("Summe ist niedriger als vorher! 0 Punkte.")
            return 0
        
        punkte += 1
        
        if punkte == 1:
            # Erster Wurf - keine Bedingung
            letzte_summe = aktuelle_summe
            nochmals = input("Nochmals würfeln? (JA/NEIN): ")
            if nochmals.upper() != "JA":
                print("Spieler erhält " + str(punkte) + " Punkt(e).")
                return punkte
        else:
            # Weitere Würfe - Summe muss mindestens gleich bleiben
            if aktuelle_summe < letzte_summe:
                print("Summe ist niedriger als vorher! 0 Punkte.")
                return 0
            
            letzte_summe = aktuelle_summe
            nochmals = input("Nochmals würfeln? (JA/NEIN): ")
            if nochmals.upper() != "JA":
                print("Spieler erhält " + str(punkte) + " Punkt(e).")
                return punkte

def computerSpielt():
    """Führt den Spielzug des Computers aus"""
    print("")
    print("Computer ist an der Reihe")
    punkte = 0
    letzte_summe = 0
    
    while True:
        links, rechts = wuerfeln()
        aktuelle_summe = links + rechts
        print("Es wurde " + str(links) + " und " + str(rechts) + " gewuerfelt.")
        print("Summe: " + str(aktuelle_summe))
        
        # Zeichne die Würfel und verschiebe Anzeige nach rechts oben
        clear()
        zeigeTeilB()
        zeichneWuerfelResultat(links, rechts)
        zeichnePunkte(punkte + 1, 200, 150)  # Rechts oben
        zeichneSumme(aktuelle_summe, 200, 120)  # Rechts oben
        
        # Prüfe ob die Summe mindestens so hoch ist wie die vorherige
        if punkte > 0 and aktuelle_summe < letzte_summe:
            print("Summe ist niedriger als vorher! 0 Punkte.")
            return 0
        
        punkte += 1
        
        if punkte == 1:
            # Erster Wurf - keine Bedingung
            letzte_summe = aktuelle_summe
            # Computer entscheidet zufällig
            if randint(0, 1) == 0:
                print("Computer würfelt nochmals.")
                delay(2000)
            else:
                print("Computer hält bei " + str(punkte) + " Punkt(en).")
                return punkte
        else:
            # Weitere Würfe - Summe muss mindestens gleich bleiben
            if aktuelle_summe < letzte_summe:
                print("Summe ist niedriger als vorher! 0 Punkte.")
                return 0
            
            letzte_summe = aktuelle_summe
            # Computer entscheidet basierend auf Risiko
            if aktuelle_summe >= 10 and randint(0, 2) == 0:
                print("Computer hält bei " + str(punkte) + " Punkt(en).")
                return punkte
            elif aktuelle_summe >= 8 and randint(0, 1) == 0:
                print("Computer hält bei " + str(punkte) + " Punkt(en).")
                return punkte
            else:
                print("Computer würfelt nochmals.")
                delay(2000)

def resultateFuerTeilB(color, x, y):
    """Zeichnet die Hintergrundfelder für Teil B"""
    setPenColor(color)
    setFillColor(color)
    setPos(x, y)
    startPath()
    repeat 2:
        fd(400)
        rt(90)
        fd(95)
        rt(90)
    fillPath()

#--------------------------           
# Ab hier Hauptprogramm
#-------------------------- 

# Teil A - Startbildschirm mit 6 Würfeln (verschoben nach rechts oben)
def zeigeTeilA():
    """Zeigt die 6 möglichen Würfelzahlen zu Beginn"""
    clear()
    setFontSize(20)
    setPos(-200, 200)
    label("Würfelspiel - Die 6 möglichen Würfelzahlen")
    
   
    zeichneWuerfel(-240, 40, augenZahlen[0])
    zeichneWuerfel(-65, 40, augenZahlen[1])
    zeichneWuerfel(110, 40, augenZahlen[2])
    zeichneWuerfel(-240, -135, augenZahlen[3])
    zeichneWuerfel(-65, -135, augenZahlen[4])
    zeichneWuerfel(110, -135, augenZahlen[5])

    
    delay(3000)

# Teil B - Spielbereich
def zeigeTeilB():
    """Zeigt den Spielbereich mit Hintergrund"""
    resultateFuerTeilB("salmon", -300, -200)
    resultateFuerTeilB("maroon", 200, -200)

# Hauptspiel
def spieleSpiel():
    """Hauptfunktion zum Spielen des Würfelspiels"""
    # Zeige Startbildschirm
    zeigeTeilA()
    
    # Starte das Spiel
    clear()
    zeigeTeilB()
    
    # Spieler spielt
    punkteSpieler = userSpielt()
    
    # Computer spielt
    punkteComputer = computerSpielt()
    
    # Ergebnis anzeigen
    clear()
    setFontSize(40)
    setPos(-200, 0)
    
    print("")
    print("=== Endergebnis ===")
    print("Spieler: " + str(punkteSpieler) + " Punkte")
    print("Computer: " + str(punkteComputer) + " Punkte")
    
    if punkteSpieler > punkteComputer:
        label("Spieler gewinnt!")
        print("Spieler hat das Spiel gewonnen!")
    elif punkteComputer > punkteSpieler:
        label("Computer gewinnt!")
        print("Computer hat das Spiel gewonnen!")
    else:
        label("Unentschieden!")
        print("Das Spiel endet unentschieden!")

# Starte das Spiel
spieleSpiel()



