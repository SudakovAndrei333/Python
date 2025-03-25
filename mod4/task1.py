def check(s):
    nums = list(map(int, s.split()))
    if all(x == nums[0] for x in nums):
        return "Числа равны"
    elif len(nums) == len(set(nums)):
        return "Числа разные"
    else:
        return "Есть равные и неравные числа"

print(check(input("Введите последовательность целых чисел через пробел: ")))