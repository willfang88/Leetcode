class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        #Go through every character in the first string (strs[0])
        for i in range(len(strs[0])):
            # Iterate through all the strings
            for s in strs:
                #1: Out of bounds if index is = to len(s) 
                #2: check every single string at index i is the same
                if i == len(s) or s[i] != strs[0][i]:
                    #Out of bounds or !=, return res
                    return res
            #Add the character to result
            res += strs[0][i]
        return res
                    



        