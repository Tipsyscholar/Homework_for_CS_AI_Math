import numpy as np

def jensen_shannon_divergence(P: list[float], Q: list[float]) -> float:
    """
    Compute the Jensen-Shannon Divergence between two probability distributions.
    
    Args:
        P: First probability distribution
        Q: Second probability distribution
    
    Returns:
        Jensen-Shannon Divergence value
    """
    # Your code here
    def entropy(p):
        p=np.array(p)
        q=p.copy()
        q[q==0]=1e-15
        return  -np.sum(p*np.log(q))
    def cross(p,q):
        p=np.array(p)
        q=np.array(q)
        q[q==0]=1e-15
        return -np.sum(p*np.log(q))
    def KL(p,q):
        return  cross(p,q)-entropy(p)
    M=[1/2*(i+j) for i,j in zip(P,Q)]
    return 1/2 *KL(P,M)+1/2 *KL(Q,M)



jsd = jensen_shannon_divergence([1.0, 0.0], [0.0, 1.0])
print(round(jsd, 6))
