# from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator
import numpy as np

# define dataset
series = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])


def generate_data(series):
    x = []
    y = []
    for i in range(len(series)):
        if i > 7 and len(series[i: i + 8]) == 8:
            x.append(series[i - 8:i])
            y.append(series[i: i + 8])
    print(x)
    print(y)

generate_data(series)
