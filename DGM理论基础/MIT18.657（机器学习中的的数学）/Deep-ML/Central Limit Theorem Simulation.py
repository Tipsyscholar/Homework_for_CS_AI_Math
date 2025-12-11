import numpy as np

def simulate_clt(distribution: str, n: int, runs: int = 10000, seed: int = 42) -> dict:
    """
    Simulate the Central Limit Theorem.

    Args:
        distribution (str): The distribution to sample from ('uniform', 'exponential', 'bernoulli').
        n (int): Sample size.
        runs (int): Number of repeated experiments.
        seed (int): Random seed for reproducibility.

    Returns:
        dict: {'mean': float, 'std': float} of the standardized sample means.
    """
    #中心极限定理Sn-n\mu/\sqrt(n) \sigma \rightarrow d N(0,1)
    np.random.seed(seed)
    if distribution=='bernoulli':
        sample=np.random.binomial(1,0.3,size=(runs,n))

    else:
        dis=getattr(np.random,distribution)
        sample=dis(size=(runs,n))
    mean=0
    std=0
    
    if distribution=="uniform" :
        mean=0.5
        std=np.sqrt(1/12)
    elif distribution=="exponential":
        mean=1
        std=1
    else:
        mean=0.3
        std=np.sqrt(0.3*0.7)
    sample=np.sum(sample,axis=-1)/n
    sample=(sample-mean)/(std/np.sqrt(n))
    
    a={}
    a["mean"]=np.mean(sample)
    a["std"]=np.std(sample)

    return a