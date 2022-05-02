from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

from tensorflow.keras.layers import GRU
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
from src.create_model.model.train import train_gru
# from src.processing.reshaping import sequences_convert


def preprocess(data, len_sq, train_split):
    """_summary_

    Args:
        data (_type_): _description_
        len_sq (_type_): _description_
        train_split (_type_): _description_

    Returns:
        _type_: _description_
    """
    data = sequences_convert(data, len_sq)
    num_train = int(train_split * data.shape[0])

    X_train = data[:num_train, :-1, :]
    y_train = data[:num_train, -1, :]
    X_test = data[num_train:, :-1, :]
    y_test = data[num_train:, -1, :]

    return X_train, y_train, X_test, y_test


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


# normalize
def normalize(dataset):
    """_summary_

    Args:
        dataset (_type_): _description_

    Returns:
        _type_: _description_
    """
    min_max_scaler = MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(dataset.values)
    return pd.DataFrame(x_scaled, columns=dataset.columns, index=dataset.index)


def create_dataset(dataset, time_step=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-time_step-1):
        a = dataset[i:(i+time_step), 0]
        dataX.append(a)
        dataY.append(dataset[i + time_step, 0])
    return np.array(dataX), np.array(dataY)


def normalize_model(dataset):
    scaler = MinMaxScaler(feature_range=(0, 1))
    df1 = scaler.fit_transform(np.array(dataset).reshape(-1, 1))

    training_size = int(len(df1)*0.80)
    test_size = len(df1)-training_size
    train_data, test_data = df1[0:training_size,
                                :], df1[training_size:len(df1), :1]
    print("split data")

    time_step = 5
    X_train, y_train = create_dataset(train_data, time_step)
    X_test, y_test = create_dataset(test_data, time_step)

    X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
    X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

    print("Split the data")
    model = Sequential()
    model.add(GRU(3, return_sequences=True, input_shape=(time_step, 1)))  # GRU
    model.add(GRU(3, return_sequences=True))
    model.add(GRU(3))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')

    train_gru(model, X_train, y_train, X_test, y_test)
