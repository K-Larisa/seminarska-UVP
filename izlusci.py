import requests
import os
from bs4 import BeautifulSoup
import re

#<a class="link" href="/ebooks/10215" accesskey="9">
#<span class="cell leftcell with-cover">
#<img class="cover-thumb" src="/cache/epub/10215/pg10215.cover.small.jpg" alt="">
#</span>
#<span class="cell content">
#<span class="title">Manfredo Palavicino, o, I Francesi e gli Sforzeschi: Storia Italiana (Italian)</span>
#<span class="subtitle">Giuseppe Rovani</span>
#<span class="extra">230 downloads</span>
#</span>

##############################
#za vsako search stran imamo html datoteko knjige1.html, kjige2.html... s podatki o knjigah
#odpremo vsak html, ga preberemo ter ven najdemo podatke o id ter naslovu
#vse skupah shranimo v seznam oblike [(id, naslov), (id, naslov), ...]

def izlusci_id_knjige(od, do):

    knjige_glavno = []
    for stran in range(od, do):
        with open(os.path.join("knjige", f"knjige{stran}.html"), "r", encoding="utf-8") as dat:
            knjiga = dat.read()
            soup = BeautifulSoup(knjiga, "html.parser")

            #za enkrat dobi id in naslov za eno knjigo
            #za vec : 
            for link in soup.find_all("a", class_="link"):
           #link = soup.find('a', class_='link') #delamo samo z enim linkom
                if link:
                    # ID iz href-a
                    href = link.get("href", "")
                    #if href.startswith('/ebooks/'): 
                    #    id_knjige = href.split('/ebooks/')[1]
                    if re.fullmatch(r"/ebooks/\d+", href):   #d+ rabi ker v prvih dveh straneh najde title, ki ni naslov knjige ampak nekaj s search
                        id_knjige = href.split("/")[2]

                        # Naslov iz <span class="title">
                        znacka_title = link.find("span", class_="title")
                        title = znacka_title.get_text(strip=True) if znacka_title else "" #odstrani vodilne in zaključne presledke (strip=True).
                        
                        knjige_glavno.append((id_knjige, title))
                        #print(f"stran {stran}  ID: {id_knjige}, Naslov: {title}")
    return(knjige_glavno)



def izlusci_ostale_podatke(knjige_glavno):
    podatki_o_knjigi = []
    for knjiga in knjige_glavno:
        id = knjiga[0]
        
        avtor = ""
        id_osebe = ""
        osebe = []
        naslov = ""
        jezik = ""
        st_prenosov = ""
        datum_objave = ""
        zanri = []
        id_zanra = ""
        ilustrator = ""
        prevajalec = ""
        tezavnost = ""
        

        with open(os.path.join("knjige", f"knjige{id}.html"), "r", encoding="utf-8") as dat:
            podatki = dat.read()
            soup = BeautifulSoup(podatki, "html.parser")

            tabela = soup.find_all("tr")
            for vrstica in tabela:
                th = vrstica.find("th")
                td = vrstica.find("td")
                if not th or not td:
                    continue

                geslo = th.text.strip()
                vsebina_celice = td.text.strip()

                if geslo == "Title":
                    naslov = vsebina_celice
                elif geslo == "Language":
                    jezik = vsebina_celice
                elif geslo == "Reading Level":
                    ujemanje = re.search(r'(\d+(\.\d+)?)', vsebina_celice)
                    tezavnost = ujemanje.group(1) if ujemanje else ""

                elif geslo == "Release Date":
                    leto = re.search(r'\b\d{4}\b', vsebina_celice)  #datum prej se z mesecem in dnevom
                    datum_objave = leto.group(0) if leto else ""

                elif geslo == "Downloads":
                    stevilo = re.search(r'\d+', vsebina_celice)
                    st_prenosov = int(stevilo.group(0)) if stevilo else 0
                # elif geslo == "Release Date":
                #     datum_objave = vsebina_celice
                # elif geslo == "Downloads":
                #     st_prenosov = vsebina_celice

                elif geslo == "Subject":
                    # zanri.append(vsebina_celice)
                    povezava = td.find("a")
                    ## spodnje ni bilo najboljše, ker so bili zapisi v obliki British -- Italy -- Fiction
                    if povezava: 
                       id_zanra = povezava["href"].split("/")[-1]
                       zanri.append((id_zanra, vsebina_celice)) 
                    # if povezava:
                    #     id_zanra = povezava["href"].split("/")[-1]
                    #     zapis_zanra = povezava.text.strip()
                        
                    #     seznam_zanrov = zapis_zanra.split("--")
                    #     for zanr in seznam_zanrov:
                    #         en_zanr = zanr.strip()
                    #         zanri.append((id_zanra, en_zanr))


                
                elif geslo == "Author":
                    avtor = vsebina_celice
                    povezava = td.find("a")
                    if povezava:
                        id_osebe = povezava["href"].split("/")[-1] 
                                            #[href] dobi ven vrednost kar je v href
                                            #primer <a href="/ebooks/author/7" ...
                                            #razdeli glede / in vzame zadnjega iz seznama(sifro)
                        osebe.append((id_osebe, avtor, "A"))

                elif geslo == "Illustrator":
                    ilustrator = vsebina_celice
                    povezava = td.find("a")
                    if povezava:
                        id_osebe = povezava["href"].split("/")[-1]
                        osebe.append((id_osebe, ilustrator, "I"))

                
                elif geslo == "Translator":
                    prevajalec = vsebina_celice
                    povezava = td.find("a")
                    if povezava:
                        id_osebe = povezava["href"].split("/")[-1]
                        osebe.append((id_osebe, prevajalec, "P"))
        
            podatki_o_knjigi.append(
                {
                    "id": id,
                    "naslov": naslov,
                    "osebe": osebe,
                    "jezik": jezik,
                    "zanri": zanri,
                    "datum objave": datum_objave,
                    "stevilo prenosov": st_prenosov,
                    "tezavnost": tezavnost
                }
                )
    return podatki_o_knjigi
 

#.text.strip() in .get_text(strip=True) za enostavne <span> deluje enako, za gnezdene elemente <span><b>Ime</b> <i>Avtor</i></span>
#pa je bolje .get..., saj zdruzi vse podelemente, pocisti presledke