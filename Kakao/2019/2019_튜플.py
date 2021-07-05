def solution(s):
    nums = eval(s[1:-1])
    if len(nums) > 1:
        nums = sorted(nums, key=lambda n : sum(n))
    else:
        return list(nums)
    answer = []
    for num in nums:
        for n in num:
            if n not in answer:
                answer.append(n)
    return answer