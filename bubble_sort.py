def bubble_sort(A):
	for i in range(len(A)):
		for j in range(len(A)-1, i, -1):
			if A[j] < A[j-1]:
				A[j], A[j-1] = A[j-1], A[j]
	return A

if __name__ == "__main__":
	A = [4,2,4,6,7,723,1,3,4,51,1]
	print (bubble_sort(A))