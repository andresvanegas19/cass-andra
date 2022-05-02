# from tensorflow.keras.layers import Bidirectional, Dropout, Activation, Dense, LSTM
# from tensorflow.python.keras.layers import CuDNNLSTM
# from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
import tensorflow as tf


def create_model():
    model = tf.keras.Sequential()
    model.add(
        layers.LSTM(
            units=32,
            return_sequences=True,
            input_shape=(99, 1),
            dropout=0.2
        )
    )
    model.add(
        layers.LSTM(
            units=32,
            return_sequences=True,
            dropout=0.2
        )
    )
    model.add(layers.LSTM(units=32, dropout=0.2))
    model.add(layers.Dense(units=1))
    # adding 4 layers
    model.summary()
    model.compile(
        loss='mean_squared_error',
        optimizer='adam'
    )
    return model

