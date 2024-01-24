from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        values = list(freq.values())
        max_freq = max(values)
        min_freq = min(values)
        
        return values.count(max_freq) == 1 and max_freq - min_freq == 1 or \
               values.count(min_freq) == 1 and min_freq == 1 and len(set(values)) == 2