import numpy as np

def compute_qkv(X,W_q,W_k,W_v):
    return np.matmul(X,W_q),np.matmul(X,W_k),np.matmul(X,W_v)

def self_attention(Q, K, V):

    def softmax(x:np.array):
        """
        注意(2,)和(2,1)不一样,前者其实就是(2)，从而广播顺序会出错，
        后者需要设定keepdims
        pytorch里面命令则是keepdim (少个s)
        """
        x=x-np.max(x,axis=-1,keepdims=True)
        ex=np.exp(x)
        sum=np.sum(ex,axis=-1,keepdims=True)
        return ex/sum
    Qk=np.matmul(Q,K.T)
    d=Q.shape[-1]    
    attention_output=np.matmul(softmax(Qk/np.sqrt(d)),V)
    return attention_output



X = np.array([[1, 0], [0, 1]]) 
W_q = np.array([[1, 0], [0, 1]]) 
W_k = np.array([[1, 0], [0, 1]]) 
W_v = np.array([[1, 2], [3, 4]]) 
Q, K, V = compute_qkv(X, W_q, W_k, W_v) 
output = self_attention(Q, K, V) 
print(output)
