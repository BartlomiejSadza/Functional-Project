import pandas as pd
from sklearn.preprocessing import LabelEncoder

def remove_outliers(df, column, threshold):
    df.drop(columns=["Booking_ID"], axis=1, inplace=True)  # Nikomu nie jest ona potrzebna
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

def encode_categorical_column(df, column):
    lb = LabelEncoder()
    print(f"Kodowanie kolumny {column}")
    df[column] = lb.fit_transform(df[column])
    print(f"unikalne wartości przed kodowaniem: {lb.classes_}")
    return df