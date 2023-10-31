class Solution(object):
    def largestAltitude(self, gain):
        altitudes = [0] * (len(gain) + 1) 
        for i, num in enumerate(gain):
            altitudes[i+1] = gain[i] + altitudes[i]
        return max(altitudes)

        