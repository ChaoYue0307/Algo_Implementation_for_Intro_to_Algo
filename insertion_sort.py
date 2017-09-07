

def insertion_sort(A):
	for j in range(1,len(A)):
		key = A[j]
		i = j - 1
		while i>-1 and A[i] > key:
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key
	return A		


if __name__ == "__main__":
	A = [6,2,1,4,7,7,8,3,3,222,21]
	print (insertion_sort(A))