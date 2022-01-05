import csv


def write_csv():
    data = [
        {
            'first_name': 'Harvey',
            'last_name': 'Specter'
        },
        {
            'first_name': 'Michael',
            'last_name': 'Ross'
        }
    ]

    with open('output_dict.tsv', 'w') as csvfile:
        csv_writer = csv.DictWriter(csvfile, delimiter='\t', fieldnames=['first_name', 'last_name'])
        csv_writer.writeheader()
        csv_writer.writerows(data)


if __name__ == '__main__':
    write_csv()
