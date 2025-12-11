import numpy as np
def adam_optimizer(f, grad, x0, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, num_iterations=10):
	# Your code here
    gt=grad(x0)
    m=0
    v=0
    for i in range(1,num_iterations+1):
        m= beta1*m+(1-beta1)*gt
        v=beta2*v+(1-beta2)*gt**2
        mtidle=m/(1-beta1**(i))
        vtidle=v/(1-beta2**(i))
        x0=x0-learning_rate*mtidle/(np.sqrt(vtidle)+epsilon)
        gt=grad(x0)
    return x0

def objective_function(x): 
    return x[0]**2 + x[1]**2 

def gradient(x): 
    return np.array([2*x[0], 2*x[1]]) 


x0 = np.array([1.0, 1.0]) 
x_opt = adam_optimizer(objective_function, gradient, x0) 
print(x_opt)