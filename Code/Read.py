import csv

ReadFile = open('Data.csv')
reader = csv.reader(ReadFile, delimiter=';')
object = list(reader)
Products = {}

for line in object:
    n = 3
    if line[1] == 'ADD':
        while n < len(line):
            if line[n] == "":
                continue
            temp = line[n].split(':')
            Products[temp[0]] = Products.get(temp[0], 0) + int(temp[1])
            n += 1

    else:
        while n < len(line):
            if line[n] == "":
                continue
            temp = line[n].split(':')
            Products[temp[0]] = Products.get(temp[0], 0) - int(temp[1])
            n += 1

print(Products)

ReadFile.close()

