from tensorflow.keras.layers import (
    Dense,
    Dropout,
    LSTM
)
from tensorflow.keras.models import Sequential


def lstm_model(x_train):
    model = Sequential()
    model.add(LSTM(64, activation='relu', input_shape=(x_train.shape[1], x_train.shape[2]), return_sequences=True))
    model.add(LSTM(32, activation='relu', return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(x_train.shape[1]))
    return model