# Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

# For a given query word, the spell checker handles two categories of spelling mistakes:

# Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
# Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
# Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
# Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
# Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
# Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
# Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
# Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
# In addition, the spell checker operates under the following precedence rules:

# When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
# When the query matches a word up to capitlization, you should return the first such match in the wordlist.
# When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
# If the query has no matches in the wordlist, you should return the empty string.
# Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

from typing import List

class Solution:
    def spellChecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # Converting the wordlist to a unique value set
        exact_match = set(wordlist)
        # Defining an empty dictionary to store the words that exactly match with the queries
        case_match = {}

        # Iterating through wordlist and converting to lower case
        for word in wordlist:
            lower = word.lower()

            # Check if the lower case value exist in above dictionary
            if lower not in case_match:
                case_match[lower] = word

        # Defining a variable for vowels and empty dictionary to store the word
        vowels = 'aeiou'
        vow_match = {}

        # Function to join the string with * in place of vowels eg: keto -> k*t*
        def vowelMatch(word: str) -> str:
            return ''.join('*' if ch in vowels else ch for ch in word.lower())
        
        # Now check for each word if exist in the above dictionary
        for word in wordlist:
            key = vowelMatch(word)

            if key not in vow_match:
                vow_match[key] = word

        # Defining an empty list to store the words that statisfy the conditions
        res = []
        for q in queries:
            # Check if queried word exist in exact_match dictionary
            if q in exact_match:
                res.append(q)
            # Check if queries word exist in case_match dictionary
            elif q.lower() in case_match:
                res.append(case_match[q.lower()])
            # Check if queries word exist in vow_match dictionary
            elif vowelMatch(q) in vow_match:
                res.append(vow_match[vowelMatch(q)])
            # If no condition is satisfied -> append an empty string
            else:
                res.append['']

        return res