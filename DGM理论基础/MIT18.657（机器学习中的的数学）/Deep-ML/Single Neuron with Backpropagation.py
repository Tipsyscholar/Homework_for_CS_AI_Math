import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
    def sigmoid(x):
        return 1/(1+np.exp(-x))
    updated_weights=initial_weights
    updated_bias=initial_bias
    mse_values=[]
    N=features.shape[0]
    for i in range(epochs):
        linear=np.matmul(updated_weights,features.T)+updated_bias
        front=2*(sigmoid(linear)-labels)*(1-sigmoid(linear))*sigmoid(linear)/N
        nabla_weights=np.matmul(front,features)
        nabla_bias=np.matmul(front,np.ones_like(labels.T))
        mse_values.append(np.sum((sigmoid(linear)-labels)**2)/N)
        updated_weights=updated_weights-learning_rate*nabla_weights
        updated_bias=updated_bias-learning_rate*nabla_bias
    mse_values=np.round(np.array(mse_values),decimals=4).tolist()
    updated_bias=np.round(updated_bias,4)
    updated_weights=np.round(updated_weights,4)
    return updated_weights, updated_bias, mse_values


print(train_neuron(np.array([[1.0, 2.0], [2.0, 1.0], [-1.0, -2.0]]), np.array([1, 0, 0]), np.array([0.1, -0.2]), 0.0, 0.1, 2))

print(train_neuron(np.array([[1, 2], [2, 3], [3, 1]]), np.array([1, 0, 1]), np.array([0.5, -0.2]), 0, 0.1, 3))

