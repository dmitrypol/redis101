#   https://realpython.com/python-csv/
import csv
import random

with open('tmp/data.csv', mode='w') as log_file:
    csv_writer = csv.writer(log_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for lp in range(100000):
        ip = ".".join(map(str, (random.randint(0, 5) 
                        for _ in range(4))))
        csv_writer.writerow([ip])
