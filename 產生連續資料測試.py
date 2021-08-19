import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def generate_data(series):
    x = []
    y = []
    for i in range(len(series)):
        if i > 7 and len(series[i: i + 8, :]) == 8:
            x.append(series[i - 8:i, :])
            y.append(series[i: i + 8, :])
    return x, y


def min_max_scale(df):
    scaler = MinMaxScaler()
    new_df = scaler.fit_transform(df)
    return new_df, scaler


if __name__ == '__main__':
    df = pd.read_csv('2017_2020.csv')
    col_name = ['MB_TEMP', 'WD_HR', 'WIND_DIREC', 'WIND_SPEED', 'RINFLL', 'PM2.5']
    data = df[col_name]
    data_after_scale, scaler = min_max_scale(data)

    print(f"data_after_scale shape : {data_after_scale.shape}")

    x, y = generate_data(data_after_scale)
    x = np.array(x)
    # print(x.shape)
    x = x.reshape(-1, 1, 6)
    print(x.shape)














    # 儲存標準化後的資料
    # new_df = pd.DataFrame(data_after_scale, columns=col_name)
    # new_df.to_csv('test.csv', index=False)
