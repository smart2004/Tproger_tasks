word = 'арбузузубра'

l = len(word)

if word[::-1] == word[::1]:
    print('палиндром')
if word[::-1] != word[::1]:
    print('хрень')
