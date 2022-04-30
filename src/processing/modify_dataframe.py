import pandas as pd


def change_date_to_column(dataframe, is_timestap=False):
    """_summary_

    Args:
        df (_type_): _description_
        is_timestap (bool, optional): _description_. Defaults to False.
    """
    if is_timestap:
        dataframe["Timestamp"] = pd.to_datetime(dataframe.Timestamp, unit='s')
        dataframe.set_index("Timestamp", inplace=True)
    else:
        return


def change_column_name(dataframe, columns):
    """
    change the column for certain dataframe

    Args:
        dataframe (_type_): _description_
        columns (_type_): _description_

    Returns:
        _type_: _description_
    """
    # ["Open", "High",	"Low",	"Close",	"Volume_(BTC)"]
    dataframe_bitstamp = dataframe[columns]
    dataframe_bitstamp.rename(
        columns={'Volume_(BTC)': 'Volume'},
        inplace=True
    )

    return dataframe_bitstamp


def nasqad(dataframe):
    df_nasqad = dataframe[["Open",	"High",	"Low",	"Close", "Volume", "Date"]]
    df_nasqad["Date"] = df_nasqad['Date'].apply(
        lambda row: str(pd.Timestamp(row))
    )

    df_nasqad = df_nasqad.loc[df_nasqad['Date'] > '2017-10-21']
    df_nasqad.set_index("Date", inplace=True)

    return df_nasqad
