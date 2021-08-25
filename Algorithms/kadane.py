"""
Algorithm for Maximum Subarray Problem: https://en.wikipedia.org/wiki/Maximum_subarray_problem
Time Complexity: O(n)
Description:
    Takes in a list of int nums and scans for nums[1...n] form left to right.
    in the jth step (steps in between 1...n [exclusive]) it computes the largest sum ending at j and stores it in
    a varibale current_sum. best_sum maintains the largest sum anywhere in num[1...j] and stores current_sum if current_sum > best_sum

    current_sum = max(num[j], current_sum + num[j]) allows instances of num that contains no positive number to return the largest value
    (value closest to 0) or negative infinity (-inf) since None is never chosen in min/max functions.
"""
from typing import List

class Kadane:
    # taken from: https://en.wikipedia.org/wiki/Maximum_subarray_problem
    def __max_sum(self, nums: List[int]) -> int:
        # # inf initilization disallows empty subarrays
        best_sum: float = float('-inf')
        # to keep track of sum as we loop
        current_sum: int = 0
        for num in nums:
            # by using max we reset current sum to either the current number or current_sum + num if current_sum + current number > current number
            current_sum = max(num, current_sum + num)
            # store whatever the best current_sum was duirng the loop.
            # having an -inf value ensures at least 1 value from the list is used
            best_sum = max(best_sum, current_sum)
        return best_sum

    # taken from: https://en.wikipedia.org/wiki/Maximum_subarray_problem
    def __max_sum_w_indicies(self, nums: List[int]) -> tuple[int,int,int]:
        # inf initilization disallows empty subarrays
        best_sum: float = float('-inf')
        current_sum: int = 0
        best_start = best_end = 0  # or: None
        for current_end, x in enumerate(nums):
            # if out current sum is eq to or below 0
            if current_sum <= 0:
                # Start a new sequence at the current element
                current_start = current_end
                # Add to our current sum
                current_sum = x
            else:
                # Extend the existing sequence with the current element
                current_sum += x
            # when the current_sum is bigger than what was our best sum
            if current_sum > best_sum:
                # set the new bigger sum to best sum
                best_sum = current_sum
                # the best starting index would be where the new bigger value started from
                # this will only increment if the previous current_sum drops below 0 and then the current current sum is bigger than the stored best value
                best_start = current_start
                # best ending index would be where we stop looping.
                # this increments as the current_sum gets bigger
                best_end = current_end + 1  # the +1 is to make 'best_end' exclusive
        return best_sum, best_start, best_end

    def max_sum(self, nums: List[int]) -> int:
        return self.__max_sum(nums=nums)

nums = []
print(Kadane().max_sum(nums))