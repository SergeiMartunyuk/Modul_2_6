
field = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
import random
def password():     # выпадение пароля из field
    dropped = random.choice(field)
    return dropped
step = password()
index = 0
list_ = []
while True:             # поиск кратности числа
    if index == len(field):
        break
    elif step % field[index] != 0:
        index += 1
        continue
    else:
        step % field[index] == 0
        list_.append(field[index])
        index += 1
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] #суммы крат чисел
a = list_
unique_pairs = set()
for k in range(len(a)):
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            if elements[i] + elements[j] == a[k]:
                unique_pairs.add((elements[i], elements[j]))
unique_sort = sorted(unique_pairs)
print(step)
print(list_)
print(*unique_sort)