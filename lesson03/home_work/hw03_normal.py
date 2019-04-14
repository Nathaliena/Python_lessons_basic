# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    a, b = 1, 1
    lst = [1, ]
    for i in range(m):
        a, b = b, a + b
        lst.append(a)

    return lst[n - 1:m]


print(fibonacci(1,3))

output: [1, 1, 2]

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for j in range(0,len(origin_list)-1):
        for i in range(0,len(origin_list)-j-1):
            if origin_list[i] < origin_list[i+1]:
                origin_list[i],origin_list[i + 1] = origin_list[i + 1], origin_list[i]
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']


def filter(n, elements):
    new_lst = []
    for i in elements:
        if i == n:
            new_lst.append(i)
    return new_lst


print(filter("мак", mixed))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


import math

def top(x1, y1, x2 ,y2, x3 , y3, x4, y4):
    a=math.sqrt((x2-x1)+(y2-y1))
    b=math.sqrt((x3-x2)+(y3-y2))
    c=math.sqrt((x3-x4)+(y3-y4))
    d=math.sqrt((x4-x1)+(y4-y1))
    if a==c and b==d:
        return a,b,c,d

    else:
        return a

print(top(2,6,4,7,8,10,6,9))

