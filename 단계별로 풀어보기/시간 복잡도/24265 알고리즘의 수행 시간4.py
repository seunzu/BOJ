# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1
#         for j <- i + 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }
# 외부 for문: 1 ~ n-1/ 내부 for문: i+1 ~ n

n = int(input())

print(int(n*(n-1) - (n-1)*n/2))
print(2)
