# Seminarska-UVP

## Uvod
Za seminarsko nalogo pri predmetu Uvod v programiranje sem podatke črpala iz spletne strani Project Gutenberg, dostopne na https://www.gutenberg.org/. Na tej spletni strani je na voljo več kot 75 000 zastonj knjig v elektronski obliki, ki se jih lahko prenese kot HTML, EPUB, PDF, MOBI in druge. Za vsako knjigo lahko najdemo podatke o avtorjih, včasih tudi prevajalcih in ilustratorjih, jeziku, težavnosti knjige, žanrih, datumu objave, številu prenosov v zadnjih 30 dneh... Vsaka knjiga, avtor, prevajalec in ilustrator so označeni s svojo številko, kar je uporabno zlasti kasneje pri obdelavi podatkov.

## Navodila za uporabo programa
Glavna datoteka, s katero lahko uporabnik zažene program, je **main.py**. V njej najdemo na začetku dve spremenljivki: globalna_stra_od in globalna_stran_do. Njuni vrednosti sta nastavljeni tako, da bo program zajel podatke o 1000 različnih knjigah. Če želimo spremeniti število podatkov, ki jih bo program zajemal in obdeloval, spremenimo vrednosti, pri čemer upostevamo, da ima ena stran dostop do 25 različnih knjig. V primeru, da želi uporabnik zagnati program od čistega začetka ter spremljati postopek izvajanja, mora odkomentrirati dve vrstici, ki se začneta z " #pridobi.shrani...". Ta dva ukaza za vsako posamezno stran in knjigo naredita in shranita HTML datoteko s podatki o knjigah. Ker je to zamuden in dolgotrajen proces, ju raje pustimo zakomentirana. Ko se program izvede do konca, nam ustvari pet različnih CSV datotek, ki jih lahko odpremo z Excelom. Podatke smo torej zajeli in shranili.

## Analiza podatkov
Datoteka **analiza_podatkov.ipnyb* vsebuje tabele in grafe, ter analizo pridobljenih podatkov (naštetih v uvodu), pri čemer le-te jemlje iz prej omenjenih novo nastalih datotek.





Pripravila Larisa Klement, avgust 2025
