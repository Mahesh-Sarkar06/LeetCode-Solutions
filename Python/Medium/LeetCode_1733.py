# On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

# You are given an integer n, an array languages, and an array friendships where:

# There are n languages numbered 1 through n,
# languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
# friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
# You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

# Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.


from collections import defaultdict
from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # Converting language 2D array to sets
        languages = [set(l) for l in languages]
        # Defining non commuicating pair as a set
        non_communicate = set()

        # Iterating through each friends
        for a, b in friendships:
            a -= 1
            b -= 1

            if languages[a] & languages[b]:
                continue

            non_communicate.add(a)
            non_communicate.add(b)

        # Defined an empty dictionary for person that can learn
        learn = defaultdict(int)
        # Iterate through the pairs who cannot communicate
        for pair in non_communicate:
            # Iterate through the languages that has to be taught
            for l in languages[pair]:
                # Increase the count denoting learning of the language
                learn[l] += 1

        # Returning the total number of persons that has been taught from the non_communicating pairs
        return len(non_communicate) - max(learn.values() or [0])