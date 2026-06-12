class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_groups:dict[str, list[str]]={}
        for item in strs:
            if ''.join(sorted(item)) not in  final_groups:
               final_groups[''.join(sorted(item))] = [item]
            else:
                final_groups[''.join(sorted(item))].append(item)
        return (list(final_groups.values()))
        