from tensorflow.keras.layers import (
    Dense,
    Dropout,
    LSTM,
    GRU
)
from tensorflow.keras.models import Sequential


def lstm_model(x_train):
    model = Sequential()
    model.add(GRU(units=96, return_sequences=True, input_shape=(x_train.shape[1], x_train.shape[2])))
    model.add(Dropout(0.2))
    model.add(GRU(units=96, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(GRU(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(GRU(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))
    model.compile(loss="mean_squared_error", optimizer="adam")
    print(model.summary())
    return model