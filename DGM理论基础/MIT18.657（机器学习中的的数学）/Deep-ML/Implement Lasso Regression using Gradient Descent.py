import numpy as np

def l1_regularization_gradient_descent(X: np.array, y: np.array, alpha: float = 0.1, learning_rate: float = 0.01, max_iter: int = 1000, tol: float = 1e-4) -> tuple:
	n_samples, n_features = X.shape

	weights = np.zeros(n_features)
	bias = 0
	# Your code here
	pass



X = np.array([[0, 0], [1, 1], [2, 2]]) 
y = np.array([0, 1, 2]) 
alpha = 0.1 
output = l1_regularization_gradient_descent(X, y, alpha=alpha, learning_rate=0.01, max_iter=1000) 
print(output)