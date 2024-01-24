from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1  # Index of the word ending at this node
        self.palindrome_suffixes = []

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word, start, end):
            while start < end:
                if word[start] != word[end]:
                    return False
                start += 1
                end -= 1
            return True

        def add_word_to_trie(root, word, index):
            node = root
            for i, char in enumerate(word):
                if is_palindrome(word, i, len(word) - 1):
                    node.palindrome_suffixes.append(index)
                char_index = ord(char) - ord('a')
                if char_index not in node.children:
                    node.children[char_index] = TrieNode()
                node = node.children[char_index]
            node.index = index

        def search_palindrome_pairs(root, word, index):
            pairs = []
            node = root

            for i, char in enumerate(word):
                # Check for the case where a longer palindrome can be formed by appending the current word
                if node.index != -1 and node.index != index and is_palindrome(word, i, len(word) - 1):
                    pairs.append([index, node.index])

                char_index = ord(char) - ord('a')
                if char_index not in node.children:
                    return pairs
                node = node.children[char_index]

            # Check for the case where a shorter palindrome can be formed by prepending the current word
            for suffix_index in node.palindrome_suffixes:
                pairs.append([index, suffix_index])

            # Check for the case where the current word is an empty string
            if node.index != -1 and node.index != index:
                pairs.append([index, node.index])

            return pairs

        trie_root = TrieNode()
        result = []

        for i, word in enumerate(words):
            add_word_to_trie(trie_root, word[::-1], i)

        for i, word in enumerate(words):
            result.extend(search_palindrome_pairs(trie_root, word, i))

        return result

# Example usage:
solution = Solution()
print(solution.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
print(solution.palindromePairs(["bat", "tab", "cat"]))
print(solution.palindromePairs(["a", ""]))
