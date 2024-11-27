
import tkinter as tk
#Tento riadok importuje modul `tkinter` a priradzuje mu skratku `tk`. Modul `tkinter` poskytuje nástroje na vytváranie grafického uívate¾ského rozhrania.

from tkinter import filedialog
#Tento riadok importuje konkrétnu funkciu `filedialog` z modulu `tkinter`. Táto funkcia poskytuje dialógové okná pre prácu so súbormi (napríklad otváranie, ukladanie súborov).

import pandas as pd
#Tento riadok importuje modul `pandas` a priradzuje mu skratku `pd`. Modul `pandas` poskytuje vysokoúrovòové dátové štruktúry a nástroje na analızu a manipuláciu s dátami.

def vypocitat_priemer():
#Tımto riadkom zaèína definícia funkcie `vypocitat_priemer()`. Táto funkcia bude vypoèítava priemer hodnôt známok na základe vstupnıch hodnôt zo vstupnıch polí.

meno = entry_meno.get()
#Tento riadok získava vstupnú hodnotu z textového po¾a `entry_meno` (ktoré obsahuje meno študenta) a ukladá ju do premennej `meno`.

if not meno:
    label_vysledok.config(text="Chyba: Zadajte meno študenta.")
    return
#Tento blok kódu overuje, èi je premenná `meno` prázdna. Ak je prázdna, znamená to, e študent nezadal meno, a v tom prípade sa na štandardnı vıstupovı label `label_vysledok` zobrazí chybová správa "Chyba: Zadajte meno študenta." a funkcia sa ukonèí pomocou `return`, èím sa zastaví ïalšie vykonávanie funkcie.

BP = entry_bp.get().upper()
GEO = entry_geo.get().upper()
GNS = entry_gns.get().upper()
PA = entry_pa.get().upper()
#Tieto riadky získavajú vstupné hodnoty z textovıch polí `entry_bp`, `entry_geo`, `entry_gns` a `entry_pa` (ktoré obsahujú známky) a ukladajú ich do premennıch `BP`, `GEO`, `GNS` a `PA` po prevedení na ve¾ké písmená pomocou metódy `upper()`. Tım sa zabezpeèí jednotnı formát zadanıch známok.

