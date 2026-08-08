from collections import Counter
def solution(order,s):
    count = Counter(s)
    result = []

    for ch in order:
        if ch in count:
            result.append(ch*count[ch])
            del count[ch]

    for ch,cnt in count.items():
        result.append(ch*cnt)
    return ''.join(result)



order = "bcafg"
s = "abcd"
print(solution(order,s))
