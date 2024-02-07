import csv

infile = open('employee_data.csv','r')

read_csv_file = csv.reader(infile)

next(read_csv_file)

efficient_employee = []
inefficient_employee = []

employee_over_40 = []
employee_over_30 = []
employee_over_20 = []

over_40 = 0
over_30 = 0
over_20 = 0

for row in read_csv_file:
    efficiency = int(row[5])/int(row[4])
    age = int(row[2])
    if efficiency > 2:
        efficient_employee.append(row[1])
    elif efficiency < 1:
        inefficient_employee.append(row[1])

    if age >= 40:
        employee_over_40.append(row[1])
        over_40 += 1
    elif age >= 30:
        employee_over_30.append(row[1])
        over_30 += 1
    else:
        employee_over_20.append(row[1])
        over_20 += 1

print('Highly Efficient Individuals:')
for name in efficient_employee:
    print(name)

print()
print()

print('Low Efficiency Individuals:')
for name in inefficient_employee:
    print(name)

print()
print()

print('Employees in their 40s')
for name in employee_over_40:
    print(name)

print()

print(f"Total number of employees in their 40s: {over_40}")

print()
print()

print('Employees in their 30s')
for name in employee_over_30:
    print(name)

print()

print(f"Total number of employees in their 30s: {over_30}")

print()
print()

print('Employees in their 20s')
for name in employee_over_20:
    print(name)

print()

print(f"Total number of employees in their 20s: {over_20}")

