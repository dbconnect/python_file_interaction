import csv


def write_csv():
    data = [
        ['first_name', 'last_name'],
        ['Harvey', 'Specter'],
        ['Michael', 'Ross']
    ]

    with open('output.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)

    with open('output_param.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';', lineterminator='\n**\n')
        csv_writer.writerows(data)


if __name__ == '__main__':
    write_csv()
