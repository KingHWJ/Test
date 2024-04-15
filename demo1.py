for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i} x {j} = {i*j}' ,end="\t")
    print("")


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 标记是否有元素进行了交换
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # 如果本轮遍历没有发生任何交换，表示数组已经有序，退出循环
        if not swapped:
            break
    return arr

# 示例
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("排序后的数组：", sorted_arr)

print("aaaa")
