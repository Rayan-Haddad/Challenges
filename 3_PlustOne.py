class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = ""
        for i in digits:
            nums += str(i)
        x = int(nums) + 1
        y = [int(digit) for digit in str(x)]
        return y