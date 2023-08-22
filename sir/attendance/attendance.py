f = open("C:\\Users\\NIYA ROSE JOY\\OneDrive\\Documents\\python\\sir\\attendance\\present.txt", "r")
w = open("C:\\Users\\NIYA ROSE JOY\\OneDrive\\Documents\\python\\sir\\attendance\\absent.txt", "r")

total_students = set()
present_students = set()

for line in f:
    total_students.add(line.rstrip("\n"))

print(total_students)

for line in w:
    present_students.add(line.rstrip("\n"))

print(present_students)

absent_students = total_students - present_students
print(absent_students)


