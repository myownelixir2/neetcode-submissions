class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anag_d = defaultdict(list)

        for s in strs:
            temp_key = f"t_{''.join(sorted(s))}"
            anag_d[temp_key].append(s)

        my_anagrams = []
        for v in anag_d.values():
            item = list(v)
            my_anagrams.append(item)

        return my_anagrams
        