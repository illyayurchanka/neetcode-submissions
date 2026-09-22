class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str = [str(sorted(s)) for s in strs]
        dick = {ss: [] for ss in sorted_str}
        for (ss, s) in zip(sorted_str, strs):
            dick[ss].append(s)
        return list(dick.values())