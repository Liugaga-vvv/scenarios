from typing import List

def find_expressions(nums: List[int], target: int) -> List[str]:
    result: List[str] = []
    for index in range(len(nums)):
        temp_num = index + 1
        while temp_num < len(nums):
            if nums[index] + nums[temp_num] == target:
                result.append(str(nums[index]) + "+" + str(nums[temp_num]))
            if nums[index] - nums[temp_num] == target:
                result.append(str(nums[index]) + "-" + str(nums[temp_num]))
            if nums[index] * nums[temp_num] == target:
                result.append(str(nums[index]) + "*" + str(nums[temp_num]))
            if nums[index] / nums[temp_num] == target:
                result.append(str(nums[index]) + "/" + str(nums[temp_num]))

            if nums[temp_num] - nums[index] == target:
                result.append(str(nums[temp_num]) + "-" + str(nums[index]))
            if nums[temp_num] / nums[index] == target:
                result.append(str(nums[temp_num]) + "/" + str(nums[index]))
            temp_num += 1

    return result