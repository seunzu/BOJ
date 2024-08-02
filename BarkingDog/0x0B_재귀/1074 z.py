# ver1 분할 정복
N, r, c = map(int, input().split())
ans = 0

while N != 0:
	N -= 1

	# 제2사분면
	if r < 2 ** N and c < 2 ** N:
		ans += ( 2 ** N ) * ( 2 ** N ) * 0

	# 제1사분면
	elif r < 2 ** N and c >= 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 1
		c -= ( 2 ** N )
        
	# 제3사분면    
	elif r >= 2 ** N and c < 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 2
		r -= ( 2 ** N )
        
	# 제4사분면    
	else:
		ans += ( 2 ** N ) * ( 2 ** N ) * 3
		r -= ( 2 ** N )
		c -= ( 2 ** N )
    
print(ans)

# ver2 재귀
N, r, c = map(int, input().split())

def z(N, r, c):

	if N == 0:
		return 0
        
	return 2*(r%2)+(c%2) + 4*z(N-1, int(r/2), int(c/2))

print(z(N, r, c))