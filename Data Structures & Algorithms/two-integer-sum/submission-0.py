class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        PREVMAP={}

        for KEY,VALUE in enumerate(nums):
            DIFF = target-VALUE

            if DIFF in PREVMAP:
                return [PREVMAP[DIFF],KEY]
            PREVMAP[VALUE]=KEY
       