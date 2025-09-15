# There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

# Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken,
# return the number of words in text you can fully type using this keyboard.


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # Splitting the text string to list for iterate through one by one
        text = text.split()
        # Variable to store the typed words count
        ans = 0

        # Iterate through each word in text
        for t in text:
            # If any character in a word matches with brokenLetters str -> continue with next word
            if any(ch in brokenLetters for ch in t):
                continue
            # Once above condition doesn't match increase the count -> typed
            ans += 1

        return ans