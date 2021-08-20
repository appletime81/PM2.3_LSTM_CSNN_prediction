import pandas as pd
import matplotlib.pyplot as plt
from lstm_model import lstm_model
from data_split import generate_data, min_max_scale
from datetime import datetime
import time


def main():
    # generate data
    df = pd.read_csv('new.csv')
    col_name = ['MB_TEMP', 'WD_HR', 'WIND_DIREC', 'WIND_SPEED', 'RINFLL', 'PM2.5']
    data = df[col_name]
    data_after_scale, scaler = min_max_scale(data)
    now = datetime.now().strftime("%Y_%m_%d_%H%M")  # 檔名時間

    x, y = generate_data(data_after_scale, 1, 1)
    x_train = x[:26114, :, :]
    print(x_train.shape)
    x_test = x[26114:, :, :]
    y_train = y[:26114, :]
    y_test = y[26114:, :]

    # start training
    model = lstm_model(x_train)
    history = model.fit(x_train, y_train, epochs=500, batch_size=256, verbose=1)
    model.save(f'lstm_{now}.h5')

    # plot training processing
    plt.figure(figsize=(15, 8))
    plt.xlabel('Epoch')
    plt.ylabel('Mean Square Error')
    plt.plot(history.epoch, history.history['loss'], label='Train Loss')
    # plt.plot(history.epoch, history.history['val_loss'], label='Val loss')
    plt.title('Model loss')
    plt.legend()
    plt.savefig(f"training_result_{now}.png")
    plt.show()


if __name__ == '__main__':
    start = time.time()
    main()
    print(f'總時間: {time.time() - start}秒')
