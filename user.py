import csv

rows = []

with open('person.csv','r') as csvfile:
    # csvreader = csv.reader(csvfile)
    # for row in csvreader:
    #     rows.append(row)
    csvreader = csv.DictReader(csvfile)
    rows = list(csvreader)
    print('Total rows :', csvreader.line_num)

# print(rows)
for row in rows[:5]:
    print(row['first_name']+ " - "+row['email'])
