def quick_sort(arr4sort):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr4sort[(low + high) // 2]
        while low <= high:
            while arr4sort[low] < pivot:
                low += 1
            while arr4sort[high] > pivot:
                high -= 1
            if low <= high:
                arr4sort[low], arr4sort[high] = arr4sort[high], arr4sort[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr4sort) - 1)


t = input()
arr = [int(input()) for y in range(int(t))]
quick_sort(arr)
print(*arr, sep='\n')
