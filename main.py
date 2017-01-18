from database import *
import ui
import user

list_all = PeopleList()
list_all.people_list = list_all.import_csv()

print(list_all.people_list)

students_list = []
mentors_list = []
employees_list = []

for obj in list_all.people_list:
    if obj.__class__.__name__ == "Student":
        students_list.append(obj)

for obj in list_all.people_list:
    if obj.__class__.__name__ == "Employee":
        employees_list.append(obj)

for obj in list_all.people_list:
    if obj.__class__.__name__ == "Mentor":
        mentors_list.append(obj)

print(students_list)
print(mentors_list)
print(employees_list)

inputs = ui.get_inputs(["username: ", "Fullname: "], "Provide personal information")
print(inputs)
list_all.add("Mentor", inputs)

print(list_all.get_list("Student"))
print(list_all.people_list)
