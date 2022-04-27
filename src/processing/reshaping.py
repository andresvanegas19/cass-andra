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


def sequences_convert(data, len_sq):
    """_summary_

    Args:
        data (_type_): _description_
        len_sq (_type_): _description_

    Returns:
        _type_: _description_
    """
    final_d = []
    for index in range(len(data) - len_sq):
        final_d.append(data[index: len_sq + index])

    return np.array(final_d)
