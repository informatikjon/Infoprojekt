from consolemenu import*                                #Console Menu Importieren
from consolemenu.items import*    
from Funktionen import Ausgabe_nach_ID
from Funktionen import Ausgabe_nach_Preis

main_menu = ConsoleMenu("htw Autokonfigurator", "Wählen Sie eine Option")

submenu1 = ConsoleMenu("Ausstattungsoptionen", "Wählen Sie eine Option")

submenu1_item1 = FunctionItem("Zeige alle Austattungsoptionen an", Ausgabe_nach_ID)
submenu1_item2 = FunctionItem("Zeige alle Austattungsoptionen nach Preis aufsteigend an", Ausgabe_nach_Preis)
submenu1.append_item(submenu1_item1)
submenu1.append_item(submenu1_item2)

main_menu.append_item(SubmenuItem("Austattungsoptionen", submenu1, main_menu))

main_menu.show()
