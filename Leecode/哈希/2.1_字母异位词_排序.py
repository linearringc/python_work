from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())

solution = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(solution.groupAnagrams(strs))