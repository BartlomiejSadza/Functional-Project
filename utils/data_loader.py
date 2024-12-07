import pandas as pd

def load_data(dane):
    data = pd.read_csv(dane)
    print(f"Dane wczytane poprawnie. Liczba rekordów: {data.shape[0]} | Liczba kolumn: {data.shape[1]}")
    return data
