class Solution:
    def sumAndMultiply(self, n: int) -> int:
        answer = 0
        temp = str(n)
        temp_sum = []
        temp_new_sum=''
        for i in temp:
            if i != '0':
                temp_sum.append(int(i))
                temp_new_sum+=i
        if(temp_sum):
            answer = sum(temp_sum)*int(temp_new_sum)
        else:
            answer = 0
        return answer
