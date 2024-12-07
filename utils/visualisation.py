import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def plot_histogram(df, column):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True, bins=30)
    plt.title(f"Histogram: {column}")
    plt.xlabel(column)
    plt.ylabel("Częstość")
    plt.grid(True)
    st.pyplot(plt.gcf())

def plot_boxplot(df, column):
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x=column)
    plt.title(f"Boxplot: {column}")
    plt.grid(True)
    st.pyplot(plt.gcf())

def plot_bar(df, column):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x=column, order=df[column].value_counts().index)
    plt.title(f"Wykres słupkowy: {column}")
    plt.xlabel(column)
    plt.ylabel("Liczba wystąpień")
    plt.grid(True)
    st.pyplot(plt.gcf())

def plot_correlation_matrix(df):
    plt.figure(figsize=(12, 8))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
    plt.title("Macierz korelacji")
    st.pyplot(plt.gcf())