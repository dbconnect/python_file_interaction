import csv


def read_csv():
    with open('persons.csv') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = []
        for line in csv_reader:
            data.append(line)
        print(data)
        print(data[0]['address'])


if __name__ == '__main__':
    read_csv()
