import requests
import os
from bs4 import BeautifulSoup
import re


def izlusci_id_knjige(od, do):

    knjige_glavno = []
    for stran in range(od, do):
        with open(os.path.join("knjige", f"knjige{stran}.html"), "r", encoding="utf-8") as dat:
            knjiga = dat.read()
            soup = BeautifulSoup(knjiga, "html.parser")

            for link in soup.find_all("a", class_="link"):
                if link:
                    # ID iz href-a
                    href = link.get("href", "")
                    if re.fullmatch(r"/ebooks/\d+", href):
                        id_knjige = href.split("/")[2]

                        # Naslov iz <span class="title">
                        znacka_title = link.find("span", class_="title")
                        title = znacka_title.get_text(strip=True) if znacka_title else ""
                        knjige_glavno.append((id_knjige, title))

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
                    leto = re.search(r'\b\d{4}\b', vsebina_celice)
                    datum_objave = leto.group(0) if leto else ""

                elif geslo == "Downloads":
                    stevilo = re.search(r'\d+', vsebina_celice)
                    st_prenosov = int(stevilo.group(0)) if stevilo else 0


                elif geslo == "Subject":
                    povezava = td.find("a")
                    if povezava: 
                       id_zanra = povezava["href"].split("/")[-1]
                       zanri.append((id_zanra, vsebina_celice)) 
                
                elif geslo == "Author":
                    avtor = vsebina_celice
                    povezava = td.find("a")
                    if povezava:
                        id_osebe = povezava["href"].split("/")[-1] 
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
