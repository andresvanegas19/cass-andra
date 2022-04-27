#!/bin/bash
""" load training datasets """
import pandas as pd


COMPLETE_PATH = 'https://drive.google.com/uc?id='
DATASETS = {
    "nasqad": 'https://drive.google.com/file/d/1-aur5DlrI4XuB3aziYMnYE6YMzcp0aIk/view?usp=sharing',
}


def circulating_bitcoins(path):
    """
    Loads the circulating bitcoins dataset.

    Args:
        path (_type_): _description_

    Returns:
        _type_: _description_
    """
    return pd.read_csv(path)


def bitstamp_1_min_transaction(path):
    """
    Loads the bitstamp 1 min transaction dataset.

    Args:
        path (_type_): _description_

    Returns:
        _type_: _description_
    """
    return pd.read_csv(path)


def nasqad_historical():
    """
    Retruning the string

    Returns:
        _type_: _description_
    """

    path: str = DATASETS.get("nasqad")
    if not path:
        return ""

    return pd.read_csv(
        f"{COMPLETE_PATH}{path.split('/')[-2]}",
        parse_dates=["Date"]
    )


# n_transactions = pd.read_csv(
#     "/content/drive/MyDrive/data/confirm-transaction-2009-2022.csv"
# )

# fee_transaction = pd.read_csv(
#     "/content/drive/MyDrive/data/datahub-2009-2018.csv"
# )

# investing_data = pd.read_csv(
#     "/content/drive/MyDrive/data/investiong-2010-202.csv"
# )

# marketcap = pd.read_csv(
#     "/content/drive/MyDrive/data/market-capitalization-bitcoinity-2010-2020.csv"
# )

# n_trade = pd.read_csv(
#     "/content/drive/MyDrive/data/trade-per-min-bitcoinity-2010-2022.csv"
# )

# trading_volume = pd.read_csv(
#     "/content/drive/MyDrive/data/trading-volume-2010-2022.csv"
# )

# yahoo_data = pd.read_csv("/content/drive/MyDrive/data/yahoo-2014-2022.csv")

# transactions_min = pd.read_csv(
#     "/content/drive/MyDrive/data/bitstamp-1-min-transaction-2012-2017.csv"
# )
