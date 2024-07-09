a, b = map(int, input().split())

# if a > b:
#     print('>')
# elif a < b:
#     print('<')
# else: print('==')

print('>') if a > b else print('<') if a < b else print('==')
