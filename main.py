import time
import matplotlib.pyplot as plt

def insertion_sort(a: list, n: int) -> float:
    start_time = time.time()
    for i in range(n):
        x = a[i]
        j = i - 1
        while j >= 0 and x < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
    stop_time = time.time()
    return stop_time - start_time
    

def selection_sort(a: list, n: int) -> float:
    start_time = time.time()
    for i in range(n):
        min_pos = i
        for j in range(i + 1, n):
            if a[j] < a[min_pos]:
                min_pos = j
        a[min_pos], a[i] = a[i], a[min_pos]
    stop_time = time.time()
    return stop_time - start_time

def interchange_sort(a: list, n: int) -> float:
    start_time = time.time()
    for i in range(n):
        for j in range(i + 1, n):
            if a[j] < a[i]:
                a[i], a[j] = a[j], a[i]
    stop_time = time.time()
    return stop_time - start_time

def heapify(a: list, i: int, n: int) -> None:
    if i * 2 + 1 >= n:
        return
    if i * 2 + 2 >= n or a[i * 2 + 1] > a[i * 2 + 2]:
        if a[i] < a[i * 2 + 1]:
            a[i], a[i * 2 + 1] = a[i * 2 + 1], a[i]
            heapify(a, i * 2 + 1, n)
    else:
        if a[i] < a[i * 2 + 2]:
            a[i], a[i * 2 + 2] = a[i * 2 + 2], a[i]
            heapify(a, i * 2 + 2, n)

