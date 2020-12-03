import random
import time

def generate_numbers(set, n):
    for i in range(n):
        set.append(random.randint(-200, 200))

def quick_sort(set, left, right):
    i = int((left+right)/2)
    pivot = set[i]
    set[i] = set[right]
    i = left
    j = left
    while i < right:
        if set[i] < pivot:
            set[i], set[j] = set[j], set[i]
            j += 1
        i += 1
    set[right] = set[j]
    set[j] = pivot
    if left < j - 1:
        quick_sort(set, left, j - 1)
    if j + 1 < right:
        quick_sort(set, j + 1, right)


small_set = []
big_set = []

start_time_small = time.perf_counter()

generate_numbers(small_set, 100)
print("Maly zbior liczb")
print("Przed sortowaniem: ")
print(small_set)
quick_sort(small_set, 0, len(small_set)-1)
print("Po sortowaniu: ")
print(small_set)

end_time_small = time.perf_counter()
print(f'Czas: {end_time_small - start_time_small} s')

print("-----------------------")

start_time_big = time.perf_counter()

generate_numbers(big_set, 100000)
print("Duzy zbior liczb")
print("Przed sortowaniem: ")
print(big_set)
quick_sort(big_set, 0, len(big_set)-1)
print("Po sortowaniu: ")
print(big_set)

end_time_big = time.perf_counter()
print(f'Czas: {end_time_big - start_time_big} s')