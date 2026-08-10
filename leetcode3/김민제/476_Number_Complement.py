def solution(num):
    num_bin = bin(num)[2:]
    str_bin = str(num_bin)
    return int(str_bin.replace('1','x').replace('0','1').replace('x','0'),2)



print(solution(1))
