#!/usr/bin/env python3
""" running all the logic """

# from processing.cleaning import cleaning
# from src.data.load.request_live_data import request_to_alpha_vantage,
from src.data.load.load_datasets import nasqad_historical, download_csv_load_drive
from src.processing.modify_columns import change_date_to_column, change_column_name, nasqad
from src.processing.merge import concat_dataset_to_one
from src.processing.reshaping import normalize_model
from src.processing.cleaning import test
# from src.data.load.scraping import coinmarket
# from src.data.load.load_datasets import download_csv_load_drive
# print(download_csv_load_drive())
# coinmarket()
# request_to_alpha_vantage()
# cleaning()


nasqad_data = nasqad_historical()
# test(nasqad_data)
# bistamp = download_csv_load_drive()

# change_date_to_column(bistamp)
# df_bistamp = change_column_name(
#     bistamp, ["Open", "High",	"Low",	"Close", "Volume_(BTC)"])
# # print(df_bistamp)
df_nasqad = nasqad(nasqad_data)
# # print(df_nasqad)

# df = concat_dataset_to_one(df_bistamp, df_nasqad)

# # normalize_model
# # print(df)
model = normalize_model(df_nasqad)
# print(model.describe())
