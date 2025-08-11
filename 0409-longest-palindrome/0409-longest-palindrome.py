class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Create a dictionary     
        freq = defaultdict(int)
        #map number of repetitions on eahc charcater
        for c in s:
            freq[c] += 1
        #Map how many pairs of characters
        count = 0
        for c in freq.values():
            if c % 2 ==0: #if even increment count
                count += c
            else: # if odd then reduce the count to 1 becuse only 2 can be pair 
                count += c-1

        # if there are leftover letters use one fort the midle
        if count < len(s):
            count += 1
        return count           