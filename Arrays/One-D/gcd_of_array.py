# find greatest common divisor of array

# Given an integer array nums, return the greatest common divisor
# of the smallest number and largest number in nums.

# The greatest common divisor of two numbers is the
# largest positive integer that evenly divides both numbers.

# Example 1:

# Input: nums = [2,5,6,9,10]
# Output: 2
# Explanation:
# The smallest number in nums is 2.
# The largest number in nums is 10.
# The greatest common divisor of 2 and 10 is 2.


# Example 2:

# Input: nums = [7,5,6,8,3]
# Output: 1
# Explanation:
# The smallest number in nums is 3.
# The largest number in nums is 8.
# The greatest common divisor of 3 and 8 is 1.


# Example 3:

# Input: nums = [3,3]
# Output: 3
# Explanation:
# The smallest number in nums is 3.
# The largest number in nums is 3.
# The greatest common divisor of 5 and 3 is 3.

class Solution:
    def findGCD(self, nums: list[int]) -> int:
        a = max(nums)
        b = min(nums)
        return self.gcd(a, b)

    def gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)


if __name__ == "__main__":
    gcd = Solution()

    nums = [2, 5, 6, 9, 10]
    nums2 = [7, 5, 6, 8, 3]
    nums3 = [3, 3]

    print(gcd.findGCD(nums))
    print(gcd.findGCD(nums2))
    print(gcd.findGCD(nums3))
