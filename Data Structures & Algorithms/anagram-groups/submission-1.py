class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_groups:dict[str, list[str]]={}
        for item in strs:
            item_chars = list(item)
            ordered_chars = sorted(item_chars)
            ordered_chars_str = ''.join(ordered_chars)
            if ordered_chars_str not in  final_groups:
               final_groups[ordered_chars_str] = [item]
            else:
                final_groups[ordered_chars_str].append(item)
        return (list(final_groups.values()))
        