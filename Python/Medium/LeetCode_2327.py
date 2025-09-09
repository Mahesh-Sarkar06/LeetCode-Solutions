# On day 1, one person discovers a secret.

# You are given an integer delay, which means that each person will share the secret with a new person every day,
# starting from delay days after discovering the secret. You are also given an integer forget, which means that each person will forget the secret forget days after discovering it.
# A person cannot share the secret on the same day they forgot it, or on any day afterwards.

# Given an integer n, return the number of people who know the secret at the end of day n. Since the answer may be very large, return it modulo 109 + 7.




class Solution:
    def peopleAwareOfSecrets(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7

        secret_learned = [0] * (n+1)
        secret_learned[1] = 1
        shared = 0

        for day in range(2, n+1):
            if day - delay >= 1:
                shared = (shared + secret_learned[day - delay]) % MOD

            if day - forget >= 1:
                shared = (shared - secret_learned[day - forget]) % MOD

            secret_learned[day] = shared

        remembered = 0
        for day in range(n - forget, n+1):
            remembered = (shared + secret_learned[day]) % MOD

        return remembered