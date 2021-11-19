#!/usr/bin/python3

import requests as req
import pandas as pd
import operator

resp = req.get(
    "https://data.covid19.go.id/public/api/pemeriksaan-vaksinasi.json")

pemeriksaan = resp.json()["pemeriksaan"]["harian"]
pemeriksaan = pd.DataFrame(pemeriksaan)

vaksinasi = resp.json()["vaksinasi"]["harian"]
vaksinasi = pd.DataFrame(vaksinasi)


def extract_data(df, name):
    data_string = df[[
        "key_as_string", "key", "doc_count"]]

    data_value = df.drop(
        ['key_as_string', 'key', 'doc_count'], axis=1)
    data_value = data_value.applymap(operator.itemgetter('value'))

    data_join = data_string.join(data_value)
    data_join.to_csv(name, index=False)


extract_data(pemeriksaan, "nasional/pemeriksaan.csv")
extract_data(vaksinasi, "nasional/vaksinasi.csv")
