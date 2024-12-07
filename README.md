# Functional-Project

**Autor**: Bartłomiej Sadza

**Przedmiot**: Zaawansowane Programowanie w Języku Python

## Opis projektu

Celem projektu było stworzenie aplikacji do eksploracyjnej analizy danych (EDA) dotyczących rezerwacji hotelowych. Aplikacja umożliwia wczytywanie, przetwarzanie i wizualizację danych, oferując użytkownikowi interaktywne narzędzia do analizy.

## Funkcjonalności

- **Wczytywanie danych**: Aplikacja umożliwia wczytanie danych z pliku CSV zawierającego informacje o rezerwacjach hotelowych.

- **Czyszczenie danych**: Implementacja funkcji do usuwania wartości odstających oraz brakujących danych.

- **Kodowanie zmiennych kategorycznych**: Zamiana zmiennych kategorycznych na wartości numeryczne w celu ułatwienia analizy.

- **Wizualizacja danych**: Generowanie interaktywnych wykresów, takich jak histogramy, boxploty, wykresy słupkowe oraz scatterploty.

- **Interfejs użytkownika**: Intuicyjny interfejs stworzony za pomocą biblioteki Streamlit, umożliwiający użytkownikowi wybór analizowanych zmiennych oraz dostosowanie parametrów wizualizacji.

## Struktura projektu

Projekt składa się z następujących modułów:

- **app/**: Zawiera główny plik aplikacji `eda_app.py`, odpowiedzialny za uruchomienie interfejsu użytkownika oraz integrację poszczególnych funkcji.

- **data/**: Katalog przechowujący plik `hotel_reservations.csv` z danymi do analizy.

- **utils/**: Zawiera moduły pomocnicze:
  - `data_loader.py`: Funkcje do wczytywania danych.
  - `data_cleaning.py`: Funkcje do przetwarzania i czyszczenia danych.
  - `visualisation.py`: Funkcje do tworzenia wykresów.

## Wymagania

Aby uruchomić aplikację, należy zainstalować wymagane biblioteki, korzystając z pliku `requirements.txt`. Główne zależności to:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `streamlit`

Instalacja zależności:

```bash
pip install -r requirements.txt
```

## Uruchomienie aplikacji

Aby uruchomić aplikację, wykonaj poniższe kroki:

1. Upewnij się, że wszystkie wymagane biblioteki są zainstalowane.
2. W terminalu przejdź do katalogu zawierającego plik `eda_app.py`.
3. Uruchom aplikację poleceniem:

   ```bash
   streamlit run eda_app.py
   ```

Aplikacja zostanie uruchomiona w przeglądarce internetowej, umożliwiając interaktywną analizę danych.

## Analiza danych

Aplikacja umożliwia przeprowadzenie następujących analiz:

- **Histogramy**: Analiza rozkładu wartości liczbowych w wybranych kolumnach.
- **Boxploty**: Identyfikacja wartości odstających oraz porównanie rozkładów.
- **Wykresy słupkowe**: Wizualizacja częstości występowania kategorii w zmiennych kategorycznych.
- **Scatterploty**: Analiza zależności między dwiema zmiennymi liczbowymi.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
