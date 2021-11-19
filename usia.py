#!/usr/bin/python3

from pandas import json_normalize
import requests as req
import pandas as pd

resp = req.get("https://data.covid19.go.id/public/api/prov.json")
tanggal = resp.json()["last_date"]
data = resp.json()["list_data"]
data = pd.DataFrame(data)

data_usia = pd.DataFrame()

for x in range(len(data)):
    bucket = pd.DataFrame()
    total = 0
    for y in data["kelompok_umur"][x]:
        z = json_normalize(y)
        col = z.iloc[0]["key"]
        val = z.iloc[0]["doc_count"]
        total += val
        bucket[col] = [val]
    bucket["tidak_diketahui"] = data["jumlah_kasus"][x] - total
    bucket["provinsi"] = data["key"][x]
    first_column = bucket.pop("provinsi")
    bucket.insert(0, 'provinsi', first_column)
    data_usia = data_usia.append(bucket)

data_usia = data_usia.reset_index(drop=True)
data_usia.insert(0, 'tanggal', tanggal)
data_usia.to_csv("nasional/usia.csv", index=False)

data_usia_nasinal = data_usia.groupby("tanggal").sum()
data_usia_nasinal.to_csv("nasional/usia_nasional.csv")

resp = req.get("https://data.covid19.go.id/public/api/prov.json")
tanggal = resp.json()["last_date"]
data = resp.json()["list_data"]
data = pd.DataFrame(data)

data_usia = pd.DataFrame()

for x in range(len(data)):
    bucket = pd.DataFrame()
    total = 0
    for y in data["kelompok_umur"][x]:
        z = json_normalize(y)
        col = z.iloc[0]["key"]
        val = z.iloc[0]["doc_count"]
        total += val
        bucket[col] = [val]
    bucket["tidak_diketahui"] = data["jumlah_kasus"][x] - total
    bucket["provinsi"] = data["key"][x]
    first_column = bucket.pop("provinsi")
    bucket.insert(0, 'provinsi', first_column)
    data_usia = data_usia.append(bucket)

data_usia = data_usia.reset_index(drop=True)
data_usia.insert(0, 'tanggal', tanggal)


######

data_csv = pd.read_csv('nasional/usia.csv')

data_join = pd.concat([data_usia, data_csv])
data_join.drop_duplicates().reset_index()
#

######

data_csv = pd.read_csv('nasional/usia.csv')

data_join = pd.concat([data_usia, data_csv]
                      ).drop_duplicates().reset_index(drop=True)

###

data_join.to_csv("nasional/usia.csv", index=False)

data_usia_nasinal = data_join.groupby("tanggal").sum()
data_usia_nasinal.to_csv("nasional/usia_nasional.csv")
