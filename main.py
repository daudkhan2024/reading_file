# Reading a file
employee_file = open("employes.txt","r")
print(employee_file.readline()[2])
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.close())
employee_file.close()

