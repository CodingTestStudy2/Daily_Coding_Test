def solution(arr,k):
    for i in range(len(arr)):
        missing = arr[i] - i - 1
        print(missing)

        if missing >= k:
            return arr[i] - (missing - k + 1)
    return arr[-1] + (k - missing)

arr = [5,6,7,8,9]
k = 9

print(solution(arr,k))


