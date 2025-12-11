import numpy as np

def entropy_and_cross_entropy(P: list[float], Q: list[float]) -> tuple[float, float]:
	"""
	Compute entropy of P and cross-entropy between P and Q.
	
	Args:
		P: True probability distribution
		Q: Predicted probability distribution
	
	Returns:
		Tuple of (entropy H(P), cross-entropy H(P,Q))
		
	"""
	# Your code here
	epsilon=1e-15
	p=np.maximum(np.array(P),epsilon)
	q=np.maximum(np.array(Q),epsilon)
	entropy=np.sum(p*(-np.log(p)))
	cross=np.sum(p*(-np.log(q)))
	return entropy,cross

h, ce = entropy_and_cross_entropy([1.0, 0.0, 0.0], [0.9, 0.05, 0.05])
print(round(h, 6), round(ce, 6))