def heap_sort(a: list, n: int) -> float:
    start_time = time.time()
    for i in range(n // 2, -1, -1):
        heapify(a, i, n)
    for i in range(n - 1, -1, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, 0, i)
    stop_time = time.time()
    return stop_time - start_time

def quick_sort(a: list, l: int, r: int) -> float:
    start_time = time.time()
    if l >= r:
        return
    x = a[(l + r) // 2]
    i, j = l, r
    while i < j:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    quick_sort(a, l, j)
    quick_sort(a, i, r)
    stop_time = time.time()
    return stop_time - start_time

def merge_arr(a: list, l: int, r: int) -> None:
    mid = (l + r) // 2
    i, j = l, mid + 1
    temp = []
    while i <= mid and j <= r:
        if a[i] < a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1
    while i <= mid:
        temp.append(a[i])
        i += 1
    while j <= r:
        temp.append(a[j])
        j += 1
    for i in range(len(temp)):
        a[l + i] = temp[i]

def merge_sort(a: list, l: int, r: int) -> float:
    start_time = time.time()
    if l >= r:
        return
    mid = (l + r) // 2
    merge_sort(a, l, mid)
    merge_sort(a, mid + 1, r)
    merge_arr(a, l, r)
    stop_time = time.time()
    return stop_time - start_time

def counting_sort(a: list, n: int) -> float:
    start_time = time.time()
    mn, mx = a[0], a[0]
    for i in range(n):
        mn = min(mn, a[i])
    for i in range(n):
        if mn < 0:
            a[i] -= mn
        mx = max(mx, a[i])
    cnt = [0] * (mx + 1)
    for i in a:
        cnt[i] += 1
    for i in range(1, mx + 1):
        cnt[i] = cnt[i - 1] + cnt[i]
    temp = a.copy()
    for i in temp:
        a[cnt[i] - 1] = i + (mn if mn < 0 else 0)
        cnt[i] -= 1
    stop_time = time.time()
    return stop_time - start_time

def get_digit(a: int, k: int) -> int:
    while k:
        a //= 10
        k -= 1
    return a % 10

def radix_sort_kth_digit(a: list, n: int, k: int) -> None:
    b = [[] for _ in range(10)]
    for i in range(n):
        b[get_digit(a[i], k)].append(a[i])
    idx = 0
    for i in range(10):
        for j in b[i]:
            a[idx] = j
            idx += 1

def radix_sort(a: list, n: int) -> float:
    start_time = time.time()
    max_len = 0
    mn = a[0]
    for i in range(n):
        mn = min(mn, a[i])
    if mn < 0:
        for i in range(n):
            a[i] -= mn
    for i in range(n):
        max_len = max(max_len, len(str(a[i])))
    for i in range(max_len):
        radix_sort_kth_digit(a, n, i)
    if mn < 0:
        for i in range(n):
            a[i] += mn
    stop_time = time.time()
    return stop_time - start_time

def flash_sort(a: list, n: int) -> float:
    start_time = time.time()
    mn, mx = 0, 0
    m = int(0.45 * n)
    for i in range(1, n):
        if a[i] < a[mn]:
            mn = i
        if a[i] > a[mx]:
            mx = i
    l = [0] * (m + 1)   
    for i in range(n):
        k = int((m - 1) * (a[i] - a[mn]) / (a[mx] - a[mn]))
        l[k] += 1
    l[0] -= 1
    for i in range(1, m):
        l[i] += l[i - 1]
    a[mx], a[n - 1] = a[n - 1], a[mx]
    l[m - 1] -= 1
    mx = a[n - 1]
    mn = a[mn]
    move = n - 1
    i = 0
    while move:
        k = int((m - 1) * (a[i] - mn) / (mx - mn))
        while i != l[k] and move:
            a[i], a[l[k]] = a[l[k]], a[i]
            k = int((m - 1) * (a[i] - mn) / (mx - mn))
            move -= 1
        i += 1
    insertion_sort(a, n)
    stop_time = time.time()
    return stop_time - start_time

def get_data(filename: str):
    with open(filename, 'r') as fi:
        n = int(fi.readline())
        a = list(map(int, fi.readline().split()))
    return n, a        

if __name__ == '__main__':
    file_out = 'running_time.txt'
    list_of_len = [100, 500, 1000, 2000, 3000, 4000, 5000]
    sort_algorithm = [
        '1. Insertion Sort : ',
        '2. Selection Sort : ',
        '3. Interchange Sort : ',
        '4. Heap Sort : ',
        '5. Quick Sort : ',
        '6. Merge Sort : ',
        '7. Counting Sort : ',
        '8. Radix Sort : ',
        '9. Flash Sort : '
    ]
    with open(file_out, 'w') as fo:
        run_time = [[0] * 7 for _ in range(9)]
        # random array
        fo.writelines('+++++++++++++++++++++++RANDOM ARRAY+++++++++++++++++++++++\n')
        for i in range(7):
            n, a = get_data('./random_arr/n' + str(list_of_len[i]) + '.txt')
            running_time = [
                insertion_sort(a, n),
                selection_sort(a, n),
                interchange_sort(a, n),
                heap_sort(a, n),
                quick_sort(a, 0, n - 1),
                merge_sort(a, 0, n - 1),
                counting_sort(a, n),
                radix_sort(a, n),
                flash_sort(a, n)                
            ]
            for j in range(9):
                run_time[j][i] = running_time[j]
            fo.writelines('Length :' + str(i) + '\n')
            for i in range(9):
                fo.writelines(sort_algorithm[i] + str(running_time[i]) + '\n')
            fo.writelines('-----------------------------------\n')
        for i in range(9):
            plt.plot(list_of_len, run_time[i], label=sort_algorithm[i][3:-3])
        plt.xlabel('Array Size')
        plt.ylabel('Time(seconds)')
        plt.title('Sorting Performance: Random')
        plt.legend()
        plt.show()
            
        # ----------------------------------------------------------------------------------------
        # increasing array
        fo.writelines('+++++++++++++++++++++++INCREASING ARRAY+++++++++++++++++++++++\n')
        for i in range(7):
            n, a = get_data('./increasing_arr/n' + str(list_of_len[i]) + '.txt')
            running_time = [
                insertion_sort(a, n),
                selection_sort(a, n),
                interchange_sort(a, n),
                heap_sort(a, n),
                quick_sort(a, 0, n - 1),
                merge_sort(a, 0, n - 1),
                counting_sort(a, n),
                radix_sort(a, n),
                flash_sort(a, n)                
            ]
            for j in range(9):
                run_time[j][i] = running_time[j]
            fo.writelines('Length :' + str(i) + '\n')
            for i in range(9):
                fo.writelines(sort_algorithm[i] + str(running_time[i]) + '\n')
            fo.writelines('-----------------------------------\n')
        # for i in range(9):
        #     plt.plot(list_of_len, run_time[i], label=sort_algorithm[i][3:-3])
        # plt.xlabel('Array Size')
        # plt.ylabel('Time(seconds)')
        # plt.title('Sorting Performance: Increasing')
        # plt.legend()
        # plt.show()
        # ----------------------------------------------------------------------------------------
        # decreasing array
        fo.writelines('+++++++++++++++++++++++DECREASING ARRAY+++++++++++++++++++++++\n')
        for i in range(7):
            n, a = get_data('./decreasing_arr/n' + str(list_of_len[i]) + '.txt')
            running_time = [
                insertion_sort(a, n),
                selection_sort(a, n),
                interchange_sort(a, n),
                heap_sort(a, n),
                quick_sort(a, 0, n - 1),
                merge_sort(a, 0, n - 1),
                counting_sort(a, n),
                radix_sort(a, n),
                flash_sort(a, n)                
            ]
            for j in range(9):
                run_time[j][i] = running_time[j]
            fo.writelines('Length :' + str(i) + '\n')
            for i in range(9):
                fo.writelines(sort_algorithm[i] + str(running_time[i]) + '\n')
            fo.writelines('-----------------------------------\n')
        # for i in range(9):
        #     plt.plot(list_of_len, run_time[i], label=sort_algorithm[i][3:-3])
        # plt.xlabel('Array Size')
        # plt.ylabel('Time(seconds)')
        # plt.title('Sorting Performance: Decreasing')
        # plt.legend()
        # plt.show()
        # ----------------------------------------------------------------------------------------
        # nearly sorted array
        fo.writelines('+++++++++++++++++++++++NEARLY SORTED ARRAY+++++++++++++++++++++++\n')
        for i in range(7):
            n, a = get_data('./nearly_sorted_arr/n' + str(list_of_len[i]) + '.txt')
            running_time = [
                insertion_sort(a, n),
                selection_sort(a, n),
                interchange_sort(a, n),
                heap_sort(a, n),
                quick_sort(a, 0, n - 1),
                merge_sort(a, 0, n - 1),
                counting_sort(a, n),
                radix_sort(a, n),
                flash_sort(a, n)                
            ]
            for j in range(9):
                run_time[j][i] = running_time[j]
            fo.writelines('Length :' + str(i) + '\n')
            for i in range(9):
                fo.writelines(sort_algorithm[i] + str(running_time[i]) + '\n')
            fo.writelines('-----------------------------------\n')
        # for i in range(9):
        #     plt.plot(list_of_len, run_time[i], label=sort_algorithm[i][3:-3])
        # plt.xlabel('Array Size')
        # plt.ylabel('Time(seconds)')
        # plt.title('Sorting Performance: Nearly Sorted')
        # plt.legend()
        # plt.show()
