class Solution:
    # Function to calculate how many gas stations are needed 
    # if the maximum allowed distance between stations is 'dist'
    def number_of_gas_stations_required(self, dist, arr):
        count = 0  # total number of additional gas stations required
        n = len(arr)

        # Iterate through consecutive station positions
        for i in range(1, n):
            # Calculate how many stations are needed between arr[i-1] and arr[i]
            number_in_between = int((arr[i] - arr[i - 1]) / dist)

            # If the distance divides perfectly, we overcounted by 1,
            # so subtract one extra station
            if (arr[i] - arr[i - 1]) == dist * number_in_between:
                number_in_between -= 1

            count += number_in_between  # accumulate required stations

        return count  # return total number of extra stations needed

    # Function to minimize the maximum distance between gas stations
    def minmaxGasDist(self, arr, k):
        # Binary search between smallest (0) and largest gap in stations
        low = 0
        high = max(arr[i+1] - arr[i] for i in range(len(arr) - 1))

        diff = 1e-6  # precision tolerance for stopping condition

        # Binary search loop until precision is achieved
        while high - low > diff:
            mid = (low + high) / 2.0  # candidate distance
            count = self.number_of_gas_stations_required(mid, arr)

            # If more than k stations are required, increase distance
            if count > k:
                low = mid
            else:
                # Otherwise we can reduce the distance
                high = mid

        return high  # minimum possible maximum distance
