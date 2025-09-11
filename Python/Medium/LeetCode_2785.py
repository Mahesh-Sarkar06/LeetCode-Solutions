# Given a 0-indexed string s, permute s to get a new string t such that:

# All consonants remain in their original places. More formally, if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
# The vowels must be sorted in the nondecreasing order of their ASCII values.
# More formally, for pairs of indices i, j with 0 <= i < j < s.length such that s[i] and s[j] are vowels, then t[i] must not have a higher ASCII value than t[j].
# Return the resulting string.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.


class Solution:
    def sortVowels(self, s: str) -> str:
        # Converting string to list
        s = list(s)
        # Empty list for storing vowels from string
        vow = []

        # Iterate through list for getting vowels
        for i in range(len(s)):
            # Checking if the element exist in the given string
            if s[i] in 'AEIOUaeiou':
                # Append if exist
                vow.append(s[i])
                # Replace the vowel with asterisk (*)
                s[i] = '*'

        # Sort the vowel list as per ASCII rule
        vow.sort()
        # Initialized a variable to iterate through vowels list
        j = 0

        # Iterate through the string list
        for i in range(len(s)):
            # Check for asterisk
            if s[i] == '*':
                # If matched, replace it with the sorted elements in vowels list
                s[i] = vow[j]
                # Increment of j
                j += 1

        # Join the string list with no space between the elements
        return ''.join(s)