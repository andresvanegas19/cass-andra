#!/usr/bin/env python3
""" Module for cleaning data """

from tensorflow.keras import layers, Sequential
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# from processing.utils import change_date_formate
# from data.load_training_datasets import (
#     load_n_transaction,
#     load_fee_per_transaction_dataset,
#     number_of_transaction_per_month_dataset,
#     trading_volume_dataset,
#     transaction_per_min_dataset

# )


def set_index_to_data(df, column_data) -> pd.DataFrame:
    """
    return a dataframe with the index with data

    Args:
        df (_type_): _description_

    Returns:
        pd.DataFrame: _description_
    """
    return df.set_index(column_data)


# def cleaning():
#     """_summary_
#     """
#     fee_transaction = load_fee_per_transaction_dataset(
#     )[["date", "fees",	"averageDifficulty"]]
#     fee_transaction["date"] = fee_transaction['date'].apply(
#         lambda row: str(pd.Timestamp(row))
#     )
#     fee_transaction = set_index_to_data(fee_transaction, "date")
#     n_trade["Time"] = n_trade['Time'].apply(
#         lambda row: change_date_formate(row)
#     )
#     n_trade.set_index("Time", inplace=True)
#     n_trade["n_trade"] = n_trade.sum(axis=1)
#     n_trade = n_trade[["n_trade"]]


SEQ_LEN = 100


def to_sequences(data, seq_len):
    d = []
    for index in range(len(data) - seq_len):
        d.append(data[index: index + seq_len])

    return np.array(d)


def preprocess(data_raw, seq_len, train_split):
    data = to_sequences(data_raw, seq_len)
    num_train = int(train_split * data.shape[0])

    X_train = data[:num_train, :-1, :]
    y_train = data[:num_train, -1, :]
    X_test = data[num_train:, :-1, :]
    y_test = data[num_train:, -1, :]

    return X_train, y_train, X_test, y_test


def test(dataframe):
    scaler = MinMaxScaler()

    scaled_close = scaler.fit_transform(
        dataframe.Close.values.reshape(-1, 1)
    )
    scaled_close = scaled_close[~np.isnan(scaled_close)].reshape(-1, 1)
    X_train, y_train, X_test, y_test =\
        preprocess(scaled_close, SEQ_LEN, train_split=0.80)
    model = Sequential()
    model.add(layers.LSTM(units=32, return_sequences=True,
                          input_shape=(99, 1), dropout=0.2))
    model.add(layers.LSTM(units=32, return_sequences=True,
                          dropout=0.2))
    model.add(layers.LSTM(units=32, dropout=0.2))
    model.add(layers.Dense(units=1))
    # model.summary()
    model.compile(
        loss='mean_squared_error',
        optimizer='adam'
    )
    BATCH_SIZE = 64
    model.fit(
        X_train,
        y_train,
        epochs=30,
        batch_size=BATCH_SIZE,
        shuffle=False,
        validation_split=0.1
    )

    model.save('bitcoin.h5')
