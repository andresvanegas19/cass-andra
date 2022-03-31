#!/bin/bash
""" load training datasets """
import pandas as pd


def load_n_transaction() -> pd.DataFrame:
    """
    Load the dataset
    """
    # n_transactions = pd.read_csv(
    return pd.read_csv(
        "confirm-transaction-2009-2022.csv"
    )


def load_fee_per_transaction_dataset() -> pd.DataFrame:
    """
    load dataset

    Returns:
        pd.DataFrame: the load fee per transaction dataser
    """
    # fee_transaction = pd.read_csv(
    return pd.read_csv(
        "datahub-2009-2018.csv"
    )


def number_of_transaction_per_month_dataset() -> pd.DataFrame:
    """
    load the dataset
    """
    # n_trade = pd.read_csv(
    return pd.read_csv(
        "trade-per-min-bitcoinity-2010-2022.csv"
    )


def trading_volume_dataset() -> pd.DataFrame:
    """
    load the dataset

    Returns:
        pd.DataFrame: _description_
    """
    # trading_volume = pd.read_csv(
    return pd.read_csv(
        "trading-volume-2010-2022.csv"
    )


def transaction_per_min_dataset() -> pd.DataFrame:
    """
    load teh dataset

    Returns:
        pd.DataFrame: _description_
    """
    # transactions_min = pd.read_csv("bitstamp-1-min-transaction-2012-2017.csv")
    return pd.read_csv(
        "bitstamp-1-min-transaction-2012-2017.csv"
    )


def trade_volume_dataset() -> pd.DataFrame:
    """
    load the dataset

    Returns:
        pd.DataFrame: _description_
    """
    return pd.read_csv("trade-volume-2009-2022.csv")

# circulating_bitcoins = pd.read_csv(
#     "circulating-bitcoin-2009-2022.csv"
# )
# investing_data = pd.read_csv(
#     "investiong-2010-202.csv"
# )
# marketcap = pd.read_csv(
#     "market-capitalization-bitcoinity-2010-2020.csv"
# )
# yahoo_data = pd.read_csv("yahoo-2014-2022.csv")
# transactions_min = pd.read_csv(
#     "bitstamp-1-min-transaction-2012-2017.csv"
# )
