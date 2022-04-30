import pandas as pd

def concat_dataset_to_one(df1, df2):
    """
    concat two dataframe to one
    """
    return pd.concat([df1, df2], axis=0)
