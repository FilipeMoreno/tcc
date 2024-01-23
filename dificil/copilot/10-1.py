from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        n = len(word)
        freq = Counter(word)

        # Count the frequency of frequencies
        freq_of_freq = Counter(freq.values())

        if len(freq_of_freq) == 1:
            # If all letters have the same frequency, return True
            return True
        elif len(freq_of_freq) == 2:
            # If there are two different frequencies
            f1, count_f1 = freq_of_freq.popitem()
            f2, count_f2 = freq_of_freq.popitem()

            # Check if we can remove one character to make all frequencies equal
            if (count_f1 == 1 and (f1 - 1 == f2 or f1 == 1)) or (count_f2 == 1 and (f2 - 1 == f1 or f2 == 1)):
                return True

        return False