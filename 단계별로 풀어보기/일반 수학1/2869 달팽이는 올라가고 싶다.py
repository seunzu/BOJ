a, b, v = map(int, input().split())
# cnt = 0	

# while True:
#     cnt += 1
#     if a*cnt - b*(cnt - 1) >= v:
#         break
    
# print(cnt)

# a*cnt - b*(cnt -1) >= v
# -> cnt >= (v-b)/(a-b)
cnt = (v-b)/(a-b)
print(int(cnt) if cnt == int(cnt) else int(cnt)+1)