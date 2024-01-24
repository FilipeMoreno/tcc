class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_dict = {word: i for i, word in enumerate(words)}
        result = []
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                tmp1 = word[:j]
                tmp2 = word[j:]
                if tmp1[::-1] in word_dict and word_dict[tmp1[::-1]] != i and tmp2 == tmp2[::-1]:
                    result.append([i, word_dict[tmp1[::-1]]])
                if j != 0 and tmp2[::-1] in word_dict and word_dict[tmp2[::-1]] != i and tmp1 == tmp1[::-1]:
                    result.append([word_dict[tmp2[::-1]], i])
        return result