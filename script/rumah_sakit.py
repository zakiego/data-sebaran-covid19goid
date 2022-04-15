#!/usr/bin/python3

import requests as req
import pandas as pd

resp = req.get("https://data.covid19.go.id/public/api/rs.json")
resp = resp.json()

data = pd.DataFrame(resp)

data.to_csv("nasional/rumah_sakit.csv", index=False)
