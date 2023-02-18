import pandas as pd

students = pd.read_excel("students.xlsx")

admission = ["yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","no","no","no","no","no",]
students['admission'] = admission

type = ["stud","stud","stud","stud","stud","stud","stud","stud","stud","stud","stud","stud","stud","stud","stud",]
students['type'] = type

print(students)

stats = students['avg'].agg(['min', 'max', 'mean', 'median'])
print(f"Stat:\n{stats}")


first_try = len(students[students["attempts"] == 1])
print(f"Attempts count:{first_try}")

name_series = students['name'].squeeze()
print(name_series)
