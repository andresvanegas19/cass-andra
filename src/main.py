#!/usr/bin/env python3
""" running all the logic """

# from processing.cleaning import cleaning
# from src.data.load.request_live_data import request_to_alpha_vantage, 
# from src.data.load.scraping import coinmarket
from src.data.load.load_datasets import download_csv_load_drive

print(download_csv_load_drive())

# coinmarket()
# request_to_alpha_vantage()

# cleaning()