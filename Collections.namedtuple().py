from collections import namedtuple
n = int(input())
col = input().split()
avg_marks = 0
for _ in range(n):
    cols_fields = namedtuple('my_student', col)
    MARKS, CLASS, NAME, ID = input().split()
    my_student = cols_fields(MARKS, CLASS, NAME, ID)
    avg_marks = avg_marks+int(my_student.MARKS)
print((avg_marks / n))
