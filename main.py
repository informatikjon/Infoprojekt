### Main Python Datei für das Infoprojekt ###



# Importieren des Konfiguratordialogs
import Konfiguratordialog as Kd

# Importieren der benötigten Module
import pandas as pd # Pandas für das Einlesen der csv-Datei

# Einlesen der csv-Datei
df = pd.read_csv('Infoprojekt\data.csv')

#df zu multidimensionalarray
data = df.values.tolist()
# Funktion für den Konfiguartionsdialog

Kd.HauptDialog()

for i in data:
    print(i[1])