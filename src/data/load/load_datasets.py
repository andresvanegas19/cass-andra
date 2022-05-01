#!/bin/bash
""" load training datasets """
import pandas as pd
import gdown
import os

# TODO: make a class that has all this data with the api keys

COMPLETE_PATH = 'https://drive.google.com/uc?id='
DATASETS = {
    "nasqad": 'https://drive.google.com/file/d/1-aur5DlrI4XuB3aziYMnYE6YMzcp0aIk/view?usp=sharing',
    "bistamp": "https://drive.google.com/file/d/106S5tO9nbov5ycqeMBsJvuHKkPWBkPlu/view?usp=sharing",
}

# from pydrive.auth import GoogleAuth

# gauth = GoogleAuth()
# Create local webserver and auto handles authentication.
# gauth.LocalWebserverAuth()


def nasqad_historical(dataset=DATASETS):
    """
    Read cv from google drive

    Returns:
        the dataframe from nasqad
    """

    path = dataset.get("nasqad")

    return pd.read_csv(
        COMPLETE_PATH + path.split('/')[-2],
        parse_dates=["Date"]
    )


def download_csv_load_drive(dataset=DATASETS, name="bistamp"):
    filename = f"{name}.csv"

    # si existe el archivo y esta en modo debug no borrarlo
    # TODO: MODIFY THIS FOR NOT CONSUME MEMORY
    # if os.path.exists(filename) and os.getenv("DEBUG", False):
    if os.path.exists(filename):
        return pd.read_csv(filename)

    gdown.download(
        url=dataset.get(name),
        output=filename,
        quiet=False,
        fuzzy=True
    )

    # if os.getenv("DEBUG", False):
    #     # Delete for not overload the server
    #     os.remove(filename)

    return pd.read_csv(filename)
