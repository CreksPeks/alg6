
# lesson 6

# Интерполиционный поиск

import random

arr = []
n = 50
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)
to_search = random.randint(1, 100)
answer = -1

# ==================================

arr.sort()
left = 0
right = len(arr) - 1

while (left <= right) and (to_search >= arr[left]) and (to_search <= arr[right]):
    part1 = float(right - left) / (arr[right] - arr[left])
    part2 = to_search - arr[left]
    index = left + int(part1 * part2)

    if arr[index] == to_search:
        answer = index
        break
    if arr[index] < to_search:
        left = index + 1
    else:
        right = index - 1

# ==================================

if answer != -1:
    print(f"Эл-т есть,индекс : {answer}")
else:
    print("Эл-та в списке нет")

print(arr)
print(number)


# решето Эротосфена

n = 50
for i in range(1, n):
    arr.append(i)

arr[1] = 0

# ===========================================

for i in range(n):
    if arr[i] != 0:
        j = i * 2
        while j < n:
            arr[j] = 0
            j += i

# ===========================================

for elem in arr:
    if elem != 0:
        print(elem, end=" ")



# поиск подстроки в строке

str_where = "hello world"
str_find = " wor"

index_where = 0
index_find = 0
len_where = len(str_where)
len_find = len(str_find)
while (index_where <= (len_where - len_find)) and (index_find < len_find):
    if str_where[index_where + index_find] == str_find[index_find]:
        index_find += 1
    else:
        index_where += 1
        index_find = 0

print(f"'{str_where}'")
print(f"'{str_find}'")

if index_find == len_find:
    print(f"такая подстрока есть, ее начало тут: {index_where}")
else:
    print("Такой подстроки нет.")




# ну вот, повторил )))