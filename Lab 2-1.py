a = int(input("Сколько всего будет оценок?"))
marks = []
for i in range(a):
    mark = int(input("Введите оценку: "))
    marks.append(mark)
print("Введенные оценки:", marks)
average = sum(marks) / a
print("Средняя оценка за урок:", average)


