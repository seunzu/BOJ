s = list(input())
alphabet = [0 for _ in range(26)]

for i in s:
    # ord('a') = 97
    alphabet[ord(i) - 97] += 1
    
print(*alphabet)        