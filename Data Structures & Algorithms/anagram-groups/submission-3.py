class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # list that makes an empty key

        for s in strs:
            count = [0] * 26 # create empty counter for key we will use later

            for c in s:
                count[ord(c) - ord("a")] += 1 # creating key
            res[tuple(count)].append(s) # adding the key to the res list with the string attached
        return list(res.values())

        