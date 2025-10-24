from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = defaultdict(list)
        for str in strs:
            counts = [0] * 26
            for ch in str:
                counts[ord(ch) - ord('a')] += 1
            mp[tuple(counts)].append(str)
        return list(mp.values())


solution = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(solution.groupAnagrams(strs))