import sys
import os

# Dodanie katalogu głównego projektu do ścieżki wyszukiwania modułów ponieważ nie czytało mi utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.data_loader import load_data
from utils.data_cleaning import remove_outliers, drop_missing_values, encode_categorical_column
from utils.visualisation import plot_histogram, plot_boxplot, plot_bar, plot_scatterplot

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

# Histogram
st.subheader("Histogram")
column_hist = st.selectbox("Wybierz kolumnę liczbową do histogramu:", df.select_dtypes(include=['float', 'int']).columns, key="histogram")
plot_histogram(df, column_hist)

# Boxplot
st.subheader("Boxplot")
column_box = st.selectbox("Wybierz kolumnę liczbową do boxplotu:", df.select_dtypes(include=['float', 'int']).columns, key="boxplot")
plot_boxplot(df, column_box)

# Wykres słupkowy
st.subheader("Wykres słupkowy")
column_bar = st.selectbox("Wybierz kolumnę kategoryczną do wykresu słupkowego:", df.select_dtypes(include=['object']).columns, key="bar")
plot_bar(df, column_bar)

# Wykres punktowy (Scatterplot)
st.subheader("Wykres punktowy (Scatterplot)")
x_column = st.selectbox("Wybierz kolumnę X (liczbową):", df.select_dtypes(include=['float', 'int']).columns, key="scatter_x")
y_column = st.selectbox("Wybierz kolumnę Y (liczbową):", df.select_dtypes(include=['float', 'int']).columns, key="scatter_y")
plot_scatterplot(df, x_column, y_column)

# Porównywanie (np. słupki)
st.subheader("Porównywanie zmiennych")
col1 = st.selectbox("Wybierz pierwszą zmienną kategoryczną:", df.select_dtypes(include=['object']).columns, key="compare_1")
col2 = st.selectbox("Wybierz drugą zmienną kategoryczną:", df.select_dtypes(include=['object']).columns, key="compare_2")
if col1 and col2:
    st.write(f"Porównanie {col1} z {col2}")
    plot_bar(df, col1)