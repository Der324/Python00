# Writing & Appending to files
# Don't run the code is in append
# Writing it overrides, it can also be used to create a new file

employee_file = open("employees1.txt", "w")

employee_file.write("\nAllan - Human Resource")

employee_file.close()


employee_file = open("index.html", "w")

employee_file.write("<p>This is HTML</p>")

employee_file.close()