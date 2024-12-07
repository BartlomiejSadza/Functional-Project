
def podstawowe_statystyki(df):
    print("Podstawowe statystyki zbioru danych:")
    print(df.info())
    print("\n Opis statystyczny zbioru danych:")
    print(df.describe())
    print("\n Rozkład wartości w kolumnach:")
    for col in df.columns:
        print(f"\n {col}:")
        print(df[col].value_counts())

