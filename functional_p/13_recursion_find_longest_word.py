# Complete the find_longest_word function without a loop. It accepts string inputs, document, and optional longest_word, which is the current longest word and defaults to an empty string.

# Check if the first word is longer than the current longest_word, then recur for the rest of the document.
# Words with equal length to longest_word should be skipped.
# Ensure there are no potential index errors.
# Assume that a "word" means a series of any consecutive non-whitespace characters. For example, find_longest_word("How are you?") should return the string "you?".

# Review the provided tests in main_test.py to see the expected behavior, including edge cases.

# You can use .split with maxsplit=1.
# That will split a string into a list of [first_word, rest_of_string]



def find_longest_word(document, longest_word=""):
    if len(document.strip()) == 0:
        return ""
    # That will split a string into a list of [first_word, rest_of_string]
    splitArr = document.split(maxsplit=1)
    curr_word = splitArr[0]

    if len(longest_word) < len(curr_word):
        longest_word = curr_word
    
    if len(splitArr) == 1 :
        return longest_word

    return find_longest_word(splitArr[1], longest_word)