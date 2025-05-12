# https://leetcode.com/problems/length-of-last-word/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        def get_the_last_word(s):
            L = list(filter(None, s.split(' ')))
            return L[-1]
        
        # call get_the_last_word(s)
        last_word_size = len(get_the_last_word(s))
        return last_word_size




# about filter() 
# https://www.simplilearn.com/tutorials/python-tutorial/filter-in-python#:~:text=Filter()%20is%20a%20built,that%20you%20provide%20very%20efficiently.






