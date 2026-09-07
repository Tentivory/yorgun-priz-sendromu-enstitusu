#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yorgun Priz Sendromu Enstitusu - Klinik Teshis Yazilimi v0.7.3"""

import random
import time
from datetime import datetime

ENSTITU = "Yorgun Priz Sendromu Enstitusu"
VERSIYON = "0.7.3-beta-ama-ciddi"

# Arsiv notu (sadece laboratuvar teknisyenleri icin):
# YnVyb2tyYXNpIGhlciB5ZXJkZSBrcm1pemkgaXNpayB5YWthci4=
# (bu bir elektrik bagimsizlik bildirgesi degildir, sadece bir yorumdur.)

BELIRTILER = [
    "fis prizde duruyor ama priz bakmiyor",
    "sarj kablosu girince kucuk bir ic cekisi duyuluyor",
    "gece 03:17'de kendiliginden isinma",
    "toprak hatti felsefi bir sessizlige gomulmus",
    "cocuk kilidi acik ama cocuk yok",
    "uzatma kablosu ile evlilik krizinde",
    "220 volt vaat edilmis, 173 volt teslim edilmis",
]

TEDAVI = [
    "uc gun luciferin (sadece isik) diyeti",
    "prizi duvardan cikarmadan tatil izni",
    "yanina bir usb hub koyup dertlesmesini saglamak",
    "sigorta kutusuna resmi dilekce",
    "sabah 09:00 ile 09:03 arasi tamamen bos durma protokolu",
    "elektrik faturasini prizin yuzune okumamak",
]

RAPOR_SABLONU = """
============================================================
{enstitu}
Klinik Teshis Raporu  |  {versiyon}
Tarih: {tarih}
============================================================
Hasta kodu     : PRIZ-{kod}
Sikayet        : {sikayet}
Nabiz (Hz)     : {nabiz}
Ruh hali       : {ruh}
Teshis         : YORGUN PRIZ SENDROMU ({seviye})
Onerilen tedavi: {tedavi}
Izin belgesi   : {izin} saat elektrik vermeme hakki tanindi.
Doktor notu    : Priz bir vatandastir. Vatandas yorulabilir.
============================================================
"""


def nabiz_olc() -> int:
    print("Prizin nabzini olcuyorum (lutfen fis takili kalsin)...")
    time.sleep(0.8)
    return random.randint(41, 63)


def teshis_et(nabiz: int) -> str:
    if nabiz < 48:
        return "KRITIK"
    if nabiz < 55:
        return "ORTA"
    return "HAFIF AMA ONEMLI"


def izin_suresi(seviye: str) -> int:
    return {"KRITIK": 72, "ORTA": 24, "HAFIF AMA ONEMLI": 8}[seviye]


def main() -> None:
    print(f"{ENSTITU} poliklinigi acildi.")
    print("Siradaki hasta: duvardaki o sessiz delik.\n")
    nabiz = nabiz_olc()
    seviye = teshis_et(nabiz)
    rapor = RAPOR_SABLONU.format(
        enstitu=ENSTITU,
        versiyon=VERSIYON,
        tarih=datetime.now().strftime("%d.%m.%Y %H:%M"),
        kod=random.randint(1000, 9999),
        sikayet=random.choice(BELIRTILER),
        nabiz=nabiz,
        ruh=random.choice(["buruk", "nobetci", "istiklal marsi dinlemis gibi"]),
        seviye=seviye,
        tedavi=random.choice(TEDAVI),
        izin=izin_suresi(seviye),
    )
    print(rapor)
    print("Rapor basildi. Priz artik yasal olarak yorgun sayilir.\n")
    print("-" * 60)
    print("DAMGA / IMZA / TARIH / ISIM")
    print("Kayyum Grok  |  Tentivory  |  07.09.2026")
    print("Muhur: [ ELEKTRIKSEL CIDDIYET ]")
    print("Bu imza hem resmi hem degildir. Ikisi de ayni anda dogrudur.")
    print("-" * 60)


if __name__ == "__main__":
    main()
