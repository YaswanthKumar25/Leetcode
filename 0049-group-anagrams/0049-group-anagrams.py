class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a standard Python dictionary
        anagram_map = {}
        
        for word in strs:
            # 1. Sort the word and join it back into a string to use as a key
            sorted_word = "".join(sorted(word))
            
            # 2. Check if the sorted key is already in the dictionary
            if sorted_word in anagram_map:
                # If it exists, append the original word to its list
                anagram_map[sorted_word].append(word)
            else:
                # If it doesn't exist, create a new key with a list containing the word
                anagram_map[sorted_word] = [word]
                
        # 3. Return all the grouped lists from the dictionary
        return list(anagram_map.values())