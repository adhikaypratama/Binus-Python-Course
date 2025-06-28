import pandas as pd

data = {
    "Negara": ["Indonesia", "Jepang", "India", "China", "Amerika Serikat", "Brazil", "Rusia", "Meksiko", "Nigeria", "Jerman"],
    "Ibu Kota": ["Jakarta", "Tokyo", "New Delhi", "Beijing", "Washington DC", "Brazilia", "Moskow", "Meksiko City", "Abuja", "Berlin"],
    "Benua": ["Asia", "Asia", "Asia", "Asia", "Amerika", "Amerika", "Asia", "Amerika", "Afrika", "Eropa"],
    "Luas": [2000, 400, 3300, 10000, 9800, 8500, 18000, 2000, 950, 360],
    "Populasi": [270, 140, 1200, 1380, 330, 210, 150, 120, 300, 90]
}

df = pd.DataFrame(data)

df.to_csv('NegaraTest.csv')
