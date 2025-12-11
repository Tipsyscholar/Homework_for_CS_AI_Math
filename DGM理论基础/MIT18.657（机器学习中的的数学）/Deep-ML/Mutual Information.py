import numpy as np

def mutual_information(joint_prob: list[list[float]]) -> float:
	"""
	Compute the mutual information between two random variables.
	
	Args:
		joint_prob: 2D joint probability distribution P(X,Y)
	
	Returns:
		Mutual information I(X;Y)
	"""
	# Your code here
	def entropy(p:np.array):
		p=np.maximum(p,1e-15)
		return np.sum(p*(-np.log(p)))
	A=np.array(joint_prob)
	X=np.sum(A,axis=0)
	Y=np.sum(A,axis=1)
	return entropy(X)+entropy(Y)-entropy(A.ravel())
	

mi = mutual_information([[0.4, 0.1], [0.1, 0.4]]) 
print(round(mi, 6))