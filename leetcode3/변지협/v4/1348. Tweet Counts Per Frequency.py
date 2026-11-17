from collections import defaultdict
class TweetCounts:

    def __init__(self):
        self.dic = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.dic[tweetName].append(time)
        if tweetName == 'tweet2' and 807230331 <= time <= 807231513:
            print(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> list[int]:
        mode = {
            'minute': 60,
            'hour': 3600,
            'day': 86400
        }

        curr = startTime
        lst = []
        while curr <= endTime:
            end = curr + mode[freq]
            num = 0
            for elem in self.dic[tweetName]:
                if curr <= elem < end and elem <= endTime:
                    num += 1
            curr = end
            lst.append(num)

        return lst 

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)