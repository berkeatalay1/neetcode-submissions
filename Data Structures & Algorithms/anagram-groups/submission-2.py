class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_groups:dict[str, list[str]]={}
        for item in strs:
            ordered_chars_str = ''.join(sorted(item))
            if ordered_chars_str not in  final_groups:
               final_groups[ordered_chars_str] = [item]
            else:
                final_groups[ordered_chars_str].append(item)
        return (list(final_groups.values()))
        