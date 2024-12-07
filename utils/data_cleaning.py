import pandas as pd

def remove_outliers(df, column, threshold=1.5):
    przed = df.shape[0]
    df = df[df[column] <= threshold]
    po = df.shape[0]
    print(f"Usunięto {przed - po} rekordów w kolumnie {column}")
    return df

def drop_missing_values(df):
    przed = df.shape[0]
    df.dropna()
    po = df.shape[0]
    print(f"Usunięto {przed - po} rekordów z powodu braku danych")
    return df