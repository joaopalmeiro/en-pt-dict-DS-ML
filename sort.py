import csv

# from operator import itemgetter

PATH = "data/dict.csv"

reader = csv.reader(open(PATH), delimiter=",")
header = next(reader)

# sorting_criteria = itemgetter(0, 1)
sorting_criteria = lambda row: (row[0].casefold(), row[1].casefold())

sorted_reader = sorted(reader, key=sorting_criteria, reverse=False)

with open(PATH, "w") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(header)
    for row in sorted_reader:
        writer.writerow(row)

print("\n✨ Done!")
