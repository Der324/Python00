# Reading Files:
# R(reading)
# W(writing)
# R+(read & write)
# A(Append)

employee_file = open("employees.txt", "r")

print(employee_file.readlines()[0])

employee_file.close()


employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)

employee_file.close()