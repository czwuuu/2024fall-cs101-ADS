#冒泡排序
def bubble_sort(array, reverse = False):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    if reverse:
        array.reverse()
    return array

#改良的冒泡排序
def improved_bubble_sort(array):
    flag = True
    for i in range(len(array)-1):
        if flag:
            flag = False
            for j in range(len(array)-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    flag = True
        else:
            break
    return array

#选择排序
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

#插入排序
def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i
        while j > 0 and array[j-1] > temp:
            array[j] = array[j-1]
            j -= 1
        array[j] = temp
    return array

#希尔排序
def shell_sort(array):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2
    return array

#归并排序
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

#快速排序
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = [x for x in array[1:] if x < pivot]
        right = [x for x in array[1:] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

#堆排序
import heapq
def heap_sort(array):
    n = len(array)
    n_arr = array.copy()
    heapq.heapify(n_arr)
    for i in range(n):
        array[i] = heapq.heappop(n_arr)
    return array

#计数排序
def counting_sort(array):
    max_val = max(array)
    count = [0] * (max_val + 1)
    for num in array:
        count[num] += 1
    sorted_arr = []
    for i in range(max_val + 1):
        sorted_arr.extend([i] * count[i])
    array[:] = sorted_arr[:]
    return array





#测试模块
def measure_performance():
    import timeit
    import random

    global global_arr
    global_arr = [random.randint(1, 100) for _ in range(1000)]

    time_pysort = timeit.timeit('global_arr.copy().sort()',
                                globals=globals(), number=10)
    print(f'pysort:{time_pysort:.6f}')

    time_bubble = timeit.timeit('bubble_sort(global_arr.copy())',
                                globals=globals(), number=10)
    print(f'bubble:{time_bubble:.6f}')

    time_selection = timeit.timeit('selection_sort(global_arr.copy())',
                                  globals=globals(), number=10)
    print(f'selection:{time_selection:.6f}')
    
    time_insertion = timeit.timeit('insertion_sort(global_arr.copy())',
                                  globals=globals(), number=10)
    print(f'insertion:{time_insertion:.6f}')

    time_shell = timeit.timeit('shell_sort(global_arr.copy())',
                                  globals=globals(), number=10)
    print(f'shell:{time_shell:.6f}')
    
    time_merge = timeit.timeit('merge_sort(global_arr.copy())',
                                  globals=globals(), number=10)
    print(f'merge:{time_merge:.6f}')

    time_quick = timeit.timeit('quick_sort(global_arr.copy())',
                                  globals=globals(), number=10)
    print(f'quick:{time_quick:.6f}')
    
    time_heap = timeit.timeit('heap_sort(global_arr.copy())',
                                  globals=globals(), number=10)
    print(f'heap:{time_heap:.6f}')
    
    time_counting = timeit.timeit('counting_sort(global_arr.copy())',
                                  globals=globals(), number=10)
    print(f'counting:{time_counting:.6f}')

#主函数
if __name__ == '__main__':
    measure_performance()