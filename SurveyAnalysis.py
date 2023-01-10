import csv

#Opens CSV
csv_file = open('Sample.csv', 'r')

#Creates Iterator to read through CSV line by line
csv_reader = csv.reader(csv_file)

#For each row
for row in csv_reader:
    print (row)

csv_file.close()