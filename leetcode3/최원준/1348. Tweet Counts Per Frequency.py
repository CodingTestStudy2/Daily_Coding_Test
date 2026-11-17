#

'''
1. 아이디어 :
시간들을 정렬한 후, 이분탐색을 통해 시작점, interval 끝점 - 시작점 갯수로 카운

2. 시간복잡도 :
    O(nlogn, nlogn) x 10**4

3. 자료구조/알고리즘 :
이분탐색, 정

'''
class TweetCounts:

    def bs_left(self, nums, target):
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    
    def bs_right(self, nums, target):
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

    def __init__(self):
        self.tweets = defaultdict(list)
        self.freqs = {"minute":60, "hour":3600, "day":86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)
        self.tweets[tweetName].sort()

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> list[int]:
        times = self.tweets[tweetName]
        ans = []

        for start in range(startTime, endTime + 1, self.freqs[freq]):
            end = min(start + self.freqs[freq] - 1, endTime)

            counts = self.bs_right(times, end) - self.bs_left(times, start)
            ans.append(counts)
        return ans
    
    


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
