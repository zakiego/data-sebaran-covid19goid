#!/usr/bin/python3

from datetime import datetime
import requests as req
import pandas as pd

list_prov = ["DKI_JAKARTA",
             "JAWA_BARAT",
             "JAWA_TIMUR",
             "JAWA_TENGAH",
             "SULAWESI_SELATAN",
             "BANTEN",
             "NUSA_TENGGARA_BARAT",
             "BALI",
             "PAPUA",
             "KALIMANTAN_SELATAN",
             "SUMATERA_BARAT",
             "SUMATERA_SELATAN",
             "KALIMANTAN_TENGAH",
             "KALIMANTAN_TIMUR",
             "SUMATERA_UTARA",
             "DAERAH_ISTIMEWA_YOGYAKARTA",
             "KALIMANTAN_UTARA",
             "KEPULAUAN_RIAU",
             "KALIMANTAN_BARAT",
             "SULAWESI_TENGGARA",
             "LAMPUNG",
             "SULAWESI_UTARA",
             "SULAWESI_TENGAH",
             "RIAU",
             "PAPUA_BARAT",
             "SULAWESI_BARAT",
             "JAMBI",
             "MALUKU_UTARA",
             "MALUKU",
             "GORONTALO",
             "KEPULAUAN_BANGKA_BELITUNG",
             "ACEH",
             "BENGKULU",
             "NUSA_TENGGARA_TIMUR"]


def extract_data_provinsi(provinsi):
    resp = req.get(
        "https://data.covid19.go.id/public/api/prov_detail_"+provinsi+".json")
    resp = resp.json()["list_perkembangan"]
    data = pd.DataFrame(resp)
    data["tanggal"] = data.apply(
        lambda x: datetime.fromtimestamp(x["tanggal"]/1000), axis=1)
    name_file = "provinsi/" + provinsi + ".csv"
    data.to_csv(name_file, index=False)


for x in list_prov:
    extract_data_provinsi(x)
