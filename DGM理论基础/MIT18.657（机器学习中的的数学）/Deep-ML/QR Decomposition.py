import numpy as np

def qr_decomposition(A: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
	"""
	Perform QR decomposition 
	
	Args:
		A: An m x n matrix represented as list of lists
	
	Returns:
		Tuple of (Q, R) where Q is orthogonal and R is upper triangular
	>>> Q, R = qr_decomposition([[1, 0], [0, 1]])
	>>> print([[round(x, 4) for x in row] for row in Q])
	[[1.0, 0.0], [0.0, 1.0]]
	"""
	# Your code here
	R=np.array(A)
	m,n=R.shape
	k=min(m,n)
	Q=np.eye(m)
	for i in range(n):
		if i>=m:
			break
		unit=np.zeros(m-i)
		unit[0]=(np.sign(R[i,i]) if R[i,i]!=0 else 1.0)*np.linalg.norm(R[i:,i])
		if np.allclose(R[i:,i],-unit):
			continue
		else:
			v=(R[i:,i]+unit).reshape(-1,1)
		new=np.eye(m)
		new[i:,i:]=(np.eye(m-i)-2*np.matmul(v,v.T)/np.matmul(v.T,v))
		R=np.matmul(new,R)
		Q=np.matmul(Q,new)
	for i in range(k):
		if R[i,i]<0:
			R[i,:]*=-1
			Q[:,i]*=-1
	return Q.tolist(),R.tolist()
		
	

Q, R = qr_decomposition([[3, 0], [4, 5]])
print([[round(x, 4) for x in row] for row in Q])