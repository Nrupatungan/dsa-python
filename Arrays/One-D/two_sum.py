# Two Sum problem

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Brute Force
class TwoSum:
    def brute(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # Return empty array if no match found
        return []

    def twoPass(self, nums: list[int], target: int) -> list[int]:
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash and hash[complement] != i:
                return [i, hash[complement]]

        return []

    def onePass(self, nums: list[int], target: int) -> list[int]:
        hash = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash:
                return [i, hash[complement]]
            hash[nums[i]] = i

        return []


ts = TwoSum()
nums = [3, 3]
target = 6

print(ts.brute(nums, target))
print(ts.onePass(nums, target))
print(ts.twoPass(nums, target))
