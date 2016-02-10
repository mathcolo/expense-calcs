import csv
import sys

total = 0.0

with open(sys.argv[1], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	next(reader, None)
	for row in reader:
		if float(row[4]) < 0.0:
			total += float(row[4])

print(round(total,2))


