class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # brute force - sort all the strings then 
        result_hashmap = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in result_hashmap:
                result_hashmap[sorted_s] = [s]
            else:
                result_hashmap[sorted_s].append(s)
                # note - result_hashmap[sorted_s] = result_hashmap[sorted_s].append(s) does not work since append return None
        
        return list(result_hashmap.values())