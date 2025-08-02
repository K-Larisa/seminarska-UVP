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
    #print("Trenutna delovna mapa:", os.getcwd())

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
                        print(f"stran {stran}  ID: {id_knjige}, Naslov: {title}")
    return(knjige_glavno)



def izlusci_ostale_podatke(knjige_glavno):
    for knjiga in knjige_glavno:
        id = knjiga[0]

        avtor = ""
        jezik = ""
        st_prenosov = ""
        datum_objave = ""
        zanr = ""


        with open(os.path.join("knjige", f"knjige{id}.html"), "r", encoding="utf-8") as dat:
            podatki = dat.read()
            soup = BeautifulSoup(podatki, "html.parser")

        avtor = knjiga.find("span", class_="subtitle")
        avtor = avtor.get_text(strip=True) if avtor else ""





#.text.strip() in .get_text(strip=True) za enostavne <span> deluje enako, za gnezdene elemente <span><b>Ime</b> <i>Avtor</i></span>
#pa je bolje .get..., saj zdruzi vse podelemente, pocisti presledke