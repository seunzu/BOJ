word = input().upper()
word_list = list(set(word))
cnt = []

for i in word_list:
    count = word.count(i)
    cnt.append(count)

print("?") if cnt.count(max(cnt)) > 1 else print(word_list[cnt.index(max(cnt))])

