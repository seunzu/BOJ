word = input()

print(1) if word[::1] == word[::-1] else print(0)
# print(1) if list(word) == list(reversed(word)) else print(0)
