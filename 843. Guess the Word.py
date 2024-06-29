# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """
import collections

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type words: List[Str]
        :type master: Master
        :rtype: None
        """
        def calculate_match(word1, word2):
            return sum(c1 == c2 for c1, c2 in zip(word1, word2))

        def most_overlap_word():
            # Create a 2D list to count occurrences of each character at each position
            counts = [[0 for _ in range(26)] for _ in range(6)]
            for word in candidates:
                for i, c in enumerate(word):
                    counts[i][ord(c) - ord("a")] += 1
            
            best_score = 0
            best_word = ""
            for word in candidates:
                score = 0
                for i, c in enumerate(word):
                    score += counts[i][ord(c) - ord("a")]
                if score > best_score:
                    best_score = score
                    best_word = word
            
            return best_word

        candidates = wordlist[:]  # All remaining candidates, initially all words
        while candidates:
            # Guess the word that overlaps with most others
            guess_word = most_overlap_word()
            matches = master.guess(guess_word)

            if matches == 6:
                return
            
            # Filter candidates based on the number of matching characters
            candidates = [word for word in candidates if calculate_match(guess_word, word) == matches]




O(n^2) 看不懂def most_overlap_word()
most_overlap_word() 函数根据当前剩余的候选单词列表 candidates，选择与其他单词重叠最多的单词作为猜测目标。它统计每个位置上每个字符的出现次数，然后选择重叠度最高的单词作为猜测目标。
