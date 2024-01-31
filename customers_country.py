import csv

infile = open('customers.csv','r')
outfile = open('customer_country.csv','w')

read_csv_file = csv.reader(infile)

next(read_csv_file)

outfile.write("Full Name, Country \n")

for row in read_csv_file:
    outfile.write(f"{row[1]} {row[2]}, {row[4]} \n")

outfile.close()
    