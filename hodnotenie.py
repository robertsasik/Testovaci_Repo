
import tkinter as tk
#Tento riadok importuje modul `tkinter` a priradzuje mu skratku `tk`. Modul `tkinter` poskytuje n�stroje na vytv�ranie grafick�ho u��vate�sk�ho rozhrania.

from tkinter import filedialog
#Tento riadok importuje konkr�tnu funkciu `filedialog` z modulu `tkinter`. T�to funkcia poskytuje dial�gov� okn� pre pr�cu so s�bormi (napr�klad otv�ranie, ukladanie s�borov).

import pandas as pd
#Tento riadok importuje modul `pandas` a priradzuje mu skratku `pd`. Modul `pandas` poskytuje vysoko�rov�ov� d�tov� �trukt�ry a n�stroje na anal�zu a manipul�ciu s d�tami.

def vypocitat_priemer():
#T�mto riadkom za��na defin�cia funkcie `vypocitat_priemer()`. T�to funkcia bude vypo��tava� priemer hodn�t zn�mok na z�klade vstupn�ch hodn�t zo vstupn�ch pol�.

meno = entry_meno.get()
#Tento riadok z�skava vstupn� hodnotu z textov�ho po�a `entry_meno` (ktor� obsahuje meno �tudenta) a uklad� ju do premennej `meno`.

if not meno:
    label_vysledok.config(text="Chyba: Zadajte meno �tudenta.")
    return
#Tento blok k�du overuje, �i je premenn� `meno` pr�zdna. Ak je pr�zdna, znamen� to, �e �tudent nezadal meno, a v tom pr�pade sa na �tandardn� v�stupov� label `label_vysledok` zobraz� chybov� spr�va "Chyba: Zadajte meno �tudenta." a funkcia sa ukon�� pomocou `return`, ��m sa zastav� �al�ie vykon�vanie funkcie.

BP = entry_bp.get().upper()
GEO = entry_geo.get().upper()
GNS = entry_gns.get().upper()
PA = entry_pa.get().upper()
#Tieto riadky z�skavaj� vstupn� hodnoty z textov�ch pol� `entry_bp`, `entry_geo`, `entry_gns` a `entry_pa` (ktor� obsahuj� zn�mky) a ukladaj� ich do premenn�ch `BP`, `GEO`, `GNS` a `PA` po preveden� na ve�k� p�smen� pomocou met�dy `upper()`. T�m sa zabezpe�� jednotn� form�t zadan�ch zn�mok.

