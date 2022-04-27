from sklearn.preprocessing import MinMaxScaler
import numpy as np


def scaling(data_frame):
    """_summary_

    Args:
        data_frame (_type_): _description_

    Returns:
        _type_: _description_
    """
    scaler = MinMaxScaler()

    scaled_close = scaler.fit_transform(
        data_frame.Close.values.reshape(-1, 1)
    )
    scaled_close = scaled_close[~np.isnan(scaled_close)].reshape(-1, 1)

    return scaled_close
