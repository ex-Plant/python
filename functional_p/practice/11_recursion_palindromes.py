# def isPalindrome(word):
#     reversed = ''
#     for i in range(len(word) - 1, -1, -1):
#         reversed += word[i]
#     return "Is palindrome ❤️‍🔥" if reversed == word else "Sorry, fuck you but no 🖤"

# print(isPalindrome("aha"))


def is_palindrome_recursive(word):
    # always a palindrome if 2 or less letters
    if len(word) <=2:
        return True 
    
    # check outer chars
    if not word[0] == word[-1]:
        return False

    # strip outer chars
    stripped = word[1 : -1]
    return is_palindrome_recursive(stripped)

res = is_palindrome_recursive('alabama')
print(res)