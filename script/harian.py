#!/usr/bin/python3

import requests as req
import pandas as pd
import operator

resp = req.get("https://data.covid19.go.id/public/api/update.json")
resp = resp.json()["update"]["harian"]

data = pd.DataFrame(resp)

data_string = data[["key_as_string", "key", "doc_count"]]

data_value = data.drop(['key_as_string', 'key', 'doc_count'], axis=1)
data_value = data_value.applymap(operator.itemgetter('value'))

data_join = data_string.join(data_value)

data_join.to_csv("nasional/harian.csv", index=False)
