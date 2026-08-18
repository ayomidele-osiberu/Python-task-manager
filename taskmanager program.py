import csv



print("Welcome to the task management system. Please choose your options below")
tasks = input("Please input your task")
choice = input(" WOuld you like to add more tasks")
if choice == "Yes":
    tasks = input("Please input your task")
else:
    print("End of input")

with open("Tasktracker.csv", "a", newline = "" )as file:
    writer = csv.writer(file)
    writer.writerow([tasks])
        

