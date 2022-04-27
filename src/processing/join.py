import pandas as pd


def change_date_to_column(df, is_timestap=False):
    """_summary_

    Args:
        df (_type_): _description_
        is_timestap (bool, optional): _description_. Defaults to False.
    """
    if is_timestap:
        df["Timestamp"] = pd.to_datetime(df.Timestamp, unit='s')
        df.set_index("Timestamp", inplace=True)
    else:
        return
