"""
# Definition for an Interval.
"""
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


# Meeting Rooms 1 concept
# O[NlogN] + O[N] Time 
# O[N] Space
class Solution:
    def employeeFreeTime(self, schedule):
        workingTimes = []
        result = []
        for emp in schedule:
            for time in emp:
                workingTimes.append([time.start, time.end])           
        workingTimes.sort()   # sort it based on Start Times,            => O[NlogN]
        
        endTime = workingTimes[0][1]

        for i in range(1, len(workingTimes)):                          # => O[N]
            if workingTimes[i][0] <= endTime:     # TIME OVERLAP
                endTime = max(endTime, workingTimes[i][1])
            
            elif workingTimes[i][0] > endTime:    # BREAK
                result.append(Interval(start = endTime, end = workingTimes[i][0]))
                
                endTime = workingTimes[i][1]
        
        
        return result
            

    # O[NlogK] Time, K: # of Employees
    # O[K], only K elements at a time in MIN-HEAP
    import heapq
    def employeeFreeTime(self, schedule):
        runningMeetings = []
        for i in range(len(schedule)):
            heapq.heappush( runningMeetings, [schedule[i][0].start, schedule[i][0].end, (i, 0)] )
         
        result = []
        endTime = runningMeetings[0][1] 
        while runningMeetings != []:
            start, end, id = heapq.heappop(runningMeetings)
            emp_id = id[0]
            index = id[1]
            if start > endTime:
                result.append(Interval(endTime, start))
            if index+1 <= len(schedule[emp_id])-1:
                heapq.heappush(runningMeetings, [schedule[emp_id][index+1].start, schedule[emp_id][index+1].end, (emp_id, index+1)])
            endTime = max(endTime, end)
             
        return result