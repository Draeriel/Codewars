def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    menor = min(numbers)
    numbers.remove(menor)
    return numbers