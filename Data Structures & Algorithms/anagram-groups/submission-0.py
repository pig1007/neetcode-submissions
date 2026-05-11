class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dc = defaultdict(list) # counter:list[str]
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord("a")] += 1
            dc[tuple(count)].append(s)
        print(dc)
        return list(dc.values())