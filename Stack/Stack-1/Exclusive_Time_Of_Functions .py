class Solution:
    # O[N] Time
    # O[N] Space
    def exclusiveTimeOfFunctions(self, n, logs):
        if logs == []:
            return []

        timeRecords = [0]*n
        previousTime = 0
        st = []     # TO STORE ALL PROCESS THAT DID NOT YET END

        for log in logs:
            log = log.split(':')
            processID = int(log[0])
            time = int(log[2])

            if log[1] == 'start':
                if st != []:
                    previousProcesID = st[-1]
                    timeRecords[previousProcesID] += time - previousTime
                st.append(processID)
                previousTime = time
            elif log[1] == 'end':
                processID = st.pop()
                timeRecords[processID] += time - previousTime +1
                previousTime = time +1

        return timeRecords
