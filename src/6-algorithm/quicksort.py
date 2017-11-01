# coding=utf-8
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        index = 0  # 取第一个元素为枢纽
        # index = len(array) / 2  # 取中间元素为枢纽
        pivot = array[index]
        array = array[:index] + array[index + 1:]
        less = [i for i in array if i < pivot]
        greater = [i for i in array if i >= pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print quicksort([5, 4, 3, 2, 1])
