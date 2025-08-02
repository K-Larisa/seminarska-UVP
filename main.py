import izlusci
import pridobi

globalna_stran_od = 1
globalna_stran_do = 5
#1000 = od 1 do 41, (40 strani × 25 = 1000 knjig)

#pridobi.shrani_podatke_o_knjigah(global_stran_od, global_stran_do)
print("konec")

seznam_id_knjig = izlusci.izlusci_id_knjige(globalna_stran_od, globalna_stran_do)
print("konec izlusci")
print(seznam_id_knjig)

pridobi.shrani_html_o_posamezni_knjigi(seznam_id_knjig)
