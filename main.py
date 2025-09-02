import izlusci
import pridobi
import shrani

globalna_stran_od = 1
globalna_stran_do = 41     #(40 strani × 25 = 1000 knjig)

#pridobi.shrani_podatke_o_knjigah(globalna_stran_od, globalna_stran_do)

seznam_id_knjig = izlusci.izlusci_id_knjige(globalna_stran_od, globalna_stran_do)


#pridobi.shrani_html_o_posamezni_knjigi(seznam_id_knjig)
podatki = izlusci.izlusci_ostale_podatke(seznam_id_knjig)


shrani.shrani_knjige(podatki)
shrani.shrani_osebe(podatki)
shrani.shrani_zanre(podatki)
shrani.povezava_zanri_knjige(podatki)
shrani.povezava_osebe_knjige(podatki)
