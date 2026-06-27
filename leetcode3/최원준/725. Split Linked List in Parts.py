#

'''
1. 아이디어 :
갯수를 세며 몇개씩 나누고, 남는게 몇개인지 계산한다
파트별로 포인터를 옮겨가며 갯수에 맞게 끊어준다.

2. 시간복잡도 :
    O(n)

3. 자료구조/알고리즘 :


'''

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next
        
        part = count // k
        extra = count % k

        ans = []
        curr = head

        for i in range(k):
            ans.append(curr)

            size = part
            if i < extra:
                size += 1

            for _ in range(size - 1):
                if curr:
                    curr = curr.next

            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part

        return ans
