# def func(a, b, c):
#     res = []
#     for i in range(2, b):
#         res = (a * c ** (i-1))
#
#     print(res)

# def progress(a, b, c):
#     numbers = []
#     while a < b:
#         numbers.append(a)
#         a *= c
#     return numbers
#
#
# print(numbers(2, 100, 2))
#
# def averange(*numbers):
#   return round(sum(numbers) / len(numbers), 2)
#
#
# print(numbers)

# def numbers():
#     total = 0
#     res = []
#     for number in numbers:
#         total += number
#         numbers.append(total)
#     return res
# print(res[numbers(1, 2, 3, 4, 5, 6)])

# def accuumulate_sum(numbers):
#     s = 0
#     res = []
#     for number in numbers:
#         s += number
#         res.append(s)
#     return res
#
# res = accuumulate_sum([1, 2, 3, 4, 5, 6, 7])
#
# print(res)

def is_pangram(text):
   if letter in text in 'йцукенгшщзхъфывапролджэячсмитьбю':
       text = True
   else:
        text = False


   def is_pangram(text):
       text = text.lower()
       for letter in ascii_lowercase:
           if letter not in text:
               return False
   return True






