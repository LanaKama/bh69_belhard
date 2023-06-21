age = 34
name = 'Alex'
is_human = True

# text = "Helle your age is human'

text1 = 'Hello' + name + 'your age' + str(age) + 'is human' + str(is_human)
#text2 = 'Hello $s your age %d is human %d' % (name, age, is_human)
text3 = 'Hello {} your age {} is human'. format(name, age, is_human)
text4 = f'Hello {name} your age {age * 2} is human {is_human}'

# print(f'{name:*>10}')
# print (f'{2 * 2=     }')
# print(f'{name!r}')
# print(f'{"привет"!a}')
# print(f'{3.14159:.2f}')
#print(f'{3.14159:.2f}')

# print('\N{fire}')

text = 'Hello___world___python'
# print(text.split('___'), 1)
# # print(text.rsplit('___'), 1)
# print(' | '.join(['hello', 'world']))

text



