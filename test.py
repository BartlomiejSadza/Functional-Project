from utils.data_loader import load_data
from utils.data_cleaning import remove_outliers, drop_missing_values, encode_categorical_column
# from utils.eda import podstawowe_statystyki, wizualizacja_korelacji, wizualizacja_rozkładu, analiza_relacji_targetu

file_path = "data/hotel_reservations.csv"
df = load_data(file_path)

df = remove_outliers(df, "avg_price_per_room", 300)
df = drop_missing_values(df)

df = encode_categorical_column(df, "type_of_meal_plan")
df = encode_categorical_column(df, "room_type_reserved")
df = encode_categorical_column(df, "market_segment_type")
df = encode_categorical_column(df, "booking_status")

print(df.head())