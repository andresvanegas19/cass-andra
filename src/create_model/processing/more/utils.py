import numpy as np
import pandas as pd

def change_date_formate(row):
    """
    Change the date of the dataframe

    Args:
        row (_type_): _description_

    Returns:
        _type_: _description_
    """
    return pd.Timestamp(row).strftime('%Y-%m-%d %H:%M:%S')


def value_to_float(x):
    """
    Modify the value to be a float

    Args:
        x (_type_): _description_

    Returns:
        _type_: _description_
    """
    if type(x) == float or type(x) == int:
        return x

    if "," in x:
        x = x.replace(",", "")

    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0


def SMA(df, periods=50):

    lst = []

    for i in range(len(df)):
        if i < periods:

            lst.append(np.nan)

        else:
            # Calculating the SMA
            lst.append(round(np.mean(df[i:periods+i]), 2))

    return lst


def Stoch(closes, lows, highs, periods=14, d_periods=3):

    k_lst = []

    d_lst = []

    for i in range(len(closes)):
        if i < periods:

            k_lst.append(np.nan)

            d_lst.append(np.nan)

        else:

            highest = max(highs[i:periods+i])
            lowest = min(lows[i:periods+i])

            k = ((closes[i] - lowest) / (highest - lowest)) * 100

            k_lst.append(round(k, 2))

            if len(k_lst) < d_periods:
                d_lst.append(np.nan)
            else:
                d_lst.append(round(np.mean(k_lst[-d_periods-1:-1])))

    return k_lst, d_lst


def RSI(df, periods=14):
    """
    Calculates the Relative Strength Index

    **Values must be descending**
    """

    df = df.diff()

    lst = []

    for i in range(len(df)):
        if i < periods:

            lst.append(np.nan)

        else:

            avg_gain = (sum([x for x in df[i:periods+i] if x >= 0]) / periods)
            avg_loss = (sum([abs(x)
                        for x in df[i:periods+i] if x <= 0]) / periods)

            rs = avg_gain / avg_loss

            rsi = 100 - (100 / (1 + rs))

            lst.append(round(rsi, 2))

    return lst
