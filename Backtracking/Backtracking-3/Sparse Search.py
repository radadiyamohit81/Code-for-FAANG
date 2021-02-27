class Solution:
    def sparseSearch(self, arr, X):
        if arr == []:
            return -1

        low = 0
        high = len(arr)-1

        while low <= high:
            mid = low + (high - low)//2
            
            if arr[mid] == "":
                left = mid -1
                right = mid +1
                while True:
                    if left < low and right > high:
                        return -1
                    elif left >= low and arr[left] != "":
                        mid = left
                    elif right <= high and arr[right] != "":
                        mid = right
            if arr[mid] == X:
                return True
            elif arr[mid] > X:
                high = mid -1
            elif arr[mid] < X:
                low = mid +1

        return -1


