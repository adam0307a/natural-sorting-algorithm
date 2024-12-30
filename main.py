def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]  # Pivot eleman olarak son eleman seçiliyor
    smaller = [x for x in arr[:-1] if x <= pivot]
    larger = [x for x in arr[:-1] if x > pivot]
    return quicksort(smaller) + [pivot] + quicksort(larger)

def sort_by_digit_groups(numbers):
    # 1. Gruplandırma
    groups = {}
    for number in numbers:
        digit_count = len(str(number))  # Basamak sayısını hesapla
        if digit_count not in groups:
            groups[digit_count] = []
        groups[digit_count].append(number)
    
    # 2. Grupların sıralanması (basamak sayısına göre)
    sorted_groups = sorted(groups.items())  # (basamak sayısı, grup) çiftlerini sıralar
    
    # 3. Her grubun quicksort ile sıralanması
    result = []
    for _, group in sorted_groups:
        result.extend(quicksort(group))  # Sıralanan grubu sonuca ekle
    
    return result

# Örnek kullanım
numbers = [3, 2, 4, 22, 53, 11, 454, 987, 111]
sorted_numbers = sort_by_digit_groups(numbers)
print("Sıralı Dizi:", sorted_numbers)
