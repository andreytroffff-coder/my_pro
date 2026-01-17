word = input()
cnt = word[:word.index('.')].count('не')
if cnt % 2 == 1:
    print(f'не{word[word.index('.')+1:]}')
else:
    print(f'{word[word.index('.')+1:]}')