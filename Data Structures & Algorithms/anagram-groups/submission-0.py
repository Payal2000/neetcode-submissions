class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Create empty hashmap which can take list as key

        res = defaultdict(list)
        

        
        # Go through each word in str, get count
        for word in strs:
            count = [0] * 26
            
            
            for s in word:
                count[ord(s) - ord('a')] += 1

            res[tuple(count)].append(word)
        
        return list(res.values())



        

        








        
        