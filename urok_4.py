# numbers = [2, 4, 5, 7, 8, 2, 6, 8]
# words = ['hello', 'python', 'world']
# print(words[1][2])
# l = list('hello')
# print(l)
#
# letters = list('hello')
# numbers2 = [i ** 2 for i in range(1, 100)]
# print(numbers2)

from collections import *

# a = int(input('enter a:'))
# b = int(input('enter б:'))
# c = int(input('enter step:'))
# numbers = [i for i in range(a, b, c)]
# print(numbers)

word_counter = Counter(input().split())

text = input().lower().split()
c = {i: text.count().}


