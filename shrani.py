import csv

def shrani_knjige(knjige):
    with open("knjige.csv", "w", newline='', encoding='utf-8') as dat:

        pisatelj = csv.writer(dat, delimiter=";") #v excelu ti odpre z ;
        pisatelj.writerow(
            [
                "id knjige",
                "naslov",
                "jezik",
                "datum objave",
                "stevilo prenosov",
                "tezavnost",
            ]
        )
    
        for knjiga in knjige:
            
            pisatelj.writerow(
                [
                    knjiga["id"],
                    knjiga["naslov"],
                    knjiga["jezik"],
                    knjiga["datum objave"],
                    knjiga["stevilo prenosov"],
                    knjiga["tezavnost"],
                ]
            )


def shrani_osebe(knjige):
    with open("osebe.csv", "w", newline='', encoding='utf-8') as dat:
        pisatelj = csv.writer(dat, delimiter=";")
        pisatelj.writerow(
            [
                "id osebe",
                "oseba",
            ]
        )

        ze_dodan = set()
        for knjiga in knjige:
            for oseba in knjiga["osebe"]:
                if oseba[0] not in ze_dodan:
                    ze_dodan.add(oseba[0])

                    pisatelj.writerow(
                        [
                            oseba[0],
                            oseba[1],
                        ]
                    )

def shrani_zanre(knjige):
    with open("zanri.csv", "w", newline='', encoding='utf-8') as dat:
        pisatelj = csv.writer(dat, delimiter=";")
        pisatelj.writerow(
            [
                "id zanra",
                "zanr",
            ]
        )

        ze_dodan = set()
        for knjiga in knjige:
            for zanr in knjiga["zanri"]:
                if zanr[0] not in ze_dodan:
                    ze_dodan.add(zanr[0])

                    pisatelj.writerow(
                        [
                            zanr[0],
                            zanr[1],
                        ]
                    )

def povezava_osebe_knjige(knjige):
    with open("osebe_knjige.csv", "w", newline='', encoding='utf-8') as dat:
        pisatelj = csv.writer(dat, delimiter=";")
        pisatelj.writerow(
            [
                "id knjige",
                "id osebe",
                "vloga",
            ]
        )

        for knjiga in knjige:
            for oseba in knjiga["osebe"]:
                pisatelj.writerow([knjiga["id"], oseba[0], oseba[2]])




def povezava_zanri_knjige(knjige):
    with open("zanri_knjige.csv", "w", newline='', encoding='utf-8') as dat:
        pisatelj = csv.writer(dat, delimiter=";")
        pisatelj.writerow(
            [
                "id knjige",
                "id zanra",
            ]
        )

        for knjiga in knjige:
            for zanr in knjiga["zanri"]:
                pisatelj.writerow([knjiga["id"], zanr[0]])

