# Design a food rating system that can do the following:

# Modify the rating of a food item listed in the system.
# Return the highest-rated food item for a type of cuisine in the system.
# Implement the FoodRatings class:

# FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.
# foods[i] is the name of the ith food,
# cuisines[i] is the type of cuisine of the ith food, and
# ratings[i] is the initial rating of the ith food.
# void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
# String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.
# Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.


from typing import List
from sortedcontainers import SortedList

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # Dictionary for mapping food item with cuisine and rating
        self.foodInfo = {}
        # Dictionary for mapping cuisine item with rating and food
        self.cuisineInfo = {}

        # Combining all list together and fetching items
        for f, c, r in zip(foods, cuisines, ratings):
            # Adding food to foodInfo dictionary with values cuisine, rating
            self.foodInfo[f] = (c, r)

            # Check if cuisine exist in cuisineInfo dictionary
            if c not in self.cuisineInfo:
                # Adding cuisine with sorted value
                self.cuisineInfo[c] = SortedList(key=lambda x: (-x[0], x[1]))

            # Adding Cuisine to cuisineInfo dictionary with values rating and food
            self.cuisineInfo[c] = (r, f)


    def changeRating(self, food: str, newRating: int) -> None:
        c, oldRating = self.foodInfo[food]

        self.cuisineInfo[c].remove((oldRating, food))
        self.cuisineInfo[c].add((newRating, food))

        self.foodInfo[food] = (c, newRating)


    def highestRated(self, cuisine: str) -> str:
        # Getting top most item from cuisineInfo dictionary
        top = self.cuisineInfo[cuisine][0]

        # Returing the food name from that array
        return top[1]