from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a dictionary where the values default to an empty list
        anagram_map = defaultdict(list)
        
        for word in strs:
            # 1. Sort the characters of the word
            # sorted("eat") -> ['a', 'e', 't']
            # 2. Join them back into a string to use as a dictionary key
            # "".join(['a', 'e', 't']) -> "aet"
            sorted_word = "".join(sorted(word))
            
            # 3. Append the original word to the list matching this sorted key
            anagram_map[sorted_word].append(word)
            
        # Return all the grouped lists from the dictionary
        return list(anagram_map.values())