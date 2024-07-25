# 시간 복잡도: O(n^2)
# word = input().upper()
# word_list = list(set(word))
# cnt = []
#
# for i in word_list:
#     cnt.append(word.count(i))
#
# print("?" if cnt.count(max(cnt)) > 1 else word_list[cnt.index(max(cnt))])

# 시간 복잡도: O(n)
from collections import Counter

word = input().upper()
arr = Counter(word).most_common()

print("?" if len(arr) > 1 and arr[0][1] == arr[1][1] else arr[0][0])