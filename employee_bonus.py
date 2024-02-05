import csv

infile = open('employee_data.csv','r')

read_csv_file = csv.reader(infile)

next(read_csv_file)

for row in read_csv_file:
    salary = float(row[3])
    bonus = salary * float(row[7])
    total_pay = salary + bonus
    print(f"Name: {row[1]}")
    print(f"{'Salary:':7} $  {salary:>,.2f}")
    print(f"{'Bonus:':7} $   {bonus:>,.2f}")
    print(f"{'Pay:':7} $  {total_pay:>,.2f}\n")
    input()

