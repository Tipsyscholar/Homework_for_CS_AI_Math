import numpy as np

def compute_elbo(x: list[float], q_mean: float, q_std: float, 
                 prior_mean: float, prior_std: float,
                 likelihood_std: float, n_samples: int = 1000) -> float:
	"""
	Compute the Evidence Lower Bound (ELBO) for variational inference.
	
	Args:
		x: Observed data points
		q_mean: Mean of variational distribution
		q_std: Standard deviation of variational distribution
		prior_mean: Mean of prior distribution
		prior_std: Standard deviation of prior distribution
		likelihood_std: Standard deviation of likelihood
		n_samples: Number of Monte Carlo samples
	
	Returns:
		ELBO value
	"""
	# Your code here
	pass