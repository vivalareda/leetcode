import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = collections.defaultdict(list)

        for str in strs:
            sorted_string_list = sorted(str)
            key = " ".join(sorted_string_list)
            dict[key].append(str)

        return dict.values()
