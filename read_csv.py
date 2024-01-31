import csv

file_obj = open('customers.csv','r')

csv_file = csv.reader(file_obj)

#this will skip the first record which is the header
next(csv_file)

for rec in csv_file:
    #print(rec)
    print(f"First Name: {rec[1]} Last Name: {rec[2]}")
    input()