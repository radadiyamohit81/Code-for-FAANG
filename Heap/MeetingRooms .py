class Solution:
    # Time: O[N*log(N)] for Sorting + O[N]
    # Space: O[1]
    def canAttendMeetings(self, intervals):
        intervals.sort(key = lambda x: x[0])
        
        for i in range(0, len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
    

    # O[NlogN] Time for Sorting + O[N]
    # O[N] Space for MINHEAP
    import heapq
    def minMeetingRooms(self, intervals):
        if intervals == []:
            return 0
        
        intervals.sort(key = lambda x: x[0])     # SORT BASED ON THE START TIMES
        
        #keep running meetings in a heap
        #and the max of the heap size will be the answer
        meetings = [intervals[0][1]]
        heapq.heapify(meetings)      # START MIN-HEAP WITH END TIME OF 1ST MEETING
        roomsRequired = 1
        
        for interval in intervals[1:]:

            # If Start Time of a new meeting can be accomodated with the running Meetings latest available room *****
            if interval[0] >= meetings[0]:       
                heapq.heappop(meetings)
            heapq.heappush(meetings, interval[1])    
            roomsRequired = max(roomsRequired, len(meetings))
        return roomsRequired
            