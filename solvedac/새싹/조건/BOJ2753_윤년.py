year = int(input())

print(1) if ((year % 4 == 0) & (year % 100 != 0)) | (year % 400 == 0) else print(0)

