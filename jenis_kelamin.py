#!/usr/bin/python3

from pandas import json_normalize
import requests as req
import pandas as pd

resp = req.get("https://data.covid19.go.id/public/api/prov.json")
tanggal = resp.json()["last_date"]
data = resp.json()["list_data"]
data = pd.DataFrame(data)

data_jenis_kelamin = pd.DataFrame()

for x in range(len(data)):
    bucket = pd.DataFrame()
    total = 0
    for y in data["jenis_kelamin"][x]:
        z = json_normalize(y)
        col = z.iloc[0]["key"]
        val = z.iloc[0]["doc_count"]
        total += val
        bucket[col] = [val]
    bucket["tidak_diketahui"] = data["jumlah_kasus"][x] - total
    bucket["provinsi"] = data["key"][x]
    first_column = bucket.pop("provinsi")
    bucket.insert(0, 'provinsi', first_column)
    data_jenis_kelamin = data_jenis_kelamin.append(bucket)

data_jenis_kelamin = data_jenis_kelamin.reset_index(drop=True)
data_jenis_kelamin.insert(0, 'tanggal', tanggal)

###

data_csv = pd.read_csv('nasional/jenis_kelamin.csv')

data_join = pd.concat([data_jenis_kelamin, data_csv]
                      ).drop_duplicates().reset_index(drop=True)

###

data_join.to_csv("nasional/jenis_kelamin.csv", index=False)
data_jenis_kelamin_nasinal = data_join.groupby("tanggal").sum()
data_jenis_kelamin_nasinal.to_csv("nasional/jenis_kelamin_nasional.csv")
