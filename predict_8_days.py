import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from data_split import generate_data, min_max_scale, get_y_scaler


df = pd.read_csv('new.csv')
col_name = ['MB_TEMP', 'WD_HR', 'WIND_DIREC', 'WIND_SPEED', 'RINFLL', 'PM2.5']
data = df[col_name]
data_before_scale = data.to_numpy()
y_scaler = get_y_scaler(data)

# generate data after scale
data_after_scale, scaler = min_max_scale(data)
x, y = generate_data(data_after_scale, 1, 1)
x_train = x[:26114, :, :]
x_test = x[26114:, :, :]
y_train = y[:26114, :]
y_test = y[26114:, :]

# split original data
data_before_scale = data_before_scale.reshape(-1, 1, 6)
y_test_data_before_scale = data_before_scale[26114:, :, 5:6]
print(y_test_data_before_scale[-8:, :, :].shape)


model = load_model('lstm_2021_08_20_1300.h5')
predict_result = model.predict(x_test[-8:, :, :])
predict_result = y_scaler.inverse_transform(predict_result)

# plot predict result
plt.figure(figsize=(25, 8))
plt.ylim(0, 25)
plt.plot(range(0, y_test_data_before_scale[-8:, :, :].shape[0]), y_test_data_before_scale[-8:, :, :].reshape(-1, 1))
plt.plot(range(0, predict_result.shape[0]), predict_result)
plt.ylabel('PM2.5')
plt.xlabel('day')
plt.savefig("8_days_predict.png", dpi=300)
plt.show()
