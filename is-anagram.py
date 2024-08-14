class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map_s = {}
        hash_map_t = {}

        for i in range(0, len(s)):
            hash_map_s[s[i]] = 1 + hash_map_s.get(s[i], 0)
            hash_map_t[t[i]] = 1 + hash_map_t.get(t[i], 0)

        for j in range(0, len(s)):
            if hash_map_s[j] != hash_map_t[j]:
                return False

        return True
