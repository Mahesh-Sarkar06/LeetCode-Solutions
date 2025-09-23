# Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

# To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

# Return the following:

# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.



class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Splitting the version string at dot '.'
        v1 = version1.split('.')
        v2 = version2.split('.')

        # Iterate through the largest length of version string
        # If both are same then same value will be taken
        for i in range(max(len(v1), len(v2))):
            # Getting the value from v1 & v2 for each position, only if the position exist.
            # If not then 0 will be taken as consideration
            v_1 = int(v1[i]) if i < len(v1) else 0
            v_2 = int(v2[i]) if i < len(v2) else 0

            # Comparing the values
            if v_1 < v_2:
                return -1
            elif v_1 > v_2:
                return 1
            
        # None of the condition satisfies or the versions are same then 0
        return 0