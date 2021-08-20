import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def generate_data(series, n_past, n_future):
    x = []
    y = []
    for i in range(n_past, len(series) - n_future + 1):
        x.append(series[i - n_past:i, 0:series.shape[1]])
        y.append(series[i + n_future - 1:i + n_future, 5])

    x = np.array(x)
    y = np.array(y)
    return x, y


def min_max_scale(df):
    scaler = MinMaxScaler()
    new_df = scaler.fit_transform(df)
    return new_df, scaler


# if __name__ == '__main__':
#     df = pd.read_csv('2017_2020.csv')
#     col_name = ['MB_TEMP', 'WD_HR', 'WIND_DIREC', 'WIND_SPEED', 'RINFLL', 'PM2.5']
#     data = df[col_name]
#     data_after_scale, scaler = min_max_scale(data)
#
#     x, y = generate_data(data_after_scale, 1, 1)
#     x_train = x[:int(x.shape[0] * 0.8), :, :]
#     x_test = x[int(x.shape[0] * 0.8):, :, :]
#     y_train = y[:int(x.shape[0] * 0.8), :]
#     y_test = y[int(x.shape[0] * 0.8):, :]
#
#
#     print(x_train.shape)
#     print(x_test.shape)
#     print(y_train.shape)
#     print(y_test.shape)

