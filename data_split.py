import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler


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
    scaler = StandardScaler()
    new_df = scaler.fit_transform(df)
    return new_df, scaler


def get_y_scaler(df):
    df = df[['PM2.5']]
    new_df, scaler = min_max_scale(df)
    return scaler


# if __name__ == '__main__':
    # df = pd.read_csv('new.csv')
    # col_name = ['MB_TEMP', 'WD_HR', 'WIND_DIREC', 'WIND_SPEED', 'RINFLL', 'PM2.5']
    # data = df[col_name]
    # scaler = get_y_scaler(data)

