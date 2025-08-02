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
def izlusci_id_knjige(od,do):
    

    #print("Trenutna delovna mapa:", os.getcwd())
    for stran in range(od, do):
        
        with open(os.path.join("knjige", f"knjige{stran}.html"), "r", encoding="utf-8") as dat:
            knjiga = dat.read()
            soup = BeautifulSoup(knjiga, "html.parser")

            #za enkrat dobi id in naslov za eno knjigo
            #za vec : 
            for link in soup.find_all('a', class_='link'):
           #link = soup.find('a', class_='link') #delamo samo z enim linkom
                if link:
                    # ID iz href-a
                    href = link.get('href', '')
                    #if href.startswith('/ebooks/'): 
                    #    id_knjige = href.split('/ebooks/')[1]
                    if re.fullmatch(r'/ebooks/\d+', href):   #d+ rabi ker v prvih dveh straneh najde title, ki ni naslov knjige ampak nekaj s search
                        id_knjige = href.split('/')[2]

                        # Naslov iz <span class="title">
                        znacka_title = link.find('span', class_='title')
                        title = znacka_title.get_text(strip=True) if znacka_title else ''

                        print(f"stran {stran}  ID: {id_knjige}, Naslov: {title}")



