# Bubble Sort

v = [1, 4, 2, 5, 3, 9, 12, 6, 11, 7, 10, 8]


def bubble_sort(v):
    for i in range(len(v)-1):
        for j in range(len(v)-i-1):
            if (v[j] > v[j+1]):
                v[j], v[j+1] = v[j+1], v[j]

    return print(v)


bubble_sort(v)


# Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide a lista em duas metades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursivamente, aplica o Merge Sort nas duas metades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combina as duas metades ordenadas
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Combina as duas listas ordenadas em uma única lista ordenada
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Adiciona os elementos restantes da lista da esquerda, se houver
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Adiciona os elementos restantes da lista da direita, se houver
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


arr = [4, 7, 2, 1, 5, 9, 3, 8, 6]
sorted_arr = merge_sort(arr)
print(sorted_arr)
