#!/usr/bin/env python3
""" Module for cleaning data """

import pandas as pd

from processing.utils import change_date_formate
from data.load_training_datasets import (
    load_n_transaction,
    load_fee_per_transaction_dataset,
    number_of_transaction_per_month_dataset,
    trading_volume_dataset,
    transaction_per_min_dataset

)


def set_index_to_data(df, column_data) -> pd.DataFrame:
    """
    return a dataframe with the index with data

    Args:
        df (_type_): _description_

    Returns:
        pd.DataFrame: _description_
    """
    return df.set_index(column_data)


def cleaning():
    """_summary_
    """
    fee_transaction = load_fee_per_transaction_dataset(
    )[["date", "fees",	"averageDifficulty"]]
    fee_transaction["date"] = fee_transaction['date'].apply(
        lambda row: str(pd.Timestamp(row))
    )
    fee_transaction = set_index_to_data(fee_transaction, "date")
    n_trade["Time"] = n_trade['Time'].apply(
        lambda row: change_date_formate(row)
    )
    n_trade.set_index("Time", inplace=True)
    n_trade["n_trade"] = n_trade.sum(axis=1)
    n_trade = n_trade[["n_trade"]]
