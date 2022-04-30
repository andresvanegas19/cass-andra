import pandas as pd


def change_date_to_column(dataframe, is_timestap=False):
    """_summary_

    Args:
        df (_type_): _description_
        is_timestap (bool, optional): _description_. Defaults to False.
    """
    # if is_timestap:
    dataframe["Timestamp"] = pd.to_datetime(dataframe.Timestamp, unit='s')
    dataframe.set_index("Timestamp", inplace=True)
    # else:
    #     return


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
    return dataframe_bitstamp.rename(
        columns={'Volume_(BTC)': 'Volume'},
        # inplace=True
    )


def nasqad(dataframe):
    new_dataframe = dataframe[["Open",	"High",
                               "Low",	"Close", "Volume", "Date"]]
    new_dataframe['Date'].apply(
        lambda row: str(pd.Timestamp(row))
    )

    new_dataframe.loc[new_dataframe['Date'] > '2017-10-21']
    new_dataframe.set_index("Date", inplace=True)

    return new_dataframe
