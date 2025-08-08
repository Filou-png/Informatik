# ------------------------------------
# Algorithmus: Merge List
# ------------------------------------

# Funktion mergeList()
def mergeList(liste_a, liste_b):
    
    #schritte = 0
    
    # neue zusammengeführte Liste
    liste = []
    
    # -------- Ab hier eigener Code --------    

    # Während in beiden Elementen noch Listen vorhanden
    while len(liste_a) != 0 and len(liste_b) != 0:
        
        # Kleineres Element der neuen Liste anfügen und in der ursprünglichen Liste löschen
        if liste_a[0] <= liste_b[0]:
            liste.append(liste_a[0])
            del liste_a[0]
        else:
            liste.append(liste_b[0])
            del liste_b[0]
        #schritte += 1
    
    # Restliche Elemente der Liste A anfügen (wenn Liste B leer ist)
    while len(liste_a) != 0:
        liste.append(liste_a[0])
        del liste_a[0]
        #schritte += 1

    # Restliche Elemente der Liste B anfügen (wenn Liste A leer ist)
    while len(liste_b) != 0:
        liste.append(liste_b[0])
        del liste_b[0]
        #schritte += 1
        
    # -------- Ende eigener Code --------
    
    #print (schritte)
    return (liste)


# Hauptprogramm / Funktionsaufruf
stapel1 = [4, 7, 8, 12, 13, 22, 29, 41]
stapel2 = [1, 6, 10, 25, 26, 33, 53, 59]
maedchen = ["Anna", "Barbara", "Claudia", "Emilia", "Luisa", "Nina", "Olivia", "Sarah", "Zoe"]
knaben = ["Ben", "Erich", "Marco", "Thomas", "Tim", "Timo", "Yannick"]

neuerStapel = mergeList(stapel1, stapel2)
schueler = mergeList(maedchen, knaben)

print(neuerStapel)
print(schueler)