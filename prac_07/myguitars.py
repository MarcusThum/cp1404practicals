from guitar import Guitar
import csv

def main():
    with open('guitars.csv') as csv_file:
        guitar_list = []
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            guitar_list.append(Guitar(row[0], int(row[1]), float(row[2])))

        guitar_list.sort()
        for guitar in guitar_list:
            print(guitar)

main()