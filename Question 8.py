class ThreeSum:
    def __init__(self, nums):
        self.nums = sorted(nums)

    def find(self):
        result = []
        for i in range(len(self.nums) - 2):
            if i > 0 and self.nums[i] == self.nums[i - 1]:
                continue
            left, right = i + 1, len(self.nums) - 1
            while left < right:
                s = self.nums[i] + self.nums[left] + self.nums[right]
                if s == 0:
                    result.append([self.nums[i], self.nums[left], self.nums[right]])
                    while left < right and self.nums[left] == self.nums[left + 1]:
                        left += 1
                    while left < right and self.nums[right] == self.nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return result
