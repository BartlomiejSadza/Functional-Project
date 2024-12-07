from utils.data_loader import load_data
from utils.data_cleaning import remove_outliers, drop_missing_values

file_path = "data/hotel_reservations.csv"

df = load_data(file_path)

df_cleaned = remove_outliers(df, column="avg_price_per_room", threshold=300)

df_cleaned = drop_missing_values(df_cleaned)

print(df_cleaned.head())