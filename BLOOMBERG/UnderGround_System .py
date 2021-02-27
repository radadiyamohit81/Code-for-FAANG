class UndergroundSystem:
    # O[1] Time for all functions
    # O[ P + S*S ], S: number of stations on the network, P: number of passengers making a journey concurrently during peak time.

    def __init__(self):
        self.journey_data = {}              # (start_station, end_station):[totalTime, totalTrips]
        self.checkIn_data = {}

    def checkIn(self, user_id, start_station, start_time):
        self.checkIn_data[user_id] = [start_station, start_time]

    def checkOut(self, user_id, end_station, end_time):
        start_station, start_time = self.checkIn_data[user_id]

        journeyTime = end_time - start_time
        if (start_station, end_station) not in self.journey_data:
            self.journey_data[(start_station, end_station)] = [journeyTime, 1]
        else:
            self.journey_data[(start_station, end_station)][0] += journeyTime
            self.journey_data[(start_station, end_station)][1] += 1
        del self.checkIn_data[user_id]
    
    def getAverageTime(self, start_station, end_station):
        totalTime, totalTrips = self.journey_data[(start_station, end_station)]
        return totalTime / totalTrips


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)