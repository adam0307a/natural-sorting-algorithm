import time
import random

# Quicksort algoritması
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    smaller = [x for x in arr[:-1] if x <= pivot]
    larger = [x for x in arr[:-1] if x > pivot]
    return quicksort(smaller) + [pivot] + quicksort(larger)

# Kendi algoritmanız
def sort_by_digit_groups(numbers):
    # Gruplandırma
    groups = {}
    for number in numbers:
        digit_count = len(str(number))
        if digit_count not in groups:
            groups[digit_count] = []
        groups[digit_count].append(number)

    # Grupları sıralama
    sorted_groups = sorted(groups.items())

    # Grupları sıralama ve birleştirme
    result = []
    for _, group in sorted_groups:
        result.extend(quicksort(group))

    return result

# Performans ölçüm fonksiyonu
def measure_time(func, data):
    start_time = time.time()
    result = func(data)
    end_time = time.time()
    return result, end_time - start_time

# 10,000 elemanlı rastgele liste oluşturma
numbers = [random.randint(1, 99999) for _ in range(1000000)]
# Quicksort ölçümü
qs_result, qs_time = measure_time(quicksort, numbers)

# Kendi algoritmanızın ölçümü
custom_result, custom_time = measure_time(sort_by_digit_groups, numbers)

# Sonuçları yazdırma
print("Quicksort Süre: {:.6f} saniye".format(qs_time))
print("Kendi Algoritmanız Süre: {:.6f} saniye".format(custom_time))

# Performans karşılaştırması
if qs_time < custom_time:
    print("Quicksort daha hızlı!")
elif qs_time > custom_time:
    print("Kendi algoritmanız daha hızlı!")
else:
    print("İkisi aynı hızda!")
