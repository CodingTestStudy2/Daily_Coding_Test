class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deck.sort()
        count = {}
        first = deck[0]
        for d in deck:
            if d in count:
                count[d] += 1
            else:
                count[d] = 1
        
        values = list(count.values())
        values.sort()
        
        check = len(values)
    
        for i in range(2, values[-1] + 1):
            check = 0
            for v in values:
                if v % i == 0:
                    check += 1
                if check == len(values):
                    return True
        return False