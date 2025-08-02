import requests
import os
import time


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

def shrani_podatke_o_knjigah(od, do):
    os.makedirs("knjige", exist_ok=True)
    for stran in range(od, do):
        odgovor = requests.get(f"https://www.gutenberg.org/ebooks/search/?sort_order=downloads&start_index={(stran - 1) * 25 + 1}",
                           headers=headers,
                           )
        if odgovor.status_code != 200:
            print("napaka", stran)
            continue
          

        with open(os.path.join("knjige", f"knjige{stran}.html"), "w", encoding="utf-8") as dat:  #nujno utf-8, ce ne ne zna zapisati datoteke, moti ga nek znak
            dat.write(odgovor.text)
        time.sleep(1)  #da ne obremeni streznika
    print("konec shrani_podatke_o_knjigah")


def shrani_html_o_posamezni_knjigi(knjige_glavno): #pobira ven iz seznama [(id, naslov), (id, naslov)...]
    for knjiga in knjige_glavno:
        id = knjiga[0]
        odgovor = requests.get(f"https://www.gutenberg.org/ebooks/{id}", headers=headers)
        if odgovor.status_code != 200:
            print("napaka", id)
            continue

        with open(os.path.join("knjige", f"knjige{id}.html"), "w", encoding="utf-8") as dat:
            dat.write(odgovor.text)
        time.sleep(1)