while BP not in hodnoty and BP != '':
    entry_bp.delete(0, tk.END)
    entry_bp.insert(tk.END, "Neplatn� znamka. Zadajte znova

.")
    return
#Tento blok k�du overuje, �i zadan� hodnota `BP` je platnou zn�mkou. Pokia� nie je, odstr�ni sa obsah z textov�ho po�a `entry_bp`, vlo�� sa chybov� spr�va "Neplatn� znamka. Zadajte znova." a funkcia sa ukon��.
#Podobn� blok k�du sa opakuje pre premenn� `GEO`, `GNS` a `PA` s pr�slu�n�mi textov�mi poliami.

BP = hodnoty.get(BP, None)
GEO = hodnoty.get(GEO, None)
GNS = hodnoty.get(GNS, None)
PA = hodnoty.get(PA, None)
#Tieto riadky mapuj� hodnoty zn�mok (`BP`, `GEO`, `GNS`, `PA`) na ich ekvivalentn� numerick� hodnoty pomocou slovn�ka `hodnoty`. Ak zadan� hodnota nie je v slovn�ku, pou�ije sa hodnota `None`.

hodnoty_list = [BP, GEO, GNS, PA]
hodnoty_list = [hodnota for hodnota in hodnoty_list if hodnota is not None]
#Tieto riadky vytv�raj� zoznam `hodnoty_list`, ktor� obsahuje numerick� hodnoty zn�mok (`BP`, `GEO`, `GNS`, `PA`), pri�om sa odstr�ni v�etky hodnoty `None` z tohto zoznamu.

priemer = sum(hodnoty_list) / len(hodnoty_list) if hodnoty_list else 0
#Tento riadok vypo��ta priemer hodn�t v zozname `hodnoty_list`. Ak je zoznam pr�zdny (neobsahuje �iadne hodnoty), priemer sa nastav� na hodnotu 0.

if "FX" in hodnoty_list:
    vysledok = "Nedostato�ne"
elif priemer <= 1.5 and hodnoty_list.count("C") <= 1 and not any(hodnota in ["D", "E"] for hodnota in hodnoty_list):
    vysledok = "V�borne"
else:
    vysledok = "Vyhovel(a)"
#Tento blok k�du ur�uje v�sledok hodnotenia na z�klade priemeru a hodn�t zn�mok. Ak sa v zozname `hodnoty_list` nach�dza hodnota "FX", v�sledkom je "Nedostato�ne". Ak je priemer men�� alebo rovn� 1.5, obsahuje najviac jednu hodnotu "C" a neobsahuje �iadnu hodnotu "D" ani "E", v�sledkom je "V�borne". V opa�nom pr�pade je v�sledkom "Vyhovel(a)".

label_priemer.config(text="Priemer zn�mok: {:.2f}".format(priemer))
label_hodnotenie.config(text="Hodnotenie: " + vysledok)
#Tieto riadky nastavuj� textov� hodnoty pre labely `label_priemer` a `label_hodnotenie`. V `label_priemer` sa zobraz� hodnota priemeru zn�mok s presnos�ou na dve desatinn� miesta. V `label_hodnotenie` sa zobraz� v�sledok hodnotenia.

def export_do_excelu():
#T�mto riadkom za��na defin�cia funkcie `export_do_excelu()`. T�to funkcia bude exportova� �daje do Excelu.

meno = entry_meno.get()
vstup_bp = entry_bp.get()
vstup_geo = entry_geo.get()
vstup_gns = entry_gns.get()
vstup_pa = entry_pa.get()
priemer = label_priemer["text"].split(": ")[1]
hodnotenie = label_hodnotenie["text"].split(": ")[1]
#Tieto riadky z�skavaj� hodnoty z textov�ch pol� (`entry_meno`, `entry_bp`, `entry_geo`, `entry_gns`, `entry_pa`) a z labelov (`label_priemer`, `label_hodnotenie`) a ukladaj� ich do pr�slu�n�ch premenn�ch (`meno`, `vstup_bp`, `vstup_geo`, `vstup_gns`, `vstup_pa`, `priemer`, `hodnotenie`).

data = {
    "Meno a priezvisko": [meno],
    "Bakal�rska pr�ca a jej obhajoba": [vstup_bp],
    "Geod�zia": [vstup_geo],
    "Glob�lne geodetick� syst�my": [vstup_gns],
    "Priestorov� anal�za": [vstup_pa],
    "Priemer": [priemer],
    "Hodnotenie": [hodnotenie]
}
#Tento riadok vytv�ra slovn�k `data`, kde k���ami s� n�zvy st�pcov a hodnotami s� zoznamy s pr�slu�n�mi hodnotami (`meno`, `vstup_bp`, `vstup_geo`, `vstup_gns`, `vstup_pa`, `priemer`, `hodnotenie`).

df = pd.DataFrame(data)
#Tento riadok vytv�ra d�tov� r�mec (`DataFrame`) `df` z �dajov v slovn�ku `data` pomocou modulu `pandas`.


file_path = filedialog.asksaveasfilename(defaultextension=".xlsx")
if file_path:
    df.to_excel(file_path, index=False)
    label_export.config(text="Export do Excelu dokon�en�.")
#Tieto riadky otv�raj� dial�gov� okno pre ukladanie s�boru pomocou funkcie `asksaveasfilename` z modulu `filedialog`. Ak je vybran� s�bor a bol zadan� n�zov, d�tov� r�mec `df` sa exportuje do Excelu s pou�it�m funkcie `to_excel`, pri�om sa nastav� cesta k
#s�boru `file_path` a vyp�e sa spr�va "Export do Excelu dokon�en�" na label `label_export`.


window = tk.Tk()
#Tento riadok vytv�ra hlavn� okno aplik�cie pomocou kon�truktora `Tk` z modulu `tkinter`.


window.title("Hodnotenie �tudenta")
#Tento riadok nastavuje titulok hlavn�ho okna na "Hodnotenie �tudenta".

label_meno = tk.Label(window, text="Meno �tudenta:")
#Tento riadok vytv�ra label `label_meno` v hlavnom okne s textom "Meno �tudenta:".


entry_meno = tk.Entry(window)

#Tento riadok vytv�ra textov� pole `entry_meno` v hlavnom okne, do ktor�ho m��e �tudent zada� svoje meno.
#Podobne sa postupuje aj pre labely a textov� polia pre hodnoty zn�mok `BP`, `GEO`, `GNS` a `PA`.


button_priemer = tk.Button(window, text="Vypo��ta� priemer", command=vypocitat_priemer)
#Tento riadok vytv�ra tla�idlo `button_priemer` s textom "Vypo��ta� priemer" v hlavnom okne. Toto tla�idlo sp���a funkciu `vypocitat_priemer` po kliknut�.


button_export = tk.Button(window, text="Exportova� do Excelu", command=export_do_excelu)
#Tento riadok vytv�ra tla�idlo `button_export` s textom "Exportova� do Excelu" v hlavnom okne. Toto tla�idlo sp���a funkciu `export_do_excelu` po kliknut�.


label_priemer = tk.Label(window, text="Priemer zn�mok:")
#Tento riadok vytv�ra label `label_priemer` v hlavnom okne s textom "Priemer zn�mok:".


label_hodnotenie = tk.Label(window, text="Hodnotenie:")
#Tento riadok vytv�ra label `label_hodnotenie` v hlavnom okne s textom "Hodnotenie:".


label_export = tk.Label(window, text="")
#Tento riadok vytv�ra label `label_export` v hlavnom okne s pr�zdny textom.


label_meno.grid(row=0, column=0, sticky=tk.W)
entry_meno.grid(row=0, column=1)
#Tieto riadky umiest�uj� label `label_meno` a textov� pole `entry_meno` na prv� riadok a prv� dve st�pce hlavn�ho okna. `sticky=tk.W` znamen�, �e label a textov� pole bud� zarovnan� v�avo.
#Podobne sa postupuje aj pre labely a textov� polia pre hodnoty zn�mok `BP`, `GEO`, `GNS` a  `PA`.


button_priemer.grid(row=5, column=0, columnspan=2)
button_export.grid(row=6, column=0, columnspan=2)
#Tieto riadky umiest�uj� tla�idl� `button_priemer` a `button_export` na piaty a �iesty riadok a do oboch st�pcov hlavn�ho okna. `columnspan=2` znamen�, �e tla�idl� rozp�naj� cez oba st�pce.


label_priemer.grid(row=7, column=0, sticky=tk.W)
label_hodnotenie.grid(row=8, column=0, sticky=tk.W)
label_export.grid(row=9, column=0, columnspan=2)
#Tieto riadky umiest�uj� labely `label_priemer`, `label_hodnotenie` a `label_export` na siedmy, �smy a deviaty riadok a do prv�ch dvoch st�pcov hlavn�ho okna.


window.mainloop()
#Tento riadok sp���a hlavn� smy�ku aplik�cie, ktor� �ak� na udalosti a reaguje na ne, ako s� kliknutia na tla�idl� alebo zmeny vstupov.