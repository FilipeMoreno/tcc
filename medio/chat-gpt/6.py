from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for word in strs:
            # Sort the characters in the word to create a unique key for anagrams
            sorted_word = ''.join(sorted(word))
            
            # Add the word to the corresponding group in the dictionary
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        
        # Convert the values of the dictionary to a list to get the final result
        result = list(anagrams.values())
        return result
