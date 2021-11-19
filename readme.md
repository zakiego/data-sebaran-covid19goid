# Data Sebaran Covid-19 dari covid-19.go.id

[![Daily Update](https://github.com/zakiego/data-sebaran-covid19goid/actions/workflows/runner.yml/badge.svg)](https://github.com/zakiego/data-sebaran-covid19goid/actions/workflows/runner.yml)

## Data yang Tersedia

- [x] Kasus Harian -- nasional/provinsi
- [x] Umur -- nasional/provinsi
- [x] Jenis kelamin -- nasional/provinsi
- [x] Pemeriksaan -- nasional
- [x] Vaksinasi -- nasional
- [ ] Penyakit penyerta

## List API

### Data Harian

```
https://data.covid19.go.id/public/api/update.json
```

### Data Usia dan Jenis Kelamin

```
https://data.covid19.go.id/public/api/prov.json
```

### Data Pemeriksaan dan Vaksinasi

```
https://data.covid19.go.id/public/api/pemeriksaan-vaksinasi.json
```

### Data Per Provinsi

```
https://data.covid19.go.id/public/api/prov_detail_{$provinsi}.json
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
