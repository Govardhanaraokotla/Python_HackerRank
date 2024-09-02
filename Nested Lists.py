if __name__ == '__main__':
    student = []
    values = []
    names =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name, score])

    for item in student:
        values.append(item[1])
    values=list(set(values))
    values.sort()

    for item in student:
        if item[1] == values[1]:
            names.append(item[0])
    names.sort()

    for name in names:
        print(name)
