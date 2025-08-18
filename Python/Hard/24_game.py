# You are given an integer array cards of length 4.
# You have four cards, each containing a number in the range [1, 9].
# You should arrange the numbers on these cards in a mathematical expression using the operators
# ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.

# You are restricted with the following rules:

# The division operator '/' represents real division, not integer division.
# For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
# Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
# For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
# You cannot concatenate numbers together
# For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
# Return true if you can get such expression that evaluates to 24, and false otherwise.



class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # Typecasting items of list to double value for real division
        vals = [float(ele) for ele in cards]
        
        return self.isValid(vals)


    def isValid(self, cards: List[float]) -> bool:
        # Return float values to a range of 10^-6
        EPSILON = 1e-6
        size = len(cards)

        # Check if list consist single item
        if size == 1:
            return abs(cards[0] - 24.0) < EPSILON

        # Iterating through each cards creating a pair combination
        for i in range(size):
            for j in range(i+1, size):
                a, b = cards[i], cards[j]
                nxt_vals = [cards[k] for k in range(size) if k != i and k != j]

                # Storing possible operations that can be done
                res = [a+b, a-b, b-a, a*b]
                if abs(a) > EPSILON:
                    res.append(b/a)
                if abs(b) > EPSILON:
                    res.append(a/b)

                # Iterate through each values of result and comparing it with cards operation
                for val in res:
                    if self.isValid(nxt_vals + [val]):
                        return True
                    
        return False