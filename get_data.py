import csv
import pandas as pd


def load_csv_file(file):
    f = open(file, newline='')
    return csv.reader(f)


def generate_datafrmae(rows, file_name):
    AMB_TEMP = []
    WD_HR = []
    WIND_DIREC = []
    WIND_SPEED = []
    RAINFALL = []
    DATE = []
    PM25 = []
    index = 1

    for row in rows:
        if 'AMB_TEMP' in row[2]:
            AMB_TEMP += row[3:]
            date_list = row[index].split(' ')[0]
            # print(date_list)
            DATE += [row[index][:len(date_list)] + f' {i}:00' for i in range(24)]
        elif 'WD_HR' in row[2]:
            WD_HR += row[3:]
        elif 'WIND_DIREC' in row[2]:
            WIND_DIREC += row[3:]
        elif 'WIND_SPEED' in row[2]:
            WIND_SPEED += row[3:]
        elif 'RAINFALL' in row[2]:
            RAINFALL += row[3:]
        elif 'PM2.5' in row[2]:
            PM25 += row[3:]

    data_dict = {
        'DATE': DATE,
        'AMB_TEMP': AMB_TEMP,
        'WD_HR': WD_HR,
        'WIND_DIREC': WIND_DIREC,
        'WIND_SPEED': WIND_SPEED,
        'RAINFALL': RAINFALL,
        'PM2.5': PM25
    }

    df = pd.DataFrame(data_dict)
    df.to_csv(file_name[3:], index=False)


if __name__ == '__main__':
    csv_file = '士林_2020.csv'
    rows = load_csv_file(csv_file)
    generate_datafrmae(rows, csv_file)