while BP not in hodnoty and BP != '':
    entry_bp.delete(0, tk.END)
    entry_bp.insert(tk.END, "Neplatná znamka. Zadajte znova

.")
    return
#Tento blok kódu overuje, èi zadaná hodnota `BP` je platnou známkou. Pokia¾ nie je, odstráni sa obsah z textového po¾a `entry_bp`, vloí sa chybová správa "Neplatná znamka. Zadajte znova." a funkcia sa ukonèí.
#Podobnı blok kódu sa opakuje pre premenné `GEO`, `GNS` a `PA` s príslušnımi textovımi poliami.

BP = hodnoty.get(BP, None)
GEO = hodnoty.get(GEO, None)
GNS = hodnoty.get(GNS, None)
PA = hodnoty.get(PA, None)
#Tieto riadky mapujú hodnoty známok (`BP`, `GEO`, `GNS`, `PA`) na ich ekvivalentné numerické hodnoty pomocou slovníka `hodnoty`. Ak zadaná hodnota nie je v slovníku, pouije sa hodnota `None`.

hodnoty_list = [BP, GEO, GNS, PA]
hodnoty_list = [hodnota for hodnota in hodnoty_list if hodnota is not None]
#Tieto riadky vytvárajú zoznam `hodnoty_list`, ktorı obsahuje numerické hodnoty známok (`BP`, `GEO`, `GNS`, `PA`), prièom sa odstráni všetky hodnoty `None` z tohto zoznamu.

priemer = sum(hodnoty_list) / len(hodnoty_list) if hodnoty_list else 0
#Tento riadok vypoèíta priemer hodnôt v zozname `hodnoty_list`. Ak je zoznam prázdny (neobsahuje iadne hodnoty), priemer sa nastaví na hodnotu 0.

if "FX" in hodnoty_list:
    vysledok = "Nedostatoène"
elif priemer <= 1.5 and hodnoty_list.count("C") <= 1 and not any(hodnota in ["D", "E"] for hodnota in hodnoty_list):
    vysledok = "Vıborne"
else:
    vysledok = "Vyhovel(a)"
#Tento blok kódu urèuje vısledok hodnotenia na základe priemeru a hodnôt známok. Ak sa v zozname `hodnoty_list` nachádza hodnota "FX", vısledkom je "Nedostatoène". Ak je priemer menší alebo rovnı 1.5, obsahuje najviac jednu hodnotu "C" a neobsahuje iadnu hodnotu "D" ani "E", vısledkom je "Vıborne". V opaènom prípade je vısledkom "Vyhovel(a)".

label_priemer.config(text="Priemer známok: {:.2f}".format(priemer))
label_hodnotenie.config(text="Hodnotenie: " + vysledok)
#Tieto riadky nastavujú textové hodnoty pre labely `label_priemer` a `label_hodnotenie`. V `label_priemer` sa zobrazí hodnota priemeru známok s presnosou na dve desatinné miesta. V `label_hodnotenie` sa zobrazí vısledok hodnotenia.

def export_do_excelu():
#Tımto riadkom zaèína definícia funkcie `export_do_excelu()`. Táto funkcia bude exportova údaje do Excelu.

meno = entry_meno.get()
vstup_bp = entry_bp.get()
vstup_geo = entry_geo.get()
vstup_gns = entry_gns.get()
vstup_pa = entry_pa.get()
priemer = label_priemer["text"].split(": ")[1]
hodnotenie = label_hodnotenie["text"].split(": ")[1]
#Tieto riadky získavajú hodnoty z textovıch polí (`entry_meno`, `entry_bp`, `entry_geo`, `entry_gns`, `entry_pa`) a z labelov (`label_priemer`, `label_hodnotenie`) a ukladajú ich do príslušnıch premennıch (`meno`, `vstup_bp`, `vstup_geo`, `vstup_gns`, `vstup_pa`, `priemer`, `hodnotenie`).

data = {
    "Meno a priezvisko": [meno],
    "Bakalárska práca a jej obhajoba": [vstup_bp],
    "Geodézia": [vstup_geo],
    "Globálne geodetické systémy": [vstup_gns],
    "Priestorová analıza": [vstup_pa],
    "Priemer": [priemer],
    "Hodnotenie": [hodnotenie]
}
#Tento riadok vytvára slovník `data`, kde k¾úèami sú názvy ståpcov a hodnotami sú zoznamy s príslušnımi hodnotami (`meno`, `vstup_bp`, `vstup_geo`, `vstup_gns`, `vstup_pa`, `priemer`, `hodnotenie`).

df = pd.DataFrame(data)
#Tento riadok vytvára dátovı rámec (`DataFrame`) `df` z údajov v slovníku `data` pomocou modulu `pandas`.


file_path = filedialog.asksaveasfilename(defaultextension=".xlsx")
if file_path:
    df.to_excel(file_path, index=False)
    label_export.config(text="Export do Excelu dokonèenı.")
#Tieto riadky otvárajú dialógové okno pre ukladanie súboru pomocou funkcie `asksaveasfilename` z modulu `filedialog`. Ak je vybranı súbor a bol zadanı názov, dátovı rámec `df` sa exportuje do Excelu s pouitím funkcie `to_excel`, prièom sa nastaví cesta k
#súboru `file_path` a vypíše sa správa "Export do Excelu dokonèenı" na label `label_export`.


window = tk.Tk()
#Tento riadok vytvára hlavné okno aplikácie pomocou konštruktora `Tk` z modulu `tkinter`.


window.title("Hodnotenie študenta")
#Tento riadok nastavuje titulok hlavného okna na "Hodnotenie študenta".

label_meno = tk.Label(window, text="Meno študenta:")
#Tento riadok vytvára label `label_meno` v hlavnom okne s textom "Meno študenta:".


entry_meno = tk.Entry(window)

#Tento riadok vytvára textové pole `entry_meno` v hlavnom okne, do ktorého môe študent zada svoje meno.
#Podobne sa postupuje aj pre labely a textové polia pre hodnoty známok `BP`, `GEO`, `GNS` a `PA`.


button_priemer = tk.Button(window, text="Vypoèíta priemer", command=vypocitat_priemer)
#Tento riadok vytvára tlaèidlo `button_priemer` s textom "Vypoèíta priemer" v hlavnom okne. Toto tlaèidlo spúša funkciu `vypocitat_priemer` po kliknutí.


button_export = tk.Button(window, text="Exportova do Excelu", command=export_do_excelu)
#Tento riadok vytvára tlaèidlo `button_export` s textom "Exportova do Excelu" v hlavnom okne. Toto tlaèidlo spúša funkciu `export_do_excelu` po kliknutí.


label_priemer = tk.Label(window, text="Priemer známok:")
#Tento riadok vytvára label `label_priemer` v hlavnom okne s textom "Priemer známok:".


label_hodnotenie = tk.Label(window, text="Hodnotenie:")
#Tento riadok vytvára label `label_hodnotenie` v hlavnom okne s textom "Hodnotenie:".


label_export = tk.Label(window, text="")
#Tento riadok vytvára label `label_export` v hlavnom okne s prázdny textom.


label_meno.grid(row=0, column=0, sticky=tk.W)
entry_meno.grid(row=0, column=1)
#Tieto riadky umiestòujú label `label_meno` a textové pole `entry_meno` na prvı riadok a prvé dve ståpce hlavného okna. `sticky=tk.W` znamená, e label a textové pole budú zarovnané v¾avo.
#Podobne sa postupuje aj pre labely a textové polia pre hodnoty známok `BP`, `GEO`, `GNS` a  `PA`.


button_priemer.grid(row=5, column=0, columnspan=2)
button_export.grid(row=6, column=0, columnspan=2)
#Tieto riadky umiestòujú tlaèidlá `button_priemer` a `button_export` na piaty a šiesty riadok a do oboch ståpcov hlavného okna. `columnspan=2` znamená, e tlaèidlá rozpínajú cez oba ståpce.


label_priemer.grid(row=7, column=0, sticky=tk.W)
label_hodnotenie.grid(row=8, column=0, sticky=tk.W)
label_export.grid(row=9, column=0, columnspan=2)
#Tieto riadky umiestòujú labely `label_priemer`, `label_hodnotenie` a `label_export` na siedmy, ôsmy a deviaty riadok a do prvıch dvoch ståpcov hlavného okna.


window.mainloop()
#Tento riadok spúša hlavnú smyèku aplikácie, ktorá èaká na udalosti a reaguje na ne, ako sú kliknutia na tlaèidlá alebo zmeny vstupov.