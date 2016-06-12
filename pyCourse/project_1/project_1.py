from statistics import *
from alumnFunc import *

firstRun = True

print("\n\n=========================================\n")
print("\tWelcome to Grade Central\n\n\t[1] - Enter Grade\n\t[2] - Remove Student\n\t[3] - View Student\n\t[4] - Student Avarage Grades\n\t[5] - Exit\n\n")

while True:
	if not firstRun:
		print("\n[1]Enter Grade - [2]Remove Student - [3]View Student - [4]Student Avarage Grades - [5]Exit")
	firstRun = False

	action = int( input("What would you like to do? (Enter a number): ") )
	if action == 1:
		addGrade()
	elif action == 2:
		removeStudent()
	elif action == 3:
		viewStudent()
	elif action == 4:
		studentAvarage()
	elif action == 5:
		exit()


