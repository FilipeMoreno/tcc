from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        # Count the frequency of each letter in the word
        letter_count = Counter(word)
        
        # Count the frequency of frequencies
        frequency_count = Counter(letter_count.values())
        
        # If there is only one unique frequency, all letters have the same frequency
        if len(frequency_count) == 1:
            return True
        
        # If there are two unique frequencies, check if one of them is 1 and the other is the difference by 1
        if len(frequency_count) == 2:
            # Get the two frequencies
            freq1, freq2 = frequency_count.keys()
            
            # Check if one of them is 1 and the other is the difference by 1
            if (freq1 == 1 and frequency_count[freq1] == 1) or (freq2 == 1 and frequency_count[freq2] == 1):
                return True
            elif abs(freq1 - freq2) == 1 and (frequency_count[freq1] == 1 or frequency_count[freq2] == 1):
                return True
        
        # If none of the above conditions are met, return False
        return False