import csv


def read_csv():
    with open('persons.csv') as csvfile:
        csv_reader = csv.reader(csvfile)
        data = []
        for line in csv_reader:
            data.append(line)
        print(data)
        print(data[1][1])


if __name__ == '__main__':
    read_csv()

