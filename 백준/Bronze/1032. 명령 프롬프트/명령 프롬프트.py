N = int(input())

words = []

for _ in  range(N):
    word = input()
    words.append(word)
word = list(words[0])

for __ in range(len(words[0])):
    for ___ in range(1, N):
        if words[___][__] != word[__]:
            word[__] = '?'

print(''.join(word))