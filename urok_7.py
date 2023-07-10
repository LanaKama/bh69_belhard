# def generator(start, stop, multiplier):
#     if (start < stop) and (multiplier > 0):
#         while start < stop:
#             yield start
#             start *= multiplier
#     elif (start > stop) and (multiplier < 1):
#         while start > stop:
#             yield start
#             start *= multiplier
#     else:
#         raise ValueError
#
# for i in generator(start=2, stop=200, multiplier=1.3):
#     print(i)

def countvowels(string):

    vowels = ['e', 'y', 'u', 'i', 'o', 'a']
    total = 0
    for d in string:
        if d in vowels:
            total += 1
    return total

# print(countvowels('hello'))
#
#
# def validate_email(email):
#     for i in email:
#         if i != @
#             i = False
#             break
#         if



# def is_leap_year(s):
#     if (s % 4 == 0) and (s % 100 != 0) or (s % 400 == 0):
#          print('год високосный', s)
#     else:
#          print('год не високосный', s)
#
# print(is_leap_year(2022))

def is_leap_year(s):
    return (s % 4 == 0) and (s % 100 != 0) or (s % 400 == 0)

print(is_leap_year(2000))
print(is_leap_year(2100))
print(is_leap_year(2104))
#
# def is_leap_year(s):
#     if (s % 4 == 0) and (s % 100 != 0) or (s % 400 == 0)
#         return True
#     else:
#         return False
#
# print(is_leap_year(2100))
