# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }
# 이중 for문 -> 시간 복잡도: n^2
n = int(input())

print(n**2)
print(2)
