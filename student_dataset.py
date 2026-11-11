import csv

# CUL-CYB 371: Data Mining and Data Warehousing
# Fictional student dataset generator

students = [
    ["CUL2026001", "Cyber Security", 200, 92, 84],
    ["CUL2026002", "Computer Science", 200, 88, 76],
    ["CUL2026003", "Software Engineering", 200, 95, 91],
    ["CUL2026004", "Information Technology", 100, 79, 68],
    ["CUL2026005", "Cyber Security", 300, 86, 73],
    ["CUL2026006", "Computer Science", 100, 90, 82],
    ["CUL2026007", "Data Science", 200, 83, 79],
    ["CUL2026008", "Software Engineering", 300, 97, 88],
    ["CUL2026009", "Information Technology", 200, 75, 65],
    ["CUL2026010", "Cyber Security", 100, 89, 93],
    ["CUL2026011", "Data Science", 300, 91, 86],
    ["CUL2026012", "Computer Science", 400, 80, 72],
]

headers = [
    "Student ID",
    "Department",
    "Level",
    "Attendance Percentage",
    "Average Examination Score",
]

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(students)

print("Dataset created successfully: students.csv")
