

#
# def fibonacci(a=0, b=1):
#     while True:
#         yield a
#         a,b = b, a + b
#
#
# gen = fibonacci()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]
# def uniq_num(nums):
#     uniq = [uniq for n, uniq in enumerate(nums) if uniq not in nums[:n]]
#     yield from uniq
#
# for item in uniq_num(data):
#     print(item)
# print(20 * "-")
#
#
# def uniq_num2(nums):
#     new_set = set()
#     for n in nums:
#         if n not in new_set:
#             yield n
#             new_set.add(n)
#
#
#
# gen2 = uniq_num2(data)
# for i in uniq_num2(data):
#     print(i)
