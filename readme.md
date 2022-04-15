# Data Sebaran Covid-19 dari covid19.go.id

[![Daily Update](https://github.com/zakiego/data-sebaran-covid19goid/actions/workflows/runner.yml/badge.svg)](https://github.com/zakiego/data-sebaran-covid19goid/actions/workflows/runner.yml)

Data pada repository ini dikumpulkan dari [API covid-19.go.id](https://covid19.go.id/dokumentasi-api). Data diperbarui setiap hari menggunakan script [python](https://github.com/zakiego/dataset-sebaran-covid19goid/tree/main/script) dan dijalankan di atas [Github Action](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/.github/workflows/runner.yml).

Dokumentasi resmi bisa dilihat di sini https://covid19.go.id/dokumentasi-api.

## Data yang Tersedia


### Daftar Isi

Tingkat Nasional
1. [Data Covid-19 Harian Nasional](#1-data-covid-19-harian-nasional)
2. [Data Vaksinasi Covid-19 Harian Nasional](#2-data-vaksinasi-covid-19-harian-nasional)
3. [Data Pemeriksaan Covid-19 Harian Nasional](#3-data-pemeriksaan-covid-19-harian-nasional)
4. [Data Jenis Kelamin Covid-19 Nasional](#4-data-jenis-kelamin-covid-19-nasional)
5. [Data Usia Covid-19 Nasional](#5-data-usia-covid-19-nasional)

Tingkat Provinsi
1. [Data Covid-19 Harian Per Provinsi](#1-data-covid-19-harian-per-provinsi)
2. [Data Jenis Kelamin Covid-19 Per Provinsi](#2-data-jenis-kelamin-covid-19-per-provinsi)
3. [Data Usia Covid-19 Per Provinsi](#3-data-usia-covid-19-per-provinsi)

[Catatan](#catatan)

---

### Tingkat Nasional

#### 1. Data Covid-19 Harian Nasional

  File: https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/nasional/harian.csv
  
  API: https://data.covid19.go.id/public/api/update.json
  
  Kolom:
  - jumlah_meninggal
  - jumlah_sembuh
  - jumlah_positif
  - jumlah_dirawat
  - jumlah_positif_kum
  - jumlah_sembuh_kum
  - jumlah_meninggal_kum
  - jumlah_dirawat_kum

#### 2. Data Vaksinasi Covid-19 Harian Nasional

  File: https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/nasional/vaksinasi.csv
  
  API: https://data.covid19.go.id/public/api/pemeriksaan-vaksinasi.json
  
  Kolom:
  - jumlah_vaksinasi_1
  - jumlah_vaksinasi_2
  - jumlah_jumlah_vaksinasi_1_kum	
  - jumlah_jumlah_vaksinasi_2_kum
  
  
#### 3. Data Pemeriksaan Covid-19 Harian Nasional

  File: https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/nasional/pemeriksaan.csv
  
  API: https://data.covid19.go.id/public/api/pemeriksaan-vaksinasi.json
  
  Kolom:
  - jumlah_spesimen_pcr_tcm
  - jumlah_spesimen_pcr_tcm_kum
  - jumlah_orang_pcr_tcm
  - jumlah_orang_pcr_tcm_kum
  - jumlah_spesimen_antigen
  - jumlah_spesimen_antigen_kum
  - jumlah_orang_antigen
  - jumlah_orang_antigen_kum
  
  #### 4. Data Jenis Kelamin Covid-19 Nasional

  File: https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/nasional/jenis_kelamin_nasional.csv
  
  API: https://data.covid19.go.id/public/api/prov.json
  
  Kolom:
  - tanggal
  - LAKI-LAKI
  - PEREMPUAN
  - tidak_diketahui
  
  #### 5. Data Usia Covid-19 Nasional

  File: https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/nasional/usia_nasional.csv
  
  API: https://data.covid19.go.id/public/api/prov.json
  
  Kolom:
  - tanggal
  - 0-5
  - 6-18
  - 19-30
  - 31-45
  - 46-59
  - \>\= 60
  - tidak_diketahui

---

### Tingkat Provinsi
  
  
  #### 1. Data Covid-19 Harian Per Provinsi

  API: https://data.covid19.go.id/public/api/prov_detail_{provinsi}.json
  
  *lihat [catatan](#catatan)
  
  File: 
   1. [DKI_JAKARTA](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/DKI_JAKARTA.csv)
   2. [JAWA_BARAT](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/JAWA_BARAT.csv)
   3. [JAWA_TIMUR](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/JAWA_TIMUR.csv)
   4. [JAWA_TENGAH](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/JAWA_TENGAH.csv)
   5. [SULAWESI_SELATAN](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/SULAWESI_SELATAN.csv)
   6. [BANTEN](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/BANTEN.csv)
   7. [NUSA_TENGGARA_BARAT](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/NUSA_TENGGARA_BARAT.csv)
   8. [BALI](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/BALI.csv)
   9. [PAPUA](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/PAPUA.csv)
   10. [KALIMANTAN_SELATAN](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/KALIMANTAN_SELATAN.csv)
   11. [SUMATERA_BARAT](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/SUMATERA_BARAT.csv)
   12. [SUMATERA_SELATAN](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/SUMATERA_SELATAN.csv)
   13. [KALIMANTAN_TENGAH](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/KALIMANTAN_TENGAH.csv)
   14. [KALIMANTAN_TIMUR](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/KALIMANTAN_TIMUR.csv)
   15. [SUMATERA_UTARA](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/SUMATERA_UTARA.csv)
   16. [DAERAH_ISTIMEWA_YOGYAKARTA](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/DAERAH_ISTIMEWA_YOGYAKARTA.csv)
   17. [KALIMANTAN_UTARA](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/KALIMANTAN_UTARA.csv)
   18. [KEPULAUAN_RIAU](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/KEPULAUAN_RIAU.csv)
   19. [KALIMANTAN_BARAT](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/KALIMANTAN_BARAT.csv)
   20. [SULAWESI_TENGGARA](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/SULAWESI_TENGGARA.csv)
   21. [LAMPUNG](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/LAMPUNG.csv)
   22. [SULAWESI_UTARA](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/SULAWESI_UTARA.csv)
   23. [SULAWESI_TENGAH](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/SULAWESI_TENGAH.csv)
   24. [RIAU](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/RIAU.csv)
   25. [PAPUA_BARAT](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/PAPUA_BARAT.csv)
   26. [SULAWESI_BARAT](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/SULAWESI_BARAT.csv)
   27. [JAMBI](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/JAMBI.csv)
   28. [MALUKU_UTARA](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/MALUKU_UTARA.csv)
   29. [MALUKU](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/MALUKU.csv)
   30. [GORONTALO](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/GORONTALO.csv)
   31. [KEPULAUAN_BANGKA_BELITUNG](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/KEPULAUAN_BANGKA_BELITUNG.csv)
   32. [ACEH](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/ACEH.csv)
   33. [BENGKULU](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/BENGKULU.csv)
   34. [NUSA_TENGGARA_TIMUR](https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/provinsi/NUSA_TENGGARA_TIMUR.csv)
  
  Kolom:
  - tanggal
  - KASUS
  - AKUMULASI_KASUS
  - MENINGGAL
  - AKUMULASI_MENINGGAL
  - SEMBUH
  - AKUMULASI_SEMBUH
  - DIRAWAT_OR_ISOLASI
  - AKUMULASI_DIRAWAT_OR_ISOLASI
 
  #### 2. Data Jenis Kelamin Covid-19 Per Provinsi

  File: https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/nasional/jenis_kelamin.csv
  
  API: https://data.covid19.go.id/public/api/prov.json
  
  Kolom:
  - tanggal
  - LAKI-LAKI
  - PEREMPUAN
  - tidak_diketahui
  
  #### 3. Data Usia Covid-19 Per Provinsi

  File: https://github.com/zakiego/dataset-sebaran-covid19goid/blob/main/nasional/usia.csv
  
  API: https://data.covid19.go.id/public/api/prov.json
  
  Kolom:
  - tanggal
  - 0-5
  - 6-18
  - 19-30
  - 31-45
  - 46-59
  - \>\= 60
  - tidak_diketahui
  
---

### Catatan

[Data Covid-19 Harian Per Provinsi](#1-data-covid-19-harian-per-provinsi)

```
https://data.covid19.go.id/public/api/prov_detail_{provinsi}.json
```

Contoh: `https://data.covid19.go.id/public/api/prov_detail_DKI_JAKARTA.json`

List value per provinsi:

- ACEH
- BALI
- BANTEN
- BENGKULU
- DAERAH_ISTIMEWA_YOGYAKARTA
- DKI_JAKARTA
- GORONTALO
- JAMBI
- JAWA_BARAT
- JAWA_TENGAH
- JAWA_TIMUR
- KALIMANTAN_BARAT
- KALIMANTAN_SELATAN
- KALIMANTAN_TENGAH
- KALIMANTAN_TIMUR
- KALIMANTAN_UTARA
- KEPULAUAN_BANGKA_BELITUNG
- KEPULAUAN_RIAU
- LAMPUNG
- MALUKU
- MALUKU_UTARA
- NUSA_TENGGARA_BARAT
- NUSA_TENGGARA_TIMUR
- PAPUA
- PAPUA_BARAT
- RIAU
- SULAWESI_BARAT
- SULAWESI_SELATAN
- SULAWESI_TENGAH
- SULAWESI_TENGGARA
- SULAWESI_UTARA
- SUMATERA_BARAT
- SUMATERA_SELATAN
- SUMATERA_UTARA
