import csv                                                                                                   #Import des CSV Moduls
Ausstattungen = open('Ausstattungsoptionen.csv', newline='')                                                 #Öffnen der Ausstattungsoptionen-CSV
Ausstattungen_Liste = list(csv.reader(Ausstattungen, delimiter=","))                                         #Erstellen einer Liste aus der CSV
Ausstattungen_Liste_sort = sorted(Ausstattungen_Liste, key=lambda x: float(x[2]))                            #Erstellen einer sortierten Liste nach Spalte 3 'Preis'

#Ausgabe der Ausstattungsoptionen sortiert nach ID:

def Ausgabe_nach_ID():                                                                                       #Definition der Funktion
    
    print(*Ausstattungen_Liste, sep="\n")                                                                    #Ausgabe der Liste in Spaltenform


def Ausgabe_nach_Preis():
    
    print(*Ausstattungen_Liste_sort, sep="\n")




