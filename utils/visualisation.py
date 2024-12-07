
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def plot_histogram(df, column):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True, bins=30)
    plt.title(f"Histogram: {column}")
    plt.xlabel(column)
    plt.ylabel("Częstość")
    st.pyplot(plt.gcf())

def plot_boxplot(df, column):
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x=column)
    plt.title(f"Boxplot: {column}")
    st.pyplot(plt.gcf())

def plot_bar(df, column):
    plt.figure(figsize=(10, 6))
    value_counts = df[column].value_counts()
    sns.barplot(x=value_counts.index, y=value_counts.values)
    plt.title(f"Wykres słupkowy: {column}")
    plt.xlabel(column)
    plt.ylabel("Liczba wystąpień")
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())

def plot_scatterplot(df, x_column, y_column):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_column, y=y_column)
    plt.title(f"Wykres punktowy: {x_column} vs {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    st.pyplot(plt.gcf())