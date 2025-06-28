import pandas as pd

data = {
    "Negara": ["Indonesia", "Jepang", "India", "China", "Amerika Serikat", "Brazil", "Rusia", "Meksiko", "Nigeria", "Jerman"],
    "Ibu Kota": ["Jakarta", "Tokyo", "New Delhi", "Beijing", "Washington DC", "Brazilia", "Moskow", "Meksiko City", "Abuja", "Berlin"],
    "Benua": ["Asia", "Asia", "Asia", "Asia", "Amerika", "Amerika", "Asia", "Amerika", "Afrika", "Eropa"],
    "Luas": [1905, 377, 3287, 9597, 9834, 8515, 17098, 1964, 923, 357],
    "Populasi": [264, 143, 1252, 1357, 329, 210, 146, 126, 200, 83]
}

df = pd.DataFrame(data)

df.to_csv('NegaraTest.csv')
