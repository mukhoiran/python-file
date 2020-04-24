import csv

rows = [
    {'name' : 'Bruce Lee','skill' : 'Tiger Kick','power' : 100},
    {'name' : 'IP Man','skill' : 'Wing chun','power' : 200},
]

with open('data.csv','a') as csvfile:
    fields = ['name','skill','power']
    writer = csv.DictWriter(csvfile,fieldnames = fields)

    writer.writeheader()
    writer.writerows(rows)
