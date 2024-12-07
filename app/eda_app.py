import streamlit as st
from utils.data_loader import load_data
from utils.data_cleaning import remove_outliers, drop_missing_values, encode_categorical_column
from utils.eda import podstawowe_statystyki
from utils.visualisation import plot_histogram, plot_boxplot, plot_correlation_matrix, plot_bar

# Tytuł aplikacji
st.title("Eksploracyjna Analiza Danych (EDA)")

# Wczytywanie danych
file_path = "data/hotel_reservations.csv"
df = load_data(file_path)

# Czyszczenie danych
df = remove_outliers(df, "avg_price_per_room", 300)
df = drop_missing_values(df)

# Kodowanie zmiennych kategorycznych
df = encode_categorical_column(df, "type_of_meal_plan")
df = encode_categorical_column(df, "room_type_reserved")
df = encode_categorical_column(df, "market_segment_type")
df = encode_categorical_column(df, "booking_status")

# Wyświetlenie podstawowych informacji
st.subheader("Podstawowe statystyki")
if st.checkbox("Pokaż statystyki danych"):
    stats = podstawowe_statystyki(df)
    st.write(stats)

# Wykresy
st.subheader("Wizualizacje danych")

# Histogram
if st.checkbox("Pokaż histogram dla kolumny"):
    column = st.selectbox("Wybierz kolumnę:", df.select_dtypes(include=['float', 'int']).columns)
    plot_histogram(df, column)

# Boxplot
if st.checkbox("Pokaż boxplot dla kolumny"):
    column = st.selectbox("Wybierz kolumnę:", df.select_dtypes(include=['float', 'int']).columns, key="boxplot")
    plot_boxplot(df, column)

# Korelacje
if st.checkbox("Pokaż macierz korelacji"):
    plot_correlation_matrix(df)

# Wykres słupkowy
if st.checkbox("Pokaż wykres słupkowy"):
    column = st.selectbox("Wybierz kolumnę kategoryczną:", df.select_dtypes(include=['object']).columns)
    plot_bar(df, column)