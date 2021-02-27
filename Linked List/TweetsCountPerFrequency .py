class TweetCounts:

    def __init__(self):
        self.tweetTimeStamp = {}
        self.freq = {'minute':60, 'hour':3600, 'day':86400}

    def recordTweet(self, tweetName, time):
        if tweetName in self.tweetTimeStamp: 
            self.tweetTimeStamp[tweetName].append(time)
        else:
            self.tweetTimeStamp[tweetName] = [time]

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        
        array = self.tweetTimeStamp[tweetName]
        array.sort()
        
        noOfSeconds = self.freq[freq]
        ans = []
        for st in range(startTime, endTime+1, noOfSeconds):
            rightIndex = self.bs_last(array, min(endTime, st + noOfSeconds-1)) + 1
            leftIndex = self.bs_first(array, st)
            ans.append(  rightIndex - leftIndex  )
            
        return ans

    #get the index of the smallest number greater or equal to target
    def bs_first(self, array, target):
        left = 0
        right = len(array)-1
        while left <= right:
            mid = left + (right - left)//2
            if array[mid] >= target:
                right = mid -1
            else:
                left = mid +1
        return left
    
    def bs_last(self, array, target):
        left = 0
        right = len(array)-1
        while left <= right:
            mid = left + (right - left)//2
            if array[mid] <= target:
                left = mid +1
            else:
                right = mid -1
        return right
        
            

        

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)