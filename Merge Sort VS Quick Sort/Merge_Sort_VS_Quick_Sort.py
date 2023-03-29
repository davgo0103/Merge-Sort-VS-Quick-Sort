
import random
import time

def merge_sort(var):
    if len(var) <= 1:
        return var
    
    mid = len(var) // 2
    left = merge_sort(var[:mid])
    right = merge_sort(var[mid:])
    
    return merge(left, right)

def merge(left, right): #進行合併
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result += left[i:]
    result += right[j:]
    
    
    return result

def quick_sort(var):
    if len(var) <= 1:
        return var
    
    pivot = var[len(var) // 2]
    left = []
    middle = []
    right = []

    for x in var:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    
    return quick_sort(left) + middle + quick_sort(right)
    
# 產生1000筆隨機數字的測試資料
data = []
for i in range(1000):
    num = random.randint(0, 1000000)
    data.append(num)

# 測試合併排序效率
start_time = time.time()
merge_sort(data)
end_time = time.time()
print("Merge Sort: %f sec" % (end_time - start_time))

# 測試快速排序效率
start_time = time.time()
quick_sort(data)
end_time = time.time()
print("Quick Sort: %f sec" % (end_time - start_time))