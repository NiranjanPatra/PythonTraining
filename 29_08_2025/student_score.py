# Assignment 1
student_score = []
student_score.extend([85, 90, 78, 92, 88])
print("After add all scores =", student_score)

student_score.insert(5,80)
print("After insert 80 =", student_score)

student_score.remove(92)
print("After remove 92 =", student_score)

student_score.sort()
print("After sort =", student_score)

student_score.reverse()
print("After reverse =", student_score)

print("max = ", student_score[0])
print("min = ", student_score[len(student_score)-1])

if 90 in student_score:
    print("90 is in the list")
else:
    print("90 is not in the list")

total = 0
for item in student_score:
    total += item;
print("total = ", total)

print("First three scores =", student_score[:3])

last_index = len(student_score)-1
print("Last element = ", student_score[last_index])

student_score[2] = student_score[last_index]
print("New score = ", student_score[2])

new_student_list = student_score.copy()
print("Update student list", new_student_list)

