import csv

data = None

def load_d():
    csvfile = open('士林_2018.csv', newline='')
    return csv.reader(csvfile)

data = test()
for row in data:
    print(row)

