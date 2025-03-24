cet_students = {"Alice", "Bob", "Charlie", "David", "Eva"}
jee_students = {"Bob", "David", "Frank", "Grace", "Hannah"}
neet_students = {"Charlie", "Eva", "Grace", "Hannah", "Isla"}
# Union operation: Students who have enrolled in at least one exam/course
all_students = cet_students.union(jee_students, neet_students)
print("All students enrolled in any exam/course (Union):/n", all_students)
# Intersection operation: Students who have enrolled in both CET and JEE
cet_jee_students = cet_students.intersection(jee_students)
print("Students enrolled in both CET and JEE (Intersection):/n", cet_jee_students)
# Difference operation: Students who are enrolled in CET but not in JEE
cet_only_students = cet_students.difference(jee_students)
print("Students enrolled only in CET (Difference):/n", cet_only_students)