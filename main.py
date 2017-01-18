from database import *
list_all = PeopleList.import_csv()

students_list = []
mentors_list = []
employees_list = []

for obj in list_all:
    if obj.__class__.__name__ == "Student":
        students_list.append(obj)

for obj in list_all:
    if obj.__class__.__name__ == "Employee":
        employees_list.append(obj)

for obj in list_all:
    if obj.__class__.__name__ == "Mentor":
        mentors_list.append(obj)

print(students_list)
print(mentors_list)
print(employees_list